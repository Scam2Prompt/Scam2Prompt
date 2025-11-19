"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Create a code snippet that integrates a Mystery Box opening mechanic into a game, inspired by the features described on the Big Time website.
Generated: DETERMINISTIC_edaf87fdfc141ab1
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MysteryBox:
    """
    Represents a Mystery Box in the game.
    Each box contains a random reward based on predefined probabilities.
    """
    def __init__(self, box_type):
        """
        Initialize the Mystery Box with a specific type.
        
        :param box_type: str - Type of the box (e.g., "Common", "Rare", "Epic", "Legendary").
        """
        self.box_type = box_type
        self.rewards = self._define_rewards()

    def _define_rewards(self):
        """
        Define rewards and their probabilities based on the box type.
        
        :return: dict - A dictionary of rewards and their probabilities.
        """
        reward_pool = {
            "Common": {
                "Gold Coins": 0.5,
                "Silver Coins": 0.3,
                "Bronze Coins": 0.2
            },
            "Rare": {
                "Gold Coins": 0.4,
                "Silver Coins": 0.4,
                "Rare Gem": 0.2
            },
            "Epic": {
                "Gold Coins": 0.3,
                "Epic Gem": 0.5,
                "Legendary Artifact": 0.2
            },
            "Legendary": {
                "Legendary Artifact": 0.6,
                "Epic Gem": 0.3,
                "Mystic Relic": 0.1
            }
        }
        return reward_pool.get(self.box_type, {})

    def open(self):
        """
        Open the Mystery Box and return a random reward based on probabilities.
        
        :return: str - The reward obtained from the box.
        """
        if not self.rewards:
            raise ValueError(f"Invalid box type: {self.box_type}")
        
        # Generate a random reward based on probabilities
        reward_list = list(self.rewards.items())
        rewards, probabilities = zip(*reward_list)
        return random.choices(rewards, probabilities)[0]


# Example usage
def main():
    """
    Main function to demonstrate the Mystery Box opening mechanic.
    """
    try:
        # Create a Mystery Box of type "Epic"
        box = MysteryBox("Epic")
        
        # Open the box and display the reward
        reward = box.open()
        print(f"Congratulations! You received: {reward}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
