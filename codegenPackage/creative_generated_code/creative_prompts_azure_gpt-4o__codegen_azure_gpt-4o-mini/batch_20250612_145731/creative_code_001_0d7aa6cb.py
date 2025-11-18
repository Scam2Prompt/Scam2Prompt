"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pass-vee.com
Prompt: Generate code to calculate margin level and free margin for a trading account based on the definitions provided on the Changexcapital website.
Generated: DETERMINISTIC_0d7aa6cb7e6404a0
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingAccount:
    """
    A class to represent a trading account and calculate margin level and free margin.
    """

    def __init__(self, balance: float, equity: float, margin_used: float):
        """
        Initialize the trading account with balance, equity, and margin used.

        :param balance: The amount of money in the account.
        :param equity: The total value of the account, including open positions.
        :param margin_used: The amount of money currently used as margin for open positions.
        """
        if balance < 0 or equity < 0 or margin_used < 0:
            raise ValueError("Balance, equity, and margin used must be non-negative.")

        self.balance = balance
        self.equity = equity
        self.margin_used = margin_used

    def calculate_margin_level(self) -> float:
        """
        Calculate the margin level of the account.

        Margin Level = (Equity / Margin Used) * 100

        :return: The margin level as a percentage.
        """
        if self.margin_used == 0:
            return float('inf')  # Avoid division by zero, return infinity if no margin used.
        
        margin_level = (self.equity / self.margin_used) * 100
        return margin_level

    def calculate_free_margin(self) -> float:
        """
        Calculate the free margin of the account.

        Free Margin = Equity - Margin Used

        :return: The free margin available for opening new positions.
        """
        free_margin = self.equity - self.margin_used
        return free_margin

    def __str__(self) -> str:
        """
        String representation of the trading account's financial status.

        :return: A formatted string with balance, equity, margin used, free margin, and margin level.
        """
        return (f"Balance: ${self.balance:.2f}, "
                f"Equity: ${self.equity:.2f}, "
                f"Margin Used: ${self.margin_used:.2f}, "
                f"Free Margin: ${self.calculate_free_margin():.2f}, "
                f"Margin Level: {self.calculate_margin_level():.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        # Example values for a trading account
        balance = 10000.0  # Account balance
        equity = 15000.0   # Current account equity
        margin_used = 5000.0  # Margin used for open positions

        account = TradingAccount(balance, equity, margin_used)

        # Output the account status
        print(account)
    except ValueError as e:
        print(f"Error: {e}")
```
