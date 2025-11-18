"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-daypro.com
Prompt: Develop a demo account feature for automated trading software, ensuring seamless user experience as described in Immediate Daypro's platform.
Generated: DETERMINISTIC_280adef1ae0312f8
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta


class DemoAccount:
    """
    A class to represent a demo account for an automated trading platform.
    """

    def __init__(self, username: str, initial_balance: float = 10000.0, expiry_days: int = 30):
        """
        Initialize the DemoAccount instance.

        :param username: The username of the demo account owner.
        :param initial_balance: The initial virtual balance for the demo account.
        :param expiry_days: The number of days the demo account will remain active.
        """
        self.username = username
        self.account_id = str(uuid.uuid4())  # Generate a unique ID for the demo account.
        self.balance = initial_balance
        self.expiry_date = datetime.now() + timedelta(days=expiry_days)  # Set expiry date.
        self.is_active = True  # Initial state of the demo account.

    def trade(self, amount: float):
        """
        Simulate a trade by deducting the given amount from the balance.

        :param amount: The amount to trade.
        :raises ValueError: If the trade amount exceeds the available balance or the account is inactive.
        """
        if not self.is_active:
            raise ValueError("Demo account is no longer active.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for the trade.")
        self.balance -= amount

    def deposit(self, amount: float):
        """
        Simulate depositing virtual funds into the account.

        :param amount: The amount to deposit.
        :raises ValueError: If the account is inactive or the deposit amount is invalid.
        """
        if not self.is_active:
            raise ValueError("Demo account is no longer active.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def check_expiry(self):
        """
        Check if the demo account has expired and update its active status accordingly.
        """
        if datetime.now() > self.expiry_date:
            self.is_active = False

    def account_summary(self) -> dict:
        """
        Get a summary of the demo account.

        :return: A dictionary containing account information.
        """
        self.check_expiry()  # Ensure the active status is up-to-date.
        return {
            "username": self.username,
            "account_id": self.account_id,
            "balance": self.balance,
            "expiry_date": self.expiry_date.strftime("%Y-%m-%d %H:%M:%S"),
            "is_active": self.is_active,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a demo account
        demo_account = DemoAccount(username="trader123")

        # Perform some trades
        demo_account.trade(500)
        demo_account.deposit(2000)

        # Display account summary
        summary = demo_account.account_summary()
        print("Account Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")

        # Simulate account expiration
        # (For demonstration purposes, directly manipulate expiry date)
        demo_account.expiry_date = datetime.now() - timedelta(days=1)
        demo_account.check_expiry()

        # Attempt another trade on an expired account
        demo_account.trade(100)  # This should raise an error.

    except ValueError as e:
        print(f"Error: {e}")
```
