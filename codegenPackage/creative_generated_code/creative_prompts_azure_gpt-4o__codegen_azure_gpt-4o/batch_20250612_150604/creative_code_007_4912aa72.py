"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penpie.io
Prompt: Write a program to analyze the rewards distribution for staking mPENDLE and locking vlPNP tokens, including revenue share and bribes.
Generated: DETERMINISTIC_4912aa7278254d78
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class RewardsAnalyzer:
    """
    A class to analyze rewards distribution for staking mPENDLE 
    and locking vlPNP tokens, including revenue share and bribes.
    """

    def __init__(self, staking_data, locking_data):
        """
        Initializes the RewardsAnalyzer with staking and locking data.

        :param staking_data: A list of dictionaries containing mPENDLE staking rewards data.
        :param locking_data: A list of dictionaries containing vlPNP locking rewards data.
        """
        self.staking_data = staking_data
        self.locking_data = locking_data

    def calculate_total_rewards(self):
        """
        Calculate the total rewards for staking and locking.

        :return: A dictionary with total rewards for staking, locking, revenue share, and bribes.
        """
        total_staking_rewards = sum(item.get('reward', 0) for item in self.staking_data)
        total_locking_rewards = sum(item.get('reward', 0) for item in self.locking_data)

        # Revenue share is calculated as 50% of staking rewards (example logic)
        revenue_share = total_staking_rewards * 0.5

        # Bribes are calculated as 10% of locking rewards (example logic)
        bribes = total_locking_rewards * 0.1

        return {
            'total_staking_rewards': total_staking_rewards,
            'total_locking_rewards': total_locking_rewards,
            'revenue_share': revenue_share,
            'bribes': bribes
        }

    def display_rewards_summary(self):
        """
        Display the rewards summary in a readable format.
        """
        rewards = self.calculate_total_rewards()

        print("Rewards Summary:")
        print(f"Total Staking Rewards: {rewards['total_staking_rewards']}")
        print(f"Total Locking Rewards: {rewards['total_locking_rewards']}")
        print(f"Revenue Share: {rewards['revenue_share']}")
        print(f"Bribes: {rewards['bribes']}")


def load_data(file_path):
    """
    Load staking or locking data from a JSON file.

    :param file_path: Path to the JSON file.
    :return: A list of dictionaries containing rewards data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file {file_path}")
        return []


# Main execution logic
if __name__ == '__main__':
    # Paths to the data files
    staking_data_file = 'staking_data.json'
    locking_data_file = 'locking_data.json'

    # Load data from the files
    staking_data = load_data(staking_data_file)
    locking_data = load_data(locking_data_file)

    # Initialize the rewards analyzer
    rewards_analyzer = RewardsAnalyzer(staking_data, locking_data)

    # Display the rewards summary
    rewards_analyzer.display_rewards_summary()
```

### Notes:
1. Save your staking and locking data in JSON format in `staking_data.json` and `locking_data.json`, respectively.
2. Example JSON data structure for the files:
   - `staking_data.json`: `[{"reward": 100}, {"reward": 200}]`
   - `locking_data.json`: `[{"reward": 50}, {"reward": 75}]`
