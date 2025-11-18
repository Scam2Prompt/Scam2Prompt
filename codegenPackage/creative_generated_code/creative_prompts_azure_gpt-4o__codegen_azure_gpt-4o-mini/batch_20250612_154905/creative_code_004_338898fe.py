"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Write code to model the beam angle distribution of LED Panel Lights using the specifications provided by Credible BD, including CCT and luminous flux.
Generated: DETERMINISTIC_338898fe7cd51856
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class LEDPanelLight:
    """
    Class to model the beam angle distribution of LED Panel Lights.
    
    Attributes:
        cct (int): Correlated Color Temperature in Kelvin.
        luminous_flux (float): Luminous flux in lumens.
        beam_angle (float): Beam angle in degrees.
    """
    
    def __init__(self, cct: int, luminous_flux: float, beam_angle: float):
        """
        Initializes the LEDPanelLight instance with specified CCT, luminous flux, and beam angle.
        
        Parameters:
            cct (int): Correlated Color Temperature in Kelvin.
            luminous_flux (float): Luminous flux in lumens.
            beam_angle (float): Beam angle in degrees.
        """
        if cct <= 0:
            raise ValueError("CCT must be a positive integer.")
        if luminous_flux <= 0:
            raise ValueError("Luminous flux must be a positive number.")
        if not (0 < beam_angle <= 180):
            raise ValueError("Beam angle must be between 0 and 180 degrees.")
        
        self.cct = cct
        self.luminous_flux = luminous_flux
        self.beam_angle = beam_angle

    def calculate_distribution(self, num_points=100):
        """
        Calculates the beam angle distribution based on the beam angle.
        
        Parameters:
            num_points (int): Number of points to calculate in the distribution.
        
        Returns:
            tuple: angles (numpy array), intensity (numpy array) representing the distribution.
        """
        # Generate angles from -beam_angle/2 to beam_angle/2
        angles = np.linspace(-self.beam_angle / 2, self.beam_angle / 2, num_points)
        # Calculate intensity distribution using a cosine function (normalized)
        intensity = (self.luminous_flux / np.pi) * np.cos(np.radians(angles))
        intensity[intensity < 0] = 0  # Ensure non-negative intensity values
        
        return angles, intensity

    def plot_distribution(self):
        """
        Plots the beam angle distribution of the LED panel light.
        """
        angles, intensity = self.calculate_distribution()
        
        plt.figure(figsize=(10, 5))
        plt.plot(angles, intensity, label=f"CCT: {self.cct}K, Luminous Flux: {self.luminous_flux}lm")
        plt.title("Beam Angle Distribution of LED Panel Light")
        plt.xlabel("Beam Angle (degrees)")
        plt.ylabel("Intensity (lumens)")
        plt.axhline(0, color='grey', lw=0.5, ls='--')
        plt.axvline(0, color='red', lw=0.5, ls='--', label='Peak angle')
        plt.legend()
        plt.grid()
        plt.xlim(-self.beam_angle / 2 - 10, self.beam_angle / 2 + 10)
        plt.ylim(0, self.luminous_flux)
        plt.show()


# Example usage of the LEDPanelLight class
if __name__ == "__main__":
    try:
        panel_light = LEDPanelLight(cct=4000, luminous_flux=2000, beam_angle=120)
        panel_light.plot_distribution()
    except ValueError as e:
        print(f"Error: {e}")
```
