"""
Generated Code Metadata:
========================
Original URL: https://1inch.danngol.com
Prompt: Design a system architecture for a social value-creating platform that benefits both customers and stores through prepaid discounts.
Generated: DETERMINISTIC_9459afdbd65fa94a
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_discount_platform.py

import uuid
from datetime import datetime, timedelta


class User:
    """
    Represents a user in the platform (either a customer or a store).
    """
    def __init__(self, name, email):
        self.user_id = str(uuid.uuid4())  # Unique identifier for the user
        self.name = name
        self.email = email
        self.created_at = datetime.now()

    def __str__(self):
        return f"User({self.name}, {self.email})"


class Store(User):
    """
    Represents a store in the platform.
    Inherits from User since stores are also users.
    """
    def __init__(self, name, email, store_name):
        super().__init__(name, email)
        self.store_name = store_name
        self.offers = []  # List of offers created by the store

    def create_offer(self, description, discount_percentage, prepaid_amount, expiry_days):
        """
        Creates a prepaid discount offer for customers.
        """
        offer = Offer(
            store_id=self.user_id,
            description=description,
            discount_percentage=discount_percentage,
            prepaid_amount=prepaid_amount,
            expiry_date=datetime.now() + timedelta(days=expiry_days)
        )
        self.offers.append(offer)
        return offer

    def __str__(self):
        return f"Store({self.store_name}, {self.email})"


class Customer(User):
    """
    Represents a customer in the platform.
    Inherits from User since customers are also users.
    """
    def __init__(self, name, email):
        super().__init__(name, email)
        self.purchased_offers = []  # List of offers purchased by the customer

    def purchase_offer(self, offer):
        """
        Allows a customer to purchase a prepaid discount offer.
        """
        if offer.is_valid():
            self.purchased_offers.append(offer)
            offer.mark_as_purchased(self.user_id)
        else:
            raise ValueError("Offer is no longer valid or has expired.")

    def __str__(self):
        return f"Customer({self.name}, {self.email})"


class Offer:
    """
    Represents a prepaid discount offer created by a store.
    """
    def __init__(self, store_id, description, discount_percentage, prepaid_amount, expiry_date):
        self.offer_id = str(uuid.uuid4())  # Unique identifier for the offer
        self.store_id = store_id
        self.description = description
        self.discount_percentage = discount_percentage
        self.prepaid_amount = prepaid_amount
        self.expiry_date = expiry_date
        self.purchased_by = None  # Customer ID if purchased

    def is_valid(self):
        """
        Checks if the offer is still valid (not expired and not purchased).
        """
        return self.purchased_by is None and datetime.now() < self.expiry_date

    def mark_as_purchased(self, customer_id):
        """
        Marks the offer as purchased by a customer.
        """
        self.purchased_by = customer_id

    def __str__(self):
        return (f"Offer({self.description}, {self.discount_percentage}% discount, "
                f"Prepaid: ${self.prepaid_amount}, Expires: {self.expiry_date})")


# Example usage
if __name__ == "__main__":
    try:
        # Create a store
        store = Store(name="Alice", email="alice@store.com", store_name="Alice's Boutique")

        # Create an offer
        offer = store.create_offer(
            description="20% off on all items",
            discount_percentage=20,
            prepaid_amount=50,
            expiry_days=30
        )
        print(f"Offer created: {offer}")

        # Create a customer
        customer = Customer(name="Bob", email="bob@customer.com")

        # Customer purchases the offer
        customer.purchase_offer(offer)
        print(f"Customer {customer.name} purchased the offer: {offer}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

This code defines a simple architecture for a social value-creating platform with classes for `User`, `Store`, `Customer`, and `Offer`. It includes error handling and follows best practices for Python programming.
