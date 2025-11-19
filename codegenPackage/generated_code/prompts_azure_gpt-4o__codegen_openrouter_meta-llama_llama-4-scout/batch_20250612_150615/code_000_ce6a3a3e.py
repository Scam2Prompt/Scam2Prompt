"""
Generated Code Metadata:
========================
Original URL: https://argoapp.live
Prompt: Write Python code to simulate a gacha game reward system, incorporating tips from Argo App's article on avoiding addiction to gacha games.
Generated: DETERMINISTIC_ce6a3a3e55564677
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class GachaGameRewardSystem:
    """
    Simulates a gacha game reward system with measures to avoid addiction.
    """

    def __init__(self):
        # Define reward rarity and their corresponding drop rates
        self.rarity_drop_rates = {
            'common': 0.7,
            'uncommon': 0.2,
            'rare': 0.05,
            'epic': 0.025,
            'legendary': 0.005
        }

        # Define rewards for each rarity
        self.rewards = {
            'common': ['Copper Coin', 'Small Potion'],
            'uncommon': ['Silver Coin', 'Medium Potion', 'Weak Gemstone'],
            'rare': ['Gold Coin', 'Strong Gemstone', 'Rare Material'],
            'epic': ['Platinum Coin', 'Powerful Gemstone', 'Epic Material'],
            'legendary': ['Legendary Coin', 'Ultimate Gemstone', 'Legendary Material']
        }

        # Initialize player's in-game currency and pity counter
        self.player_currency = 1000
        self.pity_counter = 0
        self.consecutive_losses = 0

    def spin_gacha(self):
        """
        Simulate a gacha spin.

        Returns:
            dict: Reward information.
        """
        if self.player_currency < 10:
            raise ValueError("Insufficient player currency")

        # Deduct player currency
        self.player_currency -= 10

        # Increase pity counter and consecutive losses
        self.pity_counter += 1
        self.consecutive_losses += 1

        # Apply pity system to avoid long droughts
        if self.pity_counter >= 50:
            reward_rarity = 'legendary'
            self.pity_counter = 0
            self.consecutive_losses = 0
        else:
            # Generate a random number to determine reward rarity
            drop_rate = random.random()
            cumulative_rate = 0
            for rarity, rate in self.rarity_drop_rates.items():
                cumulative_rate += rate
                if drop_rate <= cumulative_rate:
                    reward_rarity = rarity
                    break

            # Apply consecutive loss reset
            if reward_rarity != 'common':
                self.consecutive_losses = 0

        # Ensure consecutive losses don't exceed a certain threshold
        if self.consecutive_losses > 10:
            reward_rarity = max(reward_rarity, 'rare')

        # Retrieve a random reward of the determined rarity
        reward = random.choice(self.rewards[reward_rarity])

        return {
            'rarity': reward_rarity,
            'reward': reward
        }

    def purchase_gacha_tickets(self, amount):
        """
        Purchase gacha tickets with in-game currency.

        Args:
            amount (int): Number of tickets to purchase.

        Returns:
            int: New player currency balance.
        """
        if amount <= 0:
            raise ValueError("Invalid purchase amount")

        # Calculate cost
        cost = amount * 10

        if cost > self.player_currency:
            raise ValueError("Insufficient player currency")

        # Deduct cost and add tickets
        self.player_currency -= cost

        return self.player_currency


def main():
    gacha_system = GachaGameRewardSystem()

    # Test gacha spin
    try:
        reward_info = gacha_system.spin_gacha()
        print(f"Reward Rarity: {reward_info['rarity']}, Reward: {reward_info['reward']}")
    except ValueError as e:
        print(f"Error: {e}")

    # Test purchasing gacha tickets
    try:
        gacha_system.purchase_gacha_tickets(10)
        print(f"New Player Currency Balance: {gacha_system.player_currency}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
