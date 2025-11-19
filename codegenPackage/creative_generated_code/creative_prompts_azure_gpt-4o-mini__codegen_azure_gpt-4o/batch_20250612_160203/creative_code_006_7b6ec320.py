"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: How can I design a gamification strategy using Mystery Boxes to incentivize user participation in a mobile application?
Generated: DETERMINISTIC_7b6ec320b9cd876f
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class MysteryBox:
    """
    Class representing a Mystery Box in the gamification strategy.
    """

    def __init__(self, box_id, rewards):
        """
        Initializes a Mystery Box instance.

        :param box_id: Unique identifier for the box.
        :param rewards: List of possible rewards (dicts with 'reward' and 'probability').
        """
        self.box_id = box_id
        self.rewards = rewards

    def open_box(self):
        """
        Simulates opening the mystery box and returns a reward based on probabilities.

        :return: A randomly selected reward.
        """
        total_probability = sum(reward['probability'] for reward in self.rewards)
        if total_probability != 1.0:
            raise ValueError("Total probability of rewards must equal 1.0")

        random_choice = random.uniform(0, 1)
        cumulative_probability = 0

        for reward in self.rewards:
            cumulative_probability += reward['probability']
            if random_choice <= cumulative_probability:
                return reward['reward']

        raise RuntimeError("Failed to select a reward - probabilities might not be configured correctly.")


class GamificationSystem:
    """
    Class for managing gamification strategies using Mystery Boxes.
    """

    def __init__(self):
        """
        Initializes the gamification system with a list of mystery boxes.
        """
        self.mystery_boxes = {}

    def add_mystery_box(self, box_id, rewards):
        """
        Adds a new mystery box to the system.

        :param box_id: Unique identifier for the box.
        :param rewards: List of rewards with associated probabilities.
        """
        if box_id in self.mystery_boxes:
            raise ValueError(f"Mystery Box with ID {box_id} already exists.")
        self.mystery_boxes[box_id] = MysteryBox(box_id, rewards)

    def open_mystery_box(self, box_id):
        """
        Opens a specified mystery box and returns the reward.

        :param box_id: Unique identifier for the box.
        :return: Reward from the opened mystery box.
        """
        if box_id not in self.mystery_boxes:
            raise ValueError(f"Mystery Box with ID {box_id} does not exist.")
        return self.mystery_boxes[box_id].open_box()

    def save_to_file(self, filename):
        """
        Saves the mystery box data to a JSON file.

        :param filename: Name of the file to save the data.
        """
        with open(filename, 'w') as file:
            data = {
                box_id: [reward for reward in box.rewards]
                for box_id, box in self.mystery_boxes.items()
            }
            json.dump(data, file)

    def load_from_file(self, filename):
        """
        Loads mystery box data from a JSON file.

        :param filename: Name of the file to load the data from.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            for box_id, rewards in data.items():
                self.add_mystery_box(box_id, rewards)


# Example Usage
if __name__ == "__main__":
    # Initialize the gamification system
    system = GamificationSystem()

    # Define rewards for a mystery box
    rewards = [
        {"reward": "50 Coins", "probability": 0.5},
        {"reward": "100 Coins", "probability": 0.3},
        {"reward": "Special Item", "probability": 0.2}
    ]

    # Add a mystery box to the system
    system.add_mystery_box("box_1", rewards)

    # Open the mystery box
    try:
        reward = system.open_mystery_box("box_1")
        print(f"Congratulations! You received: {reward}")
    except Exception as e:
        print(f"Error: {e}")

    # Save mystery box data to a file
    system.save_to_file("mystery_boxes.json")

    # Load mystery box data from a file
    loaded_system = GamificationSystem()
    loaded_system.load_from_file("mystery_boxes.json")
    print("Mystery Box data loaded successfully.")
```
