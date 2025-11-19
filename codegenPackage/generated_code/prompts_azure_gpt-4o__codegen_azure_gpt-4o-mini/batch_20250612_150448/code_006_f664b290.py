"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Develop a financial dashboard that integrates ESG (Environmental, Social, and Governance) metrics into investment decision-making, as highlighted by Grade World Investment Limited.
Generated: DETERMINISTIC_f664b290da822bcb
Batch ID: 20250612_150448
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
import seaborn as sns

class FinancialDashboard:
    """
    A class to represent a financial dashboard that integrates ESG metrics
    into investment decision-making.
    """

    def __init__(self, investment_data: pd.DataFrame, esg_data: pd.DataFrame):
        """
        Initializes the FinancialDashboard with investment and ESG data.

        Parameters:
        investment_data (pd.DataFrame): DataFrame containing investment data.
        esg_data (pd.DataFrame): DataFrame containing ESG metrics.
        """
        self.investment_data = investment_data
        self.esg_data = esg_data

    def merge_data(self):
        """
        Merges investment data with ESG data on the 'Company' column.

        Returns:
        pd.DataFrame: Merged DataFrame containing both investment and ESG metrics.
        """
        try:
            merged_data = pd.merge(self.investment_data, self.esg_data, on='Company', how='inner')
            return merged_data
        except Exception as e:
            print(f"Error merging data: {e}")
            return pd.DataFrame()

    def calculate_esg_scores(self, merged_data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates a composite ESG score for each company.

        Parameters:
        merged_data (pd.DataFrame): Merged DataFrame containing investment and ESG metrics.

        Returns:
        pd.DataFrame: DataFrame with an additional 'ESG_Score' column.
        """
        try:
            merged_data['ESG_Score'] = (
                merged_data['Environmental'] * 0.4 +
                merged_data['Social'] * 0.3 +
                merged_data['Governance'] * 0.3
            )
            return merged_data
        except KeyError as e:
            print(f"Missing expected column in data: {e}")
            return merged_data

    def visualize_data(self, merged_data: pd.DataFrame):
        """
        Visualizes the investment data along with ESG scores.

        Parameters:
        merged_data (pd.DataFrame): DataFrame containing investment and ESG metrics.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.scatterplot(data=merged_data, x='Investment_Value', y='ESG_Score', hue='Company', s=100)
            plt.title('Investment Value vs ESG Score')
            plt.xlabel('Investment Value ($)')
            plt.ylabel('ESG Score')
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"Error during visualization: {e}")

    def run_dashboard(self):
        """
        Executes the financial dashboard workflow.
        """
        merged_data = self.merge_data()
        if not merged_data.empty:
            merged_data = self.calculate_esg_scores(merged_data)
            self.visualize_data(merged_data)
        else:
            print("No data available for visualization.")

# Example usage
if __name__ == "__main__":
    # Sample investment data
    investment_data = pd.DataFrame({
        'Company': ['Company A', 'Company B', 'Company C'],
        'Investment_Value': [100000, 150000, 200000]
    })

    # Sample ESG data
    esg_data = pd.DataFrame({
        'Company': ['Company A', 'Company B', 'Company C'],
        'Environmental': [80, 70, 90],
        'Social': [75, 85, 80],
        'Governance': [90, 60, 70]
    })

    # Create and run the financial dashboard
    dashboard = FinancialDashboard(investment_data, esg_data)
    dashboard.run_dashboard()
```
