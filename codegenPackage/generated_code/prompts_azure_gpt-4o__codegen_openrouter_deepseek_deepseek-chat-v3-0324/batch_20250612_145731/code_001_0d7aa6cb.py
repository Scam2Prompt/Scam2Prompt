"""
Generated Code Metadata:
========================
Original URL: https://pass-vee.com
Prompt: Generate code to calculate margin level and free margin for a trading account based on the definitions provided on the Changexcapital website.
Generated: DETERMINISTIC_0d7aa6cb7e6404a0
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingAccount:
    """
    A class to represent a trading account and calculate margin-related metrics.
    
    Attributes:
        balance (float): The current balance of the trading account.
        equity (float): The current equity of the trading account (balance + unrealized P/L).
        margin (float): The amount of margin currently used by open positions.
    """
    
    def __init__(self, balance: float, equity: float, margin: float):
        """
        Initialize the TradingAccount with balance, equity, and margin.
        
        Args:
            balance (float): The account balance.
            equity (float): The account equity.
            margin (float): The used margin.
        """
        self.balance = balance
        self.equity = equity
        self.margin = margin
        
    def calculate_margin_level(self) -> float:
        """
        Calculate the margin level as a percentage.
        
        Formula: (Equity / Used Margin) * 100
        
        Returns:
            float: The margin level percentage. Returns 0 if margin is 0 to avoid division by zero.
        """
        if self.margin == 0:
            return 0.0
        return (self.equity / self.margin) * 100
    
    def calculate_free_margin(self) -> float:
        """
        Calculate the free margin available for opening new positions.
        
        Formula: Equity - Used Margin
        
        Returns:
            float: The free margin amount.
        """
        return self.equity - self.margin
    
    def is_margin_call(self, margin_call_level: float = 100.0) -> bool:
        """
        Check if the account is in margin call state.
        
        Args:
            margin_call_level (float, optional): The margin level threshold for margin call. Defaults to 100.0.
            
        Returns:
            bool: True if margin level is below the threshold, False otherwise.
        """
        return self.calculate_margin_level() < margin_call_level
    
    def is_stop_out(self, stop_out_level: float = 50.0) -> bool:
        """
        Check if the account is in stop out state.
        
        Args:
            stop_out_level (float, optional): The margin level threshold for stop out. Defaults to 50.0.
            
        Returns:
            bool: True if margin level is below the threshold, False otherwise.
        """
        return self.calculate_margin_level() < stop_out_level


# Example usage
if __name__ == "__main__":
    try:
        # Initialize account with sample values
        account = TradingAccount(balance=10000.0, equity=9500.0, margin=5000.0)
        
        # Calculate metrics
        margin_level = account.calculate_margin_level()
        free_margin = account.calculate_free_margin()
        margin_call = account.is_margin_call()
        stop_out = account.is_stop_out()
        
        # Print results
        print(f"Margin Level: {margin_level:.2f}%")
        print(f"Free Margin: {free_margin:.2f}")
        print(f"Margin Call: {'Yes' if margin_call else 'No'}")
        print(f"Stop Out: {'Yes' if stop_out else 'No'}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
