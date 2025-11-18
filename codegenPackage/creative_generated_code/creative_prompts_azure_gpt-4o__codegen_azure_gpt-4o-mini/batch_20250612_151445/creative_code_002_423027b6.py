"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Generate code for a referral program system similar to DominoBet's, where users can earn rewards by inviting friends to join.
Generated: DETERMINISTIC_423027b6006efc3a
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from collections import defaultdict

class User:
    """Represents a user in the referral program."""

    def __init__(self, username):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Unique referral code
        self.referred_users = []  # List of users referred by this user
        self.rewards = 0  # Points or rewards earned

    def refer_user(self, user):
        """Refer a new user and record the referral."""
        self.referred_users.append(user)
        self.rewards += 10  # Example: Earn 10 points for each referral
        print(f"{user.username} referred by {self.username}.")

class ReferralProgram:
    """Manages the overall referral program."""

    def __init__(self):
        self.users = {}
        self.invitation_logs = defaultdict(list)  # Keep track of invitations

    def register_user(self, username):
        """Register a new user and return their referral code."""
        if username in self.users:
            raise ValueError("Username already exists.")
        new_user = User(username)
        self.users[username] = new_user
        return new_user.referral_code

    def invite_friend(self, inviter_username, invitee_username):
        """Invite a friend using the inviter's referral code."""
        if inviter_username not in self.users:
            raise ValueError("Inviter does not exist.")
        if invitee_username in self.users:
            raise ValueError("Invitee already exists.")

        invitee_code = self.register_user(invitee_username)
        inviter = self.users[inviter_username]
        inviter.refer_user(self.users[invitee_username])
        
        # Log the invitation details
        self.invitation_logs[inviter_username].append({
            'invitee_username': invitee_username,
            'date_invited': datetime.now()
        })

    def get_user_rewards(self, username):
        """Get the total rewards for a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.users[username].rewards

    def get_referral_history(self, username):
        """Get the referral history of a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.invitation_logs[username]

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Register users
    try:
        alice_code = referral_program.register_user("Alice")
        bob_code = referral_program.register_user("Bob")
        print(f"Alice's referral code: {alice_code}")
        print(f"Bob's referral code: {bob_code}")

        # Alice invites Charlie
        referral_program.invite_friend("Alice", "Charlie")
        
        # Get rewards and referral history
        print(f"Alice's rewards: {referral_program.get_user_rewards('Alice')}")
        print("Alice's referral history:", referral_program.get_referral_history('Alice'))
        
    except ValueError as e:
        print(f"Error: {e}")
```
