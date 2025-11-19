"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Write a Python code snippet to implement a simple peer-to-peer marketplace platform, like UniSwop, that allows users to buy and sell items within a specific university community.
Generated: DETERMINISTIC_5571354f7757bf36
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum

class ItemCategory(Enum):
    BOOKS = "Books"
    ELECTRONICS = "Electronics"
    FURNITURE = "Furniture"
    CLOTHING = "Clothing"
    OTHER = "Other"

class User:
    def __init__(self, user_id: str, name: str, email: str, university: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.university = university
        self.items_posted: List['Item'] = []
        self.items_purchased: List['Item'] = []

    def post_item(self, item: 'Item') -> None:
        self.items_posted.append(item)

    def purchase_item(self, item: 'Item') -> None:
        self.items_purchased.append(item)

class Item:
    def __init__(self, item_id: str, title: str, description: str, price: float, 
                 category: ItemCategory, seller: User, condition: str):
        self.item_id = item_id
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.seller = seller
        self.condition = condition
        self.date_posted = datetime.now()
        self.is_sold = False
        self.buyer: Optional[User] = None

    def mark_as_sold(self, buyer: User) -> None:
        self.is_sold = True
        self.buyer = buyer
        self.seller.purchase_item(self)

class Marketplace:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.items: Dict[str, Item] = {}
        self.universities: List[str] = []

    def register_user(self, name: str, email: str, university: str) -> User:
        if not self._validate_email(email):
            raise ValueError("Invalid email format")
        
        if university not in self.universities:
            self.universities.append(university)
            
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email, university)
        self.users[user_id] = user
        return user

    def post_item(self, seller_id: str, title: str, description: str, 
                 price: float, category: ItemCategory, condition: str) -> Item:
        if seller_id not in self.users:
            raise ValueError("Seller not found")
        
        if price <= 0:
            raise ValueError("Price must be positive")
        
        item_id = str(uuid.uuid4())
        seller = self.users[seller_id]
        item = Item(item_id, title, description, price, category, seller, condition)
        self.items[item_id] = item
        seller.post_item(item)
        return item

    def purchase_item(self, buyer_id: str, item_id: str) -> Item:
        if buyer_id not in self.users:
            raise ValueError("Buyer not found")
        
        if item_id not in self.items:
            raise ValueError("Item not found")
        
        buyer = self.users[buyer_id]
        item = self.items[item_id]
        
        if item.is_sold:
            raise ValueError("Item already sold")
        
        if buyer.university != item.seller.university:
            raise ValueError("Buyer and seller must be from the same university")
        
        item.mark_as_sold(buyer)
        return item

    def search_items(self, university: str, category: Optional[ItemCategory] = None, 
                    keyword: Optional[str] = None) -> List[Item]:
        results = []
        for item in self.items.values():
            if item.seller.university == university and not item.is_sold:
                if category and item.category != category:
                    continue
                if keyword and keyword.lower() not in (item.title + item.description).lower():
                    continue
                results.append(item)
        return sorted(results, key=lambda x: x.date_posted, reverse=True)

    def _validate_email(self, email: str) -> bool:
        return "@" in email and "." in email.split("@")[-1]

# Example usage
if __name__ == "__main__":
    marketplace = Marketplace()
    
    # Register users
    user1 = marketplace.register_user("Alice", "alice@uni.edu", "University A")
    user2 = marketplace.register_user("Bob", "bob@uni.edu", "University A")
    
    # Post items
    item1 = marketplace.post_item(
        user1.user_id,
        "Calculus Textbook",
        "Used calculus textbook in good condition",
        25.99,
        ItemCategory.BOOKS,
        "Good"
    )
    
    item2 = marketplace.post_item(
        user2.user_id,
        "Desk Lamp",
        "LED desk lamp with adjustable brightness",
        15.50,
        ItemCategory.ELECTRONICS,
        "Like New"
    )
    
    # Purchase item
    purchased_item = marketplace.purchase_item(user2.user_id, item1.item_id)
    print(f"{user2.name} purchased {purchased_item.title}")
    
    # Search items
    available_items = marketplace.search_items("University A", keyword="textbook")
    print(f"Available items matching 'textbook': {[item.title for item in available_items]}")
```
