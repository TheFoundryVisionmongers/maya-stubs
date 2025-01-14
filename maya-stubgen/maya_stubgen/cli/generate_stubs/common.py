from __future__ import annotations

import inspect
from abc import ABC, abstractclassmethod, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from pkgutil import ModuleInfo
from textwrap import indent
from typing import *

from docstring_parser.common import (DocstringExample, DocstringParam,
                                     DocstringRaises, DocstringReturns)

STUB_HEADER = """\
from __future__ import annotations

from typing import *
from typing_extensions import Self

if TYPE_CHECKING:
    from _typeshed import Incomplete
else:
    Incomplete = Any

{imports}
\n
"""

TAB_LENGTH = 4
TAB = TAB_LENGTH * " "


class MISSING:
    """Used when a value is not specified as opposed to specified but purposefully None."""


class FunctionType(Enum):
    function = "function"
    method = "method"
    classmethod = "classmethod"
    staticmethod = "staticmethod"
    getter = "property"
    setter = "{name}.setter"


@dataclass
class StubItem(ABC):
    @abstractclassmethod
    def from_object(cls, obj: type, name: Optional[str] = None) -> StubItem:
        ...

    @property
    @abstractmethod
    def stub(self) -> str:
        ...

    def __str__(self) -> str:
        return self.stub


@dataclass
class Class(StubItem):
    name: str
    parent: Optional[str] = None
    members: List[Class | Function | Variable] = field(default_factory=list)

    @classmethod
    def from_object(cls, obj: object, name: str = None) -> Class:

        if name is None:
            name = obj.__name__

        try:
            parent = type.mro(obj)[1]
        except IndexError:
            parent = object

        members = []
        if parent is not None:
            parent_members = [id(m[1]) for m in inspect.getmembers(parent)]
        else:
            parent_members = []

        ignored_members = [
            # These members somehow sometime share their id with their `super`
            # but sometimes don't
            "__dict__",
            "__bases__",
            "__mro__",
            "__name__",
            "__qualname__",
            "__doc__",
            "__hash__",
            "__init_subclass__",
            "__module__",
            "__subclasscheck__",
            "__subclasshook__",
            "__weakref__",
        ]

        for member_name, member in inspect.getmembers(obj):
            if member_name in ignored_members:
                continue

            is_inherited = id(member) in parent_members

            if is_inherited:
                continue

            if inspect.isclass(member):
                members.append(Class.from_object(member))
            elif callable(member):
                method = Function.from_object(member, member_name, FunctionType.method)
                members.append(method)
            elif inspect.isgetsetdescriptor(member):
                getter = Function.from_object(member, member_name, FunctionType.getter)
                setter = Function.from_object(member, member_name, FunctionType.setter)
                members.append(getter)
                members.append(setter)
            else:
                members.append(
                    Variable(member_name, type(member), member, is_argument=True)
                )

        return cls(name, parent, members)

    @property
    def stub(self):
        stub = f"class {self.name}"

        if self.parent and self.parent is not object:
            stub += f"({self.parent.__name__})"

        stub += ":\n"

        if not self.members:
            stub += "    pass\n"

        for member in self.members:
            stub += indent(member.stub, TAB)
            stub += "\n"

        return stub


@dataclass
class Variable(StubItem):
    name: str
    type: Type = Any
    value: Any = MISSING
    is_argument: bool = False
    description: str = ""

    def __post_init__(self) -> None:
        if self.name == "self":
            self.type = MISSING

    @classmethod
    def from_object(cls, obj: type, name: Optional[str] = None) -> Variable:
        raise NotImplementedError

    @property
    def type_str(self) -> str:
        try:
            return self.type.__name__
        except AttributeError:
            return str(self.type).replace("typing.", "")

    @property
    def stub(self) -> str:

        res = self.name

        if self.type is not MISSING:
            res += f": {self.type_str}"

        if self.value is not MISSING and self.is_argument:
            res += " = ..."

        return res


@dataclass
class Function:
    name: str
    arguments: List[Variable] = field(default_factory=list)
    docstring: Optional[str | DocstringBuilder] = None
    return_type: Type = Any
    function_type: FunctionType = FunctionType.function

    def __post_init__(self):
        if isinstance(self.docstring, str):
            self.docstring = self._process_docstring(self.docstring)

        if self.function_type is FunctionType.method:
            if len(self.arguments) == 0 or self.arguments[0].name != "self":
                self.arguments.insert(0, Variable("self", "Self", is_argument=True))

    @classmethod
    def from_object(
        cls,
        obj: type,
        name: Optional[str] = None,
        function_type=FunctionType.function,
    ) -> Function:
        if name is None:
            name = obj.__name__

        try:
            signature = inspect.signature(obj)
        except:
            arguments = [Variable("*args"), Variable("**kwargs")]
            return_type = Any
        else:
            arguments = []
            for arg_name, parameter in signature.parameters.items():
                annotation = (
                    parameter.annotation
                    if parameter.annotation is not parameter.empty
                    else Any
                )
                value = (
                    parameter.default
                    if parameter.default is not parameter.empty
                    else MISSING
                )
                arg = Variable(arg_name, annotation, value, is_argument=True)
                arguments.append(arg)
            return_type = (
                signature.return_annotation
                if signature.return_annotation is not signature.empty
                else Any
            )
        docstring = obj.__doc__

        return Function(name, arguments, docstring, return_type, function_type)

    @property
    def stub(self):
        stub = self.signature

        if self.docstring:
            stub += indent(f"\n{self.docstring}", TAB)
        else:
            stub += " ..."

        return stub

    @staticmethod
    def _process_docstring(docstring: Optional[str]) -> str:
        if docstring is None:
            return None

        docstring = docstring.strip()

        lines = docstring.splitlines()

        if len(lines) == 0:
            return None
        elif len(lines) == 1:
            docstring = f'"""{docstring}"""'
        else:
            docstring = f'"""{docstring}\n"""'

        return docstring

    @property
    def arguments_str(self) -> str:
        return ", ".join(map(str, self.arguments))

    @property
    def return_type_str(self):
        return str(self.return_type).replace("typing.", "")

    @property
    def signature(self):
        if self.function_type not in [FunctionType.function, FunctionType.method]:
            signature = f"@{self.function_type.value.format(name=self.name)}\n"
        else:
            signature = ""

        signature += f"def {self.name}({self.arguments_str})"

        if self.return_type:
            signature += f" -> {self.return_type_str}"

        signature += ":"

        return signature


@dataclass
class DocstringBuilder:
    short_description: str
    long_description: Optional[str] = None
    parameters: Optional[List[DocstringParam]] = None
    returns: Optional[DocstringReturns] = None
    yields: Optional[str] = None
    raises: Optional[DocstringRaises] = None
    examples: Optional[DocstringExample] = None

    def __post_init__(self):
        if self.short_description:
            self.short_description = "\n".join(
                self.process_lines(self.short_description)
            )

        if self.long_description:
            self.long_description = "\n".join(self.process_lines(self.long_description))

        if self.returns:
            self.returns = "\n".join(self.process_lines(self.returns))

        if self.yields:
            self.yields = "\n".join(self.process_lines(self.yields))

        if self.raises:
            self.raises = "\n".join(self.process_lines(self.raises))

        self.process_examples()

    @classmethod
    def process_lines(cls, text: str) -> str:
        for line in text.splitlines():
            line = cls.process_line(line)
            yield line

    @staticmethod
    def process_line(line: str) -> str:
        # line = line.replace("\\0", "")
        line = line.strip()

        line = line.replace('"""', "'''")

        if "C:" in line:
            line = line.replace("\\\\", "\\").replace("\\", "/")
        return line

    def process_examples(self):
        if self.examples is None:
            return

        new_content = []
        for line in self.process_lines(self.examples):

            if not line:
                continue

            if not line.startswith(">>>"):
                line = ">>> " + line
            new_content.append(line)

        self.examples = "\n".join(new_content)

    def __str__(self):
        return self.stub()

    def stub(self):
        docstring = f'"""{self.short_description}'

        if self.long_description:
            docstring += f"\n\n{self.long_description}"

        if self.parameters:
            docstring += "\n\nArgs:"
            for parameter in self.parameters:
                docstring += f"\n    {parameter.arg_name}: {parameter.description}"

        if self.returns:
            docstring += "\n\nReturns:"
            docstring += f"\n    {self.returns}"

        if self.yields:
            docstring += "\n\nYields:"
            docstring += f"\n    {self.yields}"

        if self.raises:
            docstring += "\n\nRaises:"
            docstring += f"\n    {self.raises}"

        if self.raises:
            docstring += "\n\nRaises:"
            docstring += f"\n    {self.raises}"

        if self.examples:
            docstring += "\n\nExamples:"
            for line in self.examples.splitlines():
                docstring += f"\n    {line}"

        if "\n" in docstring:
            # If the docstring is a multiline, add one last line before closing it.
            docstring += "\n"

        docstring += '"""'

        return docstring


def get_stub_path(module: ModuleInfo, override=False) -> Path:
    folder_name = "maya-stubs-override" if override else "maya-stubs"

    stub_path = (
        Path()
        / "stubs"
        / "pyi"
        / Path(module.name.replace("maya", folder_name, 1).replace(".", "/"))
    )

    if module.ispkg:
        stub_path = stub_path / f"__init__.pyi"
    else:
        stub_path = stub_path.with_name(f"{stub_path.name}.pyi")

    return stub_path.resolve()


def get_classes(module: ModuleInfo) -> List[Tuple[str, Type]]:
    """Return the classes in the module sorted by inheritance."""
    sorted_classes = []
    classes = inspect.getmembers(module, inspect.isclass)
    for _, cls in classes:
        for base in reversed(type.mro(cls)):
            base_tuple = (base.__name__, base)
            if base_tuple not in sorted_classes and base_tuple in classes:
                sorted_classes.append(base_tuple)
    return sorted_classes
