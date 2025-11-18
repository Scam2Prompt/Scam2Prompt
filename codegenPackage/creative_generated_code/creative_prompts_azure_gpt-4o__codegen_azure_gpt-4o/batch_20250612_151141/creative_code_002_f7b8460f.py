"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Develop a script that allows users to claim their $BANANA or $ETH rewards only if their accrued rewards exceed 0.1E, as per the constraints outlined on the Bananagun Rewards page.
Generated: DETERMINISTIC_f7b8460fbb387feb
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class RewardClaimer:
    """
    A class to manage the claiming of rewards in $BANANA or $ETH.
    """

    def __init__(self, user_rewards):
        """
        Initialize the RewardClaimer instance.

        Args:
            user_rewards (dict): A dictionary containing user reward balances.
                                 Example: {'$BANANA': 0.2, '$ETH': 0.05}
        """
        self.user_rewards = user_rewards
        self.minimum_threshold = 0.1  # Minimum reward required to claim.

    def claim_rewards(self, reward_type):
        """
        Allows a user to claim their rewards if the balance exceeds the minimum threshold.

        Args:
            reward_type (str): The type of reward to claim ('$BANANA' or '$ETH').

        Returns:
            str: A message indicating the claim status.
        """
        try:
            # Validate input.
            if reward_type not in self.user_rewards:
                return f"Error: Unsupported reward type '{reward_type}'. Use '$BANANA' or '$ETH'."

            # Check if the accrued rewards exceed the minimum threshold.
            accrued_rewards = self.user_rewards[reward_type]
            if accrued_rewards >= self.minimum_threshold:
                # Process the claim (simulation here).
                self.user_rewards[reward_type] = 0  # Reset the balance after claiming.
                return f"Success: You have claimed your {reward_type} rewards."
            else:
                return f"Error: Your {reward_type} rewards ({accrued_rewards}E) are below the minimum threshold of {self.minimum_threshold}E."
        except Exception as e:
            # Handle unexpected errors.
            return f"Error: An unexpected error occurred while claiming rewards - {str(e)}."


# Example usage:
if __name__ == "__main__":
    # Simulate user rewards stored in a database or fetched from an API.
    user_data = '{"$BANANA": 0.2, "$ETH": 0.05}'
    user_rewards = json.loads(user_data)  # Parse user data.

    # Create an instance of RewardClaimer.
    reward_claimer = RewardClaimer(user_rewards)

    # Attempt to claim $BANANA rewards.
    print(reward_claimer.claim_rewards("$BANANA"))

    # Attempt to claim $ETH rewards.
    print(reward_claimer.claim_rewards("$ETH"))

    # Attempt to claim an unsupported reward type.
    print(reward_claimer.claim_rewards("$BTC"))
```
