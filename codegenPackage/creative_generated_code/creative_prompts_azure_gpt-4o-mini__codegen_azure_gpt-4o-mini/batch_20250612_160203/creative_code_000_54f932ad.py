"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binaryexpertise.com
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_160203
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
            "Fraudulent activity",
            "Inadequate account verification",
            "Security breaches or hacking attempts"
        ]

    def get_reasons(self):
        """Retrieve the list of common reasons for account suspension.

        Returns:
            list: A list of suspension reasons.
        """
        return self.reasons

    def display_reasons(self):
        """Display the suspension reasons in a formatted manner."""
        print("Common Reasons for Account Suspension:")
        for index, reason in enumerate(self.reasons, start=1):
            print(f"{index}. {reason}")

def main():
    """Main function to execute the program."""
    try:
        account_suspension = AccountSuspensionReason()
        account_suspension.display_reasons()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
