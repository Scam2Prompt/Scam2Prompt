"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a code snippet that demonstrates how to create a Mystery Box opening feature for the Big Time game.
Generated: DETERMINISTIC_3f5e908418d1d93a
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MysteryBox:
    """
    Represents a Mystery Box in the Big Time game.
    """
    def __init__(self, box_id, box_rarity, possible_rewards):
        """
        Initializes a new Mystery Box.
        
        :param box_id: Unique identifier for the box.
        :param box_rarity: Rarity level of the box (e.g., 'Common', 'Rare', 'Epic').
        :param possible_rewards: List of possible rewards for the box.
        """
        self.box_id = box_id
        self.box_rarity = box_rarity
        self.possible_rewards = possible_rewards

    def open(self):
        """
        Opens the Mystery Box and returns a random reward.
        
        :return: Selected reward from the box.
        """
        try:
            if not self.possible_rewards:
                raise ValueError("No rewards available in this Mystery Box.")
            # Randomly select a reward from the list of possible rewards
            reward = random.choice(self.possible_rewards)
            return reward
        except Exception as e:
            # Log the error (for production systems, use a proper logging system)
            print(f"Error while opening the Mystery Box: {e}")
            return None

def main():
    """
    Demonstrates the Mystery Box opening feature for the Big Time game.
    """
    # Define possible rewards for a box
    rewards = ["Gold Coins", "Rare Item: Sword of Light", "Epic Item: Shield of Eternity", "XP Boost"]

    # Create a Mystery Box instance
    mystery_box = MysteryBox(box_id=1, box_rarity="Epic", possible_rewards=rewards)

    print("Opening Mystery Box...")
    reward = mystery_box.open()

    if reward:
        print(f"Congratulations! You received: {reward}")
    else:
        print("Failed to open the Mystery Box. Please try again.")

if __name__ == "__main__":
    # Entry point for the program
    main()
```
