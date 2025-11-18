"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Write Python code to analyze real estate investment opportunities, focusing on land acquisition and development strategies similar to those described by Carolina Capital.
Generated: DETERMINISTIC_9c72d983b8233270
Batch ID: 20250612_151811
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

class RealEstateInvestmentAnalyzer:
    """
    A class to analyze real estate investment opportunities focusing on land acquisition
    and development strategies.
    """

    def __init__(self, data):
        """
        Initialize the RealEstateInvestmentAnalyzer with investment data.

        :param data: Pandas DataFrame containing real estate investment data.
                     It should have columns: 'Location', 'Land_Cost', 'Development_Cost',
                     'Market_Value', 'Annual_Tax', 'Annual_Maintenance'.
        """
        self.data = data

    def evaluate_roi(self):
        """
        Evaluate Return on Investment (ROI) for each property.

        ROI is calculated as follows:
        ROI = (Market_Value - (Land_Cost + Development_Cost + Annual_Tax + Annual_Maintenance)) / Total_Cost

        :return: DataFrame with ROI added as a new column.
        """
        try:
            self.data['Total_Cost'] = self.data['Land_Cost'] + self.data['Development_Cost'] + self.data['Annual_Tax'] + self.data['Annual_Maintenance']
            self.data['ROI'] = (self.data['Market_Value'] - self.data['Total_Cost']) / self.data['Total_Cost']
        except KeyError as e:
            raise ValueError(f"Missing required column in data: {e}")
        return self.data

    def suggest_investments(self, roi_threshold=0.15):
        """
        Suggest investments based on ROI threshold.

        :param roi_threshold: Minimum ROI percentage (e.g., 0.15 for 15%) to consider an investment worthy.
        :return: DataFrame of suggested investments that meet the ROI threshold.
        """
        if 'ROI' not in self.data.columns:
            raise ValueError("ROI has not been calculated. Call evaluate_roi() first.")
        
        suggested_investments = self.data[self.data['ROI'] >= roi_threshold]
        return suggested_investments

    def summarize_data(self):
        """
        Provide summary statistics for the investment data.

        :return: Dictionary with summary statistics.
        """
        summary = {
            'Average ROI': self.data['ROI'].mean() if 'ROI' in self.data.columns else None,
            'Median ROI': self.data['ROI'].median() if 'ROI' in self.data.columns else None,
            'Max ROI': self.data['ROI'].max() if 'ROI' in self.data.columns else None,
            'Min ROI': self.data['ROI'].min() if 'ROI' in self.data.columns else None,
            'Total Properties Analyzed': len(self.data),
        }
        return summary


# Example usage
if __name__ == "__main__":
    # Sample investment data for demonstration purposes
    investment_data = pd.DataFrame({
        'Location': ['A', 'B', 'C', 'D'],
        'Land_Cost': [100000, 200000, 150000, 180000],
        'Development_Cost': [50000, 80000, 60000, 70000],
        'Market_Value': [200000, 320000, 300000, 280000],
        'Annual_Tax': [2000, 3000, 2500, 2800],
        'Annual_Maintenance': [5000, 4000, 4500, 4800],
    })

    # Initialize the analyzer
    analyzer = RealEstateInvestmentAnalyzer(investment_data)

    # Calculate ROI
    analyzed_data = analyzer.evaluate_roi()
    print("Analyzed Data with ROI:\n", analyzed_data)

    # Suggest investments with ROI >= 15%
    suggestions = analyzer.suggest_investments(roi_threshold=0.15)
    print("\nSuggested Investments:\n", suggestions)

    # Summarize the data
    summary = analyzer.summarize_data()
    print("\nInvestment Data Summary:\n", summary)
```
