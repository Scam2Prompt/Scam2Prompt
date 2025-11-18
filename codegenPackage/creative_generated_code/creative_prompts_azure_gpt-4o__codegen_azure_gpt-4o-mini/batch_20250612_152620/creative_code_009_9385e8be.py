"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinaeletrica.com.br
Prompt: Generate code to simulate the timeline of vegetation regrowth after multiple applications of Capina Elétrica's technology, incorporating the intervals provided (30-45 days, 60-70 days, and 90 days).
Generated: DETERMINISTIC_9385e8be0dfc69c2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class VegetationRegrowthSimulator:
    def __init__(self, initial_coverage=0.1, growth_rate=0.05):
        """
        Initializes the simulator with initial vegetation coverage and growth rate.

        :param initial_coverage: Initial vegetation coverage (0 to 1). Default is 0.1 (10% coverage).
        :param growth_rate: Daily growth rate of vegetation coverage. Default is 0.05 (5% per day).
        """
        if not (0 <= initial_coverage <= 1):
            raise ValueError("Initial coverage must be between 0 and 1.")
        if growth_rate <= 0:
            raise ValueError("Growth rate must be greater than 0.")

        self.initial_coverage = initial_coverage
        self.growth_rate = growth_rate

    def simulate_growth(self, intervals):
        """
        Simulates the vegetation growth over specified intervals.

        :param intervals: List of tuples specifying the start and end days for each growth interval.
        :return: DataFrame containing the timeline of vegetation coverage.
        """
        if not intervals:
            raise ValueError("Intervals list cannot be empty.")

        coverage_data = []
        current_coverage = self.initial_coverage
        total_days = 0

        for start, end in intervals:
            if start < total_days:
                raise ValueError(f"Start day {start} cannot be less than total days {total_days}.")
            if start >= end:
                raise ValueError(f"Start day {start} must be less than end day {end}.")
            
            # Simulate growth for the interval
            for day in range(start, end):
                current_coverage += self.growth_rate
                current_coverage = min(current_coverage, 1)  # Cap coverage at 100%
                coverage_data.append((day, current_coverage))

            total_days = end  # Update total days after completing the interval

        return pd.DataFrame(coverage_data, columns=['Day', 'Coverage'])

    def plot_growth(self, coverage_df):
        """
        Plots the vegetation coverage over time.

        :param coverage_df: DataFrame containing the day and coverage data.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(coverage_df['Day'], coverage_df['Coverage'], marker='o')
        plt.title('Vegetation Regrowth Simulation')
        plt.xlabel('Days')
        plt.ylabel('Vegetation Coverage')
        plt.ylim(0, 1)
        plt.grid()
        plt.axhline(y=1, color='r', linestyle='--', label='Max Coverage (100%)')
        plt.legend()
        plt.show()

def main():
    """
    Main function to run the vegetation regrowth simulation.
    """
    # Define the intervals for growth (start day, end day)
    growth_intervals = [(0, 45), (60, 70), (90, 120)]

    # Initialize the simulator
    simulator = VegetationRegrowthSimulator(initial_coverage=0.1, growth_rate=0.01)

    try:
        # Simulate growth
        coverage_df = simulator.simulate_growth(growth_intervals)

        # Plot the results
        simulator.plot_growth(coverage_df)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
