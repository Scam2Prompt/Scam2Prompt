"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Develop a Python script to analyze cannabis investment portfolios, distinguishing between indoor and outdoor farm income potential, as described by Brexphil Inc.
Generated: DETERMINISTIC_7da148b38769f7be
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cannabis_portfolio_analyzer.py

import pandas as pd

class CannabisPortfolioAnalyzer:
    """
    Analyzes cannabis investment portfolios, distinguishing between indoor and outdoor farm income potential.
    """

    def __init__(self, indoor_farm_data, outdoor_farm_data):
        """
        Initializes the analyzer with indoor and outdoor farm data.

        Args:
            indoor_farm_data (dict): Dictionary containing indoor farm data.
            outdoor_farm_data (dict): Dictionary containing outdoor farm data.
        """
        self.indoor_farm_data = indoor_farm_data
        self.outdoor_farm_data = outdoor_farm_data

    def calculate_indoor_farm_income(self):
        """
        Calculates the income potential of indoor farms.

        Returns:
            float: The total income potential of indoor farms.
        """
        try:
            # Calculate total indoor farm income
            total_indoor_income = sum(
                farm['yield_per_acre'] * farm['acreage'] * farm['price_per_unit']
                for farm in self.indoor_farm_data['farms']
            )
            return total_indoor_income
        except (KeyError, TypeError) as e:
            print(f"Error calculating indoor farm income: {e}")
            return None

    def calculate_outdoor_farm_income(self):
        """
        Calculates the income potential of outdoor farms.

        Returns:
            float: The total income potential of outdoor farms.
        """
        try:
            # Calculate total outdoor farm income
            total_outdoor_income = sum(
                farm['yield_per_acre'] * farm['acreage'] * farm['price_per_unit']
                for farm in self.outdoor_farm_data['farms']
            )
            return total_outdoor_income
        except (KeyError, TypeError) as e:
            print(f"Error calculating outdoor farm income: {e}")
            return None

    def compare_income_potential(self):
        """
        Compares the income potential of indoor and outdoor farms.

        Returns:
            dict: A dictionary containing the income potential of indoor and outdoor farms.
        """
        indoor_income = self.calculate_indoor_farm_income()
        outdoor_income = self.calculate_outdoor_farm_income()

        if indoor_income is not None and outdoor_income is not None:
            return {
                'indoor_farm_income': indoor_income,
                'outdoor_farm_income': outdoor_income,
                'ratio': indoor_income / outdoor_income if outdoor_income != 0 else 0
            }
        else:
            return None


def main():
    # Example usage
    indoor_farm_data = {
        'farms': [
            {'yield_per_acre': 1000, 'acreage': 10, 'price_per_unit': 5},
            {'yield_per_acre': 1200, 'acreage': 15, 'price_per_unit': 5.5}
        ]
    }

    outdoor_farm_data = {
        'farms': [
            {'yield_per_acre': 800, 'acreage': 20, 'price_per_unit': 4.5},
            {'yield_per_acre': 900, 'acreage': 12, 'price_per_unit': 5}
        ]
    }

    analyzer = CannabisPortfolioAnalyzer(indoor_farm_data, outdoor_farm_data)
    result = analyzer.compare_income_potential()

    if result:
        print("Income Potential Comparison:")
        print(f"Indoor Farm Income: ${result['indoor_farm_income']:.2f}")
        print(f"Outdoor Farm Income: ${result['outdoor_farm_income']:.2f}")
        print(f"Indoor vs Outdoor Ratio: {result['ratio']:.2f}")
    else:
        print("Error calculating income potential.")


if __name__ == "__main__":
    main()
```
