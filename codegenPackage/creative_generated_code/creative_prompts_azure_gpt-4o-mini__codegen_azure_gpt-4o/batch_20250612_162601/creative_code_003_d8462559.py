"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfty.web.app
Prompt: Generate a script to calculate potential rewards in $TNSR tokens based on user activity on the dao-nfty platform.
Generated: DETERMINISTIC_d84625595dcdec38
Batch ID: 20250612_162601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TNSRRewardCalculator:
    """
    A class to calculate potential rewards in $TNSR tokens based on user activity 
    on the dao-nfty platform.
    """

    def __init__(self, activity_data_file):
        """
        Initializes the reward calculator with user activity data.

        :param activity_data_file: Path to the JSON file containing user activity data.
        """
        self.activity_data_file = activity_data_file
        self.activity_data = {}
        self.reward_rates = {
            "posts": 0.5,  # $TNSR per post
            "comments": 0.2,  # $TNSR per comment
            "likes": 0.1  # $TNSR per like
        }

    def load_activity_data(self):
        """
        Loads user activity data from the specified JSON file.
        """
        try:
            with open(self.activity_data_file, 'r') as file:
                self.activity_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.activity_data_file}' not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from file '{self.activity_data_file}'.")
            raise

    def calculate_rewards(self):
        """
        Calculates rewards for each user based on their activity.

        :return: A dictionary containing the calculated rewards for each user.
        """
        if not self.activity_data:
            print("Error: No activity data loaded.")
            raise ValueError("Activity data is empty.")

        user_rewards = {}
        for user, activities in self.activity_data.items():
            # Initialize the user's reward balance
            user_rewards[user] = 0

            # Calculate rewards based on activity
            for activity_type, count in activities.items():
                if activity_type in self.reward_rates:
                    user_rewards[user] += count * self.reward_rates[activity_type]
                else:
                    print(f"Warning: Unknown activity type '{activity_type}' for user '{user}'.")

        return user_rewards

    def save_rewards_to_file(self, output_file, rewards):
        """
        Saves the calculated rewards to a specified output file in JSON format.

        :param output_file: Path to the output JSON file.
        :param rewards: Dictionary containing the rewards to save.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(rewards, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save rewards to file '{output_file}'. Reason: {e}")
            raise


if __name__ == "__main__":
    # Path to the user activity data JSON file
    activity_data_file = 'user_activity.json'
    
    # Path to the output rewards JSON file
    output_rewards_file = 'user_rewards.json'

    try:
        # Initialize the reward calculator
        calculator = TNSRRewardCalculator(activity_data_file)
        
        # Load the activity data
        calculator.load_activity_data()
        
        # Calculate rewards
        rewards = calculator.calculate_rewards()
        
        # Output the calculated rewards
        print("Calculated Rewards:")
        print(json.dumps(rewards, indent=4))
        
        # Save rewards to the output file
        calculator.save_rewards_to_file(output_rewards_file, rewards)
        print(f"Rewards saved to '{output_rewards_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
1. The script assumes the activity data is provided in a JSON file with the following format:
   ```json
   {
       "user1": {
           "posts": 10,
           "comments": 5,
           "likes": 20
       },
       "user2": {
           "posts": 3,
           "comments": 8,
           "likes": 15
       }
   }
   ```
2. Make sure to replace `user_activity.json` and `user_rewards.json` with the actual file paths when running the script.
