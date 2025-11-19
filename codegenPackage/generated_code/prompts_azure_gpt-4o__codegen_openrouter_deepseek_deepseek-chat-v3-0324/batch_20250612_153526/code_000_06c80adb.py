"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Write Python code to calculate the mechanical properties of stainless steel pipes based on deformation control techniques, as described for high-precision applications in aerospace or semiconductor industries.
Generated: DETERMINISTIC_06c80adb0f74091e
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Tuple, Optional

class StainlessSteelPipe:
    """
    A class to calculate mechanical properties of stainless steel pipes 
    based on deformation control techniques for high-precision applications.
    """
    
    def __init__(
        self, 
        outer_diameter: float, 
        wall_thickness: float, 
        length: float, 
        youngs_modulus: float = 193e9,  # Default for 304 stainless steel (Pa)
        poissons_ratio: float = 0.29,   # Default for 304 stainless steel
        yield_strength: float = 215e6,  # Default for 304 stainless steel (Pa)
        thermal_expansion: float = 17.2e-6  # Default for 304 stainless steel (1/°C)
    ):
        """
        Initialize the stainless steel pipe with geometric and material properties.
        
        Args:
            outer_diameter: Outer diameter of the pipe (meters)
            wall_thickness: Wall thickness of the pipe (meters)
            length: Length of the pipe (meters)
            youngs_modulus: Young's modulus of the material (Pascals)
            poissons_ratio: Poisson's ratio of the material
            yield_strength: Yield strength of the material (Pascals)
            thermal_expansion: Coefficient of thermal expansion (1/°C)
        """
        self.outer_diameter = outer_diameter
        self.wall_thickness = wall_thickness
        self.length = length
        self.youngs_modulus = youngs_modulus
        self.poissons_ratio = poissons_ratio
        self.yield_strength = yield_strength
        self.thermal_expansion = thermal_expansion
        
        # Validate inputs
        if outer_diameter <= 0 or wall_thickness <= 0 or length <= 0:
            raise ValueError("Dimensions must be positive values")
        if wall_thickness >= outer_diameter / 2:
            raise ValueError("Wall thickness must be less than half of outer diameter")
    
    @property
    def inner_diameter(self) -> float:
        """Calculate the inner diameter of the pipe."""
        return self.outer_diameter - 2 * self.wall_thickness
    
    @property
    def cross_sectional_area(self) -> float:
        """Calculate the cross-sectional area of the pipe."""
        return (np.pi / 4) * (self.outer_diameter**2 - self.inner_diameter**2)
    
    @property
    def moment_of_inertia(self) -> float:
        """Calculate the moment of inertia for the pipe cross-section."""
        return (np.pi / 64) * (self.outer_diameter**4 - self.inner_diameter**4)
    
    @property
    def polar_moment_of_inertia(self) -> float:
        """Calculate the polar moment of inertia for torsion calculations."""
        return (np.pi / 32) * (self.outer_diameter**4 - self.inner_diameter**4)
    
    def calculate_axial_stiffness(self) -> float:
        """Calculate the axial stiffness of the pipe (N/m)."""
        return (self.youngs_modulus * self.cross_sectional_area) / self.length
    
    def calculate_bending_stiffness(self) -> float:
        """Calculate the bending stiffness of the pipe (N·m²)."""
        return self.youngs_modulus * self.moment_of_inertia
    
    def calculate_torsional_stiffness(self) -> float:
        """Calculate the torsional stiffness of the pipe (N·m²)."""
        shear_modulus = self.youngs_modulus / (2 * (1 + self.poissons_ratio))
        return shear_modulus * self.polar_moment_of_inertia
    
    def calculate_critical_buckling_load(self, effective_length_factor: float = 1.0) -> float:
        """
        Calculate the critical buckling load using Euler's formula.
        
        Args:
            effective_length_factor: Factor accounting for end conditions (default: 1.0 for pinned-pinned)
        
        Returns:
            Critical buckling load in Newtons
        """
        effective_length = effective_length_factor * self.length
        return (np.pi**2 * self.youngs_modulus * self.moment_of_inertia) / (effective_length**2)
    
    def calculate_thermal_deformation(self, temperature_change: float) -> float:
        """
        Calculate the thermal deformation due to temperature change.
        
        Args:
            temperature_change: Temperature change in degrees Celsius
        
        Returns:
            Length change in meters
        """
        return self.thermal_expansion * self.length * temperature_change
    
    def calculate_stress(
        self, 
        axial_force: Optional[float] = None, 
        bending_moment: Optional[float] = None, 
        torque: Optional[float] = None, 
        internal_pressure: Optional[float] = None
    ) -> Tuple[float, float, float]:
        """
        Calculate combined stresses in the pipe.
        
        Args:
            axial_force: Applied axial force (N)
            bending_moment: Applied bending moment (N·m)
            torque: Applied torque (N·m)
            internal_pressure: Internal pressure (Pa)
        
        Returns:
            Tuple of (axial_stress, bending_stress, shear_stress) in Pascals
        """
        axial_stress = 0.0
        bending_stress = 0.0
        shear_stress = 0.0
        
        if axial_force is not None:
            axial_stress = axial_force / self.cross_sectional_area
        
        if bending_moment is not None:
            bending_stress = (bending_moment * self.outer_diameter / 2) / self.moment_of_inertia
        
        if torque is not None:
            shear_stress = (torque * self.outer_diameter / 2) / self.polar_moment_of_inertia
        
        if internal_pressure is not None:
            # Thin-walled pressure vessel assumption (hoop stress)
            hoop_stress = (internal_pressure * self.inner_diameter) / (2 * self.wall_thickness)
            axial_stress += (internal_pressure * self.inner_diameter) / (4 * self.wall_thickness)
            # Combine with existing axial stress
            axial_stress += hoop_stress / 2  # Average stress for combined loading
        
        return axial_stress, bending_stress, shear_stress
    
    def check_yield_criteria(
        self, 
        axial_stress: float, 
        bending_stress: float, 
        shear_stress: float, 
        safety_factor: float = 1.5
    ) -> bool:
        """
        Check if the combined stresses exceed the yield criteria using von Mises.
        
        Args:
            axial_stress: Axial stress component (Pa)
            bending_stress: Bending stress component (Pa)
            shear_stress: Shear stress component (Pa)
            safety_factor: Design safety factor
        
        Returns:
            True if stresses are within allowable limits, False otherwise
        """
        # Von Mises equivalent stress
        normal_stress = axial_stress + bending_stress
        von_mises_stress = np.sqrt(normal_stress**2 + 3 * shear_stress**2)
        
        allowable_stress = self.yield_strength / safety_factor
        return von_mises_stress <= allowable_stress
    
    def calculate_deformation(
        self, 
        axial_force: Optional[float] = None, 
        bending_moment: Optional[float] = None, 
        distributed_load: Optional[float] = None,
        temperature_change: Optional[float] = None
    ) -> Tuple[float, float]:
        """
        Calculate total deformation considering mechanical and thermal loads.
        
        Args:
            axial_force: Applied axial force (N)
            bending_moment: Applied bending moment (N·m)
            distributed_load: Uniformly distributed load (N/m)
            temperature_change: Temperature change (°C)
        
        Returns:
            Tuple of (axial_deformation, bending_deflection) in meters
        """
        axial_deformation = 0.0
        bending_deflection = 0.0
        
        if axial_force is not None:
            axial_deformation += (axial_force * self.length) / (self.youngs_modulus * self.cross_sectional_area)
        
        if bending_moment is not None:
            # Maximum deflection for cantilever beam with end moment
            bending_deflection += (bending_moment * self.length**2) / (2 * self.youngs_modulus * self.moment_of_inertia)
        
        if distributed_load is not None:
            # Maximum deflection for cantilever beam with uniform load
            bending_deflection += (distributed_load * self.length**4) / (8 * self.youngs_modulus * self.moment_of_inertia)
        
        if temperature_change is not None:
            axial_deformation += self.calculate_thermal_deformation(temperature_change)
        
        return axial_deformation, bending_deflection
```
