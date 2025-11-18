"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts-usualdao.com
Prompt: Create a Python program to analyze BTC0 and ETH0 asset yields and revenue contributions to UsualDAO’s treasury, and generate a report on their impact on protocol growth.
Generated: DETERMINISTIC_0c7fa8ace3b2e11a
Batch ID: 20250612_142608
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

class AssetAnalyzer:
    """
    A class to analyze the yields and revenue contributions of BTC0 and ETH0 assets
    to UsualDAO's treasury.
    """

    def __init__(self, btc_data: pd.DataFrame, eth_data: pd.DataFrame):
        """
        Initialize the AssetAnalyzer with BTC0 and ETH0 data.

        :param btc_data: DataFrame containing BTC0 yield data
        :param eth_data: DataFrame containing ETH0 yield data
        """
        self.btc_data = btc_data
        self.eth_data = eth_data

    def calculate_yield(self):
        """
        Calculate the yield for both assets.
        
        :return: A tuple of yields for BTC0 and ETH0
        """
        try:
            btc_yield = self.btc_data['revenue'].sum() / self.btc_data['investment'].sum()
            eth_yield = self.eth_data['revenue'].sum() / self.eth_data['investment'].sum()
            return btc_yield, eth_yield
        except ZeroDivisionError:
            print("Investment sum is zero, cannot calculate yield.")
            return None, None
        except Exception as e:
            print(f"An error occurred while calculating yields: {e}")
            return None, None

    def generate_report(self, btc_yield: float, eth_yield: float):
        """
        Generate a report on the impact of yields on protocol growth.

        :param btc_yield: The yield from BTC0
        :param eth_yield: The yield from ETH0
        """
        report = f"""
        UsualDAO Treasury Asset Yield Report:
        --------------------------------------
        BTC0 Yield: {btc_yield:.2%}
        ETH0 Yield: {eth_yield:.2%}
        
        Contribution to Growth:
        BTC0 contributes significantly to the treasury with a yield of {btc_yield:.2%}.
        ETH0 complements this with a yield of {eth_yield:.2%}.
        """
        print(report)

    def visualize_data(self):
        """
        Visualize the revenue contributions of both assets.
        """
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(self.btc_data['date'], self.btc_data['revenue'], label='BTC0 Revenue', color='orange')
            plt.plot(self.eth_data['date'], self.eth_data['revenue'], label='ETH0 Revenue', color='blue')
            plt.title('Revenue Contributions of BTC0 and ETH0')
            plt.xlabel('Date')
            plt.ylabel('Revenue')
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while visualizing data: {e}")

def main():
    """
    Main function to execute the asset analysis.
    """
    # Sample DataFrame creation (In practice, load your data from a trusted source)
    btc_data = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'revenue': np.random.uniform(100, 500, size=12),
        'investment': np.random.uniform(1000, 5000, size=12)
    })

    eth_data = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'revenue': np.random.uniform(200, 600, size=12),
        'investment': np.random.uniform(1500, 6000, size=12)
    })

    # Instantiate the analyzer
    analyzer = AssetAnalyzer(btc_data, eth_data)

    # Calculate yields
    btc_yield, eth_yield = analyzer.calculate_yield()

    # Generate report if yields were successfully calculated
    if btc_yield is not None and eth_yield is not None:
        analyzer.generate_report(btc_yield, eth_yield)

    # Visualize data
    analyzer.visualize_data()

if __name__ == "__main__":
    main()
```
