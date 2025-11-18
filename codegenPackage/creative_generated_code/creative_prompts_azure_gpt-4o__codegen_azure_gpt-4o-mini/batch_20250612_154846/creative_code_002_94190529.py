"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinetworkinsight.com
Prompt: Generate code to calculate Pi cryptocurrency mining rewards based on user activity data.
Generated: DETERMINISTIC_94190529bbbfa2c5
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class UserActivity:
    """Class to represent user activity data for Pi cryptocurrency mining rewards."""
    
    def __init__(self, user_id: str, activity_data: List[Dict[str, float]]):
        """
        Initialize UserActivity with user ID and a list of activity records.
        
        :param user_id: Unique identifier for the user.
        :param activity_data: List of dictionaries containing activity records.
        """
        self.user_id = user_id
        self.activity_data = activity_data

    def calculate_rewards(self) -> float:
        """
        Calculate total mining rewards based on user activities.
        
        :return: Total mining rewards calculated.
        """
        total_rewards = 0.0
        
        # Iterate through each activity record and calculate rewards
        for record in self.activity_data:
            try:
                time_spent = record['time_spent']  # in hours
                activity_type = record['activity_type']  # e.g. 'active', 'passive'
                
                # Reward calculation based on activity type
                if activity_type == 'active':
                    reward = time_spent * 2.0  # Active users earn more
                elif activity_type == 'passive':
                    reward = time_spent * 1.0  # Passive users earn less
                else:
                    raise ValueError(f"Unknown activity type: {activity_type}")

                total_rewards += reward
            
            except KeyError as e:
                print(f"Missing key in activity record: {e}")
            except TypeError as e:
                print(f"Type error in activity data: {e}")
            except Exception as e:
                print(f"An error occurred while processing record: {e}")

        return total_rewards

def main():
    """Main function to demonstrate the calculation of Pi mining rewards."""
    # Sample user activity data
    user_id = "user123"
    activity_data = [
        {"time_spent": 5, "activity_type": "active"},
        {"time_spent": 3, "activity_type": "passive"},
        {"time_spent": 2, "activity_type": "active"},
        {"time_spent": 1.5, "activity_type": "unknown"},  # This will trigger an error
    ]

    # Create an instance of UserActivity
    user_activity = UserActivity(user_id, activity_data)

    # Calculate and print the total rewards
    total_rewards = user_activity.calculate_rewards()
    print(f"Total mining rewards for user {user_id}: {total_rewards} Pi")

if __name__ == "__main__":
    main()
```
