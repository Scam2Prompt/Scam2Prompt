"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Create a script that automates shared payouts for Farcaster Members and channels based on the Moxie Protocol's predefined reward distribution percentages.
Generated: DETERMINISTIC_dc509013e0feb656
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class RewardDistributor:
    """
    A class to automate shared payouts for Farcaster Members and channels 
    based on the Moxie Protocol's predefined reward distribution percentages.
    """

    def __init__(self, config_file):
        """
        Initializes the RewardDistributor with the configuration file.
        
        :param config_file: Path to the JSON file containing reward distribution data.
        """
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Configuration file not found: {config_file}")
        
        # Load the reward distribution configuration
        with open(config_file, 'r') as file:
            self.config = json.load(file)
        
        # Validate the configuration
        self.validate_config()

    def validate_config(self):
        """
        Validates the configuration file to ensure proper structure and percentages.
        """
        if 'members' not in self.config or 'channels' not in self.config:
            raise ValueError("Configuration file must have 'members' and 'channels' keys.")
        
        total_percentage = 0

        for member in self.config['members']:
            if 'name' not in member or 'percentage' not in member:
                raise ValueError("Each member must have 'name' and 'percentage'.")
            total_percentage += member['percentage']
        
        for channel in self.config['channels']:
            if 'name' not in channel or 'percentage' not in channel:
                raise ValueError("Each channel must have 'name' and 'percentage'.")
            total_percentage += channel['percentage']
        
        if total_percentage != 100:
            raise ValueError("The total percentage distribution must equal 100%.")
    
    def distribute_rewards(self, total_amount):
        """
        Distributes rewards based on the predefined percentages in the configuration file.
        
        :param total_amount: The total reward amount to distribute.
        :return: A dictionary containing the distributed amounts.
        """
        if total_amount <= 0:
            raise ValueError("Total reward amount must be greater than 0.")
        
        distribution = {}

        # Distribute rewards to members
        distribution['members'] = [
            {
                'name': member['name'],
                'amount': round(total_amount * (member['percentage'] / 100), 2)
            }
            for member in self.config['members']
        ]

        # Distribute rewards to channels
        distribution['channels'] = [
            {
                'name': channel['name'],
                'amount': round(total_amount * (channel['percentage'] / 100), 2)
            }
            for channel in self.config['channels']
        ]

        return distribution

# Example usage
if __name__ == "__main__":
    try:
        # Load configuration and distribute rewards
        config_path = 'reward_config.json'  # Path to your JSON configuration file
        total_rewards = 1000.0  # Total reward amount to be distributed

        distributor = RewardDistributor(config_path)
        payouts = distributor.distribute_rewards(total_rewards)
        
        print("Reward Distribution:")
        print(json.dumps(payouts, indent=4))
    
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Example `reward_config.json`
```json
{
    "members": [
        {"name": "Alice", "percentage": 30},
        {"name": "Bob", "percentage": 20}
    ],
    "channels": [
        {"name": "Channel 1", "percentage": 30},
        {"name": "Channel 2", "percentage": 20}
    ]
}
```
