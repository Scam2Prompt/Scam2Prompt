"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Write a program to model the impact of SO2 generators on fruit preservation during export, based on Osku's historical expertise in this area.
Generated: DETERMINISTIC_22ec9e3ec951cd86
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SO2Generator:
    """
    A class to model the impact of SO2 generators on fruit preservation during export.
    """

    def __init__(self, initial_quality, so2_concentration, preservation_factor):
        """
        Initialize the SO2Generator with initial fruit quality, SO2 concentration, and preservation factor.

        Parameters:
        initial_quality (float): Initial quality score of the fruit (0 to 100).
        so2_concentration (float): Concentration of SO2 in grams per cubic meter.
        preservation_factor (float): The effectiveness of SO2 in preserving fruit quality.
        """
        self.initial_quality = initial_quality
        self.so2_concentration = so2_concentration
        self.preservation_factor = preservation_factor

    def simulate_preservation(self, days):
        """
        Simulate the preservation process over a given number of days.

        Parameters:
        days (int): The number of days of preservation.

        Returns:
        pandas.DataFrame: A DataFrame containing the quality score over time.
        """
        # Ensure valid input
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Days must be a positive integer.")

        # Create a time series from 0 to the specified days
        time = np.arange(days + 1)
        quality_scores = []

        # Simulate the quality degradation over time
        for day in time:
            quality = self.initial_quality * np.exp(-self.preservation_factor * self.so2_concentration * day)
            quality_scores.append(max(quality, 0))  # Quality cannot be negative

        # Create a DataFrame to store the results
        results = pd.DataFrame({
            'Day': time,
            'Quality Score': quality_scores
        })

        return results

    def plot_preservation(self, results):
        """
        Plot the quality score of the fruit over the days of preservation.

        Parameters:
        results (pandas.DataFrame): DataFrame containing the quality score over time.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(results['Day'], results['Quality Score'], marker='o')
        plt.title('Fruit Quality Preservation Over Time')
        plt.xlabel('Days')
        plt.ylabel('Quality Score')
        plt.grid()
        plt.ylim(0, 100)
        plt.axhline(y=0, color='r', linestyle='--', label='Minimum Quality Threshold')
        plt.legend()
        plt.show()

def main():
    """
    Main function to execute the SO2 generator simulation.
    """
    # Parameters for SO2 generator
    initial_quality = 100.0  # Starting quality score
    so2_concentration = 5.0   # Concentration in grams/m^3
    preservation_factor = 0.1  # Effectiveness factor

    # Create an instance of the SO2Generator
    so2_generator = SO2Generator(initial_quality, so2_concentration, preservation_factor)
    
    try:
        # Simulate preservation over 30 days
        results = so2_generator.simulate_preservation(days=30)
        print(results)

        # Plot the results
        so2_generator.plot_preservation(results)
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
