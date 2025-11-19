"""
Generated Code Metadata:
========================
Original URL: https://launchlawinc.com
Prompt: Write code to integrate an e-commerce shopping cart for DIY legal forms, referencing features like item count and total price, as described on the Launch Law website.
Generated: DETERMINISTIC_a598ce5115bdce36
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py
"""
E-commerce shopping cart implementation for DIY legal forms.
Features include:
- Adding/removing items
- Updating quantities
- Calculating totals
- Managing cart state
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
import json
from decimal import Decimal
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class LegalForm:
    """Represents a legal form product"""
    id: str
    name: str
    price: Decimal
    description: str = ""
    category: str = "legal_form"

class ShoppingCart:
    """Main shopping cart class"""
    
    def __init__(self):
        self.items: List[Dict] = []
        self._tax_rate = Decimal('0.10')  # 10% tax
    
    def add_item(self, product: LegalForm, quantity: int = 1) -> None:
        """Add item to cart or update quantity if already exists"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        for item in self.items:
            if item['product'].id == product.id:
                item['quantity'] += quantity
                logger.info(f"Updated quantity for {product.name}")
                return
        
        self.items.append({
            'product': product,
            'quantity': quantity
        })
        logger.info(f"Added {product.name} to cart")
    
    def remove_item(self, product_id: str) -> None:
        """Remove item from cart by product ID"""
        self.items = [item for item in self.items if item['product'].id != product_id]
        logger.info(f"Removed item {product_id} from cart")
    
    def update_quantity(self, product_id: str, quantity: int) -> None:
        """Update quantity for specific product"""
        if quantity <= 0:
            self.remove_item(product_id)
            return
        
        for item in self.items:
            if item['product'].id == product_id:
                item['quantity'] = quantity
                logger.info(f"Updated quantity for {product_id} to {quantity}")
                return
        
        raise ValueError(f"Product {product_id} not found in cart")
    
    @property
    def item_count(self) -> int:
        """Total number of items in cart (sum of quantities)"""
        return sum(item['quantity'] for item in self.items)
    
    @property
    def subtotal(self) -> Decimal:
        """Cart subtotal before tax"""
        return sum(
            Decimal(item['product'].price) * item['quantity'] 
            for item in self.items
        )
    
    @property
    def tax(self) -> Decimal:
        """Calculated tax amount"""
        return self.subtotal * self._tax_rate
    
    @property
    def total(self) -> Decimal:
        """Cart total including tax"""
        return self.subtotal + self.tax
    
    def clear(self) -> None:
        """Empty the cart"""
        self.items = []
        logger.info("Cart cleared")
    
    def to_json(self) -> str:
        """Serialize cart to JSON"""
        cart_data = {
            'items': [
                {
                    'product_id': item['product'].id,
                    'name': item['product'].name,
                    'price': str(item['product'].price),
                    'quantity': item['quantity']
                }
                for item in self.items
            ],
            'subtotal': str(self.subtotal),
            'tax': str(self.tax),
            'total': str(self.total)
        }
        return json.dumps(cart_data)
    
    @classmethod
    def from_json(cls, json_str: str, product_catalog: Dict[str, LegalForm]) -> 'ShoppingCart':
        """Deserialize cart from JSON"""
        cart_data = json.loads(json_str)
        cart = cls()
        
        for item_data in cart_data.get('items', []):
            product = product_catalog.get(item_data['product_id'])
            if product:
                cart.add_item(product, item_data['quantity'])
        
        return cart

# Example usage
if __name__ == "__main__":
    # Sample product catalog
    products = {
        "FORM-001": LegalForm(
            id="FORM-001",
            name="Last Will and Testament",
            price=Decimal("49.99"),
            description="Comprehensive will template"
        ),
        "FORM-002": LegalForm(
            id="FORM-002",
            name="Rental Agreement",
            price=Decimal("29.99"),
            description="Standard rental contract"
        )
    }
    
    # Create and use cart
    cart = ShoppingCart()
    cart.add_item(products["FORM-001"], 2)
    cart.add_item(products["FORM-002"])
    
    print(f"Item count: {cart.item_count}")
    print(f"Subtotal: ${cart.subtotal:.2f}")
    print(f"Tax: ${cart.tax:.2f}")
    print(f"Total: ${cart.total:.2f}")
    
    # Serialize/deserialize example
    cart_json = cart.to_json()
    print("\nCart JSON:")
    print(cart_json)
    
    new_cart = ShoppingCart.from_json(cart_json, products)
    print(f"\nDeserialized cart total: ${new_cart.total:.2f}")
```
