"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfree.info
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_164245
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
        """Display the common reasons for account suspension in a formatted manner."""
        try:
            print("Common Reasons for Account Suspension:")
            for idx, reason in enumerate(self.get_reasons(), start=1):
                print(f"{idx}. {reason}")
        except Exception as e:
            print(f"An error occurred while displaying reasons: {e}")

def main():
    """Main function to execute the display of suspension reasons."""
    account_suspension = AccountSuspensionReason()
    account_suspension.display_reasons()

if __name__ == "__main__":
    main()
```
