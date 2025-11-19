"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soporte.arpynet.com
Prompt: What are common reasons for account suspension in web hosting, and how can I resolve them?
Generated: DETERMINISTIC_7f3fdcaea5ab7c63
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionReasons:
    """
    A class to encapsulate common reasons for account suspension in web hosting
    and methods to resolve them.
    """

    def __init__(self):
        # Dictionary to store suspension reasons and their resolutions
        self.suspension_reasons = {
            "Non-payment": "Ensure all invoices are paid. Contact billing support if needed.",
            "Exceeding resource limits": "Upgrade your hosting plan or optimize your resource usage.",
            "Violation of Terms of Service": "Review the terms and ensure compliance. Contact support for clarification.",
            "Suspicious activity": "Secure your account and review activity logs. Change passwords if necessary."
        }

    def get_resolution(self, reason):
        """
        Get the resolution for a given suspension reason.

        :param reason: str - The reason for suspension
        :return: str - Suggested resolution or a message if reason not found
        """
        try:
            resolution = self.suspension_reasons.get(reason)
            if resolution:
                return resolution
            else:
                raise ValueError("Reason not found.")
        except Exception as e:
            return f"An error occurred: {str(e)}"


def main():
    """
    Main function to demonstrate the use of the AccountSuspensionReasons class.
    """
    account_issues = AccountSuspensionReasons()
    
    # Example reasons to check
    reasons_to_check = [
        "Non-payment",
        "Exceeding resource limits",
        "Violation of Terms of Service",
        "Suspicious activity",
        "Unknown reason"  # This will trigger an error
    ]
    
    for reason in reasons_to_check:
        resolution = account_issues.get_resolution(reason)
        print(f"Reason: {reason} - Resolution: {resolution}")


if __name__ == "__main__":
    main()
```
