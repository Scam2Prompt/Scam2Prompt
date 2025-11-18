"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenroomdao.web.app
Prompt: Create a function that calculates rewards in $TNSR tokens based on user activity data retrieved from Tensor's NFT trading platform.
Generated: DETERMINISTIC_b13ac1c8ff80ae5b
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class RewardCalculator:
    def __init__(self, user_activity_data: List[Dict[str, Any]]):
        """
        Initialize the RewardCalculator with user activity data.

        :param user_activity_data: A list of dictionaries containing user activity information.
        """
        self.user_activity_data = user_activity_data

    def calculate_rewards(self) -> float:
        """
        Calculate the total rewards in $TNSR tokens based on user activity.

        :return: Total rewards amount in $TNSR tokens.
        """
        total_rewards = 0.0
        
        # Constants for reward calculation
        TRADE_REWARD_PER_NFT = 1.5  # Reward for each NFT traded
        REFERAL_REWARD = 10.0  # Reward for each successful referral
        
        for activity in self.user_activity_data:
            try:
                # Calculate rewards based on activity type
                if activity['type'] == 'trade':
                    total_rewards += activity['nfts_traded'] * TRADE_REWARD_PER_NFT
                elif activity['type'] == 'referral':
                    total_rewards += REFERAL_REWARD
                else:
                    print(f"Warning: Unknown activity type '{activity['type']}' for activity: {activity}")
            except KeyError as e:
                print(f"Error: Missing key {e} in activity: {activity}")
            except Exception as e:
                print(f"Unexpected error encountered: {e}")

        return total_rewards

def main():
    # Sample user activity data for testing
    user_activity_json = '''
    [
        {"type": "trade", "nfts_traded": 3},
        {"type": "trade", "nfts_traded": 1},
        {"type": "referral"},
        {"type": "unknown_activity"}
    ]
    '''
    
    try:
        # Parse the user activity data
        user_activity_data = json.loads(user_activity_json)
        
        # Initialize the reward calculator
        reward_calculator = RewardCalculator(user_activity_data)
        
        # Calculate and print the total rewards
        total_rewards = reward_calculator.calculate_rewards()
        print(f"Total Rewards: ${total_rewards:.2f} TNSR tokens")
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()
```
