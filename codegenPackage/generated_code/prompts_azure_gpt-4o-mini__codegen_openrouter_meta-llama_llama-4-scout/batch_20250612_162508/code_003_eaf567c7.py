"""
Generated Code Metadata:
========================
Original URL: https://nft-daop.web.app
Prompt: Develop a script that calculates the rewards in $TNSR tokens based on user activity on the NFT DAO platform.
Generated: DETERMINISTIC_eaf567c7be1e956c
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_calculator.py

"""
Calculates the rewards in $TNSR tokens based on user activity on the NFT DAO platform.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
from enum import Enum
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ActivityType(str, Enum):
    """Enum for different types of user activities."""
    CREATE_NFT = "create_nft"
    PARTICIPATE_AUCTION = "participate_auction"
    PROPOSE_VOTE = "propose_vote"

class RewardsCalculator:
    """Calculates rewards in $TNSR tokens based on user activity."""

    def __init__(self, rewards_config: Dict[str, float]):
        """
        Initializes the RewardsCalculator with a rewards configuration.

        Args:
        - rewards_config (Dict[str, float]): A dictionary mapping activity types to their corresponding rewards in $TNSR tokens.
        """
        self.rewards_config = rewards_config

    def calculate_rewards(self, user_activities: List[Dict[str, str]]) -> float:
        """
        Calculates the total rewards for a user based on their activities.

        Args:
        - user_activities (List[Dict[str, str]]): A list of user activities, where each activity is a dictionary containing the activity type.

        Returns:
        - float: The total rewards in $TNSR tokens.
        """
        total_rewards = 0.0

        for activity in user_activities:
            activity_type = activity.get("type")
            if activity_type not in self.rewards_config:
                logger.warning(f"Unknown activity type: {activity_type}. Skipping...")
                continue

            reward = self.rewards_config[activity_type]
            total_rewards += reward
            logger.info(f"Added reward of {reward} $TNSR for activity type: {activity_type}")

        return total_rewards

def main():
    # Example rewards configuration
    rewards_config = {
        ActivityType.CREATE_NFT: 10.0,
        ActivityType.PARTICIPATE_AUCTION: 5.0,
        ActivityType.PROPOSE_VOTE: 20.0
    }

    calculator = RewardsCalculator(rewards_config)

    # Example user activities
    user_activities = [
        {"type": ActivityType.CREATE_NFT},
        {"type": ActivityType.PARTICIPATE_AUCTION},
        {"type": ActivityType.PROPOSE_VOTE},
        {"type": "unknown_activity"}  # Test unknown activity type
    ]

    try:
        rewards = calculator.calculate_rewards(user_activities)
        logger.info(f"Total rewards: {rewards} $TNSR")
    except Exception as e:
        logger.error(f"Error calculating rewards: {str(e)}")

if __name__ == "__main__":
    main()
```
