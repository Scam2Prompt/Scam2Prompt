"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Write a program to design and calculate the slope stability for armirana zelena brežina (reinforced green slopes) using geotechnical parameters.
Generated: DETERMINISTIC_bef53618d96463a4
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

class SlopeStabilityAnalyzer:
    """
    A class to analyze the stability of reinforced green slopes (armirana zelena brežina)
    using geotechnical parameters and Bishop's simplified method.
    """
    
    def __init__(self):
        self.gravity = 9.81  # m/s²
    
    def calculate_slope_stability(
        self,
        slope_angle: float,
        height: float,
        soil_density: float,
        cohesion: float,
        friction_angle: float,
        reinforcement_tensile_strength: Optional[float] = None,
        reinforcement_spacing: Optional[float] = None
    ) -> Tuple[float, float, bool]:
        """
        Calculate the factor of safety for a reinforced green slope.
        
        Args:
            slope_angle: Slope angle in degrees
            height: Height of the slope in meters
            soil_density: Soil density in kN/m³
            cohesion: Cohesion in kPa
            friction_angle: Friction angle in degrees
            reinforcement_tensile_strength: Tensile strength of reinforcement in kN/m (optional)
            reinforcement_spacing: Vertical spacing between reinforcement layers in meters (optional)
            
        Returns:
            Tuple containing:
                - Factor of safety without reinforcement
                - Factor of safety with reinforcement (if applicable)
                - Stability status (True if stable)
        
        Raises:
            ValueError: If input parameters are invalid
        """
        # Validate inputs
        if slope_angle <= 0 or slope_angle >= 90:
            raise ValueError("Slope angle must be between 0 and 90 degrees")
        if height <= 0:
            raise ValueError("Height must be positive")
        if soil_density <= 0:
            raise ValueError("Soil density must be positive")
        if cohesion < 0:
            raise ValueError("Cohesion cannot be negative")
        if friction_angle <= 0 or friction_angle >= 90:
            raise ValueError("Friction angle must be between 0 and 90 degrees")
        
        # Convert angles to radians
        slope_angle_rad = np.radians(slope_angle)
        friction_angle_rad = np.radians(friction_angle)
        
        # Calculate factor of safety without reinforcement (Bishop's simplified method)
        fs_no_reinforcement = self._calculate_bishop_fs(
            slope_angle_rad, height, soil_density, cohesion, friction_angle_rad
        )
        
        # Calculate factor of safety with reinforcement if parameters are provided
        fs_reinforcement = None
        if reinforcement_tensile_strength is not None and reinforcement_spacing is not None:
            if reinforcement_tensile_strength <= 0:
                raise ValueError("Reinforcement tensile strength must be positive")
            if reinforcement_spacing <= 0:
                raise ValueError("Reinforcement spacing must be positive")
                
            fs_reinforcement = self._calculate_reinforced_fs(
                fs_no_reinforcement,
                slope_angle_rad,
                height,
                soil_density,
                reinforcement_tensile_strength,
                reinforcement_spacing
            )
        
        # Determine stability status
        stability_status = (fs_no_reinforcement >= 1.3) and (
            fs_reinforcement is None or fs_reinforcement >= 1.5
        )
        
        return fs_no_reinforcement, fs_reinforcement, stability_status
    
    def _calculate_bishop_fs(
        self,
        slope_angle_rad: float,
        height: float,
        soil_density: float,
        cohesion: float,
        friction_angle_rad: float
    ) -> float:
        """
        Calculate factor of safety using Bishop's simplified method.
        
        Args:
            slope_angle_rad: Slope angle in radians
            height: Height of the slope in meters
            soil_density: Soil density in kN/m³
            cohesion: Cohesion in kPa
            friction_angle_rad: Friction angle in radians
            
        Returns:
            Factor of safety
        """
        # Simplified Bishop's method for circular failure surface
        # Using average values for calculation
        m_alpha = np.cos(slope_angle_rad) + (
            np.sin(slope_angle_rad) * np.tan(friction_angle_rad)
        ) / 1.3  # Initial guess for FS
        
        weight = soil_density * height * height / (2 * np.tan(slope_angle_rad))
        resisting_moment = cohesion * height / np.sin(slope_angle_rad) + weight * np.cos(slope_angle_rad) * np.tan(friction_angle_rad)
        driving_moment = weight * np.sin(slope_angle_rad)
        
        fs = resisting_moment / driving_moment
        
        # Iterative solution for more accurate FS
        for _ in range(5):  # Typically converges in few iterations
            m_alpha = np.cos(slope_angle_rad) + (
                np.sin(slope_angle_rad) * np.tan(friction_angle_rad)
            ) / fs
            fs = (cohesion * height / np.sin(slope_angle_rad) + weight * np.cos(slope_angle_rad) * np.tan(friction_angle_rad) / m_alpha) / driving_moment
        
        return fs
    
    def _calculate_reinforced_fs(
        self,
        fs_no_reinforcement: float,
        slope_angle_rad: float,
        height: float,
        soil_density: float,
        tensile_strength: float,
        spacing: float
    ) -> float:
        """
        Calculate the additional factor of safety provided by reinforcement.
        
        Args:
            fs_no_reinforcement: Factor of safety without reinforcement
            slope_angle_rad: Slope angle in radians
            height: Height of the slope in meters
            soil_density: Soil density in kN/m³
            tensile_strength: Tensile strength of reinforcement in kN/m
            spacing: Vertical spacing between reinforcement layers in meters
            
        Returns:
            Improved factor of safety with reinforcement
        """
        # Number of reinforcement layers
        num_layers = int(height / spacing)
        if num_layers < 1:
            num_layers = 1
        
        # Additional resisting force from reinforcement
        total_reinforcement_force = num_layers * tensile_strength
        
        # Calculate additional resisting moment
        weight = soil_density * height * height / (2 * np.tan(slope_angle_rad))
        driving_moment = weight * np.sin(slope_angle_rad)
        
        # Assume reinforcement acts at mid-height of each layer
        reinforcement_moment = total_reinforcement_force * height / 2
        
        # Improved factor of safety
        fs_reinforced = fs_no_reinforcement + (reinforcement_moment / driving_moment)
        
        return fs_reinforced


def main():
    """Example usage of the SlopeStabilityAnalyzer."""
    analyzer = SlopeStabilityAnalyzer()
    
    try:
        # Example parameters for a green reinforced slope
        slope_angle = 30  # degrees
        height = 10  # meters
        soil_density = 18  # kN/m³
        cohesion = 15  # kPa
        friction_angle = 25  # degrees
        tensile_strength = 50  # kN/m
        spacing = 1  # meters
        
        fs_no_reinf, fs_reinf, stable = analyzer.calculate_slope_stability(
            slope_angle=slope_angle,
            height=height,
            soil_density=soil_density,
            cohesion=cohesion,
            friction_angle=friction_angle,
            reinforcement_tensile_strength=tensile_strength,
            reinforcement_spacing=spacing
        )
        
        print(f"Factor of Safety (no reinforcement): {fs_no_reinf:.2f}")
        print(f"Factor of Safety (with reinforcement): {fs_reinf:.2f}")
        print(f"Slope is {'stable' if stable else 'unstable'}")
        
    except ValueError as e:
        print(f"Error in input parameters: {e}")


if __name__ == "__main__":
    main()
```
