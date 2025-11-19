"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Design a loyalty program, similar to BaxBet's, that rewards users with cashback and bonuses, using a Python-based data analysis tool to track user activity and reward eligibility.
Generated: DETERMINISTIC_c07a7c4cd08c886e
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoyaltyProgram:
    """
    A class to manage a loyalty program that rewards users with cashback and bonuses
    based on their activity.
    """
    def __init__(self):
        # Initialize user activity and rewards data
        self.user_activity = {}  # Format: {user_id: {'spend': float, 'last_active': datetime}}
        self.user_rewards = {}   # Format: {user_id: {'cashback': float, 'bonuses': list}}

    def track_activity(self, user_id, amount_spent):
        """
        Tracks user activity by recording their spending and updating their last active date.

        :param user_id: Unique identifier for the user
        :param amount_spent: Amount spent by the user
        """
        if user_id not in self.user_activity:
            self.user_activity[user_id] = {'spend': 0.0, 'last_active': None}
            self.user_rewards[user_id] = {'cashback': 0.0, 'bonuses': []}

        self.user_activity[user_id]['spend'] += amount_spent
        self.user_activity[user_id]['last_active'] = datetime.datetime.now()

        logging.info(f"Activity tracked for user {user_id}: spent ${amount_spent:.2f}")

    def calculate_rewards(self, user_id):
        """
        Calculates rewards for a user based on their spending.

        :param user_id: Unique identifier for the user
        """
        if user_id not in self.user_activity:
            logging.error(f"User {user_id} not found in activity records.")
            return

        spend = self.user_activity[user_id]['spend']
        cashback = spend * 0.05  # 5% cashback
        bonuses = []

        # Example bonus logic: reward bonus for spending over $100
        if spend > 100:
            bonuses.append("Free Gift")
        if spend > 500:
            bonuses.append("VIP Access")

        # Update rewards
        self.user_rewards[user_id]['cashback'] = cashback
        self.user_rewards[user_id]['bonuses'] = bonuses

        logging.info(f"Rewards calculated for user {user_id}: cashback ${cashback:.2f}, bonuses {bonuses}")

    def get_rewards(self, user_id):
        """
        Retrieves the rewards for a user.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing cashback and bonuses
        """
        if user_id not in self.user_rewards:
            logging.error(f"User {user_id} not found in rewards records.")
            return None

        return self.user_rewards[user_id]

    def display_user_summary(self, user_id):
        """
        Displays a summary of user activity and rewards.

        :param user_id: Unique identifier for the user
        """
        if user_id not in self.user_activity or user_id not in self.user_rewards:
            logging.error(f"User {user_id} not found in records.")
            return

        activity = self.user_activity[user_id]
        rewards = self.user_rewards[user_id]

        print(f"User ID: {user_id}")
        print(f"Total Spend: ${activity['spend']:.2f}")
        print(f"Last Active: {activity['last_active']}")
        print(f"Cashback Earned: ${rewards['cashback']:.2f}")
        print(f"Bonuses: {', '.join(rewards['bonuses']) if rewards['bonuses'] else 'None'}")

    def reset_rewards(self, user_id):
        """
        Resets the rewards for a user.

        :param user_id: Unique identifier for the user
        """
        if user_id not in self.user_rewards:
            logging.error(f"User {user_id} not found in rewards records.")
            return

        self.user_rewards[user_id] = {'cashback': 0.0, 'bonuses': []}
        logging.info(f"Rewards reset for user {user_id}.")

# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()

    # Simulate user activity
    program.track_activity("user123", 150.0)
    program.track_activity("user456", 50.0)

    # Calculate rewards
    program.calculate_rewards("user123")
    program.calculate_rewards("user456")

    # Display user summaries
    program.display_user_summary("user123")
    program.display_user_summary("user456")

    # Reset rewards for a user
    program.reset_rewards("user123")
    program.display_user_summary("user123")
```
