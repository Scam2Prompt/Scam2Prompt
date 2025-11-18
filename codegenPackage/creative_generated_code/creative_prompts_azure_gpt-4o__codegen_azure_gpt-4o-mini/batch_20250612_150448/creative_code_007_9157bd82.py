"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Provide code examples for analyzing high-quality asset investments using systematic approaches, similar to the strategies employed by Grade World Investment Limited.
Generated: DETERMINISTIC_9157bd82fca9903a
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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class AssetAnalyzer:
    """
    A class to analyze high-quality asset investments using systematic approaches.
    """

    def __init__(self, data):
        """
        Initializes the AssetAnalyzer with data.
        
        Parameters:
        data (DataFrame): A Pandas DataFrame containing asset investment data.
        """
        self.data = data
        self.results = None

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and outliers.
        """
        # Handle missing values by dropping or filling
        self.data.dropna(inplace=True)

        # Identify and remove outliers using z-score
        z_scores = np.abs(stats.zscore(self.data.select_dtypes(include=[np.number])))
        self.data = self.data[(z_scores < 3).all(axis=1)]

    def calculate_returns(self):
        """
        Calculate the returns of each asset in the portfolio.
        
        Returns:
        DataFrame: A DataFrame containing returns for each asset.
        """
        try:
            returns = self.data.pct_change().dropna()
            return returns
        except Exception as e:
            print(f"Error calculating returns: {e}")
            return None

    def compute_sharpe_ratio(self, returns, risk_free_rate=0.01):
        """
        Calculate the Sharpe Ratio for the given returns.

        Parameters:
        returns (DataFrame): Asset returns DataFrame.
        risk_free_rate (float): The risk-free rate.

        Returns:
        Series: Sharpe ratios for each asset.
        """
        try:
            excess_returns = returns.mean() - risk_free_rate
            volatility = returns.std()
            sharpe_ratio = excess_returns / volatility
            return sharpe_ratio
        except Exception as e:
            print(f"Error computing Sharpe Ratio: {e}")
            return None

    def plot_heatmap(self, returns):
        """
        Visualizes the correlation matrix of asset returns using a heatmap.
        
        Parameters:
        returns (DataFrame): Asset returns DataFrame.
        """
        try:
            plt.figure(figsize=(10, 8))
            correlation_matrix = returns.corr()
            sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
            plt.title("Correlation Matrix of Asset Returns")
            plt.show()
        except Exception as e:
            print(f"Error plotting heatmap: {e}")

    def analyze_investments(self):
        """
        Main method to perform the investment analysis.
        It preprocesses data, calculates returns, computes Sharpe ratios, and plots heatmap.
        """
        self.preprocess_data()
        
        returns = self.calculate_returns()
        if returns is not None:
            self.results = {
                'returns': returns,
                'sharpe_ratio': self.compute_sharpe_ratio(returns)
            }
            self.plot_heatmap(returns)

# Example usage:
if __name__ == "__main__":
    # Load your asset investment data into a Pandas DataFrame
    try:
        # Replace 'your_data.csv' with your actual data source
        asset_data = pd.read_csv('your_data.csv')
        analyzer = AssetAnalyzer(asset_data)
        analyzer.analyze_investments()
    except FileNotFoundError:
        print("The data file was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
