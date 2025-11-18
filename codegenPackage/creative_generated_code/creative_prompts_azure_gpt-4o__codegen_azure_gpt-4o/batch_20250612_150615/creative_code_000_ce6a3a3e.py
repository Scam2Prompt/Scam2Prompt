"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argoapp.live
Prompt: Write Python code to simulate a gacha game reward system, incorporating tips from Argo App's article on avoiding addiction to gacha games.
Generated: DETERMINISTIC_ce6a3a3e55564677
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class GachaGame:
    """
    A class to simulate a gacha game reward system with safeguards
    to promote responsible play and avoid addictive behaviors.
    """
    def __init__(self, available_rewards, premium_rewards, daily_free_pulls=1, pity_counter_threshold=50):
        """
        Initialize the gacha game system.

        :param available_rewards: List of standard rewards (common and rare items).
        :param premium_rewards: List of premium (ultra-rare) rewards.
        :param daily_free_pulls: Number of free pulls the user gets daily.
        :param pity_counter_threshold: Number of pulls before guaranteeing a premium reward.
        """
        self.available_rewards = available_rewards
        self.premium_rewards = premium_rewards
        self.daily_free_pulls = daily_free_pulls
        self.pity_counter_threshold = pity_counter_threshold
        self.pity_counter = 0
        self.balance = 0  # In-game currency balance
        self.pull_cost = 10  # Cost of a single pull in in-game currency

    def pull(self):
        """
        Perform a single pull in the gacha game.
        :return: The reward obtained from the pull.
        """
        # Increment the pity counter
        self.pity_counter += 1

        # Determine reward
        if self.pity_counter >= self.pity_counter_threshold:
            # Guarantee a premium reward if pity counter threshold is reached
            reward = random.choice(self.premium_rewards)
            self.pity_counter = 0  # Reset pity counter
        else:
            # Pick from standard rewards with a small chance for a premium reward
            if random.random() < 0.05:  # 5% chance for a premium reward
                reward = random.choice(self.premium_rewards)
            else:
                reward = random.choice(self.available_rewards)

        return reward

    def daily_free_pull(self):
        """
        Perform a free pull that is available daily.
        :return: The reward obtained from the pull.
        """
        if self.daily_free_pulls > 0:
            self.daily_free_pulls -= 1
            return self.pull()
        else:
            raise ValueError("No free pulls left for today. Please try again tomorrow.")

    def buy_pull(self):
        """
        Perform a pull using in-game currency.
        :return: The reward obtained from the pull.
        """
        if self.balance >= self.pull_cost:
            self.balance -= self.pull_cost
            return self.pull()
        else:
            raise ValueError("Insufficient balance to perform a pull.")

    def add_balance(self, amount):
        """
        Add in-game currency to the player's balance.

        :param amount: Amount of currency to add.
        """
        if amount <= 0:
            raise ValueError("Amount to add must be greater than zero.")
        self.balance += amount

    def reset_daily_free_pulls(self):
        """
        Reset the daily free pulls (to be called once per day).
        """
        self.daily_free_pulls = 1

# Example of how to set up and use the GachaGame class
if __name__ == "__main__":
    # Define rewards
    standard_rewards = ["Potion", "Elixir", "Iron Sword", "Steel Armor"]
    premium_rewards = ["Legendary Sword", "Mythical Staff", "Dragon Mount"]

    # Initialize the gacha game
    game = GachaGame(available_rewards=standard_rewards, premium_rewards=premium_rewards)

    # Simulate adding balance
    game.add_balance(100)  # Add 100 in-game currency

    # Perform daily free pull
    try:
        print("Daily Free Pull Reward:", game.daily_free_pull())
    except ValueError as e:
        print(e)

    # Perform paid pulls
    try:
        for _ in range(5):
            print("Paid Pull Reward:", game.buy_pull())
    except ValueError as e:
        print(e)

    # Reset daily free pulls at the end of the day
    game.reset_daily_free_pulls()
```
