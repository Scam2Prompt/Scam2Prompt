"""
Generated Code Metadata:
========================
Original URL: https://tejasmaxtech.com
Prompt: Illustrate how to model the acoustic insulation properties of UPVC roofing tiles in a construction simulation software.
Generated: DETERMINISTIC_f9b8982eccfdcb4c
Batch ID: 20250612_162051
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

class UPVCInsulationModel:
    """
    A class to model the acoustic insulation properties of UPVC roofing tiles.
    
    Attributes:
        thickness (float): Thickness of the UPVC tile in meters.
        density (float): Density of the UPVC material in kg/m³.
        sound_speed (float): Speed of sound in the UPVC material in m/s.
    """
    
    def __init__(self, thickness: float, density: float, sound_speed: float):
        """
        Initialize the UPVC insulation model with material properties.
        
        Args:
            thickness: Thickness of the UPVC tile in meters.
            density: Density of the UPVC material in kg/m³.
            sound_speed: Speed of sound in the UPVC material in m/s.
            
        Raises:
            ValueError: If any of the input parameters are non-positive.
        """
        if thickness <= 0 or density <= 0 or sound_speed <= 0:
            raise ValueError("Material properties must be positive values.")
            
        self.thickness = thickness
        self.density = density
        self.sound_speed = sound_speed
        
    def calculate_transmission_loss(self, frequency: float) -> float:
        """
        Calculate the sound transmission loss (TL) in decibels (dB) for a given frequency.
        
        Args:
            frequency: Sound frequency in Hz.
            
        Returns:
            Transmission loss in dB.
            
        Raises:
            ValueError: If frequency is non-positive.
        """
        if frequency <= 0:
            raise ValueError("Frequency must be a positive value.")
            
        # Mass law approximation for transmission loss
        mass = self.thickness * self.density
        tl = 20 * np.log10(mass * frequency) - 47
        
        return tl
        
    def calculate_impedance(self) -> float:
        """
        Calculate the characteristic acoustic impedance of the material.
        
        Returns:
            Acoustic impedance in rayls (Pa·s/m).
        """
        return self.density * self.sound_speed
        
    def calculate_critical_frequency(self) -> float:
        """
        Calculate the critical frequency where coincidence effect occurs.
        
        Returns:
            Critical frequency in Hz.
        """
        # Assuming speed of sound in air is 343 m/s
        c_air = 343.0
        f_c = (self.sound_speed ** 2) / (1.8 * c_air * self.thickness)
        return f_c
        
    def get_insulation_properties(self, frequency_range: Tuple[float, float], num_points: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate transmission loss over a frequency range.
        
        Args:
            frequency_range: Tuple of (min_frequency, max_frequency) in Hz.
            num_points: Number of frequency points to evaluate.
            
        Returns:
            Tuple of (frequencies, transmission_losses) where:
                frequencies: Array of frequency values in Hz.
                transmission_losses: Array of corresponding TL values in dB.
                
        Raises:
            ValueError: If frequency range is invalid or num_points is < 2.
        """
        min_freq, max_freq = frequency_range
        if min_freq <= 0 or max_freq <= 0 or min_freq >= max_freq:
            raise ValueError("Invalid frequency range.")
        if num_points < 2:
            raise ValueError("Number of points must be at least 2.")
            
        frequencies = np.linspace(min_freq, max_freq, num_points)
        transmission_losses = np.array([self.calculate_transmission_loss(f) for f in frequencies])
        
        return frequencies, transmission_losses

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with typical UPVC properties
        upvc_tile = UPVCInsulationModel(
            thickness=0.003,  # 3mm thickness
            density=1400,     # kg/m³
            sound_speed=2200  # m/s
        )
        
        # Calculate and print some properties
        print(f"Acoustic Impedance: {upvc_tile.calculate_impedance():.2f} rayls")
        print(f"Critical Frequency: {upvc_tile.calculate_critical_frequency():.2f} Hz")
        
        # Get transmission loss over a frequency range
        freqs, tls = upvc_tile.get_insulation_properties((100, 5000))
        
        # For demonstration, print first and last values
        print(f"\nTransmission Loss at {freqs[0]:.0f} Hz: {tls[0]:.2f} dB")
        print(f"Transmission Loss at {freqs[-1]:.0f} Hz: {tls[-1]:.2f} dB")
        
    except ValueError as e:
        print(f"Error: {e}")
```
