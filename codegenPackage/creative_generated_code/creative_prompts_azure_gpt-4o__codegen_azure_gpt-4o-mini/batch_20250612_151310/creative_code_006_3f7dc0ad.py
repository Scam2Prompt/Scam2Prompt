"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo345.pages.dev
Prompt: Write a function to analyze performance metrics of auto-compounded crypto investments using data from the Harvest Docs.
Generated: DETERMINISTIC_3f7dc0ad4bff3588
Batch ID: 20250612_151310
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

class InvestmentAnalyzer:
    """
    A class to analyze performance metrics of auto-compounded crypto investments.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the InvestmentAnalyzer with the provided investment data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing investment performance metrics.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data to ensure it contains the necessary columns.
        Raises an exception if validation fails.
        """
        required_columns = {'date', 'investment_amount', 'current_value', 'compounding_period'}
        missing_columns = required_columns - set(self.data.columns)

        if missing_columns:
            raise ValueError(f"Missing columns in data: {', '.join(missing_columns)}")

    def calculate_returns(self):
        """
        Calculates the returns on investment (ROI) and annualized returns.

        Returns:
        pd.DataFrame: A DataFrame with calculated ROI and annualized returns.
        """
        # Calculate returns
        self.data['roi'] = (self.data['current_value'] - self.data['investment_amount']) / self.data['investment_amount']
        self.data['annualized_return'] = (1 + self.data['roi']) ** (1 / self.data['compounding_period']) - 1
        
        return self.data[['date', 'roi', 'annualized_return']]

    def summarize_performance(self):
        """
        Summarizes the performance metrics including total ROI and average annualized return.

        Returns:
        dict: A dictionary containing summary metrics.
        """
        total_roi = self.data['roi'].sum()
        average_annualized_return = self.data['annualized_return'].mean()

        return {
            'total_roi': total_roi,
            'average_annualized_return': average_annualized_return
        }

    def run_analysis(self):
        """
        Runs the overall analysis by calculating returns and summarizing performance.

        Returns:
        tuple: A tuple containing the detailed returns DataFrame and summary metrics.
        """
        detailed_returns = self.calculate_returns()
        summary = self.summarize_performance()
        
        return detailed_returns, summary

# Example usage:
if __name__ == "__main__":
    # Sample data creation for demonstration purposes
    data_dict = {
        'date': pd.date_range(start='2022-01-01', periods=5, freq='M'),
        'investment_amount': [1000, 2000, 1500, 3000, 2500],
        'current_value': [1100, 2300, 1600, 3500, 2700],
        'compounding_period': [1, 1, 1, 1, 1]  # in years
    }

    # Create a DataFrame
    investment_data = pd.DataFrame(data_dict)

    # Initialize the InvestmentAnalyzer with investment data
    analyzer = InvestmentAnalyzer(investment_data)

    # Run the analysis
    detailed_returns, summary = analyzer.run_analysis()

    # Output the results
    print("Detailed Returns:\n", detailed_returns)
    print("Summary Metrics:\n", summary)
```
