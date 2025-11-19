"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wilsonelectronics.co
Prompt: Generate code to assess cellular signal coverage using a Distributed Antenna System (DAS) for a large building.
Generated: DETERMINISTIC_b6df06c6f358a771
Batch ID: 20250612_164005
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


class DistributedAntennaSystem:
    def __init__(self, building_dimensions, antenna_locations, signal_strength):
        """
        Initializes the Distributed Antenna System.

        :param building_dimensions: A tuple representing the (width, height) of the building in meters.
        :param antenna_locations: A list of tuples representing the (x, y) coordinates of each antenna in meters.
        :param signal_strength: A float representing the signal strength transmitted by each antenna in dBm.
        """
        self.width, self.height = building_dimensions
        self.antenna_locations = antenna_locations
        self.signal_strength = signal_strength
        self.coverage_map = np.zeros((self.width, self.height))

    def calculate_signal_coverage(self):
        """
        Calculates the signal coverage within the building based on antenna locations and signal strength.
        """
        for antenna in self.antenna_locations:
            x, y = antenna
            for i in range(self.width):
                for j in range(self.height):
                    distance = np.sqrt((x - i) ** 2 + (y - j) ** 2)
                    if distance == 0:
                        continue  # Skip the antenna location itself to avoid infinite signal strength

                    # Simple model: signal strength decreases with distance
                    strength_at_point = self.signal_strength - (20 * np.log10(distance))
                    if strength_at_point > 0:  # Only consider positive signal strength
                        self.coverage_map[i, j] = max(self.coverage_map[i, j], strength_at_point)

    def visualize_coverage(self):
        """
        Visualizes the signal coverage using a heatmap.
        """
        plt.imshow(self.coverage_map, extent=(0, self.width, 0, self.height), origin='lower', cmap='hot')
        plt.colorbar(label='Signal Strength (dBm)')
        plt.title('Cellular Signal Coverage Map')
        plt.xlabel('Width (m)')
        plt.ylabel('Height (m)')
        plt.show()

    def assess_coverage(self, threshold):
        """
        Assesses the coverage of the building based on a signal strength threshold.

        :param threshold: A float representing the minimum acceptable signal strength in dBm for coverage.
        :return: A boolean indicating whether the coverage is acceptable.
        """
        return np.any(self.coverage_map >= threshold)


def main():
    try:
        # Parameters for the building and antennas
        building_dimensions = (100, 50)  # Width: 100m, Height: 50m
        antenna_locations = [(10, 10), (90, 10), (50, 25)]  # Three antennas' locations
        signal_strength = 100  # Signal strength in dBm

        # Instantiate the Distributed Antenna System
        das = DistributedAntennaSystem(building_dimensions, antenna_locations, signal_strength)

        # Calculate signal coverage
        das.calculate_signal_coverage()

        # Visualize the coverage map
        das.visualize_coverage()

        # Assess coverage quality
        threshold = -100  # Minimum acceptable signal strength
        coverage_ok = das.assess_coverage(threshold)
        if coverage_ok:
            print("Coverage is acceptable.")
        else:
            print("Coverage is not acceptable.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
