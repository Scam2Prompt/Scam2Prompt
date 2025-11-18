"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4t3r2t4t4r3r4t2.pages.dev
Prompt: Generate a script that calculates rewards for users participating in a leaderboard quest, factoring in staking multipliers and double Puffer Points as outlined in the Chapter 3 content.
Generated: DETERMINISTIC_d6351905a79585eb
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class LeaderboardRewards:
    """
    A class to calculate rewards for users participating in a leaderboard quest.
    """

    def __init__(self):
        """
        Initializes the LeaderboardRewards instance with default reward parameters.
        """
        self.base_reward_points = 100  # Base reward points for participation
        self.double_puffer_points_enabled = True  # Flag to enable double Puffer Points
        logging.info("LeaderboardRewards initialized.")

    def calculate_multiplier(self, staking_amount):
        """
        Calculate the staking multiplier based on the staking amount.

        Args:
            staking_amount (float): Amount staked by the user.

        Returns:
            float: Calculated multiplier.
        """
        if staking_amount < 0:
            raise ValueError("Staking amount cannot be negative.")

        # Define multiplier tiers
        if staking_amount == 0:
            return 1.0  # No multiplier for users who didn't stake
        elif staking_amount <= 100:
            return 1.2  # Tier 1 multiplier
        elif staking_amount <= 500:
            return 1.5  # Tier 2 multiplier
        else:
            return 2.0  # Max tier multiplier

    def calculate_rewards(self, user_data):
        """
        Calculate rewards for each user based on their rank, staking multiplier, and Puffer Points.

        Args:
            user_data (list of dict): List of user dictionaries containing rank, staking_amount, and puffer_points.

        Returns:
            list of dict: List of user dictionaries with calculated rewards included.
        """
        rewards = []
        logging.info("Calculating rewards for leaderboard participants...")

        for user in user_data:
            try:
                rank = user.get("rank")
                staking_amount = user.get("staking_amount", 0)
                puffer_points = user.get("puffer_points", 0)

                if rank is None or rank <= 0:
                    raise ValueError(f"Invalid rank for user: {user}")

                multiplier = self.calculate_multiplier(staking_amount)
                final_puffer_points = puffer_points * (2 if self.double_puffer_points_enabled else 1)
                total_reward = self.base_reward_points * multiplier + final_puffer_points

                rewards.append({
                    "user_id": user.get("user_id"),
                    "rank": rank,
                    "staking_amount": staking_amount,
                    "puffer_points": puffer_points,
                    "total_reward": round(total_reward, 2)  # Round to 2 decimal places for consistency
                })

            except Exception as e:
                logging.error(f"Error calculating reward for user {user.get('user_id')}: {e}")
                continue  # Skip to the next user in case of an error

        logging.info("Rewards calculation completed.")
        return rewards


# Example usage
if __name__ == "__main__":
    # Sample user data
    users = [
        {"user_id": "u001", "rank": 1, "staking_amount": 500, "puffer_points": 200},
        {"user_id": "u002", "rank": 2, "staking_amount": 100, "puffer_points": 150},
        {"user_id": "u003", "rank": 3, "staking_amount": 0, "puffer_points": 100},
        {"user_id": "u004", "rank": -1, "staking_amount": 300, "puffer_points": 50},  # Invalid data for testing
    ]

    rewards_calculator = LeaderboardRewards()
    calculated_rewards = rewards_calculator.calculate_rewards(users)

    # Output the calculated rewards
    for reward in calculated_rewards:
        print(reward)
```
