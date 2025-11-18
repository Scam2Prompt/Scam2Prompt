"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Create a notification system that alerts users when their accrued rewards exceed the claimable threshold, factoring in the specific rules for $BANANA, ETH, and SOL rewards.
Generated: DETERMINISTIC_888e9566cfca276a
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardNotificationSystem:
    def __init__(self, claimable_threshold: float):
        """
        Initializes the RewardNotificationSystem with a claimable threshold.

        :param claimable_threshold: The minimum rewards that must be accrued before notifying the user.
        """
        self.claimable_threshold = claimable_threshold
        self.users_rewards: Dict[str, Dict[str, float]] = {}  # user_id -> { 'BANANA': float, 'ETH': float, 'SOL': float }

    def add_user(self, user_id: str):
        """
        Adds a new user to the notification system.

        :param user_id: Unique identifier for the user.
        """
        if user_id not in self.users_rewards:
            self.users_rewards[user_id] = {'BANANA': 0.0, 'ETH': 0.0, 'SOL': 0.0}
            logging.info(f"User {user_id} added to the notification system.")
        else:
            logging.warning(f"User {user_id} already exists in the system.")

    def update_rewards(self, user_id: str, rewards: Dict[str, float]):
        """
        Updates the rewards for a given user.

        :param user_id: Unique identifier for the user.
        :param rewards: A dictionary containing the reward types and their respective amounts.
        """
        if user_id not in self.users_rewards:
            logging.error(f"User {user_id} does not exist. Cannot update rewards.")
            return
        
        for reward_type, amount in rewards.items():
            if reward_type in self.users_rewards[user_id]:
                self.users_rewards[user_id][reward_type] += amount
                logging.info(f"Updated {reward_type} rewards for user {user_id}: {self.users_rewards[user_id][reward_type]}")
            else:
                logging.warning(f"Unknown reward type '{reward_type}' for user {user_id}. Update skipped.")

        self.check_notifications(user_id)

    def check_notifications(self, user_id: str):
        """
        Checks if the user has accrued rewards exceeding the claimable threshold and sends notifications.

        :param user_id: Unique identifier for the user.
        """
        rewards = self.users_rewards[user_id]
        for reward_type, amount in rewards.items():
            if amount >= self.claimable_threshold:
                self.notify_user(user_id, reward_type, amount)

    def notify_user(self, user_id: str, reward_type: str, amount: float):
        """
        Notifies the user about their claimable rewards.

        :param user_id: Unique identifier for the user.
        :param reward_type: The type of reward that is claimable.
        :param amount: The amount of claimable rewards.
        """
        logging.info(f"Notification: User {user_id}, your {reward_type} rewards have exceeded the threshold! Current amount: {amount:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        threshold = 100.0  # Set claimable threshold
        notification_system = RewardNotificationSystem(claimable_threshold=threshold)

        notification_system.add_user("user123")
        notification_system.update_rewards("user123", {'BANANA': 50, 'ETH': 70, 'SOL': 30})
        notification_system.update_rewards("user123", {'BANANA': 60})  # This should trigger a notification

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
