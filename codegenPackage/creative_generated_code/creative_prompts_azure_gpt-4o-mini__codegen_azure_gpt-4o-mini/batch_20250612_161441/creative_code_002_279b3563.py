"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminiairdrop.net
Prompt: What are common reasons for a website account suspension, and how can I prevent it in the future?
Generated: DETERMINISTIC_279b35634b4f9e77
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionManager:
    """
    A class to manage account suspension reasons and prevention strategies.
    """

    def __init__(self, user_id):
        """
        Initialize the AccountSuspensionManager with the user's ID.
        
        Args:
            user_id (str): The unique identifier for the user account.
        """
        self.user_id = user_id
        self.suspension_reasons = {
            "Violation of Terms of Service": "Always read and adhere to the terms and conditions.",
            "Fraudulent Activity": "Avoid sharing your account details and report suspicious activities.",
            "Spamming": "Do not engage in unsolicited messaging or promote irrelevant content.",
            "Inactivity": "Regularly log in to your account to avoid automatic suspension due to inactivity.",
            "User Complaints": "Maintain respectful interactions and resolve conflicts amicably."
        }

    def get_suspension_reasons(self):
        """
        Retrieve the common reasons for account suspension.
        
        Returns:
            dict: A dictionary of suspension reasons and their corresponding prevention strategies.
        """
        return self.suspension_reasons

    def prevent_suspension(self, reason):
        """
        Provide advice on how to prevent account suspension for a given reason.
        
        Args:
            reason (str): The reason for potential suspension.
        
        Returns:
            str: Advice on prevention, or a message indicating that the reason is not recognized.
        """
        try:
            return self.suspension_reasons[reason]
        except KeyError:
            return "Reason not recognized. Please refer to the list of common suspension reasons."

    def main(self):
        """
        Main method to demonstrate the functionality of the AccountSuspensionManager.
        """
        print(f"Account Suspension Reasons for User ID: {self.user_id}\n")
        reasons = self.get_suspension_reasons()
        for reason, prevention in reasons.items():
            print(f"{reason}: {prevention}")

        # Example usage of prevention advice
        example_reason = "Spamming"
        advice = self.prevent_suspension(example_reason)
        print(f"\nPrevention Advice for '{example_reason}': {advice}")


if __name__ == "__main__":
    # Example user ID
    user_id = "user123"
    account_manager = AccountSuspensionManager(user_id)
    account_manager.main()
```
