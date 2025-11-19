"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavalentinamegacentro.com
Prompt: What are common reasons for a web hosting account to be suspended, and how can I prevent it?
Generated: DETERMINISTIC_87a29c3d1b73cde9
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HostingAccount:
    def __init__(self, username: str, storage_limit: int, bandwidth_limit: int):
        self.username = username
        self.storage_used = 0
        self.bandwidth_used = 0
        self.storage_limit = storage_limit
        self.bandwidth_limit = bandwidth_limit
        self.is_suspended = False

    def use_storage(self, amount: int):
        """Simulate using storage and check for suspension."""
        try:
            if self.is_suspended:
                raise Exception("Account is suspended. Cannot use storage.")
            if amount < 0:
                raise ValueError("Amount must be positive.")
            self.storage_used += amount
            self.check_storage_limit()
            logging.info(f"{self.username} used {amount}MB of storage.")
        except Exception as e:
            logging.error(e)

    def use_bandwidth(self, amount: int):
        """Simulate using bandwidth and check for suspension."""
        try:
            if self.is_suspended:
                raise Exception("Account is suspended. Cannot use bandwidth.")
            if amount < 0:
                raise ValueError("Amount must be positive.")
            self.bandwidth_used += amount
            self.check_bandwidth_limit()
            logging.info(f"{self.username} used {amount}MB of bandwidth.")
        except Exception as e:
            logging.error(e)

    def check_storage_limit(self):
        """Check if the storage limit has been exceeded."""
        if self.storage_used > self.storage_limit:
            self.suspend_account("Storage limit exceeded.")
    
    def check_bandwidth_limit(self):
        """Check if the bandwidth limit has been exceeded."""
        if self.bandwidth_used > self.bandwidth_limit:
            self.suspend_account("Bandwidth limit exceeded.")

    def suspend_account(self, reason: str):
        """Suspend the account and log the reason."""
        self.is_suspended = True
        logging.warning(f"Account {self.username} suspended: {reason}")

    def reactivate_account(self):
        """Reactivate account if it is suspended."""
        if self.is_suspended:
            self.is_suspended = False
            logging.info(f"Account {self.username} reactivated.")
        else:
            logging.info(f"Account {self.username} is already active.")

# Example usage
if __name__ == "__main__":
    account = HostingAccount(username="example_user", storage_limit=1000, bandwidth_limit=10000)

    # Simulate usage
    account.use_storage(500)  # Using 500MB of storage
    account.use_bandwidth(5000)  # Using 5000MB of bandwidth
    account.use_storage(600)  # This will exceed the storage limit
    account.reactivate_account()  # Reactivating the account after suspension
    account.use_bandwidth(6000)  # This will exceed the bandwidth limit
```
