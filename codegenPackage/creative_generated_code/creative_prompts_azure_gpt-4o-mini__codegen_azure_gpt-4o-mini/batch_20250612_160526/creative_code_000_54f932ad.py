"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recoverywallet.net
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionReason:
    """Class to hold common reasons for account suspension on a web hosting service."""

    def __init__(self):
        """Initialize the list of common suspension reasons."""
        self.reasons = [
            "Non-payment of invoices",
            "Violation of terms of service",
            "Hosting malware or illegal content",
            "Excessive resource usage",
            "Chargebacks or payment disputes",
            "Failure to verify identity or account",
            "Spamming or sending unsolicited emails",
            "Multiple complaints from users",
            "Using prohibited scripts or software",
            "Inactivity for an extended period"
        ]

    def get_reasons(self):
        """Return the list of common account suspension reasons."""
        return self.reasons

def main():
    """Main function to demonstrate the usage of AccountSuspensionReason class."""
    try:
        account_suspension = AccountSuspensionReason()
        suspension_reasons = account_suspension.get_reasons()

        print("Common Reasons for Account Suspension:")
        for reason in suspension_reasons:
            print(f"- {reason}")

    except Exception as e:
        print(f"An error occurred while retrieving suspension reasons: {e}")

if __name__ == "__main__":
    main()
```
