"""
Generated Code Metadata:
========================
Original URL: https://lite-trades.org
Prompt: Write code to analyze the performance of multi-family, office, retail, and hospitality real estate investments, based on Lite Trade's real estate management offerings.
Generated: DETERMINISTIC_28e03ed949dc082c
Batch ID: 20250612_152358
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

class RealEstateInvestmentAnalyzer:
    """
    A class to analyze the performance of various real estate investments.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the analyzer with a DataFrame containing investment data.

        :param data: A pandas DataFrame with columns ['Type', 'Investment', 'Revenue', 'Expenses', 'Year']
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains the required columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['Type', 'Investment', 'Revenue', 'Expenses', 'Year']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for each investment type.

        :return: A DataFrame with ROI for each investment type.
        """
        self.data['ROI'] = (self.data['Revenue'] - self.data['Expenses']) / self.data['Investment']
        return self.data.groupby('Type')['ROI'].mean().reset_index()

    def plot_roi(self):
        """
        Plots the average ROI for each investment type.
        """
        roi_data = self.calculate_roi()
        plt.figure(figsize=(10, 6))
        plt.bar(roi_data['Type'], roi_data['ROI'], color=['blue', 'green', 'orange', 'red'])
        plt.title('Average ROI by Investment Type')
        plt.xlabel('Investment Type')
        plt.ylabel('Average ROI')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    def analyze_performance(self):
        """
        Analyzes the performance of the investments and generates a report.

        :return: A summary report as a DataFrame.
        """
        roi_summary = self.calculate_roi()
        total_investment = self.data.groupby('Type')['Investment'].sum().reset_index()
        total_revenue = self.data.groupby('Type')['Revenue'].sum().reset_index()
        total_expenses = self.data.groupby('Type')['Expenses'].sum().reset_index()

        report = roi_summary.merge(total_investment, on='Type', suffixes=('', '_Total'))
        report = report.merge(total_revenue, on='Type', suffixes=('', '_Total'))
        report = report.merge(total_expenses, on='Type', suffixes=('', '_Total'))

        report.columns = ['Type', 'Average ROI', 'Total Investment', 'Total Revenue', 'Total Expenses']
        return report

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'Type': ['Multi-Family', 'Office', 'Retail', 'Hospitality', 'Multi-Family', 'Office'],
        'Investment': [100000, 200000, 150000, 300000, 120000, 250000],
        'Revenue': [120000, 250000, 180000, 350000, 130000, 270000],
        'Expenses': [30000, 50000, 40000, 70000, 35000, 60000],
        'Year': [2021, 2021, 2021, 2021, 2022, 2022]
    }

    # Create a DataFrame
    investment_data = pd.DataFrame(data)

    try:
        analyzer = RealEstateInvestmentAnalyzer(investment_data)
        performance_report = analyzer.analyze_performance()
        print(performance_report)
        analyzer.plot_roi()
    except ValueError as e:
        print(f"Error: {e}")
```
