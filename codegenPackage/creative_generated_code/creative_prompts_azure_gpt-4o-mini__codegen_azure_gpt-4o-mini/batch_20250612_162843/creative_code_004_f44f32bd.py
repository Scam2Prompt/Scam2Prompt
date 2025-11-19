"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puleschain.com
Prompt: What are best practices to prevent account suspension on a web hosting service?
Generated: DETERMINISTIC_f44f32bdd301d6a5
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for monitoring account status
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Account:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.active = True
        self.usage_limits = {
            'disk_space': 1024,  # in MB
            'bandwidth': 10000   # in MB
        }
        self.current_usage = {
            'disk_space': 0,
            'bandwidth': 0
        }

    def update_usage(self, disk_space_used, bandwidth_used):
        """Update current usage and check for limits."""
        self.current_usage['disk_space'] += disk_space_used
        self.current_usage['bandwidth'] += bandwidth_used
        self.check_limits()

    def check_limits(self):
        """Check if current usage exceeds the limits."""
        if self.current_usage['disk_space'] > self.usage_limits['disk_space']:
            logging.warning(f"Disk space limit exceeded for user {self.username}.")
            self.suspend_account("Disk space limit exceeded.")

        if self.current_usage['bandwidth'] > self.usage_limits['bandwidth']:
            logging.warning(f"Bandwidth limit exceeded for user {self.username}.")
            self.suspend_account("Bandwidth limit exceeded.")

    def suspend_account(self, reason):
        """Suspend the account and log the reason."""
        self.active = False
        logging.error(f"Account suspended for user {self.username}: {reason}")

    def reactivate_account(self):
        """Reactivate the account if conditions are met."""
        if not self.active:
            self.active = True
            logging.info(f"Account reactivated for user {self.username}.")
        else:
            logging.info(f"Account for user {self.username} is already active.")

    def display_status(self):
        """Display the current account status."""
        status = "Active" if self.active else "Suspended"
        logging.info(f"Account Status for {self.username}: {status}")


def main():
    # Example usage of the Account class
    try:
        account = Account("user123", "user123@example.com")
        account.update_usage(500, 2000)  # Normal usage
        account.display_status()
        account.update_usage(600, 15000)  # Exceeding bandwidth usage
        account.display_status()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
