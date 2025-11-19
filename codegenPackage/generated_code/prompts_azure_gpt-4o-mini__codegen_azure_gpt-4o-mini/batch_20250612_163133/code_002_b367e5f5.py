"""
Generated Code Metadata:
========================
Original URL: https://arbigo.io
Prompt: What are common reasons for a web hosting account to be suspended and how can I prevent it?
Generated: DETERMINISTIC_b367e5f52604bdc0
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HostingAccount:
    def __init__(self, account_id, usage_limit):
        """
        Initializes a new hosting account.

        :param account_id: Unique identifier for the hosting account
        :param usage_limit: Maximum allowed resource usage (e.g., bandwidth, storage)
        """
        self.account_id = account_id
        self.usage_limit = usage_limit
        self.current_usage = 0
        self.suspended = False

    def use_resources(self, amount):
        """
        Simulates resource usage for the hosting account.

        :param amount: Amount of resources to use
        :raises ValueError: If the amount exceeds the usage limit
        """
        if self.suspended:
            raise Exception("Account is suspended. Cannot use resources.")
        
        if amount < 0:
            raise ValueError("Usage amount must be non-negative.")
        
        self.current_usage += amount
        
        if self.current_usage > self.usage_limit:
            self.suspend_account()

    def suspend_account(self):
        """Suspends the hosting account due to excessive resource usage."""
        self.suspended = True
        print(f"Account {self.account_id} has been suspended due to excessive usage.")

    def reactivate_account(self):
        """Reactivates the hosting account if it is suspended."""
        if not self.suspended:
            print(f"Account {self.account_id} is already active.")
            return
        
        self.suspended = False
        self.current_usage = 0  # Reset usage upon reactivation
        print(f"Account {self.account_id} has been reactivated.")

    def check_status(self):
        """Checks the current status of the hosting account."""
        status = "suspended" if self.suspended else "active"
        print(f"Account {self.account_id} is currently {status}.")

def main():
    try:
        # Create a new hosting account with a usage limit of 1000 units
        account = HostingAccount(account_id="12345", usage_limit=1000)

        # Simulate resource usage
        account.use_resources(500)  # Should be fine
        account.check_status()       # Should be active

        account.use_resources(600)  # Should trigger suspension
        account.check_status()       # Should be suspended

        account.reactivate_account()  # Reactivate the account
        account.check_status()        # Should be active again

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
