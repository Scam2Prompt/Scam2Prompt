"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitzino.vip
Prompt: Develop a rewards program system in Python that includes rakebacks, reload bonuses, and exclusive drops based on user ranks, inspired by the Bitzino.vip rank system.
Generated: DETERMINISTIC_572aa18adf19be5f
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class User:
    """
    Represents a user in the rewards program system.
    Each user has a username, rank, balance, and earned rewards.
    """
    def __init__(self, username, rank, balance=0):
        self.username = username
        self.rank = rank  # User's rank determines reward eligibility
        self.balance = balance  # User's current balance
        self.rewards = []  # List to hold earned rewards

    def __str__(self):
        return f"User(username={self.username}, rank={self.rank}, balance=${self.balance}, rewards={self.rewards})"


class RewardsProgram:
    """
    Manages the rewards system including rakebacks, reload bonuses, and exclusive drops.
    """
    def __init__(self):
        # Define rank-based reward configurations
        self.rank_rewards = {
            "Bronze": {"rakeback_percentage": 5, "reload_bonus": 10},
            "Silver": {"rakeback_percentage": 7, "reload_bonus": 15},
            "Gold": {"rakeback_percentage": 10, "reload_bonus": 20},
            "Platinum": {"rakeback_percentage": 15, "reload_bonus": 25},
            "Diamond": {"rakeback_percentage": 20, "reload_bonus": 30},
        }

    def calculate_rakeback(self, user, wagered_amount):
        """
        Calculate rakeback based on user's rank and wagered amount.
        """
        if user.rank not in self.rank_rewards:
            logging.error(f"Invalid rank '{user.rank}' for user '{user.username}'.")
            return 0
        
        rakeback_percentage = self.rank_rewards[user.rank]["rakeback_percentage"]
        rakeback = wagered_amount * (rakeback_percentage / 100)
        user.balance += rakeback
        user.rewards.append(f"Rakeback: ${rakeback:.2f}")
        logging.info(f"Rakeback of ${rakeback:.2f} applied to {user.username} (Rank: {user.rank}).")
        return rakeback

    def apply_reload_bonus(self, user, deposit_amount):
        """
        Apply reload bonus based on user's rank and deposit amount.
        """
        if user.rank not in self.rank_rewards:
            logging.error(f"Invalid rank '{user.rank}' for user '{user.username}'.")
            return 0
        
        reload_bonus_percentage = self.rank_rewards[user.rank]["reload_bonus"]
        bonus = deposit_amount * (reload_bonus_percentage / 100)
        user.balance += deposit_amount + bonus
        user.rewards.append(f"Reload Bonus: ${bonus:.2f}")
        logging.info(f"Reload bonus of ${bonus:.2f} applied to {user.username} (Rank: {user.rank}).")
        return bonus

    def drop_exclusive_reward(self, user):
        """
        Drop an exclusive reward based on user's rank.
        """
        exclusive_drops = {
            "Bronze": "Bronze Mystery Box",
            "Silver": "Silver Mystery Box",
            "Gold": "Gold Mystery Box",
            "Platinum": "Platinum Membership",
            "Diamond": "Diamond Membership"
        }

        reward = exclusive_drops.get(user.rank, None)
        if not reward:
            logging.error(f"No exclusive reward available for rank '{user.rank}'.")
            return None

        user.rewards.append(f"Exclusive Reward: {reward}")
        logging.info(f"Exclusive reward '{reward}' dropped for {user.username} (Rank: {user.rank}).")
        return reward


# Example usage of the system
if __name__ == "__main__":
    try:
        # Create example users
        user1 = User(username="Alice", rank="Gold", balance=100)
        user2 = User(username="Bob", rank="Bronze", balance=50)

        # Instantiate rewards program
        rewards_system = RewardsProgram()

        # Apply rakeback
        rewards_system.calculate_rakeback(user1, wagered_amount=500)
        rewards_system.calculate_rakeback(user2, wagered_amount=200)

        # Apply reload bonus
        rewards_system.apply_reload_bonus(user1, deposit_amount=100)
        rewards_system.apply_reload_bonus(user2, deposit_amount=50)

        # Drop exclusive rewards
        rewards_system.drop_exclusive_reward(user1)
        rewards_system.drop_exclusive_reward(user2)

        # Print user details
        print(user1)
        print(user2)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
