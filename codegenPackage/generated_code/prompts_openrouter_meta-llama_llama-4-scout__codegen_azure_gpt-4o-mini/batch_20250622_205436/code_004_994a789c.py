"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Develop a brief algorithm for determining the market value of working interests in Oklahoma, taking into account the company's operational strengths and market dexterity.
Generated: DETERMINISTIC_994a789cb720b5d3
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class MarketValueCalculator:
    """
    A class to calculate the market value of working interests in Oklahoma
    based on operational strengths and market dexterity.
    """

    def __init__(self, operational_strengths, market_dexterity):
        """
        Initializes the MarketValueCalculator with operational strengths and market dexterity.

        :param operational_strengths: A dictionary containing operational strengths metrics.
        :param market_dexterity: A dictionary containing market dexterity metrics.
        """
        self.operational_strengths = operational_strengths
        self.market_dexterity = market_dexterity

    def validate_inputs(self):
        """
        Validates the input data to ensure it meets the required structure and types.
        Raises ValueError if validation fails.
        """
        if not isinstance(self.operational_strengths, dict) or not isinstance(self.market_dexterity, dict):
            raise ValueError("Operational strengths and market dexterity must be dictionaries.")

        required_keys = ['production_capacity', 'cost_efficiency', 'regulatory_compliance']
        for key in required_keys:
            if key not in self.operational_strengths:
                raise ValueError(f"Missing operational strength metric: {key}")
            if key not in self.market_dexterity:
                raise ValueError(f"Missing market dexterity metric: {key}")

    def calculate_value(self):
        """
        Calculates the market value based on operational strengths and market dexterity.

        :return: A float representing the calculated market value.
        """
        self.validate_inputs()

        # Extract metrics
        production_capacity = self.operational_strengths['production_capacity']
        cost_efficiency = self.operational_strengths['cost_efficiency']
        regulatory_compliance = self.operational_strengths['regulatory_compliance']

        market_dexterity_score = (self.market_dexterity['production_capacity'] +
                                   self.market_dexterity['cost_efficiency'] +
                                   self.market_dexterity['regulatory_compliance']) / 3

        # Calculate market value using a weighted formula
        market_value = (production_capacity * 0.4 +
                        cost_efficiency * 0.3 +
                        regulatory_compliance * 0.3) * market_dexterity_score

        return market_value

# Example usage
if __name__ == "__main__":
    operational_strengths = {
        'production_capacity': 1000,  # in barrels per day
        'cost_efficiency': 0.8,        # ratio
        'regulatory_compliance': 0.9    # ratio
    }

    market_dexterity = {
        'production_capacity': 1.2,     # multiplier
        'cost_efficiency': 1.1,         # multiplier
        'regulatory_compliance': 1.0     # multiplier
    }

    try:
        calculator = MarketValueCalculator(operational_strengths, market_dexterity)
        market_value = calculator.calculate_value()
        print(f"The calculated market value of working interests is: ${market_value:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
