"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Write a Python program to model the noise reduction features of VinaRoy air blowers, using real-world parameters from the FB250-W model.
Generated: DETERMINISTIC_16f72ea9809ae6f4
Batch ID: 20250612_153224
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

class VinaRoyAirBlower:
    """
    A class to model the noise reduction features of VinaRoy air blowers
    based on real-world parameters from the FB250-W model.
    """

    def __init__(self, power_rating: float, noise_level: float, distance: float):
        """
        Initialize the air blower with given parameters.

        :param power_rating: Power rating of the blower in watts (W)
        :param noise_level: Noise level of the blower in decibels (dB)
        :param distance: Distance from the blower in meters (m)
        """
        self.power_rating = power_rating
        self.noise_level = noise_level
        self.distance = distance

    def calculate_noise_reduction(self) -> float:
        """
        Calculate the noise reduction at a specified distance using the inverse square law.

        :return: Noise level at the specified distance in dB
        """
        if self.distance <= 0:
            raise ValueError("Distance must be greater than zero.")

        # Noise reduction decreases with the square of the distance
        # The formula used is: Lp2 = Lp1 - 20 * log10(d2/d1)
        # Assuming d1 (initial distance) is 1 meter
        initial_distance = 1.0
        noise_reduction = 20 * np.log10(self.distance / initial_distance)

        adjusted_noise_level = self.noise_level - noise_reduction
        return max(adjusted_noise_level, 0)  # Noise level cannot be negative

    def visualize_noise_reduction(self, max_distance: float):
        """
        Visualize the noise reduction over a range of distances.

        :param max_distance: Maximum distance for the visualization in meters
        """
        if max_distance <= 0:
            raise ValueError("Max distance must be greater than zero.")

        distances = np.linspace(1, max_distance, 100)  # Generate distances from 1 to max_distance
        noise_levels = [self.calculate_noise_reduction_at_distance(d) for d in distances]

        plt.figure(figsize=(10, 6))
        plt.plot(distances, noise_levels, label='Noise Level (dB)')
        plt.title('Noise Reduction of VinaRoy FB250-W Air Blower')
        plt.xlabel('Distance from Blower (m)')
        plt.ylabel('Noise Level (dB)')
        plt.ylim(0, self.noise_level)  # Limit y-axis to max noise level
        plt.grid()
        plt.legend()
        plt.show()

    def calculate_noise_reduction_at_distance(self, distance: float) -> float:
        """
        Calculate the noise reduction at a specific distance.

        :param distance: Distance from the blower in meters (m)
        :return: Noise level at the specified distance in dB
        """
        self.distance = distance  # Update distance for calculation
        return self.calculate_noise_reduction()

def main():
    """
    Main function to execute the noise reduction model and visualization.
    """
    # Instantiate the VinaRoy air blower with real-world parameters
    blower = VinaRoyAirBlower(power_rating=2500, noise_level=85, distance=1.0)

    # Calculate and print the noise reduction at a distance of 5 meters
    try:
        noise_at_5m = blower.calculate_noise_reduction_at_distance(5.0)
        print(f"Noise level at 5 meters: {noise_at_5m:.2f} dB")
        
        # Visualize the noise reduction from 1 to 10 meters
        blower.visualize_noise_reduction(max_distance=10.0)
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
