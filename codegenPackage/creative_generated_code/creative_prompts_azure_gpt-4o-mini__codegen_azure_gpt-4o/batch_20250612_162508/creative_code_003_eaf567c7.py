"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-daop.web.app
Prompt: Develop a script that calculates the rewards in $TNSR tokens based on user activity on the NFT DAO platform.
Generated: DETERMINISTIC_eaf567c7be1e956c
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class NFTDAORewardsCalculator:
    """
    A class to calculate $TNSR token rewards based on user activity on the NFT DAO platform.
    """

    def __init__(self):
        """
        Initializes the reward calculation parameters.
        """
        # Constants for reward calculation
        self.base_reward = 10  # Base reward per activity (in $TNSR tokens)
        self.activity_weights = {
            "minting": 1.5,  # Higher weight for minting NFTs
            "trading": 1.2,  # Medium weight for trading NFTs
            "voting": 1.0,   # Lower weight for participating in votes
        }

    def calculate_rewards(self, user_activities):
        """
        Calculates rewards for a user based on their activities on the platform.

        :param user_activities: A dictionary containing activity counts for the user.
                                e.g., {"minting": 5, "trading": 10, "voting": 20}
        :return: Total rewards in $TNSR tokens.
        """
        try:
            total_rewards = 0

            # Validate input
            if not isinstance(user_activities, dict):
                raise ValueError("user_activities must be a dictionary.")

            # Calculate rewards based on activity counts and weights
            for activity, count in user_activities.items():
                if activity not in self.activity_weights:
                    logging.warning(f"Unknown activity: {activity}. Skipping...")
                    continue

                if not isinstance(count, int) or count < 0:
                    logging.warning(f"Invalid count for activity '{activity}': {count}. Skipping...")
                    continue

                reward = count * self.base_reward * self.activity_weights[activity]
                total_rewards += reward

            return total_rewards
        except Exception as e:
            logging.error(f"Error occurred while calculating rewards: {e}")
            return 0

# Example usage of the NFTDAORewardsCalculator class
if __name__ == "__main__":
    # Instantiate the rewards calculator
    rewards_calculator = NFTDAORewardsCalculator()

    # Example user activity data
    user_activities = {
        "minting": 5,
        "trading": 10,
        "voting": 20,
        "unknown_activity": 3  # This will be ignored due to validation
    }

    # Calculate rewards
    rewards = rewards_calculator.calculate_rewards(user_activities)

    # Output total rewards
    logging.info(f"Total rewards for the user: {rewards:.2f} $TNSR tokens")
```
