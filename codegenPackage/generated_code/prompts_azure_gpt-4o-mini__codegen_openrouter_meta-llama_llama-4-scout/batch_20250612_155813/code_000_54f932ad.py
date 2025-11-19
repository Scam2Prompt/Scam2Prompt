"""
Generated Code Metadata:
========================
Original URL: https://bridges-sonicslab.com
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# account_suspension_reasons.py

class AccountSuspensionReasons:
    """Provides common reasons for account suspension on a web hosting service."""

    def __init__(self):
        # Initialize a dictionary to store common suspension reasons
        self.suspension_reasons = {
            "payment_issues": "Payment issues, such as overdue invoices or failed payments.",
            "terms_of_service_violation": "Violation of terms of service, including but not limited to, illegal activities or content.",
            "excessive_resource_usage": "Excessive resource usage, including CPU, memory, or bandwidth overages.",
            "suspicious_activity": "Suspicious activity, such as unauthorized login attempts or malware detection.",
            "incomplete_information": "Incomplete or inaccurate account information.",
            "abuse_complaints": "Abuse complaints from other users or third-party services.",
        }

    def get_suspension_reasons(self):
        """Returns a dictionary of common suspension reasons."""
        return self.suspension_reasons

    def get_suspension_reason(self, reason_code):
        """
        Returns a specific suspension reason by code.

        Args:
            reason_code (str): The code of the suspension reason.

        Returns:
            str: The suspension reason message.

        Raises:
            ValueError: If the reason code is not found.
        """
        try:
            return self.suspension_reasons[reason_code]
        except KeyError:
            raise ValueError(f"Invalid reason code: {reason_code}")


def main():
    try:
        suspension_reasons = AccountSuspensionReasons()
        print("Common Account Suspension Reasons:")
        for reason_code, reason_message in suspension_reasons.get_suspension_reasons().items():
            print(f"{reason_code}: {reason_message}")

        # Example usage: Get a specific suspension reason
        reason_code = "payment_issues"
        print(f"\nSuspension Reason for {reason_code}:")
        print(suspension_reasons.get_suspension_reason(reason_code))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
