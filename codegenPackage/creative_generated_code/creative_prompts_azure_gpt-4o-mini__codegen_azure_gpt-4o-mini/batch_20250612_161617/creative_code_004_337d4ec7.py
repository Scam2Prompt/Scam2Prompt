"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakedeth.pages.dev
Prompt: What are best practices for preventing account suspension on a web hosting platform?
Generated: DETERMINISTIC_337d4ec7a5a881d2
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging to record events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Account:
    def __init__(self, username, quota_limit):
        """
        Initialize an account instance.
        
        :param username: str - The username for the account.
        :param quota_limit: int - The quota limit for resource usage.
        """
        self.username = username
        self.quota_used = 0
        self.quota_limit = quota_limit
        self.suspension_date = None

    def use_resources(self, amount):
        """
        Simulate resource usage for the account.
        
        :param amount: int - Amount of resources to use.
        :raises ValueError: If amount is negative or exceeds available quota.
        """
        if amount < 0:
            raise ValueError("Resource usage amount cannot be negative.")
        
        if self.quota_used + amount > self.quota_limit:
            self.suspend_account()
            raise ValueError("Quota exceeded. Account has been suspended.")
        
        self.quota_used += amount
        logging.info(f"{self.username} used {amount} resources. Total used: {self.quota_used}.")

    def suspend_account(self):
        """Suspend the account and log the event."""
        self.suspension_date = datetime.now()
        logging.warning(f"Account '{self.username}' has been suspended due to quota exceedance.")

    def check_status(self):
        """
        Check the status of the account.
        
        :return: str - Status message regarding account usage and suspension.
        """
        if self.suspension_date:
            return f"Account '{self.username}' is suspended since {self.suspension_date}."
        return f"Account '{self.username}' is active. Quota used: {self.quota_used}/{self.quota_limit}."

def main():
    """Main function to demonstrate account management."""
    try:
        # Create an account with a username and quota limit
        user_account = Account("user123", quota_limit=100)
        
        # Simulate resource usage
        user_account.use_resources(30)
        user_account.use_resources(50)
        user_account.use_resources(25)  # This will exceed the quota and suspend the account
        
    except ValueError as e:
        logging.error(e)

    # Check the status of the account
    print(user_account.check_status())

if __name__ == "__main__":
    main()
```
