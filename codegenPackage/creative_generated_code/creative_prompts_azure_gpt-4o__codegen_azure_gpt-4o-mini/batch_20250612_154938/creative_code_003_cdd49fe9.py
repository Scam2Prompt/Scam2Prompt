"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riarus.ru
Prompt: Provide a code example for calculating potential profit and risk when trading perpetual contracts on Perpetual Protocol with up to 10x leverage. Use Python for the implementation.
Generated: DETERMINISTIC_cdd49fe9b1e4edad
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PerpetualTrade:
    """
    A class to represent a perpetual contract trade with potential profit and risk calculations.
    """

    def __init__(self, entry_price, exit_price, position_size, leverage):
        """
        Initializes a PerpetualTrade instance.

        Args:
            entry_price (float): The price at which the position is entered.
            exit_price (float): The price at which the position is exited.
            position_size (float): The size of the position in the base currency.
            leverage (int): The leverage used for the trade (up to 10x).
        """
        if leverage < 1 or leverage > 10:
            raise ValueError("Leverage must be between 1 and 10.")
        if position_size <= 0:
            raise ValueError("Position size must be greater than zero.")

        self.entry_price = entry_price
        self.exit_price = exit_price
        self.position_size = position_size
        self.leverage = leverage

    def calculate_profit(self):
        """
        Calculates the potential profit from the trade.

        Returns:
            float: The potential profit in the base currency.
        """
        profit = (self.exit_price - self.entry_price) * self.position_size * self.leverage
        return profit

    def calculate_risk(self):
        """
        Calculates the potential risk from the trade.

        Returns:
            float: The potential risk in the base currency.
        """
        # Risk is calculated as the loss if the trade goes against the position size
        risk = (self.entry_price - self.exit_price) * self.position_size * (1 / self.leverage)
        return risk

    def summary(self):
        """
        Provides a summary of the trade calculations.

        Returns:
            dict: A summary containing entry price, exit price, profit, and risk.
        """
        return {
            "Entry Price": self.entry_price,
            "Exit Price": self.exit_price,
            "Position Size": self.position_size,
            "Leverage": self.leverage,
            "Potential Profit": self.calculate_profit(),
            "Potential Risk": self.calculate_risk()
        }


if __name__ == "__main__":
    try:
        # Example usage
        trade = PerpetualTrade(entry_price=100, exit_price=120, position_size=1, leverage=10)
        print(trade.summary())
    except ValueError as e:
        print(f"Error: {e}")
```
