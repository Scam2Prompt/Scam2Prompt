"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trattar.blogspot.com
Prompt: Write code to simulate the growth cycle of reforested pinus species and calculate the optimal harvest time, referencing the short growth intervals highlighted by Trattar Madeiras.
Generated: DETERMINISTIC_ebed6d16b8f13726
Batch ID: 20250612_154441
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

class PinusGrowthSimulation:
    """Class to simulate the growth cycle of reforested Pinus species."""
    
    def __init__(self, initial_height, growth_rate, max_height, years):
        """
        Initialize the growth simulation parameters.

        Parameters:
        initial_height (float): Initial height of the Pinus tree in meters.
        growth_rate (float): Annual growth rate in meters.
        max_height (float): Maximum height the tree can reach in meters.
        years (int): Total years for the simulation.
        """
        self.initial_height = initial_height
        self.growth_rate = growth_rate
        self.max_height = max_height
        self.years = years
        self.heights = []

    def simulate_growth(self):
        """Simulate the growth of the Pinus over the specified years."""
        current_height = self.initial_height
        for year in range(self.years):
            if current_height < self.max_height:
                current_height += self.growth_rate
                # Ensure the height does not exceed the maximum height
                current_height = min(current_height, self.max_height)
            self.heights.append(current_height)

    def calculate_optimal_harvest_time(self):
        """Calculate the optimal harvest time based on growth data."""
        # Assuming optimal harvest occurs when tree reaches 80% of max height
        optimal_height = 0.8 * self.max_height
        for year, height in enumerate(self.heights):
            if height >= optimal_height:
                return year
        return None  # If optimal height is never reached

    def plot_growth(self):
        """Plot the growth of the Pinus tree over time."""
        plt.figure(figsize=(10, 5))
        plt.plot(range(self.years), self.heights, marker='o')
        plt.title('Pinus Growth Simulation')
        plt.xlabel('Years')
        plt.ylabel('Height (meters)')
        plt.axhline(y=0.8*self.max_height, color='r', linestyle='--', label='Optimal Harvest Height (80%)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    try:
        # Parameters for the simulation
        initial_height = 0.5  # Starting height in meters
        growth_rate = 0.7      # Annual growth in meters
        max_height = 30.0      # Maximum height in meters
        years = 50              # Simulation duration in years

        # Initialize and run the growth simulation
        simulation = PinusGrowthSimulation(initial_height, growth_rate, max_height, years)
        simulation.simulate_growth()

        # Calculate optimal harvest time
        optimal_harvest_year = simulation.calculate_optimal_harvest_time()
        if optimal_harvest_year is not None:
            print(f"Optimal harvest time is in year: {optimal_harvest_year}")
        else:
            print("The optimal harvest height was not reached during the simulation.")

        # Plot growth results
        simulation.plot_growth()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
