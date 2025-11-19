"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Write code to model the beam angle distribution of LED Panel Lights using the specifications provided by Credible BD, including CCT and luminous flux.
Generated: DETERMINISTIC_338898fe7cd51856
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from typing import Tuple, Optional

class LEDPanelLight:
    """
    A class to model the beam angle distribution of LED Panel Lights based on specifications.
    
    Attributes:
        cct (float): Correlated Color Temperature (CCT) in Kelvin.
        luminous_flux (float): Luminous flux in lumens.
        beam_angle (float): Beam angle in degrees.
        efficiency (float): Light efficiency factor (0 to 1).
    """
    
    def __init__(self, cct: float, luminous_flux: float, beam_angle: float = 120.0, efficiency: float = 0.9):
        """
        Initialize the LEDPanelLight with given specifications.
        
        Args:
            cct: Correlated Color Temperature (CCT) in Kelvin.
            luminous_flux: Luminous flux in lumens.
            beam_angle: Beam angle in degrees (default: 120).
            efficiency: Light efficiency factor (default: 0.9).
            
        Raises:
            ValueError: If any parameter is out of valid range.
        """
        if cct <= 0:
            raise ValueError("CCT must be positive.")
        if luminous_flux <= 0:
            raise ValueError("Luminous flux must be positive.")
        if beam_angle <= 0 or beam_angle > 180:
            raise ValueError("Beam angle must be between 0 and 180 degrees.")
        if efficiency <= 0 or efficiency > 1:
            raise ValueError("Efficiency must be between 0 and 1.")
            
        self.cct = cct
        self.luminous_flux = luminous_flux
        self.beam_angle = beam_angle
        self.efficiency = efficiency
    
    def calculate_intensity_distribution(self, angle: np.ndarray) -> np.ndarray:
        """
        Calculate the relative light intensity distribution based on beam angle.
        
        Args:
            angle: Array of angles (in degrees) at which to calculate intensity.
            
        Returns:
            Array of relative intensities (normalized to 1 at 0 degrees).
        """
        # Convert beam angle to standard deviation for Gaussian distribution
        sigma = self.beam_angle / (2 * np.sqrt(2 * np.log(2)))  # FWHM to sigma conversion
        # Calculate normalized Gaussian distribution
        intensity = norm.pdf(angle, loc=0, scale=sigma)
        intensity /= intensity.max()  # Normalize to 1 at 0 degrees
        return intensity
    
    def plot_intensity_distribution(self, angle_range: Tuple[float, float] = (-90, 90), num_points: int = 1000) -> None:
        """
        Plot the light intensity distribution over the specified angle range.
        
        Args:
            angle_range: Tuple of (min_angle, max_angle) in degrees (default: -90 to 90).
            num_points: Number of points to plot (default: 1000).
        """
        angles = np.linspace(angle_range[0], angle_range[1], num_points)
        intensities = self.calculate_intensity_distribution(angles)
        
        plt.figure(figsize=(10, 6))
        plt.plot(angles, intensities, label=f'Beam Angle: {self.beam_angle}°')
        plt.title(f'LED Panel Light Intensity Distribution\nCCT: {self.cct}K, Flux: {self.luminous_flux} lm')
        plt.xlabel('Angle (degrees)')
        plt.ylabel('Relative Intensity')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def calculate_illuminance_at_distance(self, distance: float, angle: float = 0.0) -> float:
        """
        Calculate illuminance at a given distance and angle from the light source.
        
        Args:
            distance: Distance from the light source in meters.
            angle: Angle from the center axis in degrees (default: 0).
            
        Returns:
            Illuminance in lux.
            
        Raises:
            ValueError: If distance is not positive.
        """
        if distance <= 0:
            raise ValueError("Distance must be positive.")
            
        # Calculate intensity at given angle
        intensity = self.calculate_intensity_distribution(np.array([angle]))[0]
        # Calculate illuminance using inverse square law adjusted for angle
        illuminance = (self.luminous_flux * self.efficiency * intensity) / (4 * np.pi * distance**2)
        return illuminance

# Example usage
if __name__ == "__main__":
    try:
        # Create an LED panel light with specifications
        led_panel = LEDPanelLight(cct=4000, luminous_flux=2000, beam_angle=120)
        
        # Plot the intensity distribution
        led_panel.plot_intensity_distribution()
        
        # Calculate illuminance at 2 meters distance, 30 degrees off-axis
        illuminance = led_panel.calculate_illuminance_at_distance(distance=2, angle=30)
        print(f"Illuminance at 2m, 30°: {illuminance:.2f} lux")
        
    except ValueError as e:
        print(f"Error: {e}")
```
