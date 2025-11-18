"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beyond-blitz.pages.dev
Prompt: Generate code for an airdrop system that distributes cryptocurrency rewards based on user contribution levels, similar to the "Claim $BEYOND Rewards" feature on Beyond Blitz.
Generated: DETERMINISTIC_3093892653be894b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AirdropSystem:
    """
    AirdropSystem handles cryptocurrency reward distribution based on user contributions.
    """

    def __init__(self, total_rewards: float):
        """
        Initializes the AirdropSystem.

        :param total_rewards: Total cryptocurrency rewards available for distribution.
        """
        self.total_rewards = total_rewards
        self.user_contributions = {}  # Stores user contributions as {user_id: contribution}

    def add_contribution(self, user_id: str, contribution: float) -> None:
        """
        Adds or updates a user's contribution.

        :param user_id: Unique identifier of the user.
        :param contribution: Contribution amount by the user.
        :raises ValueError: If the contribution is negative.
        """
        if contribution < 0:
            raise ValueError("Contribution cannot be negative.")

        self.user_contributions[user_id] = self.user_contributions.get(user_id, 0) + contribution
        logging.info(f"Added/Updated contribution for user {user_id}: {contribution}")

    def calculate_rewards(self) -> dict:
        """
        Calculates rewards for each user based on their contribution level.

        :return: A dictionary of rewards as {user_id: reward}.
        """
        total_contributions = sum(self.user_contributions.values())

        if total_contributions == 0:
            logging.warning("No contributions present. Rewards cannot be calculated.")
            return {}

        # Calculate rewards based on contribution percentage
        rewards = {}
        for user_id, contribution in self.user_contributions.items():
            reward = (contribution / total_contributions) * self.total_rewards
            rewards[user_id] = reward

        logging.info("Rewards calculated successfully.")
        return rewards

    def claim_reward(self, user_id: str) -> float:
        """
        Allows a user to claim their reward.

        :param user_id: Unique identifier of the user.
        :return: The reward amount claimed by the user.
        :raises KeyError: If the user_id is not found in the contributions.
        """
        rewards = self.calculate_rewards()
        if user_id not in rewards:
            raise KeyError(f"User {user_id} not found or has no contributions.")

        reward = rewards[user_id]
        logging.info(f"User {user_id} claimed reward: {reward}")
        return reward


# Example usage of the AirdropSystem
if __name__ == "__main__":
    try:
        # Initialize the airdrop system with total rewards (e.g., 1000 $BEYOND tokens)
        airdrop = AirdropSystem(1000)

        # Add user contributions
        airdrop.add_contribution("user1", 300)
        airdrop.add_contribution("user2", 500)
        airdrop.add_contribution("user3", 200)

        # Calculate rewards
        rewards = airdrop.calculate_rewards()
        print("Rewards Distribution:")
        for user_id, reward in rewards.items():
            print(f"{user_id}: {reward:.2f} $BEYOND")

        # Claim a reward
        user_id_to_claim = "user1"
        claimed_reward = airdrop.claim_reward(user_id_to_claim)
        print(f"{user_id_to_claim} claimed reward: {claimed_reward:.2f} $BEYOND")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
