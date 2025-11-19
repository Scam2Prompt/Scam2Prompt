"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: Generate code to simulate the timeline of vegetation regrowth after multiple applications of Capina Elétrica's technology, incorporating the intervals provided (30-45 days, 60-70 days, and 90 days).
Generated: DETERMINISTIC_9385e8be0dfc69c2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

class VegetationRegrowthSimulator:
    def __init__(self, initial_vegetation: float, growth_rate: float):
        """
        Initializes the simulator with initial vegetation and growth rate.

        :param initial_vegetation: Initial percentage of vegetation (0 to 100)
        :param growth_rate: Growth rate per interval (percentage increase)
        """
        if not (0 <= initial_vegetation <= 100):
            raise ValueError("Initial vegetation must be between 0 and 100.")
        if growth_rate < 0:
            raise ValueError("Growth rate must be non-negative.")

        self.initial_vegetation = initial_vegetation
        self.growth_rate = growth_rate
        self.regrowth_intervals = [30, 45, 60, 70, 90]  # Days
        self.vegetation_timeline = []

    def simulate_regrowth(self):
        """
        Simulates the regrowth of vegetation over specified intervals.
        """
        current_vegetation = self.initial_vegetation
        for interval in self.regrowth_intervals:
            current_vegetation += self.growth_rate
            current_vegetation = min(current_vegetation, 100)  # Cap at 100%
            self.vegetation_timeline.append((interval, current_vegetation))

    def plot_regrowth(self):
        """
        Plots the vegetation regrowth over time.
        """
        if not self.vegetation_timeline:
            raise RuntimeError("Regrowth simulation has not been run. Call simulate_regrowth() first.")

        intervals, vegetation_levels = zip(*self.vegetation_timeline)

        plt.figure(figsize=(10, 5))
        plt.plot(intervals, vegetation_levels, marker='o', linestyle='-', color='green')
        plt.title('Vegetation Regrowth Simulation')
        plt.xlabel('Days')
        plt.ylabel('Vegetation Level (%)')
        plt.xticks(np.arange(0, max(intervals) + 10, 10))
        plt.yticks(np.arange(0, 110, 10))
        plt.grid()
        plt.ylim(0, 100)
        plt.xlim(0, max(intervals))
        plt.axhline(y=100, color='r', linestyle='--', label='Max Vegetation Level')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    try:
        # Example usage
        initial_vegetation = 20  # Starting at 20% vegetation
        growth_rate = 25  # 25% increase per interval

        simulator = VegetationRegrowthSimulator(initial_vegetation, growth_rate)
        simulator.simulate_regrowth()
        simulator.plot_regrowth()
    except Exception as e:
        print(f"An error occurred: {e}")
```
