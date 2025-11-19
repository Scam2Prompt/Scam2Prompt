"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Write a code snippet that demonstrates how to implement a system for inviting friends to earn $BIGTIME rewards in a game like Big Time.
Generated: DETERMINISTIC_15e3bb1c149baf1b
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardSystem:
    def __init__(self):
        """
        Initializes the RewardSystem with an empty list of invites.
        """
        self.invites = {}
        self.rewards = {}

    def invite_friend(self, inviter_id, invitee_email):
        """
        Sends an invitation to a friend via email.

        :param inviter_id: Unique identifier for the user sending the invite.
        :param invitee_email: Email address of the friend being invited.
        :raises ValueError: If the inviter_id or invitee_email is invalid.
        """
        if not inviter_id or not invitee_email:
            raise ValueError("Both inviter_id and invitee_email must be provided.")

        self.invites[invitee_email] = inviter_id
        print(f"Invitation sent from {inviter_id} to {invitee_email}.")

    def accept_invite(self, invitee_email):
        """
        Accepts an invitation from a friend and grants $BIGTIME rewards.

        :param invitee_email: Email address of the friend accepting the invitation.
        :raises KeyError: If the invitee_email is not found in the invites.
        """
        if invitee_email not in self.invites:
            raise KeyError("No invitation found for this email.")

        inviter_id = self.invites[invitee_email]
        self._grant_reward(inviter_id, invitee_email)

    def _grant_reward(self, inviter_id, invitee_email):
        """
        Grants $BIGTIME rewards to both the inviter and invitee.

        :param inviter_id: Unique identifier for the user who invited.
        :param invitee_email: Email address of the user accepting the invite.
        """
        # Grant rewards to the inviter
        if inviter_id not in self.rewards:
            self.rewards[inviter_id] = 0
        self.rewards[inviter_id] += 10  # Example reward points for inviter

        # Grant rewards to the invitee
        if invitee_email not in self.rewards:
            self.rewards[invitee_email] = 0
        self.rewards[invitee_email] += 5   # Example reward points for invitee

        print(f"Rewards granted: {inviter_id} earned 10 BIGTIME, {invitee_email} earned 5 BIGTIME.")

    def get_rewards(self, user_id):
        """
        Retrieves the total rewards earned by a user.

        :param user_id: Unique identifier of the user.
        :return: Total rewards earned by the user.
        :raises KeyError: If the user_id is not found in the rewards.
        """
        if user_id not in self.rewards:
            raise KeyError("User not found in rewards.")
        return self.rewards[user_id]

# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()

    # Inviting friends
    try:
        reward_system.invite_friend("user123", "friend@example.com")
        reward_system.invite_friend("user123", "anotherfriend@example.com")
        
        # Accepting invites
        reward_system.accept_invite("friend@example.com")
        reward_system.accept_invite("anotherfriend@example.com")

        # Checking rewards
        print(f"Rewards for user123: {reward_system.get_rewards('user123')}")
        print(f"Rewards for friend@example.com: {reward_system.get_rewards('friend@example.com')}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
