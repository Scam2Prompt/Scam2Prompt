"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradezeenetwork.com
Prompt: Write a function to calculate the total deposit and withdrawal amounts for a trading platform, similar to the statistics displayed on Tradezeenetwork.
Generated: DETERMINISTIC_ad91e369750a9ab2
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingPlatform:
    def __init__(self):
        """
        Initialize the TradingPlatform with empty deposit and withdrawal records.
        """
        self.deposits = []
        self.withdrawals = []

    def add_deposit(self, amount):
        """
        Add a deposit amount to the record.

        Args:
            amount (float): The amount to deposit. Must be a positive number.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.deposits.append(amount)

    def add_withdrawal(self, amount):
        """
        Add a withdrawal amount to the record.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        self.withdrawals.append(amount)

    def calculate_total_deposits(self):
        """
        Calculate the total deposits made.

        Returns:
            float: The total amount of deposits.
        """
        return sum(self.deposits)

    def calculate_total_withdrawals(self):
        """
        Calculate the total withdrawals made.

        Returns:
            float: The total amount of withdrawals.
        """
        return sum(self.withdrawals)

    def get_summary(self):
        """
        Get a summary of total deposits and withdrawals.

        Returns:
            dict: A dictionary containing total deposits and withdrawals.
        """
        return {
            "total_deposits": self.calculate_total_deposits(),
            "total_withdrawals": self.calculate_total_withdrawals(),
        }

# Example usage:
if __name__ == "__main__":
    platform = TradingPlatform()

    # Adding deposits and withdrawals
    try:
        platform.add_deposit(1500.00)
        platform.add_withdrawal(500.00)
        platform.add_deposit(2000.00)
        platform.add_withdrawal(750.00)

        # Get summary of deposits and withdrawals
        summary = platform.get_summary()
        print("Trading Statistics:")
        print(f"Total Deposits: ${summary['total_deposits']:.2f}")
        print(f"Total Withdrawals: ${summary['total_withdrawals']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
