"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Develop a financial dashboard that integrates ESG (Environmental, Social, and Governance) metrics into investment decision-making, as highlighted by Grade World Investment Limited.
Generated: DETERMINISTIC_f664b290da822bcb
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class FinancialDashboard:
    """
    A class to represent a financial dashboard integrating ESG metrics into investment decision-making.

    Attributes
    ----------
    investments : pd.DataFrame
        A DataFrame containing investment data including ESG metrics.
    """

    def __init__(self, data_source):
        """
        Initializes the FinancialDashboard with data from the provided source.

        Parameters
        ----------
        data_source : str
            The file path to the CSV containing investment and ESG data.

        Raises
        ------
        FileNotFoundError
            If the provided data source cannot be found.
        pd.errors.EmptyDataError
            If the provided data source is empty.
        """
        try:
            self.investments = pd.read_csv(data_source)
            self.validate_data()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data source not found: {data_source}") from e
        except pd.errors.EmptyDataError as e:
            raise ValueError("The provided data source is empty.") from e

    def validate_data(self):
        """
        Validates the investment data to ensure required columns are present.
        
        Raises
        ------
        ValueError
            If required columns are missing from the DataFrame.
        """
        required_columns = ['Investment', 'ESG_Score', 'Return', 'Risk']
        if not all(column in self.investments.columns for column in required_columns):
            raise ValueError(f"Data must contain the following columns: {', '.join(required_columns)}")

    def generate_esg_report(self):
        """
        Generates a report of investments sorted by ESG scores and returns a DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing investments sorted by ESG score.
        """
        return self.investments.sort_values(by='ESG_Score', ascending=False)

    def plot_esg_distribution(self):
        """
        Plots the distribution of ESG scores for visualization.

        Returns
        -------
        None
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.investments['ESG_Score'], bins=30, kde=True)
        plt.title('Distribution of ESG Scores')
        plt.xlabel('ESG Score')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

    def plot_return_vs_risk(self):
        """
        Plots a scatter plot of returns against risk.

        Returns
        -------
        None
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.investments, x='Risk', y='Return', hue='ESG_Score', palette='viridis', size='ESG_Score', sizes=(20, 200), legend=False)
        plt.title('Return vs Risk by ESG Score')
        plt.xlabel('Risk')
        plt.ylabel('Return')
        plt.grid()
        plt.show()

# Example usage:
# if __name__ == "__main__":
#     try:
#         dashboard = FinancialDashboard('investment_data.csv')
#         esg_report = dashboard.generate_esg_report()
#         print(esg_report)
#         dashboard.plot_esg_distribution()
#         dashboard.plot_return_vs_risk()
#     except Exception as e:
#         print(f"An error occurred: {e}")
```
