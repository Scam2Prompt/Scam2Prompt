"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subdamanhtuan.site
Prompt: What are common reasons for a website account suspension, and how can I prevent it?
Generated: DETERMINISTIC_ad3f5c752ae15b36
Batch ID: 20250612_160019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionChecker:
    """
    A class to check common reasons for website account suspension and provide prevention tips.
    """

    def __init__(self, username):
        """
        Initializes the checker with a username.

        :param username: The username of the account to check.
        """
        self.username = username
        self.common_reasons = {
            1: "Violation of terms of service",
            2: "Inactivity for an extended period",
            3: "Fraudulent activity or chargebacks",
            4: "Inappropriate content or behavior",
            5: "Multiple accounts without permission"
        }
        self.prevention_tips = {
            1: "Familiarize yourself with the website's terms of service.",
            2: "Log in regularly to keep your account active.",
            3: "Use legitimate payment methods and avoid chargebacks.",
            4: "Engage respectfully with the community and avoid offensive behavior.",
            5: "Check the website's policy on multiple accounts before creating them."
        }

    def get_common_reasons(self):
        """
        Returns a dictionary of common reasons for account suspension.

        :return: Dictionary of suspension reasons.
        """
        return self.common_reasons

    def get_prevention_tips(self):
        """
        Returns a dictionary of tips to prevent account suspension.

        :return: Dictionary of prevention tips.
        """
        return self.prevention_tips

    def display_info(self):
        """
        Displays common reasons for account suspension and prevention tips.
        """
        print(f"Common reasons for account suspension for user '{self.username}':")
        for key, reason in self.common_reasons.items():
            print(f"{key}: {reason}")

        print("\nPrevention tips:")
        for key, tip in self.prevention_tips.items():
            print(f"{key}: {tip}")

def main():
    """
    Main function to run the AccountSuspensionChecker.
    """
    try:
        username = input("Enter your username: ")
        if not username.strip():
            raise ValueError("Username cannot be empty.")

        checker = AccountSuspensionChecker(username)
        checker.display_info()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
