"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Design an algorithm in Python to calculate the rewards for players based on their registration tier (e.g., Pebble x50 for 10K, Poop x1M for 50K, etc.) as described on the SIMemes site.
Generated: DETERMINISTIC_0c79cfeacbca8d76
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_calculator.py

class RegistrationTier:
    """Represents a registration tier with its corresponding reward."""
    def __init__(self, name, threshold, reward_amount, reward_unit):
        """
        Initializes a RegistrationTier instance.

        Args:
            name (str): The name of the tier.
            threshold (int): The minimum registration count required for the tier.
            reward_amount (int): The amount of the reward.
            reward_unit (str): The unit of the reward (e.g., 'x50', 'x1M').
        """
        self.name = name
        self.threshold = threshold
        self.reward_amount = reward_amount
        self.reward_unit = reward_unit

    def __str__(self):
        return f"{self.name} - {self.reward_amount}{self.reward_unit}"


class RewardsCalculator:
    """Calculates rewards for players based on their registration tier."""
    def __init__(self):
        # Define the registration tiers and their corresponding rewards.
        self.tiers = [
            RegistrationTier("Pebble", 10_000, 50, "x"),
            RegistrationTier("Poop", 50_000, 1_000_000, "x"),
            # Add more tiers as needed.
        ]
        self.tiers.sort(key=lambda tier: tier.threshold)

    def calculate_reward(self, registration_count):
        """
        Calculates the reward for a player based on their registration count.

        Args:
            registration_count (int): The player's registration count.

        Returns:
            str: The reward for the player (e.g., "Pebble x50").
        """
        if registration_count < 0:
            raise ValueError("Registration count cannot be negative.")

        # Find the highest tier that the player's registration count qualifies for.
        qualifying_tier = next((tier for tier in reversed(self.tiers) if registration_count >= tier.threshold), None)

        if qualifying_tier:
            return f"{qualifying_tier.name} {qualifying_tier.reward_unit}{qualifying_tier.reward_amount}"
        else:
            return "No reward eligible."


def main():
    calculator = RewardsCalculator()

    # Example usage:
    registration_counts = [5_000, 15_000, 75_000]
    for count in registration_counts:
        try:
            reward = calculator.calculate_reward(count)
            print(f"Registration count: {count}, Reward: {reward}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
