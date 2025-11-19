"""
Generated Code Metadata:
========================
Original URL: https://action-coin.com
Prompt: Create a function that calculates potential profits and losses when trading CFDs on stocks using Action Coin's trading parameters.
Generated: DETERMINISTIC_9b21eb498dddf76c
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CFDTrading:
    """
    A class to represent a CFD trading scenario for stocks.
    """

    def __init__(self, leverage: float, commission_rate: float):
        """
        Initializes the CFDTrading class with leverage and commission rate.

        :param leverage: The leverage ratio for trading.
        :param commission_rate: The commission rate as a decimal (e.g., 0.01 for 1%).
        """
        if leverage <= 0:
            raise ValueError("Leverage must be a positive number.")
        if commission_rate < 0:
            raise ValueError("Commission rate cannot be negative.")

        self.leverage = leverage
        self.commission_rate = commission_rate

    def calculate_profit_loss(self, entry_price: float, exit_price: float, quantity: int) -> dict:
        """
        Calculates potential profits and losses from a CFD trade.

        :param entry_price: The price at which the stock was bought.
        :param exit_price: The price at which the stock is sold.
        :param quantity: The number of shares traded.
        :return: A dictionary containing profit/loss and net profit/loss after commission.
        """
        if entry_price <= 0 or exit_price <= 0:
            raise ValueError("Entry and exit prices must be positive numbers.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate gross profit/loss
        gross_profit_loss = (exit_price - entry_price) * quantity

        # Calculate commission cost
        commission_cost = gross_profit_loss * self.commission_rate

        # Calculate net profit/loss
        net_profit_loss = gross_profit_loss - commission_cost

        return {
            "gross_profit_loss": gross_profit_loss,
            "commission_cost": commission_cost,
            "net_profit_loss": net_profit_loss
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize CFD trading parameters
        trading = CFDTrading(leverage=10, commission_rate=0.01)

        # Calculate profit/loss for a trade
        result = trading.calculate_profit_loss(entry_price=100, exit_price=110, quantity=5)

        # Print the results
        print("Gross Profit/Loss:", result["gross_profit_loss"])
        print("Commission Cost:", result["commission_cost"])
        print("Net Profit/Loss:", result["net_profit_loss"])

    except ValueError as e:
        print(f"Error: {e}")
```
