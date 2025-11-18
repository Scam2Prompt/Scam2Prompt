"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://action-coin.com
Prompt: Write a script to calculate potential profits or losses when trading CFDs on stocks, using the concept of price movement in either direction, as explained on Action Coin.
Generated: DETERMINISTIC_466bdba358b64474
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CFDTradingCalculator:
    def __init__(self, initial_investment, leverage_ratio):
        """
        Initializes the CFDTradingCalculator with the initial investment and leverage ratio.

        :param initial_investment: The amount of money the trader is willing to invest.
        :param leverage_ratio: The leverage ratio for the CFD trading.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if leverage_ratio <= 1:
            raise ValueError("Leverage ratio must be greater than one.")

        self.initial_investment = initial_investment
        self.leverage_ratio = leverage_ratio

    def calculate_position_size(self):
        """
        Calculates the total position size based on initial investment and leverage.

        :return: Total position size.
        """
        return self.initial_investment * self.leverage_ratio

    def calculate_profit_loss(self, entry_price, exit_price, number_of_shares):
        """
        Calculates potential profit or loss from a CFD trade.

        :param entry_price: The price at which the position is entered.
        :param exit_price: The price at which the position is exited.
        :param number_of_shares: The number of shares in the position.
        :return: Potential profit or loss.
        """
        if number_of_shares <= 0:
            raise ValueError("Number of shares must be greater than zero.")
        if entry_price <= 0 or exit_price <= 0:
            raise ValueError("Entry and exit prices must be greater than zero.")

        # Calculate profit or loss
        profit_loss = (exit_price - entry_price) * number_of_shares
        return profit_loss

    def summary(self, entry_price, exit_price, number_of_shares):
        """
        Provides a summary of the trade showing potential profit or loss.

        :param entry_price: The price at which the position is entered.
        :param exit_price: The price at which the position is exited.
        :param number_of_shares: The number of shares in the position.
        """
        try:
            position_size = self.calculate_position_size()
            pnl = self.calculate_profit_loss(entry_price, exit_price, number_of_shares)
            return {
                "Initial Investment": self.initial_investment,
                "Leverage Ratio": self.leverage_ratio,
                "Position Size": position_size,
                "Profit/Loss": pnl
            }
        except ValueError as e:
            return {"Error": str(e)}


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with an initial investment of $1000 and leverage of 5
        calculator = CFDTradingCalculator(initial_investment=1000, leverage_ratio=5)

        # Define trade parameters
        entry_price = 50.0  # Example entry price
        exit_price = 55.0   # Example exit price
        number_of_shares = 10  # Number of shares traded

        # Get the summary of the trade
        trade_summary = calculator.summary(entry_price, exit_price, number_of_shares)
        print(trade_summary)

    except Exception as e:
        print(f"An error occurred: {e}")
```
