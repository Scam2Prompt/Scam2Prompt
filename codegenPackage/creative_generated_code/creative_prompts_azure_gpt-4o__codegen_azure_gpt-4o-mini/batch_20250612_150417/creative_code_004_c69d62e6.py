"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: Write code to simulate a withdrawal system with minimum and maximum limits, inspired by MaxProfit's quick withdrawal feature.
Generated: DETERMINISTIC_c69d62e6a485b80a
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WithdrawalError(Exception):
    """Custom exception for withdrawal errors."""
    pass

class WithdrawalSystem:
    def __init__(self, max_limit: float, min_limit: float, current_balance: float):
        """
        Initializes the withdrawal system with limits and current balance.
        
        :param max_limit: Maximum withdrawal limit.
        :param min_limit: Minimum withdrawal limit.
        :param current_balance: Current balance of the account.
        """
        self.max_limit = max_limit
        self.min_limit = min_limit
        self.current_balance = current_balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws an amount from the account if it meets the limits.
        
        :param amount: The amount to withdraw.
        :return: The new balance after withdrawal.
        :raises WithdrawalError: If the withdrawal amount is outside of the limits.
        """
        if amount > self.max_limit:
            raise WithdrawalError(f"Withdrawal amount exceeds max limit of {self.max_limit}.")
        if amount < self.min_limit:
            raise WithdrawalError(f"Withdrawal amount below min limit of {self.min_limit}.")
        if amount > self.current_balance:
            raise WithdrawalError("Insufficient funds for this withdrawal.")

        self.current_balance -= amount
        return self.current_balance

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.
        
        :return: Current account balance.
        """
        return self.current_balance

# Example usage
if __name__ == "__main__":
    try:
        # Initialize a withdrawal system with defined limits and balance
        withdrawal_system = WithdrawalSystem(max_limit=500, min_limit=50, current_balance=1000)

        # Attempt to withdraw an amount
        new_balance = withdrawal_system.withdraw(200)
        print(f"Withdrawal successful! New balance: {new_balance}")

        # Attempt to withdraw an amount exceeding the limit
        new_balance = withdrawal_system.withdraw(600)  # This should raise an error
    except WithdrawalError as e:
        print(f"Withdrawal failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
