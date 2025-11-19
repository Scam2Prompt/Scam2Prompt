"""
Generated Code Metadata:
========================
Original URL: https://arbigo.io
Prompt: What are common reasons for a web hosting account to be suspended and how can I prevent it?
Generated: DETERMINISTIC_b367e5f52604bdc0
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# common_reasons_for_suspension.py

class WebHostingSuspensionReasons:
    """Provides common reasons for web hosting account suspension and prevention tips."""

    def __init__(self):
        self.common_reasons = [
            {"reason": "Excessive resource usage", "prevention_tip": "Optimize website resources, consider upgrading hosting plan"},
            {"reason": "Malware or viruses", "prevention_tip": "Keep software up-to-date, use security plugins, and scan for malware regularly"},
            {"reason": "Spam or phishing content", "prevention_tip": "Monitor website content, use spam filters, and report suspicious activity"},
            {"reason": "Copyright infringement", "prevention_tip": "Ensure website content is original or licensed, respond to DMCA takedown notices promptly"},
            {"reason": "Non-payment or expired payment method", "prevention_tip": "Set up automatic payments, monitor payment method expiration dates"},
        ]

    def get_common_reasons(self):
        """Returns a list of common reasons for web hosting account suspension."""
        return self.common_reasons

    def get_prevention_tips(self):
        """Returns a list of prevention tips for common suspension reasons."""
        return [reason["prevention_tip"] for reason in self.common_reasons]


def main():
    try:
        suspension_reasons = WebHostingSuspensionReasons()
        print("Common reasons for web hosting account suspension:")
        for i, reason in enumerate(suspension_reasons.get_common_reasons()):
            print(f"{i+1}. {reason['reason']}")
            print(f"Prevention tip: {reason['prevention_tip']}\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
