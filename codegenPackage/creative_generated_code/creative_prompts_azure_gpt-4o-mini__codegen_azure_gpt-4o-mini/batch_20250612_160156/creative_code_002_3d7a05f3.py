"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growth-geniuscapital.com.dhlcourierservices.com
Prompt: What are common reasons for a web hosting account to be suspended?
Generated: DETERMINISTIC_3d7a05f3188640eb
Batch ID: 20250612_160156
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
        Initialize a new hosting account with a given account ID and status.

        :param account_id: Unique identifier for the hosting account
        :param account_status: Current status of the hosting account, defaults to 'active'
        """
        self.account_id = account_id
        self.account_status = account_status

    def suspend_account(self, reason):
        """
        Suspend the hosting account for a specified reason.

        :param reason: Reason for the suspension
        """
        try:
            if self.account_status != 'active':
                raise ValueError("Account is already suspended or inactive.")
            logging.info(f'Suspending account {self.account_id} for reason: {reason}')
            self.account_status = 'suspended'
            logging.info(f'Account {self.account_id} has been suspended.')
        except Exception as e:
            logging.error(f'Error suspending account {self.account_id}: {e}')

    def get_suspension_reasons(self):
        """
        Get a list of common reasons for web hosting account suspension.

        :return: List of common suspension reasons
        """
        return [
            "Non-payment of hosting fees",
            "Violation of terms of service",
            "Exceeding resource usage limits",
            "Hosting illegal content",
            "Inactivity or abandonment",
            "Security issues or malware",
            "Excessive spam complaints or malicious activities"
        ]

def main():
    # Example usage of the HostingAccount class
    account = HostingAccount(account_id='12345')
    
    # Displaying common suspension reasons
    reasons = account.get_suspension_reasons()
    logging.info('Common reasons for account suspension:')
    for reason in reasons:
        logging.info(f'- {reason}')
    
    # Suspending the account
    account.suspend_account("Non-payment of hosting fees")

if __name__ == "__main__":
    main()
```
