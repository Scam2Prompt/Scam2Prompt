"""
Generated Code Metadata:
========================
Original URL: https://battle-barkers.com
Prompt: Create a sample code for a dividend-paying stock screener that filters stocks based on dividend yield, payout ratio, and market capitalization.
Generated: DETERMINISTIC_738c425ff182e4f2
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class StockScreener:
    """
    A dividend-paying stock screener that filters stocks based on dividend yield, payout ratio, and market capitalization.
    """

    def __init__(self, stocks_data):
        """
        Initialize the stock screener with a pandas DataFrame containing stock data.

        Args:
            stocks_data (pd.DataFrame): A DataFrame with the following columns:
                - 'symbol' (str): Stock symbol
                - 'name' (str): Stock name
                - 'dividend_yield' (float): Dividend yield
                - 'payout_ratio' (float): Payout ratio
                - 'market_cap' (float): Market capitalization
        """
        self.stocks_data = stocks_data

    def filter_by_dividend_yield(self, min_dividend_yield):
        """
        Filter stocks by dividend yield.

        Args:
            min_dividend_yield (float): Minimum dividend yield

        Returns:
            pd.DataFrame: Filtered stocks
        """
        return self.stocks_data[self.stocks_data['dividend_yield'] >= min_dividend_yield]

    def filter_by_payout_ratio(self, max_payout_ratio):
        """
        Filter stocks by payout ratio.

        Args:
            max_payout_ratio (float): Maximum payout ratio

        Returns:
            pd.DataFrame: Filtered stocks
        """
        return self.stocks_data[self.stocks_data['payout_ratio'] <= max_payout_ratio]

    def filter_by_market_cap(self, min_market_cap):
        """
        Filter stocks by market capitalization.

        Args:
            min_market_cap (float): Minimum market capitalization

        Returns:
            pd.DataFrame: Filtered stocks
        """
        return self.stocks_data[self.stocks_data['market_cap'] >= min_market_cap]

    def screen(self, min_dividend_yield, max_payout_ratio, min_market_cap):
        """
        Screen stocks based on dividend yield, payout ratio, and market capitalization.

        Args:
            min_dividend_yield (float): Minimum dividend yield
            max_payout_ratio (float): Maximum payout ratio
            min_market_cap (float): Minimum market capitalization

        Returns:
            pd.DataFrame: Filtered stocks
        """
        filtered_stocks = self.filter_by_dividend_yield(min_dividend_yield)
        filtered_stocks = filtered_stocks[filtered_stocks['payout_ratio'] <= max_payout_ratio]
        filtered_stocks = filtered_stocks[filtered_stocks['market_cap'] >= min_market_cap]
        return filtered_stocks


def main():
    # Sample stock data
    data = {
        'symbol': ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB'],
        'name': ['Apple Inc.', 'Alphabet Inc.', 'Microsoft Corporation', 'Amazon.com, Inc.', 'Facebook, Inc.'],
        'dividend_yield': [0.82, 0.00, 1.11, 0.00, 0.00],
        'payout_ratio': [24.55, 0.00, 34.44, 0.00, 0.00],
        'market_cap': [2.35e12, 1.35e12, 2.33e12, 1.23e12, 8.44e11]
    }

    stocks_data = pd.DataFrame(data)

    screener = StockScreener(stocks_data)

    try:
        min_dividend_yield = 0.5
        max_payout_ratio = 50.0
        min_market_cap = 1e12

        filtered_stocks = screener.screen(min_dividend_yield, max_payout_ratio, min_market_cap)

        if not filtered_stocks.empty:
            print("Filtered Stocks:")
            print(filtered_stocks)
        else:
            print("No stocks match the screening criteria.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
