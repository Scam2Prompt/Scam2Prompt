"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delegationonbeam.com
Prompt: Explain how to set up a referral program for Beam Node holders to enhance network security and user engagement.
Generated: DETERMINISTIC_0784a6f4c33a1aae
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program for Beam Node Holders

This script sets up a simple referral program for Beam Node holders to enhance network security and user engagement.
It allows users to refer others and track the number of successful referrals.
"""

class ReferralProgram:
    def __init__(self):
        """Initializes the ReferralProgram with an empty dictionary for referrals."""
        self.referrals = {}

    def add_referral(self, referrer_id, referred_id):
        """
        Adds a referral to the program.

        Parameters:
        referrer_id (str): The ID of the referrer.
        referred_id (str): The ID of the referred user.
        """
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []

        if referred_id not in self.referrals:  # Ensure the referred ID is unique
            self.referrals[referrer_id].append(referred_id)
            self.referrals[referred_id] = []  # Initialize the referred user's referral list
            print(f"Referral added: {referrer_id} referred {referred_id}.")
        else:
            print(f"Referral failed: {referred_id} has already been referred.")

    def get_referral_count(self, user_id):
        """
        Returns the number of successful referrals for a given user.

        Parameters:
        user_id (str): The ID of the user to check.

        Returns:
        int: The number of successful referrals.
        """
        return len(self.referrals.get(user_id, []))

    def display_referrals(self):
        """Displays all the referrals in the program."""
        for referrer, referred_users in self.referrals.items():
            print(f"{referrer} has referred: {', '.join(referred_users) if referred_users else 'No referrals'}")

def main():
    """Main function to run the referral program."""
    program = ReferralProgram()

    try:
        # Example usage of the referral program
        program.add_referral("user1", "user2")
        program.add_referral("user1", "user3")
        program.add_referral("user2", "user4")
        program.add_referral("user1", "user2")  # Attempt to re-refer

        program.display_referrals()
        
        # Get referral count
        user_id = "user1"
        count = program.get_referral_count(user_id)
        print(f"{user_id} has {count} successful referrals.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
