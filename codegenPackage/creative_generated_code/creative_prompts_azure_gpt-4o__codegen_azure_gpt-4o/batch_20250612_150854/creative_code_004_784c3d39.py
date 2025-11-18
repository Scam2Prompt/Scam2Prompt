"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Write a Python script to analyze investment risks and returns for different types of assets, such as cryptocurrencies, forex, and mutual funds, as outlined on Immediate Peak.
Generated: DETERMINISTIC_784c3d3979f03cd7
Batch ID: 20250612_150854
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
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Define constants for the types of assets
ASSET_TYPES = ["Cryptocurrency", "Forex", "Mutual Funds"]

class InvestmentAnalyzer:
    """
    Class to analyze investment risks and returns for various asset types.
    """

    def __init__(self, data):
        """
        Initializes the InvestmentAnalyzer with provided data.

        :param data: A Pandas DataFrame containing asset data with columns:
            'Asset Type', 'Name', 'Returns', and 'Volatility'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data format.
        Raises an exception if the format is incorrect.
        """
        required_columns = ['Asset Type', 'Name', 'Returns', 'Volatility']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        if not all(asset in ASSET_TYPES for asset in self.data['Asset Type']):
            raise ValueError("Invalid asset type detected in the data.")

    def calculate_risk_return_metrics(self):
        """
        Calculates risk and return metrics (mean return, standard deviation, skewness, and kurtosis)
        for each asset type.

        :return: A Pandas DataFrame with the metrics for each asset type.
        """
        metrics = []
        for asset_type in ASSET_TYPES:
            asset_data = self.data[self.data['Asset Type'] == asset_type]['Returns']
            if len(asset_data) == 0:  # Skip if no data for the asset type
                continue
            metrics.append({
                'Asset Type': asset_type,
                'Mean Return': np.mean(asset_data),
                'Volatility (Std Dev)': np.std(asset_data),
                'Skewness': skew(asset_data),
                'Kurtosis': kurtosis(asset_data)
            })
        return pd.DataFrame(metrics)

    def plot_asset_metrics(self):
        """
        Plots the risk-return characteristics for each asset type.
        """
        avg_returns = []
        avg_volatility = []
        labels = []

        for asset_type in ASSET_TYPES:
            asset_data = self.data[self.data['Asset Type'] == asset_type]
            if len(asset_data) == 0:
                continue
            avg_returns.append(asset_data['Returns'].mean())
            avg_volatility.append(asset_data['Volatility'].mean())
            labels.append(asset_type)

        plt.figure(figsize=(10, 6))
        plt.scatter(avg_volatility, avg_returns, c='blue', label='Assets')
        for i, label in enumerate(labels):
            plt.text(avg_volatility[i], avg_returns[i], label, fontsize=10)

        plt.title('Risk vs Return Analysis')
        plt.xlabel('Volatility (Risk)')
        plt.ylabel('Average Returns')
        plt.grid(True)
        plt.legend()
        plt.show()

    def analyze(self):
        """
        Performs a complete analysis, including calculating metrics and plotting.

        :return: A Pandas DataFrame containing the risk-return metrics.
        """
        print("Calculating risk-return metrics...")
        metrics = self.calculate_risk_return_metrics()
        print(metrics)

        print("\nPlotting asset metrics...")
        self.plot_asset_metrics()
        return metrics


if __name__ == "__main__":
    # Example data for testing (replace with actual data)
    example_data = pd.DataFrame({
        'Asset Type': ['Cryptocurrency', 'Cryptocurrency', 'Forex', 'Forex', 'Mutual Funds', 'Mutual Funds'],
        'Name': ['Bitcoin', 'Ethereum', 'EUR/USD', 'GBP/USD', 'Fund A', 'Fund B'],
        'Returns': [0.12, 0.08, 0.02, 0.03, 0.05, 0.06],
        'Volatility': [0.5, 0.45, 0.1, 0.12, 0.2, 0.18]
    })

    # Instantiate the analyzer and run the analysis
    try:
        analyzer = InvestmentAnalyzer(example_data)
        results = analyzer.analyze()
    except Exception as e:
        print(f"Error occurred during analysis: {e}")
```
