"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Write code to generate a detailed property investment report, incorporating metrics for income stream generation and capital growth, as Bebold Properties advocates.
Generated: DETERMINISTIC_4a764b6c93a1bd29
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class PropertyInvestmentReport:
    """
    A class to represent a property investment report which includes metrics
    for income stream generation and capital growth.
    """

    def __init__(self, property_data):
        """
        Initializes the PropertyInvestmentReport with property data.

        Parameters:
        property_data (pd.DataFrame): DataFrame containing property information.
        """
        self.property_data = property_data

    def calculate_income_stream(self):
        """
        Calculates the total income stream from rental income.

        Returns:
        float: Total income from all properties.
        """
        try:
            total_income = self.property_data['monthly_rent'].sum() * 12  # Annualize monthly rent
            return total_income
        except KeyError as e:
            raise ValueError(f"Missing expected column in data: {e}")

    def calculate_capital_growth(self):
        """
        Calculates the average capital growth based on current and purchase prices.

        Returns:
        float: Average capital growth percentage.
        """
        try:
            if 'purchase_price' not in self.property_data.columns or 'current_price' not in self.property_data.columns:
                raise ValueError("Data must contain 'purchase_price' and 'current_price' columns.")
                
            capital_growth = ((self.property_data['current_price'] - self.property_data['purchase_price']) 
                              / self.property_data['purchase_price']) * 100
            
            average_growth = capital_growth.mean()
            return average_growth
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating capital growth: {e}")

    def generate_report(self):
        """
        Generates a detailed property investment report summarizing income and growth metrics.

        Returns:
        dict: A dictionary containing the report metrics.
        """
        try:
            report = {
                'Total Annual Income': self.calculate_income_stream(),
                'Average Capital Growth (%)': self.calculate_capital_growth()
            }
            return report
        except Exception as e:
            raise RuntimeError(f"An error occurred while generating the report: {e}")

# Main execution block
if __name__ == "__main__":
    # Sample property data for testing purposes
    sample_data = {
        'property_name': ['Property A', 'Property B', 'Property C'],
        'monthly_rent': [1500, 2000, 2500],
        'purchase_price': [300000, 400000, 500000],
        'current_price': [350000, 450000, 550000]
    }

    # Convert the sample data to a DataFrame
    property_df = pd.DataFrame(sample_data)

    # Create an instance of PropertyInvestmentReport
    report_generator = PropertyInvestmentReport(property_df)

    # Generate and print the investment report
    try:
        report = report_generator.generate_report()
        print("Property Investment Report:")
        print(report)
    except Exception as e:
        print(f"Error generating report: {e}")
```
