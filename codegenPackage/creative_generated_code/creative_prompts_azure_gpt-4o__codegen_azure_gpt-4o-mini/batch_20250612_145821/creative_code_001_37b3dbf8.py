"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-moca.com
Prompt: Generate code to calculate margin level and free margin for a trading account based on the formulas provided in CFD trading documentation.
Generated: DETERMINISTIC_37b3dbf818849bb6
Batch ID: 20250612_145821
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

    Attributes
    ----------
    account_balance : float
        The total balance available in the trading account.
    margin_used : float
        The total margin currently used for open positions.
    """
    
    def __init__(self, account_balance: float, margin_used: float):
        """
        Constructs all the necessary attributes for the TradingAccount object.

        Parameters
        ----------
        account_balance : float
            Initial balance of the trading account.
        margin_used : float
            Initial margin used for open positions.
        """
        if account_balance < 0:
            raise ValueError("Account balance cannot be negative.")
        if margin_used < 0:
            raise ValueError("Margin used cannot be negative.")
        
        self.account_balance = account_balance
        self.margin_used = margin_used

    def calculate_free_margin(self) -> float:
        """
        Calculates the free margin available in the trading account.

        Returns
        -------
        float
            The free margin calculated as account balance minus margin used.
        """
        free_margin = self.account_balance - self.margin_used
        if free_margin < 0:
            free_margin = 0  # Free margin cannot be negative
        return free_margin

    def calculate_margin_level(self) -> float:
        """
        Calculates the margin level of the trading account.

        Returns
        -------
        float
            The margin level as a percentage calculated using the formula:
            (Equity / Margin Used) * 100
        """
        equity = self.account_balance  # Assuming account balance equals equity in this context
        if self.margin_used == 0:
            return float('inf')  # If no margin is used, margin level is infinite
        
        margin_level = (equity / self.margin_used) * 100
        return margin_level

# Example usage:
try:
    account = TradingAccount(account_balance=10000.0, margin_used=2000.0)
    free_margin = account.calculate_free_margin()
    margin_level = account.calculate_margin_level()
    
    print(f"Free Margin: {free_margin:.2f}")
    print(f"Margin Level: {margin_level:.2f}%")
except ValueError as e:
    print(f"Error: {e}")
```
