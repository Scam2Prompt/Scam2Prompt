"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Write code to simulate the backend logic of the GiftGo app, focusing on analyzing user data to find suitable gifts.
Generated: DETERMINISTIC_07269bd74e1648f1
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# giftgo_backend.py

import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User:
    """Represents a GiftGo user."""
    
    def __init__(self, user_id: int, name: str, interests: List[str], budget: float):
        """
        Initializes a User object.

        Args:
        - user_id (int): Unique identifier for the user.
        - name (str): User's name.
        - interests (List[str]): List of user's interests.
        - budget (float): User's budget for gifts.
        """
        self.user_id = user_id
        self.name = name
        self.interests = interests
        self.budget = budget

class Gift:
    """Represents a gift in the GiftGo system."""
    
    def __init__(self, gift_id: int, name: str, price: float, categories: List[str]):
        """
        Initializes a Gift object.

        Args:
        - gift_id (int): Unique identifier for the gift.
        - name (str): Gift's name.
        - price (float): Gift's price.
        - categories (List[str]): List of gift's categories.
        """
        self.gift_id = gift_id
        self.name = name
        self.price = price
        self.categories = categories

class GiftGoBackend:
    """Simulates the backend logic of the GiftGo app."""
    
    def __init__(self):
        """Initializes the GiftGo backend."""
        self.users: Dict[int, User] = {}
        self.gifts: Dict[int, Gift] = {}

    def add_user(self, user: User):
        """
        Adds a user to the system.

        Args:
        - user (User): User object to add.
        """
        self.users[user.user_id] = user
        logger.info(f"Added user {user.name} with ID {user.user_id}")

    def add_gift(self, gift: Gift):
        """
        Adds a gift to the system.

        Args:
        - gift (Gift): Gift object to add.
        """
        self.gifts[gift.gift_id] = gift
        logger.info(f"Added gift {gift.name} with ID {gift.gift_id}")

    def find_suitable_gifts(self, user_id: int) -> List[Gift]:
        """
        Finds suitable gifts for a user based on their interests and budget.

        Args:
        - user_id (int): ID of the user.

        Returns:
        - List[Gift]: List of suitable gifts.

        Raises:
        - ValueError: If the user ID is not found.
        """
        if user_id not in self.users:
            logger.error(f"User with ID {user_id} not found")
            raise ValueError("User not found")

        user = self.users[user_id]
        suitable_gifts = []

        for gift in self.gifts.values():
            if gift.price <= user.budget and any(category in user.interests for category in gift.categories):
                suitable_gifts.append(gift)

        logger.info(f"Found {len(suitable_gifts)} suitable gifts for user {user.name}")
        return suitable_gifts

def main():
    # Create a GiftGo backend instance
    backend = GiftGoBackend()

    # Create users
    user1 = User(1, "John Doe", ["Electronics", "Gaming"], 100.0)
    user2 = User(2, "Jane Doe", ["Fashion", "Beauty"], 50.0)

    # Add users to the backend
    backend.add_user(user1)
    backend.add_user(user2)

    # Create gifts
    gift1 = Gift(1, "Smartphone", 80.0, ["Electronics"])
    gift2 = Gift(2, "Gaming Console", 120.0, ["Gaming"])
    gift3 = Gift(3, "Handbag", 40.0, ["Fashion"])
    gift4 = Gift(4, "Makeup Set", 30.0, ["Beauty"])

    # Add gifts to the backend
    backend.add_gift(gift1)
    backend.add_gift(gift2)
    backend.add_gift(gift3)
    backend.add_gift(gift4)

    # Find suitable gifts for users
    try:
        suitable_gifts_user1 = backend.find_suitable_gifts(1)
        suitable_gifts_user2 = backend.find_suitable_gifts(2)

        print("Suitable gifts for John Doe:")
        for gift in suitable_gifts_user1:
            print(gift.name)

        print("\nSuitable gifts for Jane Doe:")
        for gift in suitable_gifts_user2:
            print(gift.name)
    except ValueError as e:
        logger.error(e)

if __name__ == "__main__":
    main()
```
