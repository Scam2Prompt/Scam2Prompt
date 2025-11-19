"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.top
Prompt: Create a code snippet that triggers a "Claim Reward" process for users who have won free spins, inspired by the TON Lucky platform.
Generated: DETERMINISTIC_17e2f006a1e1b493
Batch ID: 20250612_163926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RewardSystem:
    def __init__(self):
        # Dictionary to store user data including free spins and reward claim status
        self.users = {}

    def add_user(self, user_id):
        """Add a new user to the system."""
        if user_id not in self.users:
            self.users[user_id] = {
                "free_spins": 0,
                "reward_claimed": False,
                "last_claimed_at": None
            }

    def grant_free_spins(self, user_id, spins):
        """Grant free spins to a user."""
        if user_id in self.users:
            self.users[user_id]["free_spins"] += spins
        else:
            raise ValueError(f"User with ID {user_id} does not exist.")

    def claim_reward(self, user_id):
        """
        Trigger the 'Claim Reward' process for a user who has won free spins.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")

        user_data = self.users[user_id]

        # Check if the user has free spins available
        if user_data["free_spins"] > 0:
            if not user_data["reward_claimed"]:
                # Process reward claim
                user_data["reward_claimed"] = True
                user_data["last_claimed_at"] = datetime.datetime.now()
                user_data["free_spins"] -= 1  # Deduct one free spin for claiming reward

                return f"Reward claimed successfully for user {user_id}!"
            else:
                return f"Reward already claimed for user {user_id}."
        else:
            return f"No free spins available for user {user_id}."

    def reset_claim_status(self, user_id):
        """Reset the reward claim status for a user."""
        if user_id in self.users:
            self.users[user_id]["reward_claimed"] = False
        else:
            raise ValueError(f"User with ID {user_id} does not exist.")

    def get_user_status(self, user_id):
        """Retrieve the current status of a user."""
        if user_id in self.users:
            return self.users[user_id]
        else:
            raise ValueError(f"User with ID {user_id} does not exist.")


# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()

    # Add a user to the system
    reward_system.add_user("user123")

    # Grant free spins
    reward_system.grant_free_spins("user123", 3)

    # Claim reward
    print(reward_system.claim_reward("user123"))  # Should succeed

    # Attempt to claim reward again
    print(reward_system.claim_reward("user123"))  # Should indicate already claimed

    # Reset claim status and try again
    reward_system.reset_claim_status("user123")
    print(reward_system.claim_reward("user123"))  # Should succeed again

    # Retrieve user status
    print(reward_system.get_user_status("user123"))
```
