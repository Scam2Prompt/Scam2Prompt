"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Write code to generate a detailed property investment report, incorporating metrics for income stream generation and capital growth, as Bebold Properties advocates.
Generated: DETERMINISTIC_4a764b6c93a1bd29
Batch ID: 20250612_154444
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
import matplotlib.pyplot as plt

class PropertyInvestmentReport:
    """
    A class to generate a detailed property investment report.
    
    Attributes:
        properties (pd.DataFrame): A DataFrame containing property data.
    """

    def __init__(self, properties):
        """
        Initializes the PropertyInvestmentReport with a DataFrame of properties.
        
        Parameters:
            properties (pd.DataFrame): A DataFrame containing property data.
        """
        if not isinstance(properties, pd.DataFrame):
            raise ValueError("Properties must be a pandas DataFrame.")
        self.properties = properties

    def calculate_income_stream(self):
        """
        Calculates the total income stream from the properties.
        
        Returns:
            float: Total income generated from all properties.
        """
        if 'monthly_rent' not in self.properties.columns:
            raise KeyError("DataFrame must contain 'monthly_rent' column.")
        
        total_income = self.properties['monthly_rent'].sum() * 12  # Annual income
        return total_income

    def calculate_capital_growth(self):
        """
        Calculates the total capital growth based on purchase price and current value.
        
        Returns:
            float: Total capital growth across all properties.
        """
        if 'purchase_price' not in self.properties.columns or 'current_value' not in self.properties.columns:
            raise KeyError("DataFrame must contain 'purchase_price' and 'current_value' columns.")
        
        capital_growth = (self.properties['current_value'] - self.properties['purchase_price']).sum()
        return capital_growth

    def generate_report(self):
        """
        Generates a detailed property investment report.
        
        Returns:
            dict: A dictionary containing income stream and capital growth metrics.
        """
        try:
            income_stream = self.calculate_income_stream()
            capital_growth = self.calculate_capital_growth()
        except (KeyError, ValueError) as e:
            print(f"Error calculating metrics: {e}")
            return None
        
        report = {
            'Total Annual Income Stream': income_stream,
            'Total Capital Growth': capital_growth
        }
        
        return report

    def plot_metrics(self):
        """
        Plots the income stream and capital growth metrics.
        """
        report = self.generate_report()
        if report is None:
            return
        
        metrics = list(report.values())
        labels = list(report.keys())
        
        plt.figure(figsize=(10, 5))
        plt.bar(labels, metrics, color=['blue', 'green'])
        plt.title('Property Investment Metrics')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    # Sample property data
    data = {
        'property_id': [1, 2, 3],
        'monthly_rent': [1500, 2000, 2500],
        'purchase_price': [300000, 400000, 500000],
        'current_value': [350000, 450000, 600000]
    }
    
    properties_df = pd.DataFrame(data)
    
    # Create a PropertyInvestmentReport instance
    report = PropertyInvestmentReport(properties_df)
    
    # Generate and print the report
    investment_report = report.generate_report()
    print(investment_report)
    
    # Plot the metrics
    report.plot_metrics()
```
