"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Create a Python script to calculate unstake periods and track the 10-day lock-in for unstaked EGLD tokens on MultiversX.
Generated: DETERMINISTIC_b8e3b39d647a8a48
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class EGLDUnstakeTracker:
    """
    A class to track unstake periods and manage a 10-day lock-in period for unstaked EGLD tokens.
    """

    def __init__(self):
        """
        Initialize the tracker with an empty list to store unstake records.
        Each record contains the amount unstaked and the date of unstaking.
        """
        self.unstaked_tokens = []

    def unstake_tokens(self, amount):
        """
        Record the amount of EGLD tokens unstaked along with the current date.

        Parameters:
            amount (float): The amount of EGLD tokens being unstaked.

        Returns:
            None
        """
        if amount <= 0:
            raise ValueError("Amount to unstake must be greater than zero.")

        # Record the unstaking event
        unstake_date = datetime.datetime.now()
        self.unstaked_tokens.append({
            "amount": amount,
            "unstake_date": unstake_date,
            "lock_in_expiration": unstake_date + datetime.timedelta(days=10)
        })
        print(f"{amount} EGLD tokens unstaked on {unstake_date}. Lock-in expires on {unstake_date + datetime.timedelta(days=10)}.")

    def check_lock_in_status(self):
        """
        Check which unstaked tokens are still in the lock-in period and which are available.

        Returns:
            tuple: Two lists - one for tokens still in lock-in and one for tokens that are now available.
        """
        now = datetime.datetime.now()
        still_locked = []
        available = []

        for record in self.unstaked_tokens:
            if now < record["lock_in_expiration"]:
                still_locked.append(record)
            else:
                available.append(record)

        return still_locked, available

    def display_status(self):
        """
        Display the status of all unstaked tokens, indicating whether they are still locked or available.

        Returns:
            None
        """
        still_locked, available = self.check_lock_in_status()

        print("\n--- Lock-In Status ---")
        if still_locked:
            print("Tokens Still in Lock-In Period:")
            for record in still_locked:
                print(f"Amount: {record['amount']} EGLD, Unlocks on: {record['lock_in_expiration']}")
        else:
            print("No tokens are currently in the lock-in period.")

        if available:
            print("\nTokens Available for Use:")
            for record in available:
                print(f"Amount: {record['amount']} EGLD, Unstaked on: {record['unstake_date']}")
        else:
            print("\nNo tokens are currently available for use.")

# Example Usage
if __name__ == "__main__":
    tracker = EGLDUnstakeTracker()

    try:
        # Unstake some tokens
        tracker.unstake_tokens(10.5)
        tracker.unstake_tokens(20.0)

        # Simulate checking the status after some time
        tracker.display_status()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
