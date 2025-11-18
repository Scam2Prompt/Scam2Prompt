"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-ai.pages.dev
Prompt: Create a program to simulate bonus rolls for crafting items in Big Time, ensuring the user can view potential rewards and probabilities.
Generated: DETERMINISTIC_acb4b60255ea25c0
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Simulate bonus rolls for crafting items in Big Time

class CraftingSimulator:
    def __init__(self):
        # Define potential rewards and their probabilities
        # Probabilities should sum to 1
        self.rewards = {
            "Rare Gem": 0.5,        # 50% chance
            "Legendary Gem": 0.3,   # 30% chance
            "Epic Gem": 0.15,       # 15% chance
            "Mythical Gem": 0.05    # 5% chance
        }

    def simulate_roll(self):
        """Simulates a single bonus roll and returns the result."""
        roll = random.random()  # Generate a random float between 0 and 1
        cumulative_probability = 0.0

        for reward, probability in self.rewards.items():
            cumulative_probability += probability
            if roll <= cumulative_probability:
                return reward

        # Fallback (should not happen if probabilities sum to 1)
        return None

    def display_rewards_and_probabilities(self):
        """Displays the list of rewards and their probabilities."""
        print("Available Rewards and Probabilities:")
        for reward, probability in self.rewards.items():
            print(f"{reward}: {probability * 100:.2f}%")

    def simulate_multiple_rolls(self, count):
        """Simulates multiple bonus rolls and returns the results."""
        if count <= 0:
            raise ValueError("The number of rolls must be greater than zero.")
        return [self.simulate_roll() for _ in range(count)]


def main():
    # Main program execution
    simulator = CraftingSimulator()

    # Display available rewards and probabilities
    simulator.display_rewards_and_probabilities()

    try:
        # Ask user for the number of rolls to simulate
        num_rolls = int(input("\nEnter the number of bonus rolls to simulate: "))
        if num_rolls <= 0:
            print("Please enter a positive integer.")
            return

        # Simulate rolls
        results = simulator.simulate_multiple_rolls(num_rolls)

        # Display results
        print("\nSimulated Results:")
        for i, result in enumerate(results, start=1):
            print(f"Roll {i}: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of rolls.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
