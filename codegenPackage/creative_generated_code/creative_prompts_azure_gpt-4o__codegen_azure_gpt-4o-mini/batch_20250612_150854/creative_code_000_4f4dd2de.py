"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-zenar.com
Prompt: Write Python code to simulate a value investing strategy that identifies undervalued stocks based on market capitalization and ROI metrics, as described by Immediate Zenar's investment education framework.
Generated: DETERMINISTIC_4f4dd2dea522100d
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

class ValueInvestingStrategy:
    """
    A class to represent a value investing strategy that identifies undervalued stocks
    based on market capitalization and Return on Investment (ROI) metrics.
    """

    def __init__(self, stock_data):
        """
        Initializes the ValueInvestingStrategy with stock data.

        :param stock_data: A DataFrame containing stock information with columns
                           ['ticker', 'market_cap', 'roi']
        """
        self.stock_data = stock_data

    def validate_data(self):
        """
        Validates the stock data for necessary columns and non-negative values.

        Raises:
            ValueError: If the required columns are missing or if any values are negative.
        """
        required_columns = ['ticker', 'market_cap', 'roi']
        if not all(col in self.stock_data.columns for col in required_columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")

        if (self.stock_data['market_cap'] < 0).any() or (self.stock_data['roi'] < 0).any():
            raise ValueError("Market capitalization and ROI must be non-negative.")

    def identify_undervalued_stocks(self, market_cap_threshold=1e9, roi_threshold=0.1):
        """
        Identifies undervalued stocks based on market capitalization and ROI.

        :param market_cap_threshold: Minimum market capitalization to consider a stock.
        :param roi_threshold: Minimum ROI to consider a stock as undervalued.
        :return: DataFrame of undervalued stocks.
        """
        # Validate the stock data before processing
        self.validate_data()

        # Filter stocks based on the thresholds
        undervalued_stocks = self.stock_data[
            (self.stock_data['market_cap'] < market_cap_threshold) &
            (self.stock_data['roi'] > roi_threshold)
        ]

        return undervalued_stocks.reset_index(drop=True)

def main():
    """
    Main function to run the value investing strategy.
    """
    # Sample stock data for demonstration purposes
    data = {
        'ticker': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA'],
        'market_cap': [2.5e12, 2.0e12, 1.5e12, 1.7e12, 800e9],
        'roi': [0.15, 0.12, 0.08, 0.05, 0.25]
    }

    # Create a DataFrame
    stock_data = pd.DataFrame(data)

    # Initialize the ValueInvestingStrategy
    strategy = ValueInvestingStrategy(stock_data)

    # Identify undervalued stocks
    try:
        undervalued_stocks = strategy.identify_undervalued_stocks()
        print("Undervalued Stocks:")
        print(undervalued_stocks)
    except ValueError as e:
        print(f"Error encountered: {e}")

if __name__ == "__main__":
    main()
```
