"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalty.finance
Prompt: What are some best practices for developing a loyalty finance application using the domain loyalty.finance?
Generated: DETERMINISTIC_bb2fbe3e67cc3508
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# loyalty_finance.py

"""
Loyalty Finance Application

This application provides a framework for managing a customer loyalty program.
It includes features for customer registration, points accumulation, redemption,
and rewards tracking. The code follows best practices for Python development,
including modular design, error handling, and documentation.
"""

import json
from typing import Dict, Any

class Customer:
    """Represents a customer in the loyalty program."""
    
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.points = 0

    def add_points(self, amount: int) -> None:
        """Add points to the customer's account."""
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.points += amount

    def redeem_points(self, amount: int) -> bool:
        """Redeem points from the customer's account."""
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        if amount > self.points:
            raise ValueError("Not enough points to redeem")
        self.points -= amount
        return True

    def to_dict(self) -> Dict[str, Any]:
        """Convert customer information to a dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "points": self.points
        }


class LoyaltyProgram:
    """Manages the loyalty program functionality."""
    
    def __init__(self) -> None:
        self.customers: Dict[str, Customer] = {}

    def register_customer(self, customer_id: str, name: str) -> None:
        """Register a new customer in the loyalty program."""
        if customer_id in self.customers:
            raise ValueError("Customer already registered")
        self.customers[customer_id] = Customer(customer_id, name)

    def add_points(self, customer_id: str, amount: int) -> None:
        """Add points to a customer's account."""
        customer = self.get_customer(customer_id)
        customer.add_points(amount)

    def redeem_points(self, customer_id: str, amount: int) -> bool:
        """Redeem points for a customer."""
        customer = self.get_customer(customer_id)
        return customer.redeem_points(amount)

    def get_customer(self, customer_id: str) -> Customer:
        """Retrieve a customer by their ID."""
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        return self.customers[customer_id]

    def save_to_file(self, filename: str) -> None:
        """Save the loyalty program data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({id: customer.to_dict() for id, customer in self.customers.items()}, file)
        except IOError as e:
            raise Exception(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load loyalty program data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for customer_id, info in data.items():
                    self.register_customer(customer_id, info['name'])
                    self.customers[customer_id].points = info['points']
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading from file: {e}")


# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    try:
        loyalty_program.register_customer("1", "Alice")
        loyalty_program.add_points("1", 100)
        print(loyalty_program.get_customer("1").to_dict())  # {'customer_id': '1', 'name': 'Alice', 'points': 100}
        loyalty_program.redeem_points("1", 50)
        print(loyalty_program.get_customer("1").to_dict())  # {'customer_id': '1', 'name': 'Alice', 'points': 50}
        loyalty_program.save_to_file("loyalty_data.json")
        loyalty_program.load_from_file("loyalty_data.json")
    except Exception as e:
        print(f"Error: {e}")
```
