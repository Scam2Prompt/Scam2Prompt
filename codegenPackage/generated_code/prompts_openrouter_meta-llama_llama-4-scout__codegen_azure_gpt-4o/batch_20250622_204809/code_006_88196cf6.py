"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Develop a simple example of a marketplace system for a game like ev.io, including features for buying, selling, and trading in-game items.
Generated: DETERMINISTIC_88196cf6cb59a568
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# marketplace.py

import uuid

class Item:
    """
    Represents an in-game item.
    """
    def __init__(self, name, price):
        self.id = str(uuid.uuid4())  # Unique identifier for the item
        self.name = name
        self.price = price  # Price in in-game currency

    def __str__(self):
        return f"Item(ID: {self.id}, Name: {self.name}, Price: {self.price})"


class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance  # In-game currency balance
        self.inventory = []  # List of items owned by the player

    def add_item(self, item):
        """
        Adds an item to the player's inventory.
        """
        self.inventory.append(item)

    def remove_item(self, item_id):
        """
        Removes an item from the player's inventory by ID.
        """
        for item in self.inventory:
            if item.id == item_id:
                self.inventory.remove(item)
                return item
        raise ValueError("Item not found in inventory.")

    def __str__(self):
        inventory_list = ", ".join([item.name for item in self.inventory])
        return f"Player(Username: {self.username}, Balance: {self.balance}, Inventory: [{inventory_list}])"


class Marketplace:
    """
    Represents the marketplace system for buying, selling, and trading items.
    """
    def __init__(self):
        self.listings = []  # List of items available for sale

    def list_item_for_sale(self, seller, item_id, price):
        """
        Lists an item for sale in the marketplace.
        """
        try:
            item = seller.remove_item(item_id)
            item.price = price
            self.listings.append((item, seller))
            print(f"Item '{item.name}' listed for sale at {price} by {seller.username}.")
        except ValueError as e:
            print(f"Error: {e}")

    def buy_item(self, buyer, item_id):
        """
        Allows a player to buy an item from the marketplace.
        """
        for listing in self.listings:
            item, seller = listing
            if item.id == item_id:
                if buyer.balance >= item.price:
                    buyer.balance -= item.price
                    seller.balance += item.price
                    buyer.add_item(item)
                    self.listings.remove(listing)
                    print(f"{buyer.username} bought '{item.name}' from {seller.username} for {item.price}.")
                    return
                else:
                    print("Error: Insufficient balance.")
                    return
        print("Error: Item not found in marketplace.")

    def trade_item(self, player1, player2, item_id1, item_id2):
        """
        Allows two players to trade items directly.
        """
        try:
            item1 = player1.remove_item(item_id1)
            item2 = player2.remove_item(item_id2)
            player1.add_item(item2)
            player2.add_item(item1)
            print(f"Trade completed: {player1.username} traded '{item1.name}' with {player2.username} for '{item2.name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def __str__(self):
        listings_str = "\n".join([f"Item: {item.name}, Price: {item.price}, Seller: {seller.username}" for item, seller in self.listings])
        return f"Marketplace Listings:\n{listings_str}"


# Example usage
if __name__ == "__main__":
    # Create players
    player1 = Player("Player1", 100)
    player2 = Player("Player2", 50)

    # Create items
    sword = Item("Sword", 30)
    shield = Item("Shield", 20)
    potion = Item("Potion", 10)

    # Add items to players' inventories
    player1.add_item(sword)
    player1.add_item(shield)
    player2.add_item(potion)

    # Create marketplace
    marketplace = Marketplace()

    # List items for sale
    marketplace.list_item_for_sale(player1, sword.id, 40)
    marketplace.list_item_for_sale(player1, shield.id, 25)

    # Print marketplace listings
    print(marketplace)

    # Player2 buys an item
    marketplace.buy_item(player2, sword.id)

    # Print players' details
    print(player1)
    print(player2)

    # Trade items between players
    marketplace.trade_item(player1, player2, shield.id, potion.id)

    # Print players' details after trade
    print(player1)
    print(player2)
```
