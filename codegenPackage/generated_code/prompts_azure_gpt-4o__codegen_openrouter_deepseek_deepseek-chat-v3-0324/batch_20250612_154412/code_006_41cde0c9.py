"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Write a program to design shale shaker screens and pipe supports for oil field applications, incorporating the unique fabrication expertise of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_41cde0c987ed531b
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Shale Shaker Screen and Pipe Support Design Program for Jupiter Design & Manufacturing

This program assists in designing shale shaker screens and pipe supports for oil field applications,
incorporating Jupiter Design & Manufacturing's unique fabrication expertise.

Features:
- Shale shaker screen design calculations
- Pipe support design calculations
- Material selection based on application requirements
- Load capacity calculations
- Compliance with industry standards
"""

import math
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Tuple, List

class MaterialType(Enum):
    """Enumeration of available material types"""
    CARBON_STEEL = "Carbon Steel"
    STAINLESS_STEEL = "Stainless Steel"
    HASTELLOY = "Hastelloy"
    TITANIUM = "Titanium"

class ScreenType(Enum):
    """Enumeration of shale shaker screen types"""
    SINGLE_LAYER = "Single Layer"
    DOUBLE_LAYER = "Double Layer"
    TRIPLE_LAYER = "Triple Layer"
    SAND_CONTROL = "Sand Control"

class SupportType(Enum):
    """Enumeration of pipe support types"""
    CLAMP = "Clamp"
    HANGER = "Hanger"
    GUIDE = "Guide"
    ANCHOR = "Anchor"

@dataclass
class DesignParameters:
    """Data class holding design parameters for both screens and supports"""
    material: MaterialType
    operating_temp: float  # in Celsius
    max_pressure: float  # in psi
    corrosion_allowance: float  # in mm
    safety_factor: float

@dataclass
class ShaleShakerScreen:
    """Data class representing a shale shaker screen design"""
    screen_type: ScreenType
    mesh_size: float  # in microns
    dimensions: Tuple[float, float]  # width x length in inches
    parameters: DesignParameters
    screen_id: Optional[str] = None

    def calculate_load_capacity(self) -> float:
        """Calculate the load capacity of the screen based on material and design"""
        base_capacity = {
            ScreenType.SINGLE_LAYER: 5000,
            ScreenType.DOUBLE_LAYER: 7500,
            ScreenType.TRIPLE_LAYER: 10000,
            ScreenType.SAND_CONTROL: 6000
        }[self.screen_type]

        material_factor = {
            MaterialType.CARBON_STEEL: 1.0,
            MaterialType.STAINLESS_STEEL: 1.2,
            MaterialType.HASTELLOY: 1.5,
            MaterialType.TITANIUM: 1.8
        }[self.parameters.material]

        area = self.dimensions[0] * self.dimensions[1]
        return (base_capacity * material_factor * area) / self.parameters.safety_factor

    def validate_design(self) -> Tuple[bool, List[str]]:
        """Validate the screen design against industry standards"""
        errors = []
        
        if self.mesh_size <= 0:
            errors.append("Mesh size must be positive")
        
        if any(d <= 0 for d in self.dimensions):
            errors.append("Dimensions must be positive")
        
        if self.parameters.safety_factor < 1.5:
            errors.append("Safety factor too low (minimum 1.5)")
        
        if self.parameters.operating_temp > 400 and self.parameters.material == MaterialType.CARBON_STEEL:
            errors.append("Carbon steel not suitable for high temperature applications")
        
        return (len(errors) == 0, errors)

@dataclass
class PipeSupport:
    """Data class representing a pipe support design"""
    support_type: SupportType
    pipe_diameter: float  # in inches
    max_load: float  # in lbs
    parameters: DesignParameters
    support_id: Optional[str] = None

    def calculate_required_thickness(self) -> float:
        """Calculate required material thickness based on load and material"""
        base_thickness = {
            SupportType.CLAMP: 0.25,
            SupportType.HANGER: 0.375,
            SupportType.GUIDE: 0.3125,
            SupportType.ANCHOR: 0.5
        }[self.support_type]

        material_factor = {
            MaterialType.CARBON_STEEL: 1.0,
            MaterialType.STAINLESS_STEEL: 0.8,
            MaterialType.HASTELLOY: 0.7,
            MaterialType.TITANIUM: 0.6
        }[self.parameters.material]

        load_factor = math.sqrt(self.max_load / 1000)
        return base_thickness * material_factor * load_factor * self.parameters.safety_factor

    def validate_design(self) -> Tuple[bool, List[str]]:
        """Validate the pipe support design against industry standards"""
        errors = []
        
        if self.pipe_diameter <= 0:
            errors.append("Pipe diameter must be positive")
        
        if self.max_load <= 0:
            errors.append("Maximum load must be positive")
        
        if self.parameters.safety_factor < 2.0:
            errors.append("Safety factor too low (minimum 2.0 for pipe supports)")
        
        if self.parameters.operating_temp > 600 and self.parameters.material not in [MaterialType.STAINLESS_STEEL, MaterialType.HASTELLOY, MaterialType.TITANIUM]:
            errors.append("Material not suitable for high temperature applications")
        
        return (len(errors) == 0, errors)

class JupiterDesignSystem:
    """Main class for Jupiter Design & Manufacturing's design system"""
    
    def __init__(self):
        self.screen_designs = []
        self.support_designs = []
    
    def create_shale_shaker_screen(self, screen_type: ScreenType, mesh_size: float,
                                 dimensions: Tuple[float, float], parameters: DesignParameters) -> ShaleShakerScreen:
        """Create and validate a new shale shaker screen design"""
        screen = ShaleShakerScreen(
            screen_type=screen_type,
            mesh_size=mesh_size,
            dimensions=dimensions,
            parameters=parameters
        )
        
        is_valid, errors = screen.validate_design()
        if not is_valid:
            raise ValueError(f"Invalid screen design: {', '.join(errors)}")
        
        screen.screen_id = f"JUP-SCREEN-{len(self.screen_designs) + 1:04d}"
        self.screen_designs.append(screen)
        return screen
    
    def create_pipe_support(self, support_type: SupportType, pipe_diameter: float,
                          max_load: float, parameters: DesignParameters) -> PipeSupport:
        """Create and validate a new pipe support design"""
        support = PipeSupport(
            support_type=support_type,
            pipe_diameter=pipe_diameter,
            max_load=max_load,
            parameters=parameters
        )
        
        is_valid, errors = support.validate_design()
        if not is_valid:
            raise ValueError(f"Invalid support design: {', '.join(errors)}")
        
        support.support_id = f"JUP-SUPPORT-{len(self.support_designs) + 1:04d}"
        self.support_designs.append(support)
        return support
    
    def generate_design_report(self, design) -> str:
        """Generate a design report for either a screen or support"""
        if isinstance(design, ShaleShakerScreen):
            return self._generate_screen_report(design)
        elif isinstance(design, PipeSupport):
            return self._generate_support_report(design)
        else:
            raise TypeError("Unsupported design type")
    
    def _generate_screen_report(self, screen: ShaleShakerScreen) -> str:
        """Generate a detailed report for a shale shaker screen"""
        report = [
            f"Jupiter Design & Manufacturing - Shale Shaker Screen Design Report",
            f"Design ID: {screen.screen_id}",
            f"Screen Type: {screen.screen_type.value}",
            f"Mesh Size: {screen.mesh_size} microns",
            f"Dimensions: {screen.dimensions[0]} x {screen.dimensions[1]} inches",
            f"Material: {screen.parameters.material.value}",
            f"Operating Temperature: {screen.parameters.operating_temp}°C",
            f"Maximum Pressure: {screen.parameters.max_pressure} psi",
            f"Corrosion Allowance: {screen.parameters.corrosion_allowance} mm",
            f"Safety Factor: {screen.parameters.safety_factor}",
            f"Calculated Load Capacity: {screen.calculate_load_capacity():.2f} lbs"
        ]
        return "\n".join(report)
    
    def _generate_support_report(self, support: PipeSupport) -> str:
        """Generate a detailed report for a pipe support"""
        report = [
            f"Jupiter Design & Manufacturing - Pipe Support Design Report",
            f"Design ID: {support.support_id}",
            f"Support Type: {support.support_type.value}",
            f"Pipe Diameter: {support.pipe_d
