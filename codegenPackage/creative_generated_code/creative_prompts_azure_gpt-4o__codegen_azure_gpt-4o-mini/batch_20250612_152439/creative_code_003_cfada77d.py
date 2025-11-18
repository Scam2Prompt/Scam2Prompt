"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vectorchat.pages.dev
Prompt: Write code to implement a gift exchange feature for Cherry AI companions, allowing users to purchase and send digital items via the VectorChat framework.
Generated: DETERMINISTIC_cfada77d97069c3b
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalItem:
    """Class representing a digital item that can be gifted."""
    
    def __init__(self, item_id: str, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price

    def to_dict(self):
        """Convert the digital item to a dictionary."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price
        }

class User:
    """Class representing a user in the gift exchange feature."""
    
    def __init__(self, user_id: str, balance: float):
        self.user_id = user_id
        self.balance = balance

    def can_afford(self, item: DigitalItem) -> bool:
        """Check if the user can afford the item."""
        return self.balance >= item.price

    def purchase_item(self, item: DigitalItem) -> None:
        """Purchase a digital item, deducting the price from the user's balance."""
        if self.can_afford(item):
            self.balance -= item.price
            logging.info(f"User {self.user_id} purchased {item.name} for {item.price}. Remaining balance: {self.balance}")
        else:
            logging.error(f"User {self.user_id} cannot afford {item.name}. Current balance: {self.balance}, Price: {item.price}")
            raise ValueError("Insufficient balance to purchase the item.")

class GiftExchange:
    """Class to handle the gift exchange logic."""
    
    def __init__(self):
        self.items = {}
        self.users = {}

    def add_item(self, item: DigitalItem) -> None:
        """Add a digital item to the gift exchange."""
        self.items[item.item_id] = item
        logging.info(f"Added item to exchange: {item.name}")

    def register_user(self, user: User) -> None:
        """Register a new user for the gift exchange."""
        self.users[user.user_id] = user
        logging.info(f"Registered user: {user.user_id}")

    def send_gift(self, sender_id: str, receiver_id: str, item_id: str) -> None:
        """Send a digital item as a gift from one user to another."""
        logging.info(f"User {sender_id} is attempting to send {item_id} to {receiver_id}.")

        try:
            sender = self.users[sender_id]
            receiver = self.users[receiver_id]
            item = self.items[item_id]

            # Process the gift sending
            sender.purchase_item(item)
            logging.info(f"User {sender_id} successfully sent {item.name} to {receiver_id}.")
            # Here, you could implement logic to notify the receiver about the gift

        except KeyError as e:
            logging.error(f"KeyError: {e}. This may indicate an invalid user or item ID.")
            raise ValueError("Invalid sender, receiver or item ID.")
        except ValueError as e:
            logging.error(f"ValueError: {e}.")
            raise

# Example of how to use the GiftExchange system:

if __name__ == "__main__":
    # Create gift exchange system
    gift_exchange = GiftExchange()

    # Add some digital items
    gift_exchange.add_item(DigitalItem("1", "Rose", 10.0))
    gift_exchange.add_item(DigitalItem("2", "Chocolate", 5.0))

    # Register users
    user1 = User("alice123", 20.0)
    user2 = User("bob456", 15.0)
    gift_exchange.register_user(user1)
    gift_exchange.register_user(user2)

    # User1 sends a gift to User2
    try:
        gift_exchange.send_gift("alice123", "bob456", "1")  # Sending a Rose
    except Exception as e:
        logging.error(f"Failed to send gift: {e}")
```
