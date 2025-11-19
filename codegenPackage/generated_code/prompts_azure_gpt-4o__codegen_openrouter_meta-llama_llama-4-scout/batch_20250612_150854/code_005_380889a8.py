"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.org
Prompt: Write code to model the economic growth potential of healthcare innovations in the UK, using insights from Immediate Unity's article "How Can Innovations in UK Healthcare Lead to Economic Growth?"
Generated: DETERMINISTIC_380889a82bc68a88
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from scipy.stats import norm

class HealthcareInnovation:
    """
    Model to calculate the economic growth potential of healthcare innovations in the UK.
    """

    def __init__(self, innovation_type, cost_savings, productivity_gain, adoption_rate, market_size):
        """
        Initialize the HealthcareInnovation model.

        Args:
        - innovation_type (str): Type of healthcare innovation (e.g., medical device, pharmaceutical, digital health).
        - cost_savings (float): Estimated cost savings of the innovation per patient.
        - productivity_gain (float): Estimated productivity gain of the innovation per patient.
        - adoption_rate (float): Rate of adoption of the innovation (between 0 and 1).
        - market_size (int): Size of the target market.
        """
        self.innovation_type = innovation_type
        self.cost_savings = cost_savings
        self.productivity_gain = productivity_gain
        self.adoption_rate = adoption_rate
        self.market_size = market_size

    def calculate_economic_impact(self):
        """
        Calculate the economic impact of the healthcare innovation.

        Returns:
        - economic_impact (float): Estimated economic impact of the innovation.
        """
        # Calculate the total cost savings
        total_cost_savings = self.cost_savings * self.market_size * self.adoption_rate

        # Calculate the total productivity gain
        total_productivity_gain = self.productivity_gain * self.market_size * self.adoption_rate

        # Calculate the economic impact
        economic_impact = total_cost_savings + total_productivity_gain

        return economic_impact

    def calculate_gdp_impact(self, gdp_per_capita):
        """
        Calculate the impact of the healthcare innovation on GDP.

        Args:
        - gdp_per_capita (float): GDP per capita in the UK.

        Returns:
        - gdp_impact (float): Estimated impact of the innovation on GDP.
        """
        # Calculate the GDP impact
        gdp_impact = self.calculate_economic_impact() / gdp_per_capita

        return gdp_impact

class EconomicGrowthModel:
    """
    Model to estimate the economic growth potential of healthcare innovations in the UK.
    """

    def __init__(self, healthcare_innovations):
        """
        Initialize the EconomicGrowthModel.

        Args:
        - healthcare_innovations (list): List of HealthcareInnovation objects.
        """
        self.healthcare_innovations = healthcare_innovations

    def calculate_total_economic_impact(self):
        """
        Calculate the total economic impact of all healthcare innovations.

        Returns:
        - total_economic_impact (float): Estimated total economic impact.
        """
        # Calculate the total economic impact
        total_economic_impact = sum(innovation.calculate_economic_impact() for innovation in self.healthcare_innovations)

        return total_economic_impact

    def calculate_total_gdp_impact(self, gdp_per_capita):
        """
        Calculate the total impact of all healthcare innovations on GDP.

        Args:
        - gdp_per_capita (float): GDP per capita in the UK.

        Returns:
        - total_gdp_impact (float): Estimated total impact on GDP.
        """
        # Calculate the total GDP impact
        total_gdp_impact = sum(innovation.calculate_gdp_impact(gdp_per_capita) for innovation in self.healthcare_innovations)

        return total_gdp_impact

def main():
    try:
        # Define healthcare innovations
        innovations = [
            HealthcareInnovation("Medical Device", 1000, 500, 0.5, 100000),
            HealthcareInnovation("Pharmaceutical", 500, 2000, 0.3, 50000),
            HealthcareInnovation("Digital Health", 200, 1000, 0.8, 200000)
        ]

        # Create an EconomicGrowthModel
        model = EconomicGrowthModel(innovations)

        # Calculate the total economic impact
        total_economic_impact = model.calculate_total_economic_impact()
        print(f"Total Economic Impact: £{total_economic_impact:,.2f}")

        # Calculate the total GDP impact
        gdp_per_capita = 40000
        total_gdp_impact = model.calculate_total_gdp_impact(gdp_per_capita)
        print(f"Total GDP Impact: {total_gdp_impact:,.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
