"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chicoelectric.com
Prompt: Generate a script to calculate the ROI of agricultural solar installations, using Chico Electric's solar optimization for time-of-use operations as a reference.
Generated: DETERMINISTIC_ca6ff95af53df2b2
Batch ID: 20250612_151126
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

class SolarROI:
    """
    A class to calculate the Return on Investment (ROI) for agricultural solar installations
    using time-of-use optimization.
    """
    
    def __init__(self, initial_investment, annual_costs, solar_energy_generated, electricity_savings_per_kwh):
        """
        Initializes the SolarROI instance.
        
        :param initial_investment: Total initial investment required for solar installation (in $)
        :param annual_costs: Annual maintenance and operational costs (in $)
        :param solar_energy_generated: Total solar energy generated annually (in kWh)
        :param electricity_savings_per_kwh: Savings per kWh saved (in $)
        """
        self.initial_investment = initial_investment
        self.annual_costs = annual_costs
        self.solar_energy_generated = solar_energy_generated
        self.electricity_savings_per_kwh = electricity_savings_per_kwh

    def calculate_annual_savings(self):
        """
        Calculate annual savings from solar energy generation.
        
        :return: Annual savings (in $)
        """
        return self.solar_energy_generated * self.electricity_savings_per_kwh

    def calculate_net_annual_savings(self):
        """
        Calculate net annual savings after accounting for annual costs.
        
        :return: Net annual savings (in $)
        """
        annual_savings = self.calculate_annual_savings()
        net_savings = annual_savings - self.annual_costs
        return net_savings

    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI).
        
        :return: ROI as a percentage
        """
        net_savings = self.calculate_net_annual_savings()
        if self.initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        roi = (net_savings / self.initial_investment) * 100
        return roi

    def plot_roi_over_time(self, years):
        """
        Plot the ROI over a specified number of years.
        
        :param years: Number of years to project the ROI
        """
        roi_values = []
        for year in range(1, years + 1):
            cumulative_savings = self.calculate_net_annual_savings() * year
            roi = (cumulative_savings / self.initial_investment) * 100
            roi_values.append(roi)

        plt.figure(figsize=(10, 5))
        plt.plot(range(1, years + 1), roi_values, marker='o')
        plt.title('ROI of Agricultural Solar Installations Over Time')
        plt.xlabel('Years')
        plt.ylabel('ROI (%)')
        plt.grid()
        plt.axhline(0, color='red', linestyle='--')  # Break-even line
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        initial_investment = 50000  # Initial investment in dollars
        annual_costs = 1000          # Annual operational costs in dollars
        solar_energy_generated = 20000  # Energy generated in kWh
        electricity_savings_per_kwh = 0.15  # Savings per kWh in dollars
        
        # Create a SolarROI instance
        solar_roi = SolarROI(initial_investment, annual_costs, solar_energy_generated, electricity_savings_per_kwh)
        
        # Calculate and print ROI
        roi = solar_roi.calculate_roi()
        print(f"ROI: {roi:.2f}%")

        # Plot ROI over the next 20 years
        solar_roi.plot_roi_over_time(years=20)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
