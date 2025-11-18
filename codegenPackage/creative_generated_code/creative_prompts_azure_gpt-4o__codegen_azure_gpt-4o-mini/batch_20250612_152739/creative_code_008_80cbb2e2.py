"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap.pages.dev
Prompt: Generate code to analyze trade data using CoW Protocol's analytics tools and calculate the surplus saved for users during transactions.
Generated: DETERMINISTIC_80cbb2e231c9a9e7
Batch ID: 20250612_152739
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

class TradeDataAnalyzer:
    """
    A class to analyze trade data using the CoW Protocol's analytics tools.
    This class calculates the surplus saved for users during transactions.
    """

    def __init__(self, trade_data: pd.DataFrame):
        """
        Initializes the TradeDataAnalyzer with trade data.

        :param trade_data: A pandas DataFrame containing trade data with columns:
                           ['user_id', 'trade_amount', 'market_price', 'cooperative_price']
        """
        self.trade_data = trade_data
        self.validate_trade_data()

    def validate_trade_data(self):
        """
        Validates the trade data to ensure it contains the required columns and
        appropriate data types.
        """
        required_columns = ['user_id', 'trade_amount', 'market_price', 'cooperative_price']
        for column in required_columns:
            if column not in self.trade_data.columns:
                raise ValueError(f"Missing required column: {column}")

        if not all(isinstance(val, (int, float)) for val in self.trade_data['trade_amount']):
            raise TypeError("Trade amount should be numeric.")
        
        if not all(isinstance(val, (int, float)) for val in self.trade_data['market_price']):
            raise TypeError("Market price should be numeric.")
        
        if not all(isinstance(val, (int, float)) for val in self.trade_data['cooperative_price']):
            raise TypeError("Cooperative price should be numeric.")

    def calculate_surplus_saved(self) -> pd.DataFrame:
        """
        Calculates the surplus saved for users during transactions.

        :return: A DataFrame containing the user_id and their respective surplus saved.
        """
        # Calculate the surplus saved for each trade
        self.trade_data['surplus_saved'] = np.maximum(
            self.trade_data['market_price'] - self.trade_data['cooperative_price'], 0
        ) * self.trade_data['trade_amount']

        # Group by user_id and sum the surplus saved
        surplus_summary = self.trade_data.groupby('user_id', as_index=False)['surplus_saved'].sum()

        return surplus_summary

    def analyze_trades(self) -> pd.DataFrame:
        """
        Perform the complete trade analysis and return the results.

        :return: A DataFrame containing the user_id and total surplus saved.
        """
        try:
            surplus_summary = self.calculate_surplus_saved()
            return surplus_summary
        except Exception as e:
            print(f"Error during trade analysis: {str(e)}")
            return pd.DataFrame()  # Return an empty DataFrame on error


# Example usage
if __name__ == "__main__":
    # Sample trade data
    data = {
        'user_id': [1, 2, 1, 3],
        'trade_amount': [10, 15, 5, 20],
        'market_price': [100, 110, 120, 130],
        'cooperative_price': [90, 105, 115, 125]
    }

    trade_data_df = pd.DataFrame(data)

    # Create an analyzer instance
    analyzer = TradeDataAnalyzer(trade_data_df)

    # Analyze the trades and get the surplus saved
    result = analyzer.analyze_trades()

    print(result)
```
