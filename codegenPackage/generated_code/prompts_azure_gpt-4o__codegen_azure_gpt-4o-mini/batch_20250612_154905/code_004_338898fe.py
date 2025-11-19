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

class LEDPanelLight:
    """
    A class to model the beam angle distribution of LED Panel Lights.

    Attributes:
        cct (float): Correlated Color Temperature in Kelvin.
        luminous_flux (float): Luminous flux in lumens.
        beam_angle (float): Beam angle in degrees.
    """

    def __init__(self, cct: float, luminous_flux: float, beam_angle: float):
        """
        Initializes the LEDPanelLight with specified CCT, luminous flux, and beam angle.

        Args:
            cct (float): Correlated Color Temperature in Kelvin.
            luminous_flux (float): Luminous flux in lumens.
            beam_angle (float): Beam angle in degrees.
        """
        if cct <= 0:
            raise ValueError("CCT must be a positive value.")
        if luminous_flux <= 0:
            raise ValueError("Luminous flux must be a positive value.")
        if beam_angle <= 0 or beam_angle > 180:
            raise ValueError("Beam angle must be between 0 and 180 degrees.")

        self.cct = cct
        self.luminous_flux = luminous_flux
        self.beam_angle = beam_angle

    def calculate_intensity_distribution(self, num_points: int = 360) -> np.ndarray:
        """
        Calculates the intensity distribution of the LED panel light.

        Args:
            num_points (int): Number of points to calculate in the distribution.

        Returns:
            np.ndarray: Array of intensity values corresponding to angles.
        """
        angles = np.linspace(-self.beam_angle / 2, self.beam_angle / 2, num_points)
        intensity = (self.luminous_flux / (self.beam_angle * np.pi / 180)) * np.cos(np.radians(angles))**2
        return angles, intensity

    def plot_distribution(self):
        """
        Plots the beam angle distribution of the LED panel light.
        """
        angles, intensity = self.calculate_intensity_distribution()
        
        plt.figure(figsize=(10, 6))
        plt.plot(angles, intensity, label=f'CCT: {self.cct}K, Flux: {self.luminous_flux}lm', color='blue')
        plt.title('Beam Angle Distribution of LED Panel Light')
        plt.xlabel('Angle (degrees)')
        plt.ylabel('Intensity (lm/sr)')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.xlim(-self.beam_angle / 2, self.beam_angle / 2)
        plt.ylim(0, np.max(intensity) * 1.1)
        plt.grid()
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        led_panel = LEDPanelLight(cct=4000, luminous_flux=3000, beam_angle=120)
        led_panel.plot_distribution()
    except ValueError as e:
        print(f"Error: {e}")
```
