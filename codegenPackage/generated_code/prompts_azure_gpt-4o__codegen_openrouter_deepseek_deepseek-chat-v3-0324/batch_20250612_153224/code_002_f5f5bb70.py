"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate code in Python to calculate tunnel stability using geotechnical parameters such as rock density, stress distribution, and excavation depth, which align with the underground construction services offered by URANPRES.
Generated: DETERMINISTIC_f5f5bb70f657fbb2
Batch ID: 20250612_153224
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

class TunnelStabilityCalculator:
    """
    A class to calculate tunnel stability based on geotechnical parameters.
    Implements methods for stress analysis, safety factor calculation, and stability assessment.
    """
    
    def __init__(self, rock_density: float, depth: float, 
                 cohesion: float, friction_angle: float, 
                 tunnel_radius: float, 
                 horizontal_stress_ratio: float = 1.0):
        """
        Initialize the calculator with geotechnical parameters.
        
        Args:
            rock_density: Density of the rock (kg/m³)
            depth: Depth of tunnel excavation (m)
            cohesion: Cohesion of the rock mass (Pa)
            friction_angle: Internal friction angle of the rock mass (degrees)
            tunnel_radius: Radius of the tunnel (m)
            horizontal_stress_ratio: Ratio of horizontal to vertical stress (K₀)
        """
        self.rock_density = rock_density
        self.depth = depth
        self.cohesion = cohesion
        self.friction_angle = np.radians(friction_angle)
        self.tunnel_radius = tunnel_radius
        self.horizontal_stress_ratio = horizontal_stress_ratio
        self.gravity = 9.81  # m/s²
        
        # Validate inputs
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input parameters for physical feasibility."""
        if self.rock_density <= 0:
            raise ValueError("Rock density must be positive")
        if self.depth <= 0:
            raise ValueError("Depth must be positive")
        if self.cohesion < 0:
            raise ValueError("Cohesion cannot be negative")
        if not 0 <= self.friction_angle <= np.pi/2:
            raise ValueError("Friction angle must be between 0-90 degrees")
        if self.tunnel_radius <= 0:
            raise ValueError("Tunnel radius must be positive")
        if self.horizontal_stress_ratio <= 0:
            raise ValueError("Horizontal stress ratio must be positive")
    
    def calculate_vertical_stress(self) -> float:
        """
        Calculate vertical stress at tunnel depth.
        
        Returns:
            Vertical stress in Pa
        """
        return self.rock_density * self.gravity * self.depth
    
    def calculate_horizontal_stress(self) -> float:
        """
        Calculate horizontal stress at tunnel depth.
        
        Returns:
            Horizontal stress in Pa
        """
        return self.horizontal_stress_ratio * self.calculate_vertical_stress()
    
    def calculate_hoop_stress(self, radial_distance: float) -> float:
        """
        Calculate hoop (tangential) stress around the tunnel.
        
        Args:
            radial_distance: Distance from tunnel center (m)
            
        Returns:
            Hoop stress in Pa
        """
        if radial_distance <= self.tunnel_radius:
            raise ValueError("Radial distance must be greater than tunnel radius")
            
        sigma_v = self.calculate_vertical_stress()
        sigma_h = self.calculate_horizontal_stress()
        
        # Kirsch solution for hoop stress
        term1 = (sigma_v + sigma_h) * (1 + (self.tunnel_radius**2 / radial_distance**2))
        term2 = (sigma_v - sigma_h) * (1 + (3 * self.tunnel_radius**4 / radial_distance**4))
        
        return term1 - term2
    
    def calculate_radial_stress(self, radial_distance: float) -> float:
        """
        Calculate radial stress around the tunnel.
        
        Args:
            radial_distance: Distance from tunnel center (m)
            
        Returns:
            Radial stress in Pa
        """
        if radial_distance <= self.tunnel_radius:
            raise ValueError("Radial distance must be greater than tunnel radius")
            
        sigma_v = self.calculate_vertical_stress()
        sigma_h = self.calculate_horizontal_stress()
        
        # Kirsch solution for radial stress
        term1 = (sigma_v + sigma_h) * (1 - (self.tunnel_radius**2 / radial_distance**2))
        term2 = (sigma_v - sigma_h) * (1 - (4 * self.tunnel_radius**2 / radial_distance**2) 
                                      + (3 * self.tunnel_radius**4 / radial_distance**4))
        
        return term1 + term2
    
    def calculate_safety_factor(self, radial_distance: float) -> float:
        """
        Calculate safety factor against shear failure at a given radial distance.
        
        Args:
            radial_distance: Distance from tunnel center (m)
            
        Returns:
            Safety factor (dimensionless)
        """
        sigma_theta = self.calculate_hoop_stress(radial_distance)
        sigma_r = self.calculate_radial_stress(radial_distance)
        
        # Mean stress
        sigma_mean = (sigma_theta + sigma_r) / 2
        
        # Shear stress
        tau_max = (sigma_theta - sigma_r) / 2
        
        # Mohr-Coulomb failure criterion
        shear_strength = self.cohesion + sigma_mean * np.tan(self.friction_angle)
        
        if shear_strength <= 0:
            return 0.0  # Immediate failure
            
        return shear_strength / tau_max if tau_max != 0 else float('inf')
    
    def assess_stability(self, min_safety_factor: float = 1.5, 
                         assessment_distance: float = 1.1) -> Tuple[bool, float]:
        """
        Assess tunnel stability based on safety factor.
        
        Args:
            min_safety_factor: Minimum acceptable safety factor
            assessment_distance: Radial distance for assessment (multiple of tunnel radius)
            
        Returns:
            Tuple of (is_stable, safety_factor)
        """
        if assessment_distance <= 1.0:
            raise ValueError("Assessment distance must be >1 times tunnel radius")
            
        radial_distance = self.tunnel_radius * assessment_distance
        safety_factor = self.calculate_safety_factor(radial_distance)
        
        return (safety_factor >= min_safety_factor, safety_factor)
    
    def calculate_plastic_zone_radius(self) -> Optional[float]:
        """
        Calculate radius of plastic zone around tunnel using Kastner's solution.
        
        Returns:
            Radius of plastic zone in meters, or None if no plastic zone forms
        """
        sigma_v = self.calculate_vertical_stress()
        sigma_h = self.calculate_horizontal_stress()
        p0 = (sigma_v + sigma_h) / 2  # Mean in-situ stress
        
        # Kastner's solution parameters
        k = (1 + np.sin(self.friction_angle)) / (1 - np.sin(self.friction_angle))
        A = (2 * self.cohesion * np.cos(self.friction_angle)) / (1 - np.sin(self.friction_angle))
        
        try:
            plastic_radius = self.tunnel_radius * np.exp(
                (2 * (p0 * (k - 1) - A)) / ((k + 1) * (A + self.cohesion / np.tan(self.friction_angle)))
            )
        except (ZeroDivisionError, OverflowError):
            return None
            
        return plastic_radius if plastic_radius > self.tunnel_radius else None


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters for a tunnel in moderate rock
        calculator = TunnelStabilityCalculator(
            rock_density=2500,  # kg/m³
            depth=100,          # m
            cohesion=1e6,       # Pa (1 MPa)
            friction_angle=30,  # degrees
            tunnel_radius=3,    # m
            horizontal_stress_ratio=0.7
        )
        
        # Calculate stresses
        sigma_v = calculator.calculate_vertical_stress()
        sigma_h = calculator.calculate_horizontal_stress()
        print(f"Vertical stress: {sigma_v/1e6:.2f} MPa")
        print(f"Horizontal stress: {sigma_h/1e6:.2f} MPa")
        
        # Assess stability
        is_stable, safety_factor = calculator.assess_stability()
        print(f"Tunnel stable: {is_stable}, Safety factor: {safety_factor:.2f}")
        
        # Plastic zone
        plastic_radius = calculator.calculate_plastic_zone_radius()
        if plastic_radius:
            print(f"Plastic zone radius: {plastic_radius:.2f} m")
        else:
            print("No plastic zone forms")
            
    except ValueError as e:
        print(f"Error in input parameters: {e}")
```
