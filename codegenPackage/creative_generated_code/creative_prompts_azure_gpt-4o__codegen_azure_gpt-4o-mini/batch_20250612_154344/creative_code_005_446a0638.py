"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamino-webapp.pages.dev
Prompt: Create a code snippet to calculate and visualize yield performance data for assets deployed in Kamino's liquidity layer, including USDC, USDT, and SOL.
Generated: DETERMINISTIC_446a0638bd616eae
Batch ID: 20250612_154344
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

class AssetYieldCalculator:
    """
    A class to calculate and visualize yield performance data for assets in Kamino's liquidity layer.
    
    Attributes:
        asset_data (DataFrame): A DataFrame containing asset performance data.
    """

    def __init__(self, data):
        """
        Initializes the AssetYieldCalculator with asset performance data.

        Args:
            data (dict): A dictionary containing asset names as keys and their yields as values.
        """
        self.asset_data = pd.DataFrame(data)
    
    def calculate_average_yield(self):
        """
        Calculate the average yield for each asset.

        Returns:
            DataFrame: A DataFrame containing average yield data.
        """
        try:
            average_yield = self.asset_data.mean()
            return average_yield
        except Exception as e:
            print(f"Error calculating average yield: {e}")
            return None
    
    def visualize_yield_performance(self):
        """
        Visualizes the yield performance of the assets using a bar chart.
        """
        try:
            average_yield = self.calculate_average_yield()
            if average_yield is not None:
                average_yield.plot(kind='bar', color=['blue', 'green', 'orange'])
                plt.title('Average Yield Performance of Assets')
                plt.xlabel('Assets')
                plt.ylabel('Average Yield (%)')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
        except Exception as e:
            print(f"Error visualizing yield performance: {e}")

# Sample data for assets deployed in Kamino's liquidity layer
asset_performance_data = {
    'USDC': [0.05, 0.07, 0.06, 0.08, 0.07],
    'USDT': [0.04, 0.03, 0.05, 0.06, 0.05],
    'SOL': [0.10, 0.12, 0.11, 0.13, 0.14]
}

# Instantiate the AssetYieldCalculator
yield_calculator = AssetYieldCalculator(asset_performance_data)

# Calculate and print average yields
average_yields = yield_calculator.calculate_average_yield()
if average_yields is not None:
    print("Average Yield for assets:")
    print(average_yields)

# Visualize the yield performance
yield_calculator.visualize_yield_performance()
```
