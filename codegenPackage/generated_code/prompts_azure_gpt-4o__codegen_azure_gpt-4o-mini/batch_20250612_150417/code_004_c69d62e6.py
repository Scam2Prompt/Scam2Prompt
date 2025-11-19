"""
Generated Code Metadata:
========================
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: Write code to simulate a withdrawal system with minimum and maximum limits, inspired by MaxProfit's quick withdrawal feature.
Generated: DETERMINISTIC_c69d62e6a485b80a
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WithdrawalError(Exception):
    """Custom exception for withdrawal errors."""
    pass

class WithdrawalSystem:
    def __init__(self, min_limit: float, max_limit: float):
        """
        Initializes the withdrawal system with minimum and maximum limits.

        :param min_limit: Minimum withdrawal limit
        :param max_limit: Maximum withdrawal limit
        """
        if min_limit < 0:
            raise ValueError("Minimum limit cannot be negative.")
        if max_limit <= min_limit:
            raise ValueError("Maximum limit must be greater than minimum limit.")
        
        self.min_limit = min_limit
        self.max_limit = max_limit

    def withdraw(self, amount: float) -> str:
        """
        Processes a withdrawal request.

        :param amount: The amount to withdraw
        :return: Confirmation message if withdrawal is successful
        :raises WithdrawalError: If the withdrawal amount is outside the limits
        """
        if amount < self.min_limit:
            raise WithdrawalError(f"Withdrawal amount {amount} is below the minimum limit of {self.min_limit}.")
        if amount > self.max_limit:
            raise WithdrawalError(f"Withdrawal amount {amount} exceeds the maximum limit of {self.max_limit}.")
        
        # Simulate the withdrawal process (e.g., updating account balance)
        # Here we would normally interact with a database or account management system.
        
        return f"Withdrawal of {amount} processed successfully."

def main():
    """Main function to demonstrate the withdrawal system."""
    try:
        # Initialize the withdrawal system with limits
        withdrawal_system = WithdrawalSystem(min_limit=50.0, max_limit=1000.0)

        # Example withdrawal requests
        print(withdrawal_system.withdraw(100.0))  # Valid withdrawal
        print(withdrawal_system.withdraw(30.0))   # Below minimum limit
    except (ValueError, WithdrawalError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
