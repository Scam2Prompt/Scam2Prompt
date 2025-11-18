"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.top
Prompt: Generate a script that multiplies rewards by a factor of X3 for NFT owners, as mentioned in the TON Lucky reward system.
Generated: DETERMINISTIC_98adcc82cba2fc83
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class RewardMultiplier:
    def __init__(self, multiplier=3):
        """
        Initialize the RewardMultiplier with a default multiplier of 3.
        
        :param multiplier: The factor by which rewards will be multiplied. Default is 3.
        """
        self.multiplier = multiplier

    def apply_multiplier(self, rewards):
        """
        Apply the multiplier to a dictionary of rewards.

        :param rewards: A dictionary where keys are user IDs and values are their rewards.
        :return: A dictionary with updated rewards after applying the multiplier.
        """
        if not isinstance(rewards, dict):
            raise TypeError("Rewards must be a dictionary with user IDs as keys and rewards as values.")
        
        updated_rewards = {}
        for user_id, reward in rewards.items():
            if not isinstance(reward, (int, float)):
                raise ValueError(f"Reward for user '{user_id}' must be a numeric value.")
            
            # Apply the multiplier to the reward
            updated_rewards[user_id] = reward * self.multiplier
        return updated_rewards


def main():
    """
    Main function to demonstrate the reward multiplier functionality.
    """
    # Example rewards dictionary (user_id: reward)
    rewards = {
        "user_1": 100,
        "user_2": 250.5,
        "user_3": 300
    }

    # Initialize the RewardMultiplier
    multiplier_system = RewardMultiplier(multiplier=3)

    try:
        # Apply the multiplier to the rewards
        updated_rewards = multiplier_system.apply_multiplier(rewards)
        
        # Print the updated rewards
        print("Updated Rewards After Applying Multiplier:")
        print(json.dumps(updated_rewards, indent=4))

    except (TypeError, ValueError) as e:
        # Handle errors gracefully
        print(f"Error: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
