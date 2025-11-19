"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Generate code for a shopping cart system tailored for a creative commerce platform, referencing Kroo Nation's marketplace features inspired by Onlyfans British, Czech, Irish, and Danske models.
Generated: DETERMINISTIC_135d0d1ba566a659
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py
# A shopping cart system for a creative commerce platform inspired by Kroo Nation's marketplace features.

from typing import List, Dict, Optional
import uuid
from datetime import datetime
from enum import Enum
import json

class Currency(Enum):
    """Supported currencies for the platform."""
    GBP = "GBP"  # British Pound
    CZK = "CZK"  # Czech Koruna
    EUR = "EUR"  # Euro (used by Ireland)
    DKK = "DKK"  # Danish Krone

class CartItem:
    """Represents an item in the shopping cart."""
    
    def __init__(self, product_id: str, name: str, price: float, currency: Currency, quantity: int = 1):
        """
        Initialize a cart item.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            price: Price per unit
            currency: Currency for the price
            quantity: Quantity of the product (default 1)
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.currency = currency
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert cart item to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'currency': self.currency.value,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'CartItem':
        """Create cart item from dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            currency=Currency(data['currency']),
            quantity=data['quantity']
        )

class ShoppingCart:
    """Main shopping cart class handling cart operations."""
    
    def __init__(self, user_id: str, currency: Currency = Currency.GBP):
        """
        Initialize a shopping cart.
        
        Args:
            user_id: Unique identifier for the user
            currency: Default currency for the cart (default GBP)
        """
        self.cart_id = str(uuid.uuid4())
        self.user_id = user_id
        self.currency = currency
        self.items: List[CartItem] = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def add_item(self, item: CartItem) -> None:
        """Add an item to the cart or update quantity if already exists."""
        if item.currency != self.currency:
            raise ValueError(f"Item currency {item.currency} doesn't match cart currency {self.currency}")
        
        for existing_item in self.items:
            if existing_item.product_id == item.product_id:
                existing_item.quantity += item.quantity
                self.updated_at = datetime.utcnow()
                return
        
        self.items.append(item)
        self.updated_at = datetime.utcnow()
    
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """
        Remove an item from the cart or reduce quantity.
        
        Args:
            product_id: ID of the product to remove
            quantity: Quantity to remove (default 1)
        """
        for index, item in enumerate(self.items):
            if item.product_id == product_id:
                if item.quantity <= quantity:
                    self.items.pop(index)
                else:
                    item.quantity -= quantity
                self.updated_at = datetime.utcnow()
                return
        raise ValueError(f"Product with ID {product_id} not found in cart")
    
    def clear_cart(self) -> None:
        """Remove all items from the cart."""
        self.items = []
        self.updated_at = datetime.utcnow()
    
    def get_total(self) -> float:
        """Calculate the total price of all items in the cart."""
        return sum(item.price * item.quantity for item in self.items)
    
    def get_item_count(self) -> int:
        """Get the total number of items in the cart."""
        return sum(item.quantity for item in self.items)
    
    def to_dict(self) -> Dict:
        """Convert cart to dictionary for serialization."""
        return {
            'cart_id': self.cart_id,
            'user_id': self.user_id,
            'currency': self.currency.value,
            'items': [item.to_dict() for item in self.items],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'total': self.get_total(),
            'item_count': self.get_item_count()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ShoppingCart':
        """Create cart from dictionary."""
        cart = cls(
            user_id=data['user_id'],
            currency=Currency(data['currency'])
        )
        cart.cart_id = data['cart_id']
        cart.created_at = datetime.fromisoformat(data['created_at'])
        cart.updated_at = datetime.fromisoformat(data['updated_at'])
        cart.items = [CartItem.from_dict(item) for item in data['items']]
        return cart
    
    def save_to_file(self, filename: str) -> None:
        """Save cart to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'ShoppingCart':
        """Load cart from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)

class PaymentProcessor:
    """Handles payment processing for the shopping cart."""
    
    @staticmethod
    def process_payment(cart: ShoppingCart, payment_details: Dict) -> Dict:
        """
        Process payment for the cart contents.
        
        Args:
            cart: ShoppingCart instance
            payment_details: Dictionary containing payment details
            
        Returns:
            Dictionary containing payment status and transaction details
        """
        # In a real implementation, this would interface with a payment gateway
        # This is a mock implementation
        
        if not cart.items:
            raise ValueError("Cannot process payment for empty cart")
        
        total = cart.get_total()
        
        # Mock payment processing
        transaction_id = str(uuid.uuid4())
        
        return {
            'status': 'success',
            'transaction_id': transaction_id,
            'amount': total,
            'currency': cart.currency.value,
            'timestamp': datetime.utcnow().isoformat(),
            'items': [item.to_dict() for item in cart.items]
        }

# Example usage
if __name__ == "__main__":
    # Create a cart
    cart = ShoppingCart(user_id="user123", currency=Currency.GBP)
    
    # Add items
    item1 = CartItem(
        product_id="prod1",
        name="Digital Artwork",
        price=19.99,
        currency=Currency.GBP,
        quantity=2
    )
    cart.add_item(item1)
    
    item2 = CartItem(
        product_id="prod2",
        name="Exclusive Content",
        price=9.99,
        currency=Currency.GBP
    )
    cart.add_item(item2)
    
    # Print cart details
    print(json.dumps(cart.to_dict(), indent=2))
    
    # Process payment
    try:
        payment_result = PaymentProcessor.process_payment(
            cart,
            payment_details={"card_number": "4111111111111111", "expiry": "12/25"}
        )
        print("\nPayment Result:")
        print(json.dumps(payment_result, indent=2))
        
        # Clear cart after successful payment
        cart.clear_cart()
    except Exception as e:
        print(f"Payment failed: {str(e)}")
```
