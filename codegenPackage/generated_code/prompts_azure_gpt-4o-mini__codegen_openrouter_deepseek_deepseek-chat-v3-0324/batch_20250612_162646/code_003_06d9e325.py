"""
Generated Code Metadata:
========================
Original URL: https://tsr-dao.web.app
Prompt: Develop a script that calculates potential rewards in $TNSR tokens based on user activity on the TSR DAO NFT trading platform.
Generated: DETERMINISTIC_06d9e32516975002
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta

# Constants
TNSR_TOKEN_DECIMALS = 9
BASE_REWARD_RATE = 1.0  # TNSR per activity point
ACTIVITY_POINTS = {
    'nft_purchase': 10,
    'nft_sale': 15,
    'listing': 5,
    'bidding': 3,
    'participation': 2,
}

@dataclass
class UserActivity:
    user_id: str
    activities: List[Dict[str, str]]  # List of activity records with type and timestamp

@dataclass
class RewardCalculation:
    user_id: str
    activity_points: int
    tnsr_rewards: float
    timestamp: str

class RewardCalculator:
    def __init__(self, reward_rate: float = BASE_REWARD_RATE):
        self.reward_rate = reward_rate
    
    def calculate_points(self, activities: List[Dict[str, str]]) -> int:
        """Calculate total activity points from user activities."""
        total_points = 0
        for activity in activities:
            activity_type = activity.get('type')
            if activity_type in ACTIVITY_POINTS:
                total_points += ACTIVITY_POINTS[activity_type]
        return total_points
    
    def calculate_rewards(self, user_activity: UserActivity) -> RewardCalculation:
        """Calculate TNSR rewards based on user activity."""
        try:
            if not user_activity.activities:
                raise ValueError("No activities provided for user")
            
            points = self.calculate_points(user_activity.activities)
            rewards = (points * self.reward_rate) / (10 ** TNSR_TOKEN_DECIMALS)
            
            return RewardCalculation(
                user_id=user_activity.user_id,
                activity_points=points,
                tnsr_rewards=rewards,
                timestamp=datetime.utcnow().isoformat()
            )
        except Exception as e:
            raise RuntimeError(f"Failed to calculate rewards: {str(e)}")

class ActivityValidator:
    @staticmethod
    def validate_activity(activity: Dict[str, str]) -> bool:
        """Validate an activity record."""
        required_fields = {'type', 'timestamp'}
        if not all(field in activity for field in required_fields):
            return False
        
        if activity['type'] not in ACTIVITY_POINTS:
            return False
        
        try:
            datetime.fromisoformat(activity['timestamp'])
        except ValueError:
            return False
        
        return True

def load_user_activities(file_path: str) -> List[UserActivity]:
    """Load user activities from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        users = []
        for user_data in data:
            activities = user_data.get('activities', [])
            valid_activities = [a for a in activities if ActivityValidator.validate_activity(a)]
            users.append(UserActivity(
                user_id=user_data['user_id'],
                activities=valid_activities
            ))
        
        return users
    except FileNotFoundError:
        raise FileNotFoundError(f"Activity file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in activity file")
    except Exception as e:
        raise RuntimeError(f"Error loading user activities: {str(e)}")

def save_rewards_to_file(rewards: List[RewardCalculation], file_path: str) -> None:
    """Save reward calculations to a JSON file."""
    try:
        rewards_data = [{
            'user_id': r.user_id,
            'activity_points': r.activity_points,
            'tnsr_rewards': r.tnsr_rewards,
            'timestamp': r.timestamp
        } for r in rewards]
        
        with open(file_path, 'w') as f:
            json.dump(rewards_data, f, indent=2)
    except Exception as e:
        raise RuntimeError(f"Failed to save rewards: {str(e)}")

def main():
    try:
        # Initialize calculator
        calculator = RewardCalculator()
        
        # Load user activities
        users = load_user_activities('user_activities.json')
        
        # Calculate rewards
        rewards = []
        for user in users:
            reward = calculator.calculate_rewards(user)
            rewards.append(reward)
            print(f"User {user.user_id} earned {reward.tnsr_rewards:.9f} TNSR")
        
        # Save results
        save_rewards_to_file(rewards, 'rewards_calculated.json')
        print("Reward calculation completed successfully.")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```
