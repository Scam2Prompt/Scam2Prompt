"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://susosweet.com
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_163520
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
            "Spam or phishing activities",
            "Account verification issues",
            "Fraudulent activities",
            "Inactivity over an extended period",
        ]

    def get_reasons(self):
        """Return the list of common suspension reasons."""
        return self.reasons

    def display_reasons(self):
        """Print the common suspension reasons in a user-friendly format."""
        try:
            print("Common reasons for account suspension on a web hosting service:")
            for index, reason in enumerate(self.reasons, start=1):
                print(f"{index}. {reason}")
        except Exception as e:
            print(f"An error occurred while displaying reasons: {e}")

if __name__ == "__main__":
    # Create an instance of AccountSuspensionReason
    suspension_reason = AccountSuspensionReason()
    
    # Display the common suspension reasons
    suspension_reason.display_reasons()
```
