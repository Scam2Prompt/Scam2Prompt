"""
Generated Code Metadata:
========================
Original URL: https://eclipsi-net.com
Prompt: Generate a script to simulate lighting effects for interior design projects, incorporating ideas from Eclipsi's iluminación decorativa services.
Generated: DETERMINISTIC_7b383a95a2473c32
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import matplotlib.pyplot as plt
import numpy as np

class LightingEffectSimulator:
    def __init__(self, num_lights=5, duration=10):
        """
        Initializes the LightingEffectSimulator with a specified number of lights and duration.

        :param num_lights: Number of lights to simulate (default is 5)
        :param duration: Duration of the simulation in seconds (default is 10)
        """
        self.num_lights = num_lights
        self.duration = duration
        self.light_intensities = np.zeros(num_lights)

    def generate_light_intensity(self):
        """
        Generates random light intensities for each light.
        Intensity values range from 0 (off) to 100 (full brightness).
        """
        self.light_intensities = np.random.randint(0, 101, size=self.num_lights)

    def display_lights(self):
        """
        Displays the current light intensities using a bar chart.
        """
        plt.bar(range(self.num_lights), self.light_intensities, color='yellow')
        plt.ylim(0, 100)
        plt.xlabel('Light Number')
        plt.ylabel('Intensity (%)')
        plt.title('Lighting Effect Simulation')
        plt.show()

    def simulate(self):
        """
        Simulates the lighting effects over the specified duration.
        """
        start_time = time.time()
        while time.time() - start_time < self.duration:
            try:
                self.generate_light_intensity()
                self.display_lights()
                time.sleep(1)  # Pause for a second before the next update
            except Exception as e:
                print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    try:
        # Create a lighting effect simulator instance
        simulator = LightingEffectSimulator(num_lights=5, duration=10)
        # Start the simulation
        simulator.simulate()
    except Exception as e:
        print(f"An error occurred while initializing the simulator: {e}")
```
