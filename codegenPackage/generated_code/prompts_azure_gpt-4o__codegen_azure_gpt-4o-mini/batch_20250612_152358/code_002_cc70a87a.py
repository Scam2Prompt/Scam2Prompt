"""
Generated Code Metadata:
========================
Original URL: https://startupsadvisory.com
Prompt: Generate Python code to implement a restaurant loyalty program and reward system, incorporating gift cards and feedback forms as detailed on StartUp Advisory.
Generated: DETERMINISTIC_cc70a87a8e266427
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta

class Customer:
    """Class representing a customer in the loyalty program."""
    
    def __init__(self, name, email):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.points = 0
        self.gift_cards = []
        self.feedbacks = []

    def add_points(self, points):
        """Add loyalty points to the customer's account."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points

    def redeem_points(self, points):
        """Redeem loyalty points for rewards."""
        if points > self.points:
            raise ValueError("Insufficient points to redeem.")
        self.points -= points

    def add_gift_card(self, gift_card):
        """Add a gift card to the customer's account."""
        self.gift_cards.append(gift_card)

    def submit_feedback(self, feedback):
        """Submit feedback for the restaurant."""
        self.feedbacks.append(feedback)

class GiftCard:
    """Class representing a gift card."""
    
    def __init__(self, amount):
        self.card_id = str(uuid.uuid4())
        self.amount = amount
        self.expiry_date = datetime.now() + timedelta(days=365)  # 1 year validity

    def is_valid(self):
        """Check if the gift card is still valid."""
        return datetime.now() < self.expiry_date

class LoyaltyProgram:
    """Class to manage the loyalty program."""
    
    def __init__(self):
        self.customers = {}

    def register_customer(self, name, email):
        """Register a new customer in the loyalty program."""
        if email in self.customers:
            raise ValueError("Customer with this email already exists.")
        customer = Customer(name, email)
        self.customers[email] = customer
        return customer

    def get_customer(self, email):
        """Retrieve a customer by email."""
        return self.customers.get(email)

    def issue_gift_card(self, email, amount):
        """Issue a gift card to a customer."""
        customer = self.get_customer(email)
        if not customer:
            raise ValueError("Customer not found.")
        gift_card = GiftCard(amount)
        customer.add_gift_card(gift_card)
        return gift_card

    def add_loyalty_points(self, email, points):
        """Add loyalty points to a customer's account."""
        customer = self.get_customer(email)
        if not customer:
            raise ValueError("Customer not found.")
        customer.add_points(points)

    def redeem_loyalty_points(self, email, points):
        """Redeem loyalty points for a customer."""
        customer = self.get_customer(email)
        if not customer:
            raise ValueError("Customer not found.")
        customer.redeem_points(points)

    def collect_feedback(self, email, feedback):
        """Collect feedback from a customer."""
        customer = self.get_customer(email)
        if not customer:
            raise ValueError("Customer not found.")
        customer.submit_feedback(feedback)

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Register a new customer
    try:
        customer = loyalty_program.register_customer("John Doe", "john@example.com")
        print(f"Registered customer: {customer.name} with ID: {customer.customer_id}")
        
        # Add loyalty points
        loyalty_program.add_loyalty_points("john@example.com", 100)
        print(f"Points after adding: {customer.points}")
        
        # Issue a gift card
        gift_card = loyalty_program.issue_gift_card("john@example.com", 50)
        print(f"Issued gift card with ID: {gift_card.card_id} and amount: {gift_card.amount}")
        
        # Submit feedback
        loyalty_program.collect_feedback("john@example.com", "Great service!")
        print(f"Feedback submitted: {customer.feedbacks[-1]}")
        
        # Redeem points
        loyalty_program.redeem_loyalty_points("john@example.com", 50)
        print(f"Points after redeeming: {customer.points}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
