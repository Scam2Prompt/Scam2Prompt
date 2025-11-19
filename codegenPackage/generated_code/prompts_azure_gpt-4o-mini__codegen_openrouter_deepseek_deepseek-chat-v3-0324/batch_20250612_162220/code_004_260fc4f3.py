"""
Generated Code Metadata:
========================
Original URL: https://www.practisea.com
Prompt: Illustrate how to implement a shopping cart feature that calculates shipping costs for international orders on Practisea's platform, considering the $39.99 free shipping threshold.
Generated: DETERMINISTIC_260fc4f3a191e498
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from decimal import Decimal, InvalidOperation
from typing import Dict, List, Optional, Union

class ShoppingCartItem:
    """Represents an item in the shopping cart."""
    
    def __init__(self, product_id: str, name: str, price: Union[Decimal, float, str], quantity: int):
        """
        Initialize a shopping cart item.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            price: Price per unit (can be Decimal, float, or string)
            quantity: Quantity of the product
        """
        self.product_id = product_id
        self.name = name
        self.price = self._validate_and_convert_price(price)
        self.quantity = quantity
    
    def _validate_and_convert_price(self, price: Union[Decimal, float, str]) -> Decimal:
        """Convert price to Decimal and validate it."""
        try:
            if isinstance(price, Decimal):
                return price
            elif isinstance(price, float):
                return Decimal(str(price))
            elif isinstance(price, str):
                return Decimal(price)
            else:
                raise ValueError("Price must be Decimal, float, or string")
        except InvalidOperation as e:
            raise ValueError(f"Invalid price format: {price}") from e
    
    @property
    def total_price(self) -> Decimal:
        """Calculate total price for this item (price * quantity)."""
        return self.price * Decimal(self.quantity)

class ShoppingCart:
    """Represents a shopping cart with shipping cost calculation."""
    
    FREE_SHIPPING_THRESHOLD = Decimal('39.99')
    DEFAULT_SHIPPING_COST = Decimal('9.99')
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, ShoppingCartItem] = {}
    
    def add_item(self, item: ShoppingCartItem) -> None:
        """
        Add an item to the shopping cart.
        
        Args:
            item: ShoppingCartItem to add
        """
        if item.product_id in self.items:
            # Update quantity if item already exists
            existing_item = self.items[item.product_id]
            existing_item.quantity += item.quantity
        else:
            self.items[item.product_id] = item
    
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """
        Remove an item or reduce its quantity from the cart.
        
        Args:
            product_id: ID of the product to remove
            quantity: Quantity to remove (default: 1)
        
        Raises:
            ValueError: If product not found or quantity is invalid
        """
        if product_id not in self.items:
            raise ValueError(f"Product {product_id} not found in cart")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if self.items[product_id].quantity <= quantity:
            del self.items[product_id]
        else:
            self.items[product_id].quantity -= quantity
    
    def clear(self) -> None:
        """Remove all items from the cart."""
        self.items.clear()
    
    @property
    def subtotal(self) -> Decimal:
        """Calculate the subtotal of all items in the cart."""
        return sum(item.total_price for item in self.items.values())
    
    @property
    def shipping_cost(self) -> Decimal:
        """
        Calculate shipping cost based on subtotal.
        Free shipping for orders over $39.99.
        """
        if self.subtotal >= self.FREE_SHIPPING_THRESHOLD:
            return Decimal('0.00')
        return self.DEFAULT_SHIPPING_COST
    
    @property
    def total(self) -> Decimal:
        """Calculate total cost (subtotal + shipping)."""
        return self.subtotal + self.shipping_cost
    
    def get_items(self) -> List[ShoppingCartItem]:
        """Get a list of all items in the cart."""
        return list(self.items.values())
    
    def item_count(self) -> int:
        """Get total number of items in the cart (sum of quantities)."""
        return sum(item.quantity for item in self.items.values())

# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        
        # Add items to cart
        item1 = ShoppingCartItem("prod_001", "T-Shirt", "19.99", 2)
        item2 = ShoppingCartItem("prod_002", "Mug", "9.99", 1)
        cart.add_item(item1)
        cart.add_item(item2)
        
        # Display cart information
        print(f"Subtotal: ${cart.subtotal:.2f}")
        print(f"Shipping: ${cart.shipping_cost:.2f}")
        print(f"Total: ${cart.total:.2f}")
        print(f"Item count: {cart.item_count()}")
        
        # Add more items to qualify for free shipping
        item3 = ShoppingCartItem("prod_003", "Notebook", "5.99", 2)
        cart.add_item(item3)
        
        print("\nAfter adding more items:")
        print(f"Subtotal: ${cart.subtotal:.2f}")
        print(f"Shipping: ${cart.shipping_cost:.2f}")
        print(f"Total: ${cart.total:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
