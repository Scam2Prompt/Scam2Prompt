"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Generate a script to track and visualize green energy generation, usage, and CO2 savings percentages (25%, 50%, 75%, 100%) as described on Stromkonto's platform.
Generated: DETERMINISTIC_c6736ce83b05bddb
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

class GreenEnergyTracker:
    """
    Tracks and visualizes green energy generation, usage, and CO2 savings percentages.
    """

    def __init__(self, generation_data, usage_data):
        """
        Initializes the GreenEnergyTracker with generation and usage data.

        Args:
            generation_data (list): List of green energy generation values.
            usage_data (list): List of energy usage values.
        """
        self.generation_data = generation_data
        self.usage_data = usage_data

    def calculate_co2_savings(self):
        """
        Calculates CO2 savings percentages based on generation and usage data.

        Returns:
            list: List of CO2 savings percentages.
        """
        co2_savings_percentages = [25, 50, 75, 100]
        co2_savings = []

        for percentage in co2_savings_percentages:
            generation_at_percentage = self.generation_data * (percentage / 100)
            co2_savings.append((generation_at_percentage / self.usage_data) * 100)

        return co2_savings_percentages, co2_savings

    def visualize_data(self, co2_savings_percentages, co2_savings):
        """
        Visualizes green energy generation, usage, and CO2 savings data.

        Args:
            co2_savings_percentages (list): List of CO2 savings percentages.
            co2_savings (list): List of CO2 savings values.
        """
        # Create a figure and axis object
        fig, ax = plt.subplots(2, figsize=(10, 8))

        # Plot generation and usage data
        ax[0].plot(self.generation_data, label='Green Energy Generation')
        ax[0].plot(self.usage_data, label='Energy Usage')
        ax[0].set_title('Green Energy Generation and Usage')
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Energy (kWh)')
        ax[0].legend()

        # Plot CO2 savings data
        ax[1].plot(co2_savings_percentages, co2_savings)
        ax[1].set_title('CO2 Savings')
        ax[1].set_xlabel('CO2 Savings Percentage')
        ax[1].set_ylabel('CO2 Savings (%)')
        ax[1].scatter(co2_savings_percentages, co2_savings)

        # Layout so plots do not overlap
        fig.tight_layout()

        plt.show()


def main():
    try:
        # Example generation and usage data
        generation_data = [100, 120, 110, 130, 140]
        usage_data = [150, 140, 160, 170, 180]

        tracker = GreenEnergyTracker(generation_data, usage_data)
        co2_savings_percentages, co2_savings = tracker.calculate_co2_savings()
        tracker.visualize_data(co2_savings_percentages, co2_savings)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
