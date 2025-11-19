"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avirodrian.com
Prompt: What are common reasons for a web hosting account to be suspended?
Generated: DETERMINISTIC_3d7a05f3188640eb
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Setting up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HostingAccount:
    def __init__(self, account_id, account_status='active'):
        """
        Initialize a new hosting account with a given ID and status.

        :param account_id: Unique identifier for the hosting account
        :param account_status: Current status of the account (default is 'active')
        """
        self.account_id = account_id
        self.account_status = account_status

    def suspend_account(self, reason):
        """
        Suspend the hosting account with a specified reason.

        :param reason: Reason for the suspension
        """
        # Validate reason
        if not reason:
            raise ValueError("Suspension reason cannot be empty.")
        
        self.account_status = 'suspended'
        logging.info(f"Account {self.account_id} has been suspended. Reason: {reason}")

    def get_suspension_reasons(self):
        """
        Provide common reasons for account suspension.

        :return: List of common suspension reasons
        """
        return [
            "Violation of terms of service",
            "Excessive resource usage",
            "Non-payment of hosting fees",
            "Spam or malicious activity",
            "Account security breaches",
            "Hosting prohibited content",
            "Repeated complaints from other users"
        ]

def main():
    """
    Main function to demonstrate the usage of HostingAccount class.
    """
    try:
        account = HostingAccount(account_id=12345)
        logging.info(f"Account {account.account_id} is currently {account.account_status}.")
        
        # Display common suspension reasons
        reasons = account.get_suspension_reasons()
        logging.info("Common reasons for suspension:")
        for reason in reasons:
            logging.info(f"- {reason}")

        # Suspend the account for a specific reason
        account.suspend_account("Non-payment of hosting fees")
        logging.info(f"Account status after suspension: {account.account_status}")

    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
```
