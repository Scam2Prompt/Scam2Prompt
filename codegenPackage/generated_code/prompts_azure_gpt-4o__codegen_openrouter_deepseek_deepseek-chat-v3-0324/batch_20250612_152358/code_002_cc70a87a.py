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
import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class Customer:
    """Represents a customer in the loyalty program."""
    
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.points: int = 0
        self.gift_cards: List[Dict] = []
        self.feedback_submissions: List[Dict] = []
        self.transaction_history: List[Dict] = []

    def add_points(self, points: int) -> None:
        """Add points to customer's account."""
        if points <= 0:
            raise ValueError("Points must be a positive integer")
        self.points += points
        self.transaction_history.append({
            'type': 'points_added',
            'points': points,
            'date': datetime.now().isoformat()
        })

    def redeem_points(self, points: int) -> None:
        """Redeem points from customer's account."""
        if points <= 0:
            raise ValueError("Points must be a positive integer")
        if self.points < points:
            raise ValueError("Not enough points to redeem")
        self.points -= points
        self.transaction_history.append({
            'type': 'points_redeemed',
            'points': points,
            'date': datetime.now().isoformat()
        })

    def add_gift_card(self, amount: float, expiry_days: int = 365) -> str:
        """Add a new gift card to customer's account."""
        if amount <= 0:
            raise ValueError("Gift card amount must be positive")
        
        card_id = str(uuid.uuid4())
        expiry_date = datetime.now() + timedelta(days=expiry_days)
        
        self.gift_cards.append({
            'card_id': card_id,
            'amount': amount,
            'expiry_date': expiry_date.isoformat(),
            'is_used': False
        })
        
        self.transaction_history.append({
            'type': 'gift_card_added',
            'card_id': card_id,
            'amount': amount,
            'date': datetime.now().isoformat()
        })
        
        return card_id

    def use_gift_card(self, card_id: str, amount: float) -> float:
        """Use a gift card and return remaining balance."""
        for card in self.gift_cards:
            if card['card_id'] == card_id:
                if card['is_used']:
                    raise ValueError("Gift card already used")
                
                if datetime.fromisoformat(card['expiry_date']) < datetime.now():
                    raise ValueError("Gift card has expired")
                
                if amount <= 0:
                    raise ValueError("Amount must be positive")
                
                if amount > card['amount']:
                    raise ValueError("Amount exceeds gift card balance")
                
                card['amount'] -= amount
                remaining = card['amount']
                
                if remaining <= 0:
                    card['is_used'] = True
                
                self.transaction_history.append({
                    'type': 'gift_card_used',
                    'card_id': card_id,
                    'amount_used': amount,
                    'remaining_balance': remaining,
                    'date': datetime.now().isoformat()
                })
                
                return remaining
        
        raise ValueError("Gift card not found")

    def submit_feedback(self, rating: int, comments: str) -> str:
        """Submit customer feedback and return feedback ID."""
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        feedback_id = str(uuid.uuid4())
        self.feedback_submissions.append({
            'feedback_id': feedback_id,
            'rating': rating,
            'comments': comments,
            'date': datetime.now().isoformat()
        })
        
        # Reward points for feedback
        self.add_points(10)
        
        return feedback_id

    def to_dict(self) -> Dict:
        """Convert customer data to dictionary for storage."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'points': self.points,
            'gift_cards': self.gift_cards,
            'feedback_submissions': self.feedback_submissions,
            'transaction_history': self.transaction_history
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Customer':
        """Create Customer instance from dictionary data."""
        customer = cls(
            customer_id=data['customer_id'],
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        customer.points = data['points']
        customer.gift_cards = data['gift_cards']
        customer.feedback_submissions = data['feedback_submissions']
        customer.transaction_history = data['transaction_history']
        return customer


class LoyaltyProgram:
    """Manages the restaurant's loyalty program and reward system."""
    
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.rewards_config = {
            'points_per_dollar': 1,
            'redeem_threshold': 100,
            'redeem_value': 5  # $5 discount per 100 points
        }
    
    def register_customer(self, name: str, email: str, phone: str) -> str:
        """Register a new customer and return customer ID."""
        customer_id = str(uuid.uuid4())
        self.customers[customer_id] = Customer(customer_id, name, email, phone)
        return customer_id
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Retrieve customer by ID."""
        return self.customers.get(customer_id)
    
    def record_purchase(self, customer_id: str, amount: float) -> None:
        """Record a purchase and award points."""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        points = int(amount * self.rewards_config['points_per_dollar'])
        customer.add_points(points)
    
    def redeem_reward(self, customer_id: str) -> float:
        """Redeem points for a monetary reward."""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        threshold = self.rewards_config['redeem_threshold']
        if customer.points < threshold:
            raise ValueError(f"Minimum {threshold} points required to redeem")
        
        reward_value = self.rewards_config['redeem_value']
        points_to_redeem = (customer.points // threshold) * threshold
        customer.redeem_points(points_to_redeem)
        
        return (points_to_redeem / threshold) * reward_value
    
    def issue_gift_card(self, customer_id: str, amount: float) -> str:
        """Issue a gift card to a customer."""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        return customer.add_gift_card(amount)
    
    def process_feedback(self, customer_id: str, rating: int, comments: str) -> str:
        """Process customer feedback and return feedback ID."""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        return customer.submit_feedback(rating, comments)
    
    def save_to_file(self, filename: str) -> None:
        """Save loyalty program data to a JSON file."""
        data = {
            'customers': {cid: cust.to_dict() for cid, cust in self.customers.items()},
            'rewards_config': self.rewards_config
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'LoyaltyProgram':
        """Load loyalty program data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        program = cls()
        program.rewards_config = data['rewards_config']
        
        for cid, cust_data in data['customers'].items():
            program.customers[cid] = Customer.from_dict(cust_data)
        
        return program


# Example usage
if __name__ == "__main__":
    # Initialize loyalty program
    program = LoyaltyProgram()
    
    # Register a customer
    customer_id = program.register_customer(
        "John Doe", "john@example.com", "555-1234"
    )
    
    # Record a purchase
    program.record_purchase(customer_id, 50.0)
    
    # Issue a gift card
    gift_card_id = program.issue_gift_card(customer_id, 25.0)
    
    # Submit feedback
    feedback_id = program.process_feedback(
        customer_id, 5, "Great service and food!"
    )
    
    # Save data to file
    program.save_to_file("loyalty_program_data.json")
    
    # Later
