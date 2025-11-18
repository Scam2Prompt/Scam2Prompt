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
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Reward:
    """A class to represent a reward in the E-DIGITS rewards system."""
    
    def __init__(self, user_id: str, reward_amount: float, timestamp: str):
        self.user_id = user_id
        self.reward_amount = reward_amount
        self.timestamp = datetime.fromisoformat(timestamp)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the Reward instance to a dictionary."""
        return {
            'user_id': self.user_id,
            'reward_amount': self.reward_amount,
            'timestamp': self.timestamp.isoformat()
        }

class PartnerActivity:
    """A class to represent partner activity in the E-DIGITS rewards system."""
    
    def __init__(self, partner_id: str, activity_type: str, timestamp: str):
        self.partner_id = partner_id
        self.activity_type = activity_type
        self.timestamp = datetime.fromisoformat(timestamp)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the PartnerActivity instance to a dictionary."""
        return {
            'partner_id': self.partner_id,
            'activity_type': self.activity_type,
            'timestamp': self.timestamp.isoformat()
        }

class RewardsTracker:
    """A class to manage rewards and partner activity."""
    
    def __init__(self):
        self.rewards: List[Reward] = []
        self.partner_activities: List[PartnerActivity] = []
    
    def add_reward(self, user_id: str, reward_amount: float) -> None:
        """Add a new reward for a user."""
        try:
            reward = Reward(user_id, reward_amount, datetime.now().isoformat())
            self.rewards.append(reward)
            logging.info(f"Added reward: {reward.to_dict()}")
        except Exception as e:
            logging.error(f"Failed to add reward: {e}")
    
    def add_partner_activity(self, partner_id: str, activity_type: str) -> None:
        """Add a new partner activity."""
        try:
            activity = PartnerActivity(partner_id, activity_type, datetime.now().isoformat())
            self.partner_activities.append(activity)
            logging.info(f"Added partner activity: {activity.to_dict()}")
        except Exception as e:
            logging.error(f"Failed to add partner activity: {e}")

    def get_rewards(self) -> List[Dict[str, Any]]:
        """Get a list of all rewards."""
        return [reward.to_dict() for reward in self.rewards]

    def get_partner_activities(self) -> List[Dict[str, Any]]:
        """Get a list of all partner activities."""
        return [activity.to_dict() for activity in self.partner_activities]
    
    def save_to_file(self, filename: str) -> None:
        """Save rewards and partner activities to a JSON file."""
        try:
            data = {
                'rewards': self.get_rewards(),
                'partner_activities': self.get_partner_activities()
            }
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Data saved to {filename}")
        except Exception as e:
            logging.error(f"Failed to save data to file: {e}")

# Example Usage
if __name__ == "__main__":
    tracker = RewardsTracker()
    
    # Add rewards
    tracker.add_reward("user123", 50.0)
    tracker.add_reward("user456", 30.0)

    # Add partner activity
    tracker.add_partner_activity("partner789", "transaction")
    
    # Save to file
    tracker.save_to_file('rewards_data.json')

    # Display all rewards and partner activities
    print("Rewards:", tracker.get_rewards())
    print("Partner Activities:", tracker.get_partner_activities())
```
