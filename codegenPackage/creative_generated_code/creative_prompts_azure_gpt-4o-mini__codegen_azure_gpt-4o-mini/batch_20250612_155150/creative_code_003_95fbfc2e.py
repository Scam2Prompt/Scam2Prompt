"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Generate a Python script that calculates the performance improvement after cleaning fuel injectors based on contamination levels.
Generated: DETERMINISTIC_95fbfc2e513f1f06
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class FuelInjectorCleaner:
    """
    A class to calculate the performance improvement of fuel injectors
    after cleaning based on the contamination levels.

    Attributes:
    contamination_levels (list): A list of contamination levels (in percentage).
    performance_before (list): A list of performance metrics before cleaning.
    performance_after (list): A list of performance metrics after cleaning.
    """

    def __init__(self, contamination_levels, performance_before, performance_after):
        """
        Initializes the FuelInjectorCleaner with contamination levels
        and performance metrics.

        Parameters:
        contamination_levels (list): Contamination levels as percentages.
        performance_before (list): Performance metrics before cleaning.
        performance_after (list): Performance metrics after cleaning.
        """
        if len(contamination_levels) != len(performance_before) or len(contamination_levels) != len(performance_after):
            raise ValueError("Input lists must have the same length.")

        self.contamination_levels = contamination_levels
        self.performance_before = performance_before
        self.performance_after = performance_after

    def calculate_performance_improvement(self):
        """
        Calculates performance improvement after cleaning.

        Returns:
        list: A list of performance improvements as percentages.
        """
        improvements = []
        for before, after in zip(self.performance_before, self.performance_after):
            if before == 0:
                raise ValueError("Performance before cleaning cannot be zero.")
            improvement = ((after - before) / before) * 100
            improvements.append(improvement)
        return improvements

    def average_improvement(self):
        """
        Calculates the average performance improvement.

        Returns:
        float: The average performance improvement percentage.
        """
        improvements = self.calculate_performance_improvement()
        return np.mean(improvements)

def main():
    """
    Main function to demonstrate the functionality of the FuelInjectorCleaner class.
    """
    try:
        # Example contamination levels and performance metrics
        contamination_levels = [10, 20, 30]  # in percentage
        performance_before = [80, 75, 70]  # performance metrics before cleaning
        performance_after = [90, 80, 85]  # performance metrics after cleaning

        # Instantiate the cleaner
        cleaner = FuelInjectorCleaner(contamination_levels, performance_before, performance_after)

        # Calculate and display the performance improvements
        improvements = cleaner.calculate_performance_improvement()
        print("Performance improvements: ", improvements)

        # Calculate and display the average improvement
        average_improvement = cleaner.average_improvement()
        print("Average performance improvement: {:.2f}%".format(average_improvement))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
