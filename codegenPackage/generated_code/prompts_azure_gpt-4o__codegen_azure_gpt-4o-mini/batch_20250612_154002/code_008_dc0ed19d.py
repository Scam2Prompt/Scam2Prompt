"""
Generated Code Metadata:
========================
Original URL: https://e-digitsr.com
Prompt: Create a script to track and display rewards and partner activity in a blockchain environment, referencing the E-DIGITS rewards system.
Generated: DETERMINISTIC_dc0ed19dbe780f6c
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardTracker:
    def __init__(self, blockchain_data: str):
        """
        Initialize the RewardTracker with blockchain data.

        :param blockchain_data: JSON string containing blockchain activity data
        """
        self.blockchain_data = self.load_data(blockchain_data)
        self.rewards: Dict[str, float] = {}
        self.partner_activity: Dict[str, List[Dict[str, Any]]] = {}

    def load_data(self, data: str) -> List[Dict[str, Any]]:
        """
        Load and parse blockchain data from a JSON string.

        :param data: JSON string containing blockchain activity data
        :return: List of activity records
        """
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            logging.error("Failed to decode JSON data: %s", e)
            raise ValueError("Invalid blockchain data format.")

    def track_rewards(self):
        """
        Track rewards based on blockchain activity.
        """
        for activity in self.blockchain_data:
            partner_id = activity.get('partner_id')
            reward_amount = activity.get('reward_amount', 0.0)

            if partner_id not in self.rewards:
                self.rewards[partner_id] = 0.0
            
            self.rewards[partner_id] += reward_amount
            self.log_partner_activity(partner_id, activity)

    def log_partner_activity(self, partner_id: str, activity: Dict[str, Any]):
        """
        Log activity for a specific partner.

        :param partner_id: Unique identifier for the partner
        :param activity: Activity record to log
        """
        if partner_id not in self.partner_activity:
            self.partner_activity[partner_id] = []
        
        self.partner_activity[partner_id].append(activity)

    def display_rewards(self):
        """
        Display the total rewards for each partner.
        """
        logging.info("Total Rewards by Partner:")
        for partner_id, total_reward in self.rewards.items():
            logging.info("Partner ID: %s, Total Reward: %.2f", partner_id, total_reward)

    def display_partner_activity(self):
        """
        Display the activity logs for each partner.
        """
        logging.info("Partner Activity Logs:")
        for partner_id, activities in self.partner_activity.items():
            logging.info("Partner ID: %s", partner_id)
            for activity in activities:
                logging.info("  Activity: %s", activity)

def main():
    # Example blockchain data in JSON format
    blockchain_data = '''
    [
        {"partner_id": "partner_1", "reward_amount": 10.0, "timestamp": "2023-10-01T12:00:00Z"},
        {"partner_id": "partner_2", "reward_amount": 15.0, "timestamp": "2023-10-01T12:05:00Z"},
        {"partner_id": "partner_1", "reward_amount": 5.0, "timestamp": "2023-10-01T12:10:00Z"}
    ]
    '''

    try:
        tracker = RewardTracker(blockchain_data)
        tracker.track_rewards()
        tracker.display_rewards()
        tracker.display_partner_activity()
    except ValueError as e:
        logging.error("Error in processing blockchain data: %s", e)

if __name__ == "__main__":
    main()
```
