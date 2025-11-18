"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foolz.sellpass.io
Prompt: Write code to set up referral program tracking and ratings/reviews for products sold through a Sellpass storefront.
Generated: DETERMINISTIC_8a373cc3cacd6d74
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

import uuid
from datetime import datetime
from typing import List, Dict, Optional

# Class to represent a user in the referral program
class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.referrals: List[str] = []  # List of user IDs referred by this user

# Class to represent a product sold through the Sellpass storefront
class Product:
    def __init__(self, product_id: str, name: str):
        self.product_id = product_id
        self.name = name
        self.reviews: List[Dict] = []  # List of reviews for this product

# Class to manage the referral program and product reviews
class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}  # Keyed by user ID
        self.products: Dict[str, Product] = {}  # Keyed by product ID

    def add_user(self, name: str) -> str:
        """Add a new user to the referral program and return their user ID."""
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = User(user_id=user_id, name=name)
        return user_id

    def refer_user(self, referrer_id: str, referred_id: str) -> bool:
        """Link a referred user to the referrer."""
        if referrer_id in self.users and referred_id in self.users:
            self.users[referrer_id].referrals.append(referred_id)
            return True
        return False

    def add_product(self, name: str) -> str:
        """Add a new product and return its product ID."""
        product_id = str(uuid.uuid4())  # Generate a unique product ID
        self.products[product_id] = Product(product_id=product_id, name=name)
        return product_id

    def add_review(self, product_id: str, user_id: str, rating: int, comment: str) -> Optional[str]:
        """Add a review for a product by a user."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        if user_id not in self.users:
            raise ValueError("User not found.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        
        review = {
            'user_id': user_id,
            'rating': rating,
            'comment': comment,
            'timestamp': datetime.now()
        }
        self.products[product_id].reviews.append(review)
        return "Review added successfully."

    def get_product_reviews(self, product_id: str) -> List[Dict]:
        """Retrieve all reviews for a specific product."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        return self.products[product_id].reviews

# Example Usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Add users
    user_id_1 = referral_program.add_user("Alice")
    user_id_2 = referral_program.add_user("Bob")

    # Refer Bob to Alice
    referral_program.refer_user(user_id_1, user_id_2)

    # Add a product
    product_id = referral_program.add_product("Gadget")

    # Add reviews
    try:
        referral_program.add_review(product_id, user_id_1, 5, "Excellent product!")
        referral_program.add_review(product_id, user_id_2, 4, "Very good, but could be better.")
    except ValueError as e:
        print(f"Error adding review: {e}")

    # Retrieve and print reviews
    reviews = referral_program.get_product_reviews(product_id)
    for review in reviews:
        print(review)
```
