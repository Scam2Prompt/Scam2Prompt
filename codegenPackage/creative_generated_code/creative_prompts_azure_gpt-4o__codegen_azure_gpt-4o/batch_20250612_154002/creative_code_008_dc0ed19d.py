"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-digitsr.com
Prompt: Create a script to track and display rewards and partner activity in a blockchain environment, referencing the E-DIGITS rewards system.
Generated: DETERMINISTIC_dc0ed19dbe780f6c
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("blockchain_rewards.log"), logging.StreamHandler()],
)

class EDigitsRewardsTracker:
    """
    A class to track and display rewards and partner activity in a blockchain environment.
    """

    def __init__(self):
        # Initialize data structures to track rewards and partner activities
        self.rewards = {}  # Format: {partner_id: total_rewards}
        self.partner_activity = {}  # Format: {partner_id: [activity_log]}
        logging.info("E-DIGITS Rewards Tracker initialized.")

    def add_reward(self, partner_id: str, reward: float, transaction_id: str):
        """
        Add rewards for a partner.

        :param partner_id: The ID of the partner
        :param reward: Amount of reward to add
        :param transaction_id: Associated transaction ID
        """
        try:
            if reward < 0:
                raise ValueError("Reward amount cannot be negative.")
            
            # Update total rewards
            self.rewards[partner_id] = self.rewards.get(partner_id, 0) + reward
            
            # Log the activity
            activity = {
                "timestamp": datetime.utcnow().isoformat(),
                "transaction_id": transaction_id,
                "reward_added": reward,
            }
            self.partner_activity.setdefault(partner_id, []).append(activity)
            
            logging.info(f"Reward added: {reward} to partner {partner_id} in transaction {transaction_id}")
        
        except Exception as e:
            logging.error(f"Error adding reward for partner {partner_id}: {str(e)}")

    def get_rewards(self, partner_id: str) -> float:
        """
        Retrieve total rewards for a partner.

        :param partner_id: The ID of the partner
        :return: Total rewards of the partner
        """
        return self.rewards.get(partner_id, 0)

    def get_partner_activity(self, partner_id: str) -> list:
        """
        Retrieve activity log for a partner.

        :param partner_id: The ID of the partner
        :return: List of activity logs for the partner
        """
        return self.partner_activity.get(partner_id, [])

    def display_summary(self):
        """
        Display a summary of all rewards and partner activities.
        """
        try:
            summary = {
                "rewards": self.rewards,
                "partner_activity": self.partner_activity,
            }
            # Print the summary as formatted JSON
            print(json.dumps(summary, indent=4))
            logging.info("Summary displayed.")
        except Exception as e:
            logging.error(f"Error displaying summary: {str(e)}")


# Example usage
if __name__ == "__main__":
    tracker = EDigitsRewardsTracker()

    # Add rewards for partners
    tracker.add_reward(partner_id="partner_1", reward=100.0, transaction_id="txn_123")
    tracker.add_reward(partner_id="partner_2", reward=50.0, transaction_id="txn_124")
    tracker.add_reward(partner_id="partner_1", reward=200.0, transaction_id="txn_125")

    # Retrieve rewards for a specific partner
    print(f"Total rewards for partner_1: {tracker.get_rewards('partner_1')}")

    # Retrieve activity for a specific partner
    print(f"Activity log for partner_1: {json.dumps(tracker.get_partner_activity('partner_1'), indent=4)}")

    # Display complete summary
    tracker.display_summary()
```
