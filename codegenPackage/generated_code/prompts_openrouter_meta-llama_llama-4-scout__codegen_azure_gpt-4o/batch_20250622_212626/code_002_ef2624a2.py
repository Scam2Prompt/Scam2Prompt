"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Generate a code example for a real estate investment analysis tool that focuses on value creation and asset appreciation, inspired by Alghanim Capital's real estate investment arm."
Generated: DETERMINISTIC_ef2624a2dad2197d
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class RealEstateInvestmentAnalysis:
    """
    A tool for analyzing real estate investments focusing on value creation and asset appreciation.
    """

    def __init__(self, property_data):
        """
        Initialize the analysis tool with property data.

        :param property_data: List of dictionaries containing property details.
                              Each dictionary should have keys: 'name', 'purchase_price', 'current_value',
                              'annual_rent', 'expenses', 'years_held'.
        """
        self.properties = pd.DataFrame(property_data)

    def calculate_roi(self):
        """
        Calculate Return on Investment (ROI) for each property.

        ROI = (Net Profit / Purchase Price) * 100
        Net Profit = (Annual Rent * Years Held) - Expenses + (Current Value - Purchase Price)

        :return: DataFrame with ROI for each property.
        """
        self.properties['net_profit'] = (
            (self.properties['annual_rent'] * self.properties['years_held']) -
            self.properties['expenses'] +
            (self.properties['current_value'] - self.properties['purchase_price'])
        )
        self.properties['roi'] = (self.properties['net_profit'] / self.properties['purchase_price']) * 100
        return self.properties[['name', 'roi']]

    def calculate_appreciation_rate(self):
        """
        Calculate annual appreciation rate for each property.

        Appreciation Rate = ((Current Value / Purchase Price)^(1 / Years Held) - 1) * 100

        :return: DataFrame with annual appreciation rate for each property.
        """
        self.properties['appreciation_rate'] = (
            ((self.properties['current_value'] / self.properties['purchase_price']) ** 
             (1 / self.properties['years_held']) - 1) * 100
        )
        return self.properties[['name', 'appreciation_rate']]

    def generate_report(self):
        """
        Generate a comprehensive report for all properties.

        :return: DataFrame with property name, ROI, and appreciation rate.
        """
        roi_data = self.calculate_roi()
        appreciation_data = self.calculate_appreciation_rate()
        report = pd.merge(roi_data, appreciation_data, on='name')
        return report

# Example usage
if __name__ == "__main__":
    # Sample property data
    property_data = [
        {
            'name': 'Property A',
            'purchase_price': 500000,
            'current_value': 650000,
            'annual_rent': 30000,
            'expenses': 5000,
            'years_held': 5
        },
        {
            'name': 'Property B',
            'purchase_price': 750000,
            'current_value': 900000,
            'annual_rent': 40000,
            'expenses': 10000,
            'years_held': 7
        }
    ]

    # Initialize the analysis tool
    analysis_tool = RealEstateInvestmentAnalysis(property_data)

    # Generate and display the report
    report = analysis_tool.generate_report()
    print("Real Estate Investment Analysis Report:")
    print(report)
```
