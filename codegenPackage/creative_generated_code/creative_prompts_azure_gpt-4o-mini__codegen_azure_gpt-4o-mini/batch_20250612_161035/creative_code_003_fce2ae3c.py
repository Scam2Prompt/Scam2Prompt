"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karak-network.vercel.app
Prompt: Generate a function to calculate XP earned based on user interactions in a restaking platform similar to Karak.
Generated: DETERMINISTIC_fce2ae3c8bb84621
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class XPCalculator:
    """
    A class to calculate experience points (XP) earned based on user interactions
    in a restaking platform.
    """

    def __init__(self):
        """
        Initializes the XPCalculator with preset values for each type of interaction.
        """
        self.interaction_types = {
            'stake': 10,        # XP earned for each stake action
            'unstake': 5,       # XP earned for each unstake action
            'reward_claim': 15, # XP earned for each reward claim
            'participate_event': 20  # XP earned for participating in events
        }

    def calculate_xp(self, actions):
        """
        Calculates the total XP based on a list of user interactions.

        Parameters:
        actions (list of str): A list of actions performed by the user.

        Returns:
        int: The total XP earned.

        Raises:
        ValueError: If an invalid action is provided.
        """
        total_xp = 0

        for action in actions:
            if action in self.interaction_types:
                total_xp += self.interaction_types[action]
            else:
                raise ValueError(f"Invalid action: {action}. Valid actions are {list(self.interaction_types.keys())}.")

        return total_xp


# Example usage
if __name__ == "__main__":
    xp_calculator = XPCalculator()

    try:
        user_actions = ['stake', 'stake', 'reward_claim', 'participate_event']
        total_xp = xp_calculator.calculate_xp(user_actions)
        print(f"Total XP earned: {total_xp}")
    except ValueError as e:
        print(f"Error: {e}")
```
