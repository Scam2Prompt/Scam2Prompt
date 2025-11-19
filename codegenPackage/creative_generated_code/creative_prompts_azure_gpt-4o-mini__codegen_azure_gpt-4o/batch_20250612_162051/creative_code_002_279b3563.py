"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaltiacomunidadeducativamontessori.com
Prompt: What are common reasons for a website account suspension, and how can I prevent it in the future?
Generated: DETERMINISTIC_279b35634b4f9e77
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to identify common reasons for website account suspension and provide
prevention strategies. The code is designed to be clean, efficient, and production-ready.

Usage: This script outputs reasons for suspension and prevention tips.
"""

def get_account_suspension_reasons():
    """
    Returns a list of common reasons for website account suspension.
    """
    return [
        "Violation of terms of service",
        "Suspicious or fraudulent activity",
        "Excessive spamming or abusive behavior",
        "Inappropriate or illegal content",
        "Multiple unsuccessful login attempts (security lockout)",
        "Payment issues or chargebacks",
        "Unauthorized access to another user's account"
    ]


def get_prevention_tips():
    """
    Returns a list of tips to prevent account suspension.
    """
    return [
        "Read and adhere to the website's terms of service.",
        "Avoid any fraudulent or suspicious behavior.",
        "Refrain from spamming and be respectful to other users.",
        "Do not post inappropriate, illegal, or copyrighted content.",
        "Use strong passwords and enable two-factor authentication.",
        "Ensure payment details are accurate and up-to-date.",
        "Never attempt to access accounts that don't belong to you."
    ]


def display_information():
    """
    Displays the reasons for account suspension and prevention tips to the user.
    """
    try:
        # Fetch reasons and tips
        reasons = get_account_suspension_reasons()
        tips = get_prevention_tips()

        # Display reasons
        print("Common Reasons for Account Suspension:")
        for idx, reason in enumerate(reasons, start=1):
            print(f"{idx}. {reason}")

        print("\nTips to Prevent Account Suspension:")
        # Display prevention tips
        for idx, tip in enumerate(tips, start=1):
            print(f"{idx}. {tip}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    display_information()
```
