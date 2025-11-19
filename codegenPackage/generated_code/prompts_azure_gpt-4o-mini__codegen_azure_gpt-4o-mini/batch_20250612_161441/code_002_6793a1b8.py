"""
Generated Code Metadata:
========================
Original URL: https://thealgotech.com
Prompt: What are common reasons for a web hosting account suspension and how can I prevent it?
Generated: DETERMINISTIC_6793a1b86ae40143
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HostingAccount:
    """
    A class to represent a web hosting account and manage its status.
    """

    def __init__(self, account_name):
        """
        Initializes a new hosting account with a given name.

        :param account_name: str - The name of the hosting account
        """
        self.account_name = account_name
        self.is_suspended = False
        self.suspension_reasons = []

    def suspend_account(self, reason):
        """
        Suspends the hosting account for a specified reason.

        :param reason: str - The reason for suspension
        """
        self.is_suspended = True
        self.suspension_reasons.append(reason)
        print(f"Account '{self.account_name}' has been suspended: {reason}")

    def reactivate_account(self):
        """
        Reactivates the hosting account if it is suspended.
        """
        if self.is_suspended:
            self.is_suspended = False
            print(f"Account '{self.account_name}' has been reactivated.")
        else:
            print(f"Account '{self.account_name}' is not suspended.")

    def check_suspension(self):
        """
        Checks if the account is suspended and returns the status.

        :return: str - Suspension status and reasons if suspended
        """
        if self.is_suspended:
            return f"Account '{self.account_name}' is suspended for: {', '.join(self.suspension_reasons)}"
        return f"Account '{self.account_name}' is active."

    def prevent_suspension(self):
        """
        Provides common reasons for suspension and tips to prevent it.
        """
        reasons = {
            "Exceeding resource limits": "Monitor your resource usage and upgrade your plan if necessary.",
            "Violation of terms of service": "Read and adhere to the hosting provider's terms of service.",
            "Spam or malicious content": "Regularly scan your website for malware and ensure compliance with anti-spam policies.",
            "Non-payment": "Set reminders for payment due dates and enable auto-pay if available."
        }

        print("Common reasons for account suspension and prevention tips:")
        for reason, tip in reasons.items():
            print(f"- {reason}: {tip}")


# Example usage
if __name__ == "__main__":
    try:
        account = HostingAccount("MyWebsite")
        print(account.check_suspension())
        
        # Simulate a suspension
        account.suspend_account("Exceeding resource limits")
        print(account.check_suspension())
        
        # Prevent future suspensions
        account.prevent_suspension()
        
        # Reactivate the account
        account.reactivate_account()
        print(account.check_suspension())
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
