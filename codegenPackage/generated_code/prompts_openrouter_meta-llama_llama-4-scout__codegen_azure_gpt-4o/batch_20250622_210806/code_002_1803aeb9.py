"""
Generated Code Metadata:
========================
Original URL: https://revsharelaunchpad.pages.dev
Prompt: "Generate code to calculate lifetime rewards for users on the ATOR network based on the provided network stats and token information."
Generated: DETERMINISTIC_1803aeb990548b8b
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ATORNetworkRewardsCalculator:
    """
    A class to calculate lifetime rewards for users on the ATOR network.
    """

    def __init__(self, network_stats, token_info):
        """
        Initialize the rewards calculator with network stats and token information.

        :param network_stats: Dictionary containing network statistics (e.g., total_rewards, user_contributions).
        :param token_info: Dictionary containing token information (e.g., token_value, reward_rate).
        """
        self.network_stats = network_stats
        self.token_info = token_info

    def calculate_user_rewards(self, user_id):
        """
        Calculate the lifetime rewards for a specific user.

        :param user_id: The ID of the user whose rewards are to be calculated.
        :return: Lifetime rewards for the user.
        """
        try:
            # Validate user existence in network stats
            if user_id not in self.network_stats['user_contributions']:
                raise ValueError(f"User ID '{user_id}' not found in network stats.")

            # Fetch user contribution and total rewards
            user_contribution = self.network_stats['user_contributions'][user_id]
            total_rewards = self.network_stats['total_rewards']

            # Fetch token reward rate
            reward_rate = self.token_info['reward_rate']

            # Calculate user rewards based on contribution percentage
            contribution_percentage = user_contribution / sum(self.network_stats['user_contributions'].values())
            user_rewards = total_rewards * contribution_percentage * reward_rate

            return user_rewards

        except KeyError as e:
            raise KeyError(f"Missing required data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating rewards: {e}")

    def export_rewards_to_json(self, user_id):
        """
        Export the calculated rewards for a user to a JSON file.

        :param user_id: The ID of the user whose rewards are to be exported.
        :return: None
        """
        try:
            # Calculate rewards
            user_rewards = self.calculate_user_rewards(user_id)

            # Prepare data for export
            rewards_data = {
                "user_id": user_id,
                "lifetime_rewards": user_rewards,
                "token_value": self.token_info['token_value']
            }

            # Export to JSON file
            file_name = f"user_{user_id}_rewards.json"
            with open(file_name, 'w') as json_file:
                json.dump(rewards_data, json_file, indent=4)

            print(f"Rewards successfully exported to {file_name}")

        except Exception as e:
            print(f"An error occurred while exporting rewards: {e}")


# Example usage
if __name__ == "__main__":
    # Example network stats and token info
    network_stats = {
        "total_rewards": 100000,  # Total rewards distributed in the network
        "user_contributions": {  # User contributions in the network
            "user1": 500,
            "user2": 300,
            "user3": 200
        }
    }

    token_info = {
        "token_value": 1.5,  # Value of the token in USD
        "reward_rate": 0.8   # Reward rate multiplier
    }

    # Initialize the rewards calculator
    calculator = ATORNetworkRewardsCalculator(network_stats, token_info)

    # Calculate and export rewards for a specific user
    calculator.export_rewards_to_json("user1")
```
