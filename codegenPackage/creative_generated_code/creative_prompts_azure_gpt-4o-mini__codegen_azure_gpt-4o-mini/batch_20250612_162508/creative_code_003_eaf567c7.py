"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-daop.web.app
Prompt: Develop a script that calculates the rewards in $TNSR tokens based on user activity on the NFT DAO platform.
Generated: DETERMINISTIC_eaf567c7be1e956c
Batch ID: 20250612_162508
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardCalculator:
    def __init__(self, activity_data_file):
        """
        Initialize the RewardCalculator with activity data.

        :param activity_data_file: Path to the JSON file containing user activity data
        """
        self.activity_data_file = activity_data_file
        self.user_activities = self.load_activity_data()

    def load_activity_data(self):
        """
        Load user activity data from the specified JSON file.

        :return: Dictionary containing user activities
        """
        try:
            with open(self.activity_data_file, 'r') as file:
                activities = json.load(file)
            logging.info("Activity data loaded successfully.")
            return activities
        except FileNotFoundError:
            logging.error("The specified activity data file was not found.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the activity data file.")
            return {}

    def calculate_rewards(self):
        """
        Calculate rewards based on user activity.

        :return: Dictionary containing user rewards in $TNSR tokens
        """
        rewards = {}
        for user, activity in self.user_activities.items():
            # Assuming a simple reward calculation based on the number of activities
            # Each activity earns 10 $TNSR tokens (customize based on actual reward logic)
            num_activities = len(activity)
            rewards[user] = num_activities * 10
            logging.info(f"Calculated {rewards[user]} $TNSR tokens for user: {user}")
        
        return rewards

    def save_rewards(self, rewards, output_file):
        """
        Save the calculated rewards to a JSON file.

        :param rewards: Dictionary containing user rewards
        :param output_file: Path to the output JSON file for saving rewards
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(rewards, file, indent=4)
            logging.info("Rewards saved successfully to %s", output_file)
        except IOError:
            logging.error("Error saving rewards to the output file.")

def main():
    """
    Main function to run the reward calculation process.
    """
    # Input and output file paths
    activity_data_file = 'user_activity.json'  # Modify as needed
    output_file = 'user_rewards.json'  # Output file for rewards

    # Initialize the reward calculator
    calculator = RewardCalculator(activity_data_file)

    # Calculate rewards
    rewards = calculator.calculate_rewards()
    
    # Save rewards to a file
    calculator.save_rewards(rewards, output_file)

if __name__ == "__main__":
    main()
```

### Note:
Make sure to create a `user_activity.json` file containing user activities in the expected format for the script to work.
