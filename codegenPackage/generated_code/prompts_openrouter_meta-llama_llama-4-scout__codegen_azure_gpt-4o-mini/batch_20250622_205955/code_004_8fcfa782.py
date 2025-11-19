"""
Generated Code Metadata:
========================
Original URL: https://burnfi.pages.dev
Prompt: Design a simple invite rewards system using a programming language of your choice, where a 10% reward in $burn tokens is given to the inviter when a new user burns tokens using their link.
Generated: DETERMINISTIC_8fcfa7822bcacfa2
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    Represents a user in the invite rewards system.
    Each user has a unique ID, a balance of burn tokens, and an inviter.
    """
    def __init__(self, user_id, inviter=None):
        self.user_id = user_id
        self.burn_tokens = 0.0
        self.inviter = inviter

    def burn_tokens(self, amount):
        """
        Burns a specified amount of tokens and rewards the inviter.
        
        :param amount: The amount of tokens to burn.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount to burn must be greater than zero.")
        
        self.burn_tokens += amount
        print(f"User {self.user_id} burned {amount} tokens.")
        
        # Reward the inviter with 10% of the burned amount
        if self.inviter:
            reward = amount * 0.10
            self.inviter.receive_reward(reward)

    def receive_reward(self, amount):
        """
        Increases the user's burn token balance by the specified reward amount.
        
        :param amount: The reward amount to be added.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Reward amount cannot be negative.")
        
        self.burn_tokens += amount
        print(f"User {self.user_id} received a reward of {amount} tokens.")


class InviteRewardsSystem:
    """
    Manages the invite rewards system, allowing users to burn tokens and track rewards.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, inviter_id=None):
        """
        Adds a new user to the system.
        
        :param user_id: The unique ID of the new user.
        :param inviter_id: The ID of the user who invited the new user.
        :raises ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        inviter = self.users.get(inviter_id)
        new_user = User(user_id, inviter)
        self.users[user_id] = new_user
        print(f"User {user_id} added to the system.")

    def burn_tokens(self, user_id, amount):
        """
        Burns tokens for a specified user and rewards the inviter if applicable.
        
        :param user_id: The ID of the user burning tokens.
        :param amount: The amount of tokens to burn.
        :raises KeyError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise KeyError("User ID does not exist.")
        
        user = self.users[user_id]
        user.burn_tokens(amount)


# Example usage
if __name__ == "__main__":
    try:
        rewards_system = InviteRewardsSystem()
        
        # Adding users
        rewards_system.add_user("user1")  # No inviter
        rewards_system.add_user("user2", "user1")  # user1 invites user2
        
        # User2 burns tokens
        rewards_system.burn_tokens("user2", 100)  # user2 burns 100 tokens
        
        # Check balances
        print(f"User1's burn tokens: {rewards_system.users['user1'].burn_tokens}")
        print(f"User2's burn tokens: {rewards_system.users['user2'].burn_tokens}")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
