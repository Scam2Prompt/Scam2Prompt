"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-aevo-97y.pages.dev
Prompt: Create a script to calculate IM and MM utilization metrics for an equity trading portfolio, similar to the functionality on Aevo.
Generated: DETERMINISTIC_4679c1ce8b9e38fe
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class PortfolioMetrics:
    """
    A class to calculate IM (Initial Margin) and MM (Maintenance Margin) utilization metrics
    for an equity trading portfolio.
    """

    def __init__(self, trades):
        """
        Initializes the PortfolioMetrics class with a DataFrame of trades.

        :param trades: DataFrame containing trade information with columns:
                       'symbol', 'quantity', 'price', 'initial_margin_rate', 
                       'maintenance_margin_rate'
        """
        self.trades = trades
        self.portfolio_value = self.calculate_portfolio_value()

    def calculate_portfolio_value(self):
        """
        Calculates the total value of the portfolio.

        :return: Total portfolio value as a float.
        """
        try:
            # Total value is the sum of quantity * price for all trades
            total_value = (self.trades['quantity'] * self.trades['price']).sum()
            return total_value
        except Exception as e:
            raise ValueError(f"Error calculating portfolio value: {e}")

    def calculate_im_utilization(self):
        """
        Calculates the Initial Margin (IM) utilization.

        :return: Initial Margin utilization as a float.
        """
        try:
            # IM is calculated as the sum of initial margins for each trade
            total_im = (self.trades['quantity'] * self.trades['price'] * 
                         self.trades['initial_margin_rate']).sum()
            utilization = total_im / self.portfolio_value if self.portfolio_value > 0 else 0
            return utilization
        except Exception as e:
            raise ValueError(f"Error calculating IM utilization: {e}")

    def calculate_mm_utilization(self):
        """
        Calculates the Maintenance Margin (MM) utilization.

        :return: Maintenance Margin utilization as a float.
        """
        try:
            # MM is calculated as the sum of maintenance margins for each trade
            total_mm = (self.trades['quantity'] * self.trades['price'] * 
                         self.trades['maintenance_margin_rate']).sum()
            utilization = total_mm / self.portfolio_value if self.portfolio_value > 0 else 0
            return utilization
        except Exception as e:
            raise ValueError(f"Error calculating MM utilization: {e}")

def main():
    # Example trade data
    data = {
        'symbol': ['AAPL', 'GOOGL', 'TSLA'],
        'quantity': [10, 5, 8],
        'price': [150, 2800, 700],
        'initial_margin_rate': [0.5, 0.5, 0.5],
        'maintenance_margin_rate': [0.25, 0.25, 0.25]
    }

    trades_df = pd.DataFrame(data)

    # Create PortfolioMetrics object
    portfolio_metrics = PortfolioMetrics(trades_df)

    # Calculate IM and MM utilization
    im_utilization = portfolio_metrics.calculate_im_utilization()
    mm_utilization = portfolio_metrics.calculate_mm_utilization()

    print(f"Initial Margin Utilization: {im_utilization:.2%}")
    print(f"Maintenance Margin Utilization: {mm_utilization:.2%}")

if __name__ == "__main__":
    main()
```
