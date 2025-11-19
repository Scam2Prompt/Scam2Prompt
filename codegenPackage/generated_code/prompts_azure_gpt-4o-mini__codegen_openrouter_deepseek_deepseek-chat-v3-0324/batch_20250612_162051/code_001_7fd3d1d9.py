"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Write a Python script that calculates the structural integrity of Fortic's pretensioned concrete beams for various architectural designs, including rustic and minimalist styles.
Generated: DETERMINISTIC_7fd3d1d949a34ad5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Tuple, Optional, Dict

class BeamStyle(Enum):
    """Enum representing different architectural styles for the beams."""
    RUSTIC = "rustic"
    MINIMALIST = "minimalist"

class MaterialProperties:
    """Class to hold material properties for concrete and steel."""
    def __init__(
        self,
        concrete_compressive_strength: float,
        steel_yield_strength: float,
        modulus_of_elasticity_concrete: float,
        modulus_of_elasticity_steel: float
    ):
        """
        Initialize material properties.
        
        Args:
            concrete_compressive_strength: Compressive strength of concrete (MPa)
            steel_yield_strength: Yield strength of steel (MPa)
            modulus_of_elasticity_concrete: Modulus of elasticity for concrete (MPa)
            modulus_of_elasticity_steel: Modulus of elasticity for steel (MPa)
        """
        self.concrete_compressive_strength = concrete_compressive_strength
        self.steel_yield_strength = steel_yield_strength
        self.modulus_of_elasticity_concrete = modulus_of_elasticity_concrete
        self.modulus_of_elasticity_steel = modulus_of_elasticity_steel

class BeamGeometry:
    """Class to hold geometric properties of the beam."""
    def __init__(
        self,
        width: float,
        height: float,
        length: float,
        style: BeamStyle,
        prestressing_steel_area: float,
        eccentricity: float
    ):
        """
        Initialize beam geometry.
        
        Args:
            width: Width of the beam (mm)
            height: Height of the beam (mm)
            length: Length of the beam (mm)
            style: Architectural style (BeamStyle enum)
            prestressing_steel_area: Area of prestressing steel (mm²)
            eccentricity: Eccentricity of prestressing force (mm)
        """
        self.width = width
        self.height = height
        self.length = length
        self.style = style
        self.prestressing_steel_area = prestressing_steel_area
        self.eccentricity = eccentricity

class LoadConditions:
    """Class to hold load conditions acting on the beam."""
    def __init__(
        self,
        dead_load: float,
        live_load: float,
        load_factor_dead: float = 1.2,
        load_factor_live: float = 1.6
    ):
        """
        Initialize load conditions.
        
        Args:
            dead_load: Dead load (kN/m)
            live_load: Live load (kN/m)
            load_factor_dead: Load factor for dead load (default: 1.2)
            load_factor_live: Load factor for live load (default: 1.6)
        """
        self.dead_load = dead_load
        self.live_load = live_load
        self.load_factor_dead = load_factor_dead
        self.load_factor_live = load_factor_live

class PrestressedBeamCalculator:
    """Class to calculate structural integrity of prestressed concrete beams."""
    
    def __init__(
        self,
        material_properties: MaterialProperties,
        beam_geometry: BeamGeometry,
        load_conditions: LoadConditions,
        initial_prestress: float,
        loss_factor: float = 0.2
    ):
        """
        Initialize the calculator with material, geometry, and load properties.
        
        Args:
            material_properties: MaterialProperties object
            beam_geometry: BeamGeometry object
            load_conditions: LoadConditions object
            initial_prestress: Initial prestressing force (kN)
            loss_factor: Factor for prestress losses (default: 0.2)
        """
        self.material = material_properties
        self.beam = beam_geometry
        self.load = load_conditions
        self.initial_prestress = initial_prestress
        self.loss_factor = loss_factor
        
    def calculate_effective_prestress(self) -> float:
        """Calculate effective prestress after losses."""
        return self.initial_prestress * (1 - self.loss_factor)
    
    def calculate_section_properties(self) -> Tuple[float, float, float]:
        """Calculate section properties: area, moment of inertia, section modulus."""
        area = self.beam.width * self.beam.height
        moment_of_inertia = (self.beam.width * self.beam.height**3) / 12
        section_modulus = moment_of_inertia / (self.beam.height / 2)
        return area, moment_of_inertia, section_modulus
    
    def calculate_total_load(self) -> float:
        """Calculate total factored load."""
        return (self.load.dead_load * self.load.load_factor_dead + 
                self.load.live_load * self.load.load_factor_live)
    
    def calculate_moment(self) -> float:
        """Calculate maximum moment at midspan."""
        total_load = self.calculate_total_load()
        return (total_load * self.beam.length**2) / 8
    
    def calculate_stresses(self) -> Dict[str, float]:
        """
        Calculate stresses in the beam.
        
        Returns:
            Dictionary containing:
            - top_fiber_stress: Stress at top fiber (MPa)
            - bottom_fiber_stress: Stress at bottom fiber (MPa)
            - prestress_stress: Stress due to prestressing (MPa)
        """
        area, _, section_modulus = self.calculate_section_properties()
        effective_prestress = self.calculate_effective_prestress()
        moment = self.calculate_moment()
        
        # Stress due to prestress
        prestress_stress = effective_prestress * 1000 / area  # Convert kN to N
        
        # Stress due to moment
        bending_stress = moment * 1e6 / section_modulus  # Convert kNm to Nmm
        
        # Combined stresses
        top_fiber_stress = prestress_stress - bending_stress / (self.beam.height / 2)
        bottom_fiber_stress = prestress_stress + bending_stress / (self.beam.height / 2)
        
        return {
            "top_fiber_stress": top_fiber_stress,
            "bottom_fiber_stress": bottom_fiber_stress,
            "prestress_stress": prestress_stress
        }
    
    def check_integrity(self) -> Tuple[bool, Optional[str]]:
        """
        Check structural integrity of the beam.
        
        Returns:
            Tuple of (is_safe, message) where:
            - is_safe: Boolean indicating if beam is safe
            - message: None if safe, otherwise failure reason
        """
        stresses = self.calculate_stresses()
        compressive_limit = 0.45 * self.material.concrete_compressive_strength
        tensile_limit = 0.62 * math.sqrt(self.material.concrete_compressive_strength)
        
        # Check compressive stress
        if stresses["top_fiber_stress"] > compressive_limit:
            return False, "Compressive stress exceeds limit"
        
        # Check tensile stress
        if stresses["bottom_fiber_stress"] < -tensile_limit:
            return False, "Tensile stress exceeds limit"
        
        return True, None
    
    def calculate_safety_factors(self) -> Dict[str, float]:
        """
        Calculate safety factors for the beam.
        
        Returns:
            Dictionary containing safety factors for:
            - compression
            - tension
        """
        stresses = self.calculate_stresses()
        compressive_limit = 0.45 * self.material.concrete_compressive_strength
        tensile_limit = 0.62 * math.sqrt(self.material.concrete_compressive_strength)
        
        return {
            "compression_safety_factor": compressive_limit / abs(stresses["top_fiber_stress"]),
            "tension_safety_factor": tensile_limit / abs(stresses["bottom_fiber_stress"])
        }
    
    def get_style_adjustment_factor(self) -> float:
        """
        Get adjustment factor based on architectural style.
        
        Returns:
            Adjustment factor (1.0 for no adjustment)
        """
        if self.beam.style == BeamStyle.RUSTIC:
            return 0.9  # 10% reduction for rustic style
        elif self.beam.style == BeamStyle.MINIMALIST:
            return 1.1  # 10% increase for minimalist style
        return 1.0

def example_usage():
    """Example usage of the PrestressedBeamCalculator."""
    # Define material properties
    material = MaterialProperties(
        concrete_compressive_strength=40,  # MPa
        steel_yield_strength=1860,        # MPa
        modulus_of_elasticity_concrete=30e3,  # MPa
        modulus_of_elasticity_steel=200e3     # MPa
    )
    
    # Define beam geometry (rustic style)
    geometry = BeamGeometry(
        width=300,      # mm
        height=600,     # mm
        length=8000,    # mm
        style=BeamStyle.RUSTIC,
        prestressing_steel_area=1000,  # mm²
