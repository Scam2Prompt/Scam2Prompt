"""
Generated Code Metadata:
========================
Original URL: https://connect-moca.com
Prompt: Generate code to calculate margin level and free margin for a trading account based on the formulas provided in CFD trading documentation.
Generated: DETERMINISTIC_37b3dbf818849bb6
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingAccount:
    def __init__(self, balance: float, equity: float, margin_used: float):
        """
        Initialize the TradingAccount with balance, equity, and margin used.

        :param balance: The total balance of the trading account.
        :param equity: The current equity of the trading account.
        :param margin_used: The amount of margin currently used in open positions.
        """
        self.balance = balance
        self.equity = equity
        self.margin_used = margin_used

    def calculate_margin_level(self) -> float:
        """
        Calculate the margin level of the trading account.

        Margin Level = (Equity / Margin Used) * 100

        :return: The margin level as a percentage.
        :raises ValueError: If margin_used is zero to prevent division by zero.
        """
        if self.margin_used == 0:
            raise ValueError("Margin used cannot be zero for margin level calculation.")
        
        margin_level = (self.equity / self.margin_used) * 100
        return margin_level

    def calculate_free_margin(self) -> float:
        """
        Calculate the free margin of the trading account.

        Free Margin = Equity - Margin Used

        :return: The free margin available in the trading account.
        """
        free_margin = self.equity - self.margin_used
        return free_margin

# Example usage
if __name__ == "__main__":
    try:
        # Create a trading account with sample values
        account = TradingAccount(balance=10000.0, equity=12000.0, margin_used=5000.0)

        # Calculate and print margin level
        margin_level = account.calculate_margin_level()
        print(f"Margin Level: {margin_level:.2f}%")

        # Calculate and print free margin
        free_margin = account.calculate_free_margin()
        print(f"Free Margin: {free_margin:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
