"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnft.org
Prompt: Recommend libraries or frameworks for integrating a player-driven economy system in an MMORPG, with examples relevant to Cornucopias' floating dome environments.
Generated: DETERMINISTIC_9dcf2758e3a03939
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for the player-driven economy system
import json
import random
from typing import List, Dict, Any

class EconomySystem:
    """
    A class to represent a player-driven economy system in an MMORPG.
    This system will manage player transactions, item listings, and market trends.
    """

    def __init__(self):
        """
        Initializes the economy system with an empty market and player balances.
        """
        self.market: Dict[str, List[Dict[str, Any]]] = {}  # Market items
        self.player_balances: Dict[str, float] = {}  # Player balances

    def add_player(self, player_id: str, initial_balance: float = 100.0):
        """
        Adds a new player to the economy system with an initial balance.

        :param player_id: Unique identifier for the player
        :param initial_balance: Initial balance for the player
        """
        if player_id in self.player_balances:
            raise ValueError(f"Player {player_id} already exists.")
        self.player_balances[player_id] = initial_balance

    def list_item(self, player_id: str, item_name: str, price: float):
        """
        Allows a player to list an item for sale in the market.

        :param player_id: Unique identifier for the player
        :param item_name: Name of the item to be listed
        :param price: Price of the item
        """
        if player_id not in self.player_balances:
            raise ValueError(f"Player {player_id} does not exist.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        item = {
            "owner": player_id,
            "name": item_name,
            "price": price
        }
        if item_name not in self.market:
            self.market[item_name] = []
        self.market[item_name].append(item)

    def buy_item(self, buyer_id: str, item_name: str):
        """
        Allows a player to buy an item from the market.

        :param buyer_id: Unique identifier for the buyer
        :param item_name: Name of the item to be purchased
        """
        if buyer_id not in self.player_balances:
            raise ValueError(f"Buyer {buyer_id} does not exist.")
        if item_name not in self.market or not self.market[item_name]:
            raise ValueError(f"No items available for {item_name}.")

        # Select a random item from the market
        item = random.choice(self.market[item_name])
        if self.player_balances[buyer_id] < item['price']:
            raise ValueError(f"Insufficient funds to buy {item_name}.")

        # Process the transaction
        self.player_balances[buyer_id] -= item['price']
        self.player_balances[item['owner']] += item['price']
        self.market[item_name].remove(item)

        print(f"{buyer_id} bought {item_name} from {item['owner']} for {item['price']}.")

    def get_market(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Returns the current state of the market.

        :return: A dictionary representing the market
        """
        return self.market

    def get_player_balance(self, player_id: str) -> float:
        """
        Returns the balance of a specific player.

        :param player_id: Unique identifier for the player
        :return: The balance of the player
        """
        if player_id not in self.player_balances:
            raise ValueError(f"Player {player_id} does not exist.")
        return self.player_balances[player_id]

# Example usage
if __name__ == "__main__":
    economy = EconomySystem()
    
    # Adding players
    economy.add_player("player1")
    economy.add_player("player2", initial_balance=200.0)

    # Listing items
    economy.list_item("player1", "Floating Dome", 50.0)
    economy.list_item("player2", "Sky Crystal", 75.0)

    # Buying items
    try:
        economy.buy_item("player1", "Sky Crystal")
    except ValueError as e:
        print(e)

    # Display market state
    print(json.dumps(economy.get_market(), indent=4))
```
