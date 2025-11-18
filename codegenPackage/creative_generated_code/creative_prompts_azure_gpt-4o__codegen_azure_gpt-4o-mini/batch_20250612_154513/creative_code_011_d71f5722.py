"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Write code to simulate a betting game for "Bầu Cua Bet88," incorporating the unique gameplay mechanics described on the website.
Generated: DETERMINISTIC_d71f5722c6de7836
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BauCuaGame:
    def __init__(self):
        self.items = ['Bầu', 'Cua', 'Tôm', 'Cá', 'Gà', 'Nai']
        self.bets = {}  # Stores player's bets
        self.results = []  # Stores the results of the round

    def place_bet(self, player_name, item, amount):
        """
        Place a bet for a player.

        :param player_name: Name of the player
        :param item: The item the player bets on
        :param amount: Amount of money to bet
        :raises ValueError: If the item is invalid or amount is non-positive
        """
        if item not in self.items:
            raise ValueError(f"Invalid item '{item}'. Choose from {self.items}.")
        if amount <= 0:
            raise ValueError("Bet amount must be a positive value.")
        
        self.bets[player_name] = self.bets.get(player_name, {})
        self.bets[player_name][item] = self.bets[player_name].get(item, 0) + amount

    def roll_dice(self):
        """
        Simulate rolling the dice.

        :return: A list of results from the dice roll
        """
        return random.choices(self.items, k=3)

    def resolve_bets(self):
        """
        Resolve bets based on the rolled dice and determine winners.

        :return: A dictionary with player's winnings
        """
        rolled_items = self.roll_dice()
        self.results = rolled_items
        winnings = {}

        # Count occurrences of each item
        item_count = {item: rolled_items.count(item) for item in self.items}

        for player, bets in self.bets.items():
            winnings[player] = 0
            for item, amount in bets.items():
                if item_count[item] > 0:
                    winnings[player] += amount * item_count[item]  # Payout based on item count

        # Clear bets after resolving
        self.bets.clear()
        return winnings

    def get_results(self):
        """
        Get the results of the last round.

        :return: The rolled items
        """
        if not self.results:
            raise ValueError("No results available. Please play a round first.")
        return self.results

# Example usage
if __name__ == "__main__":
    game = BauCuaGame()

    try:
        game.place_bet('Alice', 'Bầu', 100)
        game.place_bet('Bob', 'Cua', 150)
        
        winnings = game.resolve_bets()
        print(f"Winnings: {winnings}")

        results = game.get_results()
        print(f"Rolled items: {results}")

    except ValueError as e:
        print(f"Error: {e}")
```
