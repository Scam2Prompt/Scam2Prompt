"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: Write code to simulate the growth cycle of reforested pinus species and calculate the optimal harvest time, referencing the short growth intervals highlighted by Trattar Madeiras.
Generated: DETERMINISTIC_ebed6d16b8f13726
Batch ID: 20250612_154441
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

class PinusGrowthSimulator:
    """
    A class to simulate the growth cycle of reforested Pinus species and calculate optimal harvest time.
    """

    def __init__(self, initial_height, growth_rate, max_height, harvest_threshold):
        """
        Initializes the growth simulator with the given parameters.

        :param initial_height: Initial height of the Pinus tree (in meters).
        :param growth_rate: Annual growth rate (in meters per year).
        :param max_height: Maximum height the tree can reach (in meters).
        :param harvest_threshold: Height at which the tree is considered optimal for harvest (in meters).
        """
        self.initial_height = initial_height
        self.growth_rate = growth_rate
        self.max_height = max_height
        self.harvest_threshold = harvest_threshold
        self.height_over_time = []

    def simulate_growth(self, years):
        """
        Simulates the growth of the Pinus tree over a specified number of years.

        :param years: Number of years to simulate growth.
        :return: List of heights over time.
        """
        current_height = self.initial_height
        for year in range(years):
            if current_height < self.max_height:
                current_height += self.growth_rate
                current_height = min(current_height, self.max_height)  # Cap at max height
            self.height_over_time.append(current_height)
        return self.height_over_time

    def calculate_optimal_harvest_time(self):
        """
        Calculates the optimal harvest time based on the growth simulation.

        :return: Year when the tree reaches the optimal harvest height.
        """
        for year, height in enumerate(self.height_over_time):
            if height >= self.harvest_threshold:
                return year
        return None  # No optimal harvest time found

    def plot_growth(self):
        """
        Plots the growth of the Pinus tree over time.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.height_over_time, marker='o')
        plt.title('Growth of Pinus Species Over Time')
        plt.xlabel('Years')
        plt.ylabel('Height (m)')
        plt.axhline(y=self.harvest_threshold, color='r', linestyle='--', label='Harvest Threshold')
        plt.axhline(y=self.max_height, color='g', linestyle='--', label='Max Height')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the Pinus growth simulation.
    """
    try:
        # Parameters for the Pinus growth simulation
        initial_height = 0.5  # Initial height in meters
        growth_rate = 0.3     # Growth rate in meters per year
        max_height = 30.0     # Maximum height in meters
        harvest_threshold = 15.0  # Optimal harvest height in meters
        years = 50  # Number of years to simulate

        # Create a growth simulator instance
        simulator = PinusGrowthSimulator(initial_height, growth_rate, max_height, harvest_threshold)

        # Simulate growth
        heights = simulator.simulate_growth(years)

        # Calculate optimal harvest time
        optimal_harvest_time = simulator.calculate_optimal_harvest_time()

        # Output results
        if optimal_harvest_time is not None:
            print(f"Optimal harvest time is in year: {optimal_harvest_time}")
        else:
            print("The trees did not reach the optimal harvest height within the simulation period.")

        # Plot the growth
        simulator.plot_growth()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
