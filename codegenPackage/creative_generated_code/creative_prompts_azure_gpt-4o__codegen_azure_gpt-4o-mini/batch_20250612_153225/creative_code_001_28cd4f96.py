"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Recommend an API or library to simulate 3D LED flames for electric fireplaces, including options for customizable color and intensity.
Generated: DETERMINISTIC_28cd4f9652b505ab
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import numpy as np
import matplotlib.pyplot as plt

class FlameSimulator:
    """
    A class to simulate 3D LED flames for electric fireplaces.
    
    Attributes:
        color (tuple): RGB color for the flames.
        intensity (float): Intensity of the flames (0.0 to 1.0).
        flame_height (int): Height of the flame simulation.
        flame_width (int): Width of the flame simulation.
    """

    def __init__(self, color=(255, 140, 0), intensity=1.0, flame_height=10, flame_width=10):
        """
        Initializes the FlameSimulator with customizable color and intensity.
        
        Parameters:
            color (tuple): RGB color for the flames (default: orange).
            intensity (float): Intensity of the flames (default: 1.0).
            flame_height (int): Height of the flame (default: 10).
            flame_width (int): Width of the flame (default: 10).
        """
        self.color = color
        self.intensity = intensity
        self.flame_height = flame_height
        self.flame_width = flame_width
        
        # Validate color input
        if not all(0 <= c <= 255 for c in self.color):
            raise ValueError("Color values must be between 0 and 255.")
        
        # Validate intensity input
        if not (0.0 <= self.intensity <= 1.0):
            raise ValueError("Intensity must be between 0.0 and 1.0.")

    def generate_flame(self):
        """
        Generates a 3D representation of flames using random intensity and color variations.
        
        Returns:
            np.ndarray: A 3D numpy array representing flame colors.
        """
        # Create a base array for the flame
        flame_array = np.zeros((self.flame_height, self.flame_width, 3), dtype=int)

        for i in range(self.flame_height):
            for j in range(self.flame_width):
                # Randomly reduce the color intensity to simulate flickering
                flicker_intensity = random.uniform(0.5, 1.0) * self.intensity
                flame_array[i, j] = [int(c * flicker_intensity) for c in self.color]

        return flame_array

    def display_flame(self, flame_array):
        """
        Displays the generated flame using matplotlib.
        
        Parameters:
            flame_array (np.ndarray): The 3D numpy array representing the flame colors.
        """
        plt.imshow(flame_array)
        plt.axis('off')  # Hide axes
        plt.show()

    def run_simulation(self, duration=10):
        """
        Runs the flame simulation for a given duration.
        
        Parameters:
            duration (int): Duration of the simulation in seconds (default: 10).
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            flame = self.generate_flame()
            self.display_flame(flame)
            time.sleep(0.2)  # Add slight delay for simulating flame flicker

# Example usage
if __name__ == "__main__":
    try:
        simulator = FlameSimulator(color=(255, 69, 0), intensity=0.8, flame_height=20, flame_width=20)
        simulator.run_simulation(duration=15)
    except ValueError as e:
        print(f"Error: {e}")
```
