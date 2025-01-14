from __future__ import annotations

from typing import *

Unknown = Any

class MDynSweptLine(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def length(self, *args: Any, **kwargs: Any) -> Any: ...
    def normal(self, *args: Any, **kwargs: Any) -> Any: ...
    def tangent(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBFEA0>
    def vertex(self, *args: Any, **kwargs: Any) -> Any: ...

def MDynSweptLine_className(*args: Any, **kwargs: Any) -> Any: ...
class MDynSweptTriangle(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def area(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def normal(self, *args: Any, **kwargs: Any) -> Any: ...
    def normalToPoint(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC1180>
    def uvPoint(self, *args: Any, **kwargs: Any) -> Any: ...
    def vertex(self, *args: Any, **kwargs: Any) -> Any: ...

def MDynSweptTriangle_className(*args: Any, **kwargs: Any) -> Any: ...
class MDynamicsUtil(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def addNodeTypeToRunup(self, *args: Any, **kwargs: Any) -> Any: ...
    def evalDynamics2dTexture(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasValidDynamics2dTexture(self, *args: Any, **kwargs: Any) -> Any: ...
    def inRunup(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeNodeTypeFromRunup(self, *args: Any, **kwargs: Any) -> Any: ...
    def runupIfRequired(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBFBD0>

def MDynamicsUtil_addNodeTypeToRunup(*args: Any, **kwargs: Any) -> Any: ...
def MDynamicsUtil_evalDynamics2dTexture(*args: Any, **kwargs: Any) -> Any: ...
def MDynamicsUtil_hasValidDynamics2dTexture(*args: Any, **kwargs: Any) -> Any: ...
def MDynamicsUtil_inRunup(*args: Any, **kwargs: Any) -> Any: ...
def MDynamicsUtil_removeNodeTypeFromRunup(*args: Any, **kwargs: Any) -> Any: ...
def MDynamicsUtil_runupIfRequired(*args: Any, **kwargs: Any) -> Any: ...
class MFnAirField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def componentOnly(self, *args: Any, **kwargs: Any) -> Any: ...
    def direction(self, *args: Any, **kwargs: Any) -> Any: ...
    def enableSpread(self, *args: Any, **kwargs: Any) -> Any: ...
    def inheritRotation(self, *args: Any, **kwargs: Any) -> Any: ...
    def inheritVelocity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setComponentOnly(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDirection(self, *args: Any, **kwargs: Any) -> Any: ...
    def setEnableSpread(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInheritRotation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInheritVelocity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSpeed(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSpread(self, *args: Any, **kwargs: Any) -> Any: ...
    def speed(self, *args: Any, **kwargs: Any) -> Any: ...
    def spread(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC19A0>

def MFnAirField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnDragField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def direction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDirection(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUseDirection(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC1F40>
    def useDirection(self, *args: Any, **kwargs: Any) -> Any: ...

def MFnDragField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnDynSweptGeometryData(MFnData):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def lineCount(self, *args: Any, **kwargs: Any) -> Any: ...
    def sweptLine(self, *args: Any, **kwargs: Any) -> Any: ...
    def sweptTriangle(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC5220>
    def triangleCount(self, *args: Any, **kwargs: Any) -> Any: ...

def MFnDynSweptGeometryData_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnField(MFnDagNode):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def attenuation(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def falloffCurve(self, *args: Any, **kwargs: Any) -> Any: ...
    def getForceAtPoint(self, *args: Any, **kwargs: Any) -> Any: ...
    def isFalloffCurveConstantOne(self, *args: Any, **kwargs: Any) -> Any: ...
    def magnitude(self, *args: Any, **kwargs: Any) -> Any: ...
    def maxDistance(self, *args: Any, **kwargs: Any) -> Any: ...
    def perVertex(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAttenuation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMagnitude(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMaxDistance(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPerVertex(self, *args: Any, **kwargs: Any) -> Any: ...
    def setUseMaxDistance(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC1450>
    def useMaxDistance(self, *args: Any, **kwargs: Any) -> Any: ...

def MFnField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnFluid(MFnDagNode):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def create2D(self, *args: Any, **kwargs: Any) -> Any: ...
    def create3D(self, *args: Any, **kwargs: Any) -> Any: ...
    def density(self, *args: Any, **kwargs: Any) -> Any: ...
    def emitIntoArrays(self, *args: Any, **kwargs: Any) -> Any: ...
    def expandToInclude(self, *args: Any, **kwargs: Any) -> Any: ...
    def falloff(self, *args: Any, **kwargs: Any) -> Any: ...
    def fuel(self, *args: Any, **kwargs: Any) -> Any: ...
    def getColorMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def getColors(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCoordinateMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCoordinates(self, *args: Any, **kwargs: Any) -> Any: ...
    def getDensityMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def getDimensions(self, *args: Any, **kwargs: Any) -> Any: ...
    def getFalloffMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def getForceAtPoint(self, *args: Any, **kwargs: Any) -> Any: ...
    def getFuelMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def getResolution(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTemperatureMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def getVelocity(self, *args: Any, **kwargs: Any) -> Any: ...
    def getVelocityMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def gridSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def index(self, *args: Any, **kwargs: Any) -> Any: ...
    def isAutoResize(self, *args: Any, **kwargs: Any) -> Any: ...
    def isResizeToEmitter(self, *args: Any, **kwargs: Any) -> Any: ...
    def pressure(self, *args: Any, **kwargs: Any) -> Any: ...
    def setColorMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCoordinateMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDensityMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFalloffMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFuelMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTemperatureMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def setVelocityMode(self, *args: Any, **kwargs: Any) -> Any: ...
    def temperature(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC5540>
    def toGridIndex(self, *args: Any, **kwargs: Any) -> Any: ...
    def updateGrid(self, *args: Any, **kwargs: Any) -> Any: ...
    def velocityGridSizes(self, *args: Any, **kwargs: Any) -> Any: ...
    def voxelCenterPosition(self, *args: Any, **kwargs: Any) -> Any: ...

def MFnFluid_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnGravityField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def direction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDirection(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC7310>

def MFnGravityField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnInstancer(MFnDagNode):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def allInstances(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def instancesForParticle(self, *args: Any, **kwargs: Any) -> Any: ...
    def particleCount(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC74F0>

def MFnInstancer_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnNIdData(MFnData):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def getObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC7770>

def MFnNIdData_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnNObjectData(MFnData):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def getClothObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCollide(self, *args: Any, **kwargs: Any) -> Any: ...
    def getParticleObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def getRigidObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    def isCached(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCached(self, *args: Any, **kwargs: Any) -> Any: ...
    def setObjectPtr(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC79A0>

def MFnNObjectData_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnNewtonField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def minDistance(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMinDistance(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC7DB0>

def MFnNewtonField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnParticleSystem(MFnDagNode):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def acceleration(self, *args: Any, **kwargs: Any) -> Any: ...
    def age(self, *args: Any, **kwargs: Any) -> Any: ...
    def betterIllum(self, *args: Any, **kwargs: Any) -> Any: ...
    def castsShadows(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def count(self, *args: Any, **kwargs: Any) -> Any: ...
    def create(self, *args: Any, **kwargs: Any) -> Any: ...
    def deformedParticleShape(self, *args: Any, **kwargs: Any) -> Any: ...
    def disableCloudAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    def emission(self, *args: Any, **kwargs: Any) -> Any: ...
    def emit(self, *args: Any, **kwargs: Any) -> Any: ...
    def evaluateDynamics(self, *args: Any, **kwargs: Any) -> Any: ...
    def flatShaded(self, *args: Any, **kwargs: Any) -> Any: ...
    def getPerParticleAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasEmission(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasLifespan(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasOpacity(self, *args: Any, **kwargs: Any) -> Any: ...
    def hasRgb(self, *args: Any, **kwargs: Any) -> Any: ...
    def isDeformedParticleShape(self, *args: Any, **kwargs: Any) -> Any: ...
    def isPerParticleDoubleAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def isPerParticleIntAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def isPerParticleVectorAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def isValid(self, *args: Any, **kwargs: Any) -> Any: ...
    def lifespan(self, *args: Any, **kwargs: Any) -> Any: ...
    def mass(self, *args: Any, **kwargs: Any) -> Any: ...
    def opacity(self, *args: Any, **kwargs: Any) -> Any: ...
    def originalParticleShape(self, *args: Any, **kwargs: Any) -> Any: ...
    def particleIds(self, *args: Any, **kwargs: Any) -> Any: ...
    def particleName(self, *args: Any, **kwargs: Any) -> Any: ...
    def position(self, *args: Any, **kwargs: Any) -> Any: ...
    def position0(self, *args: Any, **kwargs: Any) -> Any: ...
    def position1(self, *args: Any, **kwargs: Any) -> Any: ...
    def primaryVisibility(self, *args: Any, **kwargs: Any) -> Any: ...
    def radius(self, *args: Any, **kwargs: Any) -> Any: ...
    def radius0(self, *args: Any, **kwargs: Any) -> Any: ...
    def radius1(self, *args: Any, **kwargs: Any) -> Any: ...
    def receiveShadows(self, *args: Any, **kwargs: Any) -> Any: ...
    def renderType(self, *args: Any, **kwargs: Any) -> Any: ...
    def rgb(self, *args: Any, **kwargs: Any) -> Any: ...
    def saveInitialState(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCount(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPerParticleAttribute(self, *args: Any, **kwargs: Any) -> Any: ...
    def surfaceShading(self, *args: Any, **kwargs: Any) -> Any: ...
    def tailSize(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EC7F90>
    def threshold(self, *args: Any, **kwargs: Any) -> Any: ...
    def velocity(self, *args: Any, **kwargs: Any) -> Any: ...
    def visibleInReflections(self, *args: Any, **kwargs: Any) -> Any: ...
    def visibleInRefractions(self, *args: Any, **kwargs: Any) -> Any: ...

def MFnParticleSystem_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnPfxGeometry(MFnDagNode):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def getBoundingBox(self, *args: Any, **kwargs: Any) -> Any: ...
    def getLineData(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ECC090>

def MFnPfxGeometry_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnRadialField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def radialType(self, *args: Any, **kwargs: Any) -> Any: ...
    def setType(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ECC040>

def MFnRadialField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnTurbulenceField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def frequency(self, *args: Any, **kwargs: Any) -> Any: ...
    def phase(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFrequency(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPhase(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0C9B9F0>

def MFnTurbulenceField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnUniformField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def direction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDirection(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0C8A1D0>

def MFnUniformField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnVolumeAxisField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def detailTurbulence(self, *args: Any, **kwargs: Any) -> Any: ...
    def direction(self, *args: Any, **kwargs: Any) -> Any: ...
    def directionalSpeed(self, *args: Any, **kwargs: Any) -> Any: ...
    def invertAttenuation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDirection(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDirectionalSpeed(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInvertAttenuation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSpeedAlongAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSpeedAroundAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSpeedAwayFromAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSpeedAwayFromCenter(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTurbulence(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTurbulenceFrequency(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTurbulenceOffset(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTurbulenceSpeed(self, *args: Any, **kwargs: Any) -> Any: ...
    def speedAlongAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    def speedAroundAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    def speedAwayFromAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    def speedAwayFromCenter(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ECC810>
    def turbulence(self, *args: Any, **kwargs: Any) -> Any: ...
    def turbulenceFrequency(self, *args: Any, **kwargs: Any) -> Any: ...
    def turbulenceOffset(self, *args: Any, **kwargs: Any) -> Any: ...
    def turbulenceSpeed(self, *args: Any, **kwargs: Any) -> Any: ...

def MFnVolumeAxisField_className(*args: Any, **kwargs: Any) -> Any: ...
class MFnVortexField(MFnField):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def axis(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAxis(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED00E0>

def MFnVortexField_className(*args: Any, **kwargs: Any) -> Any: ...
class MHairSystem(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def getCollisionObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def getFollicle(self, *args: Any, **kwargs: Any) -> Any: ...
    def registerCollisionSolverCollide(self, *args: Any, **kwargs: Any) -> Any: ...
    def registerCollisionSolverPreFrame(self, *args: Any, **kwargs: Any) -> Any: ...
    def registeringCallableScript(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRegisteringCallableScript(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED02C0>
    def unregisterCollisionSolverCollide(self, *args: Any, **kwargs: Any) -> Any: ...
    def unregisterCollisionSolverPreFrame(self, *args: Any, **kwargs: Any) -> Any: ...

def MHairSystem_className(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_getCollisionObject(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_getFollicle(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_registerCollisionSolverCollide(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_registerCollisionSolverPreFrame(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_registeringCallableScript(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_setRegisteringCallableScript(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_unregisterCollisionSolverCollide(*args: Any, **kwargs: Any) -> Any: ...
def MHairSystem_unregisterCollisionSolverPreFrame(*args: Any, **kwargs: Any) -> Any: ...
class MRenderLine(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def getColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def getFlatness(self, *args: Any, **kwargs: Any) -> Any: ...
    def getIncandescence(self, *args: Any, **kwargs: Any) -> Any: ...
    def getLine(self, *args: Any, **kwargs: Any) -> Any: ...
    def getParameter(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTransparency(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTwist(self, *args: Any, **kwargs: Any) -> Any: ...
    def getWidth(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED6090>

class MRenderLineArray(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def className(self, *args: Any, **kwargs: Any) -> Any: ...
    def deleteArray(self, *args: Any, **kwargs: Any) -> Any: ...
    def length(self, *args: Any, **kwargs: Any) -> Any: ...
    def renderLine(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED5DB0>

def MRenderLineArray_className(*args: Any, **kwargs: Any) -> Any: ...
def MRenderLine_className(*args: Any, **kwargs: Any) -> Any: ...
class MnCloth(MnObject):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def createNCloth(self, *args: Any, **kwargs: Any) -> Any: ...
    def getBounce(self, *args: Any, **kwargs: Any) -> Any: ...
    def getFriction(self, *args: Any, **kwargs: Any) -> Any: ...
    def getInverseMass(self, *args: Any, **kwargs: Any) -> Any: ...
    def getNumVertices(self, *args: Any, **kwargs: Any) -> Any: ...
    def getPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def getThickness(self, *args: Any, **kwargs: Any) -> Any: ...
    def getVelocities(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAddCrossLinks(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAirTightness(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBendAngleDropoff(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBendAngleScale(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBendResistance(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBendRestAngleFromPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBounce(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCollisionFlags(self, *args: Any, **kwargs: Any) -> Any: ...
    def setComputeRestAngles(self, *args: Any, **kwargs: Any) -> Any: ...
    def setComputeRestLength(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDamping(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDisableGravity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDragAndLift(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFriction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setIncompressibility(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInputMeshAttractAndRigidStrength(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInputMeshAttractDamping(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInputMeshAttractPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInverseMass(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLinksRestLengthFromPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMaxIterations(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMaxSelfCollisionIterations(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPressure(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPressureDamping(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPumpRate(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRestitutionAngle(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRestitutionTension(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSealHoles(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfCollideWidth(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfCollisionFlags(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfCollisionSoftness(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfCrossoverPush(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfTrappedCheck(self, *args: Any, **kwargs: Any) -> Any: ...
    def setShearResistance(self, *args: Any, **kwargs: Any) -> Any: ...
    def setStartPressure(self, *args: Any, **kwargs: Any) -> Any: ...
    def setStretchAndCompressionResistance(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTangentialDrag(self, *args: Any, **kwargs: Any) -> Any: ...
    def setThickness(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTopology(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTrackVolume(self, *args: Any, **kwargs: Any) -> Any: ...
    def setVelocities(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED0770>

class MnObject(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED0680>

class MnParticle(MnObject):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def createNParticle(self, *args: Any, **kwargs: Any) -> Any: ...
    def getBounce(self, *args: Any, **kwargs: Any) -> Any: ...
    def getFriction(self, *args: Any, **kwargs: Any) -> Any: ...
    def getInverseMass(self, *args: Any, **kwargs: Any) -> Any: ...
    def getNumVertices(self, *args: Any, **kwargs: Any) -> Any: ...
    def getPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def getThickness(self, *args: Any, **kwargs: Any) -> Any: ...
    def getVelocities(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBounce(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCollide(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDamping(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDisableGravity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDragAndLift(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFriction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setIncompressibility(self, *args: Any, **kwargs: Any) -> Any: ...
    def setInverseMass(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLiquidRadiusScale(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLiquidSimulation(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMaxIterations(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMaxSelfCollisionIterations(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def setRestDensity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfCollide(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfCollideWidth(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelfCollisionSoftness(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSurfaceTension(self, *args: Any, **kwargs: Any) -> Any: ...
    def setThickness(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTopology(self, *args: Any, **kwargs: Any) -> Any: ...
    def setVelocities(self, *args: Any, **kwargs: Any) -> Any: ...
    def setViscosity(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED2860>

class MnRigid(MnObject):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def createNRigid(self, *args: Any, **kwargs: Any) -> Any: ...
    def getBounce(self, *args: Any, **kwargs: Any) -> Any: ...
    def getFriction(self, *args: Any, **kwargs: Any) -> Any: ...
    def getInverseMass(self, *args: Any, **kwargs: Any) -> Any: ...
    def getNumVertices(self, *args: Any, **kwargs: Any) -> Any: ...
    def getPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def getThickness(self, *args: Any, **kwargs: Any) -> Any: ...
    def getVelocities(self, *args: Any, **kwargs: Any) -> Any: ...
    def setBounce(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCollisionFlags(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFriction(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPositions(self, *args: Any, **kwargs: Any) -> Any: ...
    def setThickness(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTopology(self, *args: Any, **kwargs: Any) -> Any: ...
    def setVelocities(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED5310>

class MnSolver(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def addNObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def createNSolver(self, *args: Any, **kwargs: Any) -> Any: ...
    def makeAllCollide(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeAllCollisions(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeNObject(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAirDensity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setDisabled(self, *args: Any, **kwargs: Any) -> Any: ...
    def setGravity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setGravityDir(self, *args: Any, **kwargs: Any) -> Any: ...
    def setMaxIterations(self, *args: Any, **kwargs: Any) -> Any: ...
    def setStartTime(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSubsteps(self, *args: Any, **kwargs: Any) -> Any: ...
    def setWindDir(self, *args: Any, **kwargs: Any) -> Any: ...
    def setWindNoiseIntensity(self, *args: Any, **kwargs: Any) -> Any: ...
    def setWindSpeed(self, *args: Any, **kwargs: Any) -> Any: ...
    def solve(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0ED5810>

class boolPtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBF540>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def boolPtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
class charPtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0BF5F90>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def charPtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
class doublePtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBF310>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def doublePtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
class floatPtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBF0E0>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def floatPtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
class intPtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBDC20>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def intPtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
class shortPtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBDE50>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def shortPtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
class uCharPtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBF9A0>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def uCharPtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
class uIntPtr(object):
    """
    """
    def __init__(self, *args) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __repr__(self) -> Any: ...
    def __swig_destroy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def assign(self, *args: Any, **kwargs: Any) -> Any: ...
    def cast(self, *args: Any, **kwargs: Any) -> Any: ...
    def frompointer(self, *args: Any, **kwargs: Any) -> Any: ...
    thisown: property = <property object at 0x0000026FF0EBF770>
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

def uIntPtr_frompointer(*args: Any, **kwargs: Any) -> Any: ...
