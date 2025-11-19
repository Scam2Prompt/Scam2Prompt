"""
Generated Code Metadata:
========================
Original URL: https://soporte.arpynet.com
Prompt: What are common reasons for account suspension in web hosting, and how can I resolve them?
Generated: DETERMINISTIC_7f3fdcaea5ab7c63
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# account_suspension.py

class AccountSuspensionError(Exception):
    """Base class for account suspension related exceptions."""
    pass

class AccountSuspensionReason:
    """Represents a common reason for account suspension."""
    def __init__(self, reason, description, resolution):
        """
        Initializes an AccountSuspensionReason instance.

        Args:
            reason (str): The reason for account suspension.
            description (str): A brief description of the reason.
            resolution (str): Steps to resolve the issue.
        """
        self.reason = reason
        self.description = description
        self.resolution = resolution

class AccountSuspensionGuide:
    """Provides information on common account suspension reasons and their resolutions."""
    def __init__(self):
        self.reasons = [
            AccountSuspensionReason(
                "Non-payment",
                "Failure to pay for hosting services.",
                "Pay outstanding balances or set up automatic payments."
            ),
            AccountSuspensionReason(
                "Terms of Service (ToS) violation",
                "Violating the hosting provider's ToS.",
                "Review and comply with the ToS, contact support if unclear."
            ),
            AccountSuspensionReason(
                "Malware or security issues",
                "Presence of malware or security vulnerabilities.",
                "Remove malware, update software, and implement security measures."
            ),
            AccountSuspensionReason(
                "Excessive resource usage",
                "Using excessive server resources.",
                "Optimize website, consider upgrading to a higher plan."
            ),
            AccountSuspensionReason(
                "Abuse or spamming",
                "Engaging in abusive or spamming activities.",
                "Cease abusive activities, contact support for assistance."
            ),
        ]

    def get_reasons(self):
        """Returns a list of common account suspension reasons."""
        return self.reasons

    def get_resolution(self, reason):
        """
        Retrieves the resolution for a specific account suspension reason.

        Args:
            reason (str): The reason for account suspension.

        Returns:
            str: The resolution for the given reason, or None if not found.

        Raises:
            AccountSuspensionError: If the reason is not found.
        """
        for r in self.reasons:
            if r.reason == reason:
                return r.resolution
        raise AccountSuspensionError(f"Unknown reason: {reason}")

def main():
    guide = AccountSuspensionGuide()
    reasons = guide.get_reasons()

    print("Common reasons for account suspension:")
    for i, reason in enumerate(reasons, start=1):
        print(f"{i}. {reason.reason} - {reason.description}")

    reason_to_resolve = "Non-payment"
    try:
        resolution = guide.get_resolution(reason_to_resolve)
        print(f"\nResolution for '{reason_to_resolve}': {resolution}")
    except AccountSuspensionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
