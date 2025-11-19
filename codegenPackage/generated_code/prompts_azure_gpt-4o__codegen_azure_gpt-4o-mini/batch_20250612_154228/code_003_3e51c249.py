"""
Generated Code Metadata:
========================
Original URL: https://bitdegree.pages.dev
Prompt: Write a function to calculate the total Bits earned based on the number of blockchain transactions tracked, adhering to Blockpit's daily or monthly limits.
Generated: DETERMINISTIC_3e51c24910a96150
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BlockpitTransactionTracker:
    """
    A class to track blockchain transactions and calculate total Bits earned
    based on daily or monthly limits set by Blockpit.
    """

    def __init__(self, daily_limit: int, monthly_limit: int):
        """
        Initializes the transaction tracker with daily and monthly limits.

        :param daily_limit: The maximum number of transactions allowed per day.
        :param monthly_limit: The maximum number of transactions allowed per month.
        """
        self.daily_limit = daily_limit
        self.monthly_limit = monthly_limit
        self.daily_transactions = 0
        self.monthly_transactions = 0

    def add_transactions(self, daily: int, monthly: int):
        """
        Adds transactions to the daily and monthly counts.

        :param daily: The number of transactions to add for the day.
        :param monthly: The number of transactions to add for the month.
        :raises ValueError: If the transactions exceed the respective limits.
        """
        if daily < 0 or monthly < 0:
            raise ValueError("Transaction counts cannot be negative.")

        if self.daily_transactions + daily > self.daily_limit:
            raise ValueError("Daily transaction limit exceeded.")

        if self.monthly_transactions + monthly > self.monthly_limit:
            raise ValueError("Monthly transaction limit exceeded.")

        self.daily_transactions += daily
        self.monthly_transactions += monthly

    def calculate_bits_earned(self) -> int:
        """
        Calculates the total Bits earned based on the transactions tracked.

        :return: The total Bits earned.
        """
        # Assuming 1 Bit is earned per transaction
        return self.daily_transactions + self.monthly_transactions

    def reset_daily_transactions(self):
        """
        Resets the daily transaction count at the end of the day.
        """
        self.daily_transactions = 0

    def reset_monthly_transactions(self):
        """
        Resets the monthly transaction count at the end of the month.
        """
        self.monthly_transactions = 0


# Example usage:
if __name__ == "__main__":
    try:
        tracker = BlockpitTransactionTracker(daily_limit=100, monthly_limit=3000)
        tracker.add_transactions(daily=50, monthly=200)
        print(f"Total Bits earned: {tracker.calculate_bits_earned()}")
        
        # Reset daily transactions for a new day
        tracker.reset_daily_transactions()
        
        # Add more transactions
        tracker.add_transactions(daily=30, monthly=100);
        print(f"Total Bits earned after reset: {tracker.calculate_bits_earned()}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
