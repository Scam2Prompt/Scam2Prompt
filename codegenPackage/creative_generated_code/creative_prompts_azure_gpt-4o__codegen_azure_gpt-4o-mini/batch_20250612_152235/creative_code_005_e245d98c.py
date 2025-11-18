"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Suggest a library or framework to implement referral systems for a sports betting platform, similar to the "Powered by Referral" feature on CoChilli SportsBook.
Generated: DETERMINISTIC_e245d98c5e38860f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

class ReferralSystem:
    """A class to handle referral management for a sports betting platform."""

    def __init__(self):
        """Initialize the referral system with an empty referral list."""
        self.referrals = {}

    def add_referral(self, user_id, referral_code):
        """
        Adds a referral to the system.
        
        Args:
            user_id (str): The ID of the user being referred.
            referral_code (str): The referral code provided by the referrer.
        
        Raises:
            ValueError: If the referral code is invalid or the user_id already exists.
        """
        if user_id in self.referrals:
            raise ValueError("User ID already exists!")
        
        if not self.is_valid_referral_code(referral_code):
            raise ValueError("Invalid referral code!")

        self.referrals[user_id] = referral_code

    def is_valid_referral_code(self, referral_code):
        """
        Checks if the provided referral code is valid.
        
        Args:
            referral_code (str): The referral code to validate.

        Returns:
            bool: True if the referral code is valid, False otherwise.
        """
        # For this example, assume a valid code is a non-empty string
        return bool(referral_code)

    def get_referrals(self, user_id):
        """
        Retrieves all referrals for a given user ID.
        
        Args:
            user_id (str): The ID of the user to retrieve referrals for.

        Returns:
            list: A list of referrals associated with the user ID.
        
        Raises:
            KeyError: If the user_id does not exist.
        """
        if user_id not in self.referrals:
            raise KeyError("User ID not found!")

        return [uid for uid, code in self.referrals.items() if code == self.referrals[user_id]]

    def __str__(self):
        """Return a string representation of the referral system for debugging."""
        return f"ReferralSystem({self.referrals})"


# Example usage of the ReferralSystem class
if __name__ == "__main__":
    referral_system = ReferralSystem()

    try:
        referral_system.add_referral("user123", "referralABC")
        referral_system.add_referral("user456", "referralABC")
        referral_system.add_referral("user789", "referralXYZ")

        print("All referrals for user123:", referral_system.get_referrals("user123"))
        print("Current state of referral system:", referral_system)

    except Exception as e:
        print(f"An error occurred: {e}")
```
