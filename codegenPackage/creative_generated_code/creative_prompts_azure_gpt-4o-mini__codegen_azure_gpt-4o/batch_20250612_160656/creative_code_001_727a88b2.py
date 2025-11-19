"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Write a Python script that models the growth potential of the Indian aerospace and defense industry, incorporating factors like government initiatives and private sector participation.
Generated: DETERMINISTIC_727a88b2ac0a6e38
Batch ID: 20250612_160656
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

class IndustryGrowthModel:
    """
    Class to model the growth potential of the Indian aerospace and defense industry.
    """
    def __init__(self, base_growth_rate, gov_initiatives_factor, private_sector_factor):
        """
        Initializes the growth model.

        :param base_growth_rate: Base annual growth rate (as a percentage).
        :param gov_initiatives_factor: Impact factor of government initiatives (value between 0 and 1).
        :param private_sector_factor: Impact factor of private sector participation (value between 0 and 1).
        """
        if not (0 <= gov_initiatives_factor <= 1):
            raise ValueError("Government initiatives factor must be between 0 and 1.")
        if not (0 <= private_sector_factor <= 1):
            raise ValueError("Private sector factor must be between 0 and 1.")
        if base_growth_rate < 0:
            raise ValueError("Base growth rate cannot be negative.")

        self.base_growth_rate = base_growth_rate
        self.gov_initiatives_factor = gov_initiatives_factor
        self.private_sector_factor = private_sector_factor

    def calculate_growth_rate(self):
        """
        Calculates the adjusted growth rate based on the base rate and the impact factors.

        :return: Adjusted annual growth rate as a percentage.
        """
        # Adjust growth rate by combining base rate with initiative and private sector factors
        adjusted_growth_rate = self.base_growth_rate * (
            1 + self.gov_initiatives_factor + self.private_sector_factor
        )
        return adjusted_growth_rate

    def project_growth(self, years):
        """
        Projects the industry growth over a given number of years.

        :param years: Number of years for the projection.
        :return: A list of projected industry values over the given years.
        """
        if years <= 0:
            raise ValueError("Number of years must be greater than 0.")

        adjusted_growth_rate = self.calculate_growth_rate() / 100  # Convert percentage to decimal
        industry_values = [1]  # Assuming initial normalized value as 1 (base year)

        for _ in range(years):
            next_value = industry_values[-1] * (1 + adjusted_growth_rate)
            industry_values.append(next_value)

        return industry_values

def plot_growth(years, industry_values):
    """
    Plots the projected industry growth.

    :param years: Number of years for the projection.
    :param industry_values: A list of projected industry values.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(years + 1), industry_values, marker='o', label="Projected Growth")
    plt.title("Growth Potential of Indian Aerospace and Defense Industry", fontsize=14)
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Industry Value (Normalized)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.show()

def main():
    """
    Main function to execute the growth model and plot results.
    """
    try:
        # Define model parameters
        base_growth_rate = 6.5  # Base annual growth rate (in %)
        gov_initiatives_factor = 0.3  # Impact of government initiatives (30%)
        private_sector_factor = 0.25  # Impact of private sector participation (25%)

        # Initialize the growth model
        growth_model = IndustryGrowthModel(base_growth_rate, gov_initiatives_factor, private_sector_factor)

        # Project industry growth for the next 10 years
        years = 10
        industry_values = growth_model.project_growth(years)

        # Plot the projected growth
        plot_growth(years, industry_values)

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
