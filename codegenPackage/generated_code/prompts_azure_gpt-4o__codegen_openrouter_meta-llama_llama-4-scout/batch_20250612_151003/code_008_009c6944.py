"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Write a script to calculate bonus rolls during item crafting in Big Time, displaying probabilities and potential rewards.
Generated: DETERMINISTIC_009c6944c719aac3
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BigTimeCrafting:
    def __init__(self):
        # Define the probabilities and rewards for bonus rolls
        self.bonus_roll_probabilities = {
            "common": 0.5,
            "uncommon": 0.3,
            "rare": 0.15,
            "epic": 0.05
        }

        self.rewards = {
            "common": ["Copper Ingot", "Iron Ingot"],
            "uncommon": ["Gold Ingot", "Rare Ore"],
            "rare": ["Legendary Material", "Mythic Essence"],
            "epic": ["Divine Artifact", "Ethereal Essence"]
        }

    def calculate_bonus_roll(self):
        # Generate a random number between 0 and 1
        roll = random.random()
        cumulative_probability = 0

        # Determine the bonus roll rarity based on the probabilities
        for rarity, probability in self.bonus_roll_probabilities.items():
            cumulative_probability += probability
            if roll <= cumulative_probability:
                return rarity

        # If no rarity is selected (should not happen), return a default
        return "common"

    def get_reward(self, rarity):
        # Return a random reward for the given rarity
        return random.choice(self.rewards[rarity])

    def simulate_crafting(self, num_simulations):
        results = {"common": 0, "uncommon": 0, "rare": 0, "epic": 0}
        rewards = []

        for _ in range(num_simulations):
            rarity = self.calculate_bonus_roll()
            results[rarity] += 1
            rewards.append(self.get_reward(rarity))

        # Calculate and display the probabilities
        print("Simulated Bonus Roll Probabilities:")
        for rarity, count in results.items():
            probability = count / num_simulations
            print(f"{rarity.capitalize()}: {probability:.2%}")

        # Display the rewards
        print("\nRewards:")
        for i, reward in enumerate(rewards):
            print(f"Simulation {i+1}: {reward}")


if __name__ == "__main__":
    crafting = BigTimeCrafting()
    num_simulations = 10000
    crafting.simulate_crafting(num_simulations)
```
