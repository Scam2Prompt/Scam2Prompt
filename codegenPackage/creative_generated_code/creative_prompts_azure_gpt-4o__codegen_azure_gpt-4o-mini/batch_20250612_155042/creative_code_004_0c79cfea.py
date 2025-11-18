"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Design an algorithm in Python to calculate the rewards for players based on their registration tier (e.g., Pebble x50 for 10K, Poop x1M for 50K, etc.) as described on the SIMemes site.
Generated: DETERMINISTIC_0c79cfeacbca8d76
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TierRewards:
    """A class to calculate rewards for players based on their registration tier."""
    
    def __init__(self):
        """Initialize the tier rewards mapping."""
        self.tiers = {
            'Pebble': (50, 10000),  # (reward_amount, threshold)
            'Poop': (1000000, 50000),
            'Diamond': (200, 20000),
            # Add more tiers and their rewards as needed
        }

    def calculate_rewards(self, registration_amount):
        """
        Calculate the rewards based on the registration amount.

        Args:
            registration_amount (int): The amount registered by the player.

        Returns:
            dict: A dictionary containing the tier names and their corresponding rewards.
        """
        if registration_amount < 0:
            raise ValueError("Registration amount cannot be negative.")
        
        rewards = {}
        
        # Iterate over tiers to calculate rewards
        for tier, (reward_amount, threshold) in self.tiers.items():
            if registration_amount >= threshold:
                rewards[tier] = reward_amount
        
        return rewards

def main():
    """Main function to demonstrate the tier reward calculation."""
    try:
        # Example registration amounts
        registration_amounts = [5000, 15000, 55000, 100000]

        # Initialize the rewards calculator
        tier_rewards = TierRewards()

        for amount in registration_amounts:
            rewards = tier_rewards.calculate_rewards(amount)
            print(f"Registration Amount: {amount} | Rewards: {rewards}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
