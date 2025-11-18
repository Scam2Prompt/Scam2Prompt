"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ketoken.com
Prompt: Create a loyalty program using KeToken that rewards customers with digital tokens for dining at partner restaurants. Include code for token distribution.
Generated: DETERMINISTIC_4b58e91ee8706cd8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, List, Optional

class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.tokens: int = 0  # Initialize tokens to 0

    def add_tokens(self, amount: int):
        """Add tokens to the customer's balance."""
        if amount < 0:
            raise ValueError("Cannot add negative tokens.")
        self.tokens += amount

    def get_tokens(self) -> int:
        """Return the customer's token balance."""
        return self.tokens


class Restaurant:
    def __init__(self, restaurant_id: str, name: str):
        self.restaurant_id = restaurant_id
        self.name = name

    def reward_tokens(self) -> int:
        """Define the number of tokens to reward for dining."""
        # Example logic: Reward between 10 to 50 tokens randomly
        return random.randint(10, 50)


class LoyaltyProgram:
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.restaurants: Dict[str, Restaurant] = {}

    def register_customer(self, customer_id: str, name: str) -> Customer:
        """Register a new customer in the loyalty program."""
        if customer_id in self.customers:
            raise ValueError("Customer already registered.")
        customer = Customer(customer_id, name)
        self.customers[customer_id] = customer
        return customer

    def register_restaurant(self, restaurant_id: str, name: str) -> Restaurant:
        """Register a new restaurant in the loyalty program."""
        if restaurant_id in self.restaurants:
            raise ValueError("Restaurant already registered.")
        restaurant = Restaurant(restaurant_id, name)
        self.restaurants[restaurant_id] = restaurant
        return restaurant

    def dine_at_restaurant(self, customer_id: str, restaurant_id: str) -> Optional[int]:
        """Reward tokens to customer for dining at a specific restaurant."""
        if customer_id not in self.customers:
            raise ValueError("Customer not registered.")
        if restaurant_id not in self.restaurants:
            raise ValueError("Restaurant not registered.")

        customer = self.customers[customer_id]
        restaurant = self.restaurants[restaurant_id]

        tokens_rewarded = restaurant.reward_tokens()
        customer.add_tokens(tokens_rewarded)
        return tokens_rewarded

    def get_customer_tokens(self, customer_id: str) -> int:
        """Retrieve the total tokens of a customer."""
        if customer_id not in self.customers:
            raise ValueError("Customer not registered.")
        return self.customers[customer_id].get_tokens()


# Example usage of the Loyalty Program
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()

    # Register customers
    customer1 = loyalty_program.register_customer("C001", "Alice")
    customer2 = loyalty_program.register_customer("C002", "Bob")

    # Register restaurants
    restaurant1 = loyalty_program.register_restaurant("R001", "Pasta Palace")
    restaurant2 = loyalty_program.register_restaurant("R002", "Burger Barn")

    # Simulate dining and earning tokens
    try:
        tokens_earned = loyalty_program.dine_at_restaurant("C001", "R001")
        print(f"Alice earned {tokens_earned} tokens.")

        tokens_earned = loyalty_program.dine_at_restaurant("C002", "R002")
        print(f"Bob earned {tokens_earned} tokens.")

        # Display token balances
        print(f"Alice's token balance: {loyalty_program.get_customer_tokens('C001')}")
        print(f"Bob's token balance: {loyalty_program.get_customer_tokens('C002')}")
    except ValueError as e:
        print(f"Error: {e}")
```
