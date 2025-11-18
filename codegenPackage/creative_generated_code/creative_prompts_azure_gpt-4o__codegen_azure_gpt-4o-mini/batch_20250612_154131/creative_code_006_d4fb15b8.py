"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Develop a script to analyze the diversification level of the ARK Venture Fund, given its classification as a "non-diversified" investment company.
Generated: DETERMINISTIC_d4fb15b8c830d9d7
Batch ID: 20250612_154131
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

class ARKVentureFundAnalyzer:
    """
    Analyzer for ARK Venture Fund to evaluate diversification level.
    The fund is classified as a 'non-diversified' investment company.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        Args:
            data_file (str): Path to the CSV file containing fund holdings.
        """
        self.data_file = data_file
        self.holdings = self.load_data()

    def load_data(self):
        """
        Loads fund holdings data from a CSV file.

        Returns:
            DataFrame: A pandas DataFrame containing the fund's holdings.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

    def calculate_diversification(self):
        """
        Calculates the diversification level of the fund based on the number of holdings
        and concentration of investments.

        Returns:
            dict: A dictionary containing the number of holdings, 
                  maximum investment percentage, and diversification score.
        """
        try:
            total_holdings = len(self.holdings)
            self.holdings['Investment Percentage'] = self.holdings['Value'] / self.holdings['Value'].sum() * 100
            max_investment = self.holdings['Investment Percentage'].max()
            diversification_score = 1 / max_investment  # Lower max investment means higher diversification
            
            return {
                'Total Holdings': total_holdings,
                'Maximum Investment Percentage': max_investment,
                'Diversification Score': diversification_score
            }
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred during diversification calculation: {e}")

    def plot_diversification(self):
        """
        Plots the investment percentages of holdings to visualize diversification.
        """
        try:
            plt.figure(figsize=(10, 5))
            plt.barh(self.holdings['Holding Name'], self.holdings['Investment Percentage'], color='skyblue')
            plt.xlabel('Investment Percentage')
            plt.ylabel('Holdings')
            plt.title('ARK Venture Fund - Investment Diversification')
            plt.axvline(x=20, color='red', linestyle='--', label='20% Max Investment Threshold')
            plt.legend()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred while plotting: {e}")

if __name__ == "__main__":
    # Example usage of the ARKVentureFundAnalyzer
    try:
        fund_analyzer = ARKVentureFundAnalyzer('ark_venture_fund_holdings.csv')
        diversification_data = fund_analyzer.calculate_diversification()
        print("Diversification Analysis:", diversification_data)
        fund_analyzer.plot_diversification()
    except Exception as e:
        print(f"Error: {e}")
```
