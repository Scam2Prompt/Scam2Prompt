"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Write a Python script to simulate the coverage of a Public Safety ERRCS system in a small building, taking into account the requirements for emergency responder radio communication systems.
Generated: DETERMINISTIC_cd57d6d7133f0b72
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import matplotlib.pyplot as plt
import numpy as np

class ERRCSCoverageSimulator:
    """
    A class to simulate the coverage of a Public Safety Emergency Responder Radio Communication System (ERRCS)
    in a small building.
    """

    def __init__(self, building_width, building_length, num_signals):
        """
        Initializes the simulator with building dimensions and number of signals.

        :param building_width: Width of the building in meters.
        :param building_length: Length of the building in meters.
        :param num_signals: Number of ERRCS signals to simulate.
        """
        self.building_width = building_width
        self.building_length = building_length
        self.num_signals = num_signals
        self.signal_strengths = []

    def generate_signal_strengths(self):
        """
        Generates random signal strengths for the ERRCS signals within the building.
        Signal strengths are simulated as random values between 0 and 100 dBm.
        """
        self.signal_strengths = [random.uniform(0, 100) for _ in range(self.num_signals)]

    def calculate_coverage(self):
        """
        Calculates the coverage area based on the generated signal strengths.
        Coverage is defined as areas where the signal strength is above a certain threshold (e.g., 75 dBm).
        
        :return: A list of tuples representing the coordinates of covered areas.
        """
        coverage_threshold = 75  # dBm
        coverage_areas = []

        for strength in self.signal_strengths:
            if strength >= coverage_threshold:
                # Simulate a random position for the signal coverage
                x = random.uniform(0, self.building_width)
                y = random.uniform(0, self.building_length)
                coverage_areas.append((x, y))

        return coverage_areas

    def plot_coverage(self, coverage_areas):
        """
        Plots the coverage areas on a 2D graph.

        :param coverage_areas: A list of tuples representing the coordinates of covered areas.
        """
        if not coverage_areas:
            print("No coverage areas to plot.")
            return

        x_coords, y_coords = zip(*coverage_areas)

        plt.figure(figsize=(10, 6))
        plt.scatter(x_coords, y_coords, c='green', marker='o', label='Coverage Area')
        plt.xlim(0, self.building_width)
        plt.ylim(0, self.building_length)
        plt.title('ERRCS Coverage Simulation')
        plt.xlabel('Building Width (m)')
        plt.ylabel('Building Length (m)')
        plt.axhline(y=75, color='r', linestyle='--', label='Coverage Threshold (75 dBm)')
        plt.legend()
        plt.grid()
        plt.show()

    def run_simulation(self):
        """
        Runs the ERRCS coverage simulation.
        """
        try:
            self.generate_signal_strengths()
            coverage_areas = self.calculate_coverage()
            self.plot_coverage(coverage_areas)
        except Exception as e:
            print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    # Define building dimensions and number of signals
    building_width = 50  # meters
    building_length = 30  # meters
    num_signals = 20  # number of ERRCS signals

    # Create an instance of the simulator and run the simulation
    simulator = ERRCSCoverageSimulator(building_width, building_length, num_signals)
    simulator.run_simulation()
```
