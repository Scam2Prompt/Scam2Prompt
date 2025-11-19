"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tallhills.com
Prompt: Provide an example of how to use experience design to improve customer engagement in a retail environment, as outlined by TallHills.
Generated: DETERMINISTIC_3d268879a9f33444
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import random
from datetime import datetime

class Customer:
    """Represents a customer in the retail environment."""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.visits = []  # List to track customer visits

    def add_visit(self, visit):
        """Records a visit to the store."""
        self.visits.append(visit)

class Store:
    """Represents the retail store."""
    def __init__(self, name):
        self.name = name
        self.customers = []  # List of customers
        self.promotions = []  # List of promotions

    def add_customer(self, customer):
        """Adds a customer to the store."""
        self.customers.append(customer)

    def add_promotion(self, promotion):
        """Adds a promotion to the store."""
        self.promotions.append(promotion)

    def engage_customer(self, customer):
        """Engages the customer based on their visit history."""
        # Check for the last visit date
        if customer.visits:
            last_visit = max(customer.visits)
            days_since_last_visit = (datetime.now() - last_visit).days
            
            # Engage customer based on days since last visit
            if days_since_last_visit > 30:
                return f"Hey {customer.name}, we miss you! Check out our new arrivals!"
            elif days_since_last_visit > 7:
                return f"Hi {customer.name}, welcome back! Enjoy a special discount on your next purchase."
            else:
                return f"Welcome back, {customer.name}! Thanks for visiting us again!"
        else:
            return f"Welcome to {self.name}, {customer.name}! Enjoy your shopping experience!"            

class Promotion:
    """Represents a promotion in the store."""
    def __init__(self, description, discount):
        self.description = description
        self.discount = discount

def main():
    """Main function to demonstrate customer engagement in a retail environment."""
    # Create a store instance
    store = Store("TallHills Retail")

    # Create customers
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    # Simulate customer visits
    customer1.add_visit(datetime.now())  # Recent visit
    customer2.add_visit(datetime.now())  # Recent visit

    # Simulate a promotion
    store.add_promotion(Promotion("20% off on all items", 20))

    # Engage customers
    print(store.engage_customer(customer1))
    print(store.engage_customer(customer2))

    # Simulate a customer returning after a long absence
    customer1.add_visit(datetime.now().replace(year=datetime.now().year - 1))  # Last visit over a month ago
    print(store.engage_customer(customer1))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
