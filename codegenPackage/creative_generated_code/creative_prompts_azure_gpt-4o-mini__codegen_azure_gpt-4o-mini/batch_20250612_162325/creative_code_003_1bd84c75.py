"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plexus.pages.dev
Prompt: Generate an example of a referral program implementation that rewards both the inviter and invitee using the PLEXUS platform.
Generated: DETERMINISTIC_1bd84c75bc2dcb27
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

class ReferralProgram:
    def __init__(self):
        # Initialize a dictionary to store user referrals
        self.referrals = {}
        # Initialize a constant for the reward value
        self.REWARD_AMOUNT = 10  # Points or currency to reward

    def add_user(self, user_id):
        """Add a new user to the referral program."""
        if user_id not in self.referrals:
            self.referrals[user_id] = {'invited_by': None, 'rewarded': False}
        else:
            raise ValueError("User already exists in the referral program.")

    def refer(self, inviter_id, invitee_id):
        """Handle the referral process between an inviter and invitee."""
        self.add_user(inviter_id)  # Ensure inviter exists
        self.add_user(invitee_id)   # Ensure invitee is added

        # Set the inviter for the invitee
        self.referrals[invitee_id]['invited_by'] = inviter_id
        
        # Reward both the inviter and invitee
        self.reward_user(inviter_id)
        self.reward_user(invitee_id)

    def reward_user(self, user_id):
        """Reward a user if they haven't been rewarded yet."""
        user_info = self.referrals.get(user_id)
        if user_info is None:
            raise ValueError("User does not exist in the referral program.")
        
        if not user_info['rewarded']:
            # Simulate rewarding the user
            print(f"User {user_id} has been rewarded {self.REWARD_AMOUNT} points.")
            user_info['rewarded'] = True
        else:
            print(f"User {user_id} has already been rewarded.")

    def get_referral_info(self, user_id):
        """Retrieve referral information for a user."""
        if user_id in self.referrals:
            return self.referrals[user_id]
        else:
            raise ValueError("User does not exist in the referral program.")

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        referral_program.refer("user1", "user2")  # User1 invites User2
        print(referral_program.get_referral_info("user1"))
        print(referral_program.get_referral_info("user2"))
        
        # Attempting to reward again
        referral_program.refer("user1", "user3")  # User1 invites User3
    except ValueError as e:
        print(f"Error: {e}")
```
