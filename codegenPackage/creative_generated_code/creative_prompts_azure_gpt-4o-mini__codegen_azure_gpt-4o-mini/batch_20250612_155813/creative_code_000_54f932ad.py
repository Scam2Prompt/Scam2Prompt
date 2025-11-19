"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridges-sonicslab.com
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_155813
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
            "Excessive resource usage",
            "Abusive behavior or spam",
            "Inactivity for an extended period",
            "Security breaches or malware",
            "Fraudulent activity or chargebacks",
            "Failure to comply with legal requirements"
        ]

    def get_reasons(self):
        """Return the list of common suspension reasons."""
        return self.reasons

def main():
    """Main function to demonstrate the usage of AccountSuspensionReason class."""
    try:
        suspension_reason = AccountSuspensionReason()
        reasons = suspension_reason.get_reasons()

        print("Common reasons for account suspension on a web hosting service:")
        for idx, reason in enumerate(reasons, start=1):
            print(f"{idx}. {reason}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
