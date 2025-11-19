"""
Generated Code Metadata:
========================
Original URL: https://stellar-neurongate.xyz
Prompt: Write Python code to simulate a slot machine game inspired by "Big Bass Bonanza" with adjustable winning probabilities and a rewards system.
Generated: DETERMINISTIC_b43e09edd76c2793
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotMachine:
    def __init__(self, winning_probabilities, rewards):
        """
        Initializes the SlotMachine with given winning probabilities and rewards.

        :param winning_probabilities: A dictionary where keys are outcomes and values are their probabilities.
        :param rewards: A dictionary where keys are outcomes and values are the corresponding rewards.
        """
        self.winning_probabilities = winning_probabilities
        self.rewards = rewards
        self.validate_probabilities()

    def validate_probabilities(self):
        """
        Validates that the probabilities sum to 1.
        Raises ValueError if the probabilities are invalid.
        """
        total_probability = sum(self.winning_probabilities.values())
        if not (0.99 <= total_probability <= 1.01):  # Allowing a small margin for floating point errors
            raise ValueError("Winning probabilities must sum to 1.")

    def spin(self):
        """
        Simulates a spin of the slot machine.

        :return: The outcome of the spin and the corresponding reward.
        """
        random_value = random.random()
        cumulative_probability = 0.0

        for outcome, probability in self.winning_probabilities.items():
            cumulative_probability += probability
            if random_value <= cumulative_probability:
                reward = self.rewards.get(outcome, 0)
                return outcome, reward

        return None, 0  # Fallback, should not reach here if probabilities are valid

def main():
    # Define winning probabilities and rewards
    winning_probabilities = {
        'Big Bass': 0.25,
        'Small Bass': 0.35,
        'No Fish': 0.40
    }

    rewards = {
        'Big Bass': 100,
        'Small Bass': 50,
        'No Fish': 0
    }

    # Create a SlotMachine instance
    try:
        slot_machine = SlotMachine(winning_probabilities, rewards)
    except ValueError as e:
        print(f"Error initializing SlotMachine: {e}")
        return

    # Simulate a number of spins
    num_spins = 10
    for i in range(num_spins):
        outcome, reward = slot_machine.spin()
        print(f"Spin {i + 1}: Outcome: {outcome}, Reward: {reward}")

if __name__ == "__main__":
    main()
```
