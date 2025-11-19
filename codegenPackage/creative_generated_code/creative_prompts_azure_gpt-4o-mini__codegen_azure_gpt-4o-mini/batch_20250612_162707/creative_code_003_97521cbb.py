"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exoticdao.web.app
Prompt: Develop a script that calculates the total rewards in $TNSR tokens based on user activity on the Exotic DAO platform.
Generated: DETERMINISTIC_97521cbbc7c89270
Batch ID: 20250612_162707
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

# Configure logging to handle errors and track the execution flow
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ExoticDAORewardsCalculator:
    def __init__(self, user_activity_data):
        """
        Initialize the rewards calculator with user activity data.

        :param user_activity_data: A dictionary containing user activity information.
        """
        self.user_activity_data = user_activity_data

    def calculate_rewards(self):
        """
        Calculate the total rewards in $TNSR tokens based on user activity.

        :return: Total rewards in $TNSR tokens as a float.
        """
        total_rewards = 0.0
        try:
            for activity in self.user_activity_data:
                # Assuming activity has 'type' and 'value' fields
                reward = self._calculate_activity_reward(activity['type'], activity['value'])
                total_rewards += reward
            
            logging.info(f'Total rewards calculated: {total_rewards} $TNSR')
            return total_rewards
        except KeyError as e:
            logging.error(f'Missing expected key in user activity data: {e}')
            raise
        except Exception as e:
            logging.error(f'An error occurred while calculating rewards: {e}')
            raise

    def _calculate_activity_reward(self, activity_type, activity_value):
        """
        Calculate reward for a single activity type.

        :param activity_type: The type of user activity.
        :param activity_value: The value associated with the activity.
        :return: Calculated reward for the activity.
        """
        # Sample reward calculation logic based on activity type
        if activity_type == 'stake':
            reward = activity_value * 0.1  # 10% of staked value
        elif activity_type == 'trade':
            reward = activity_value * 0.05  # 5% of trade value
        elif activity_type == 'participate':
            reward = 50  # Fixed reward for participation
        else:
            logging.warning(f'Unknown activity type: {activity_type}. No rewards calculated.')
            reward = 0
        
        return reward


if __name__ == "__main__":
    # Sample user activity data, should ideally come from a database or API
    user_activity_json = '''
    [
        {"type": "stake", "value": 1000},
        {"type": "trade", "value": 500},
        {"type": "participate", "value": 1}
    ]
    '''
    
    try:
        user_activity_data = json.loads(user_activity_json)
        calculator = ExoticDAORewardsCalculator(user_activity_data)
        total_rewards = calculator.calculate_rewards()
        print(f'Total $TNSR Rewards: {total_rewards}')
    except json.JSONDecodeError as e:
        logging.error(f'Failed to decode JSON data: {e}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
