"""
Generated Code Metadata:
========================
Original URL: https://medebooks.shop
Prompt: Write Python code to create a shopping cart system for an e-commerce website that sells medical books and courses, similar to medebooks.shop, including features like applying discount coupons and calculating final prices.
Generated: DETERMINISTIC_87790f235755aaae
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union

class Product:
    """Represents a product in the shopping cart."""
    
    def __init__(self, id: str, name: str, price: float, product_type: str):
        """
        Initialize a product.
        
        Args:
            id: Unique identifier for the product.
            name: Name of the product.
            price: Price of the product.
            product_type: Type of product ('book' or 'course').
        """
        self.id = id
        self.name = name
        self.price = price
        self.product_type = product_type
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'product_type': self.product_type
        }

class DiscountCoupon:
    """Represents a discount coupon."""
    
    def __init__(self, code: str, discount_percent: float, min_purchase: float = 0):
        """
        Initialize a discount coupon.
        
        Args:
            code: Coupon code.
            discount_percent: Discount percentage (0-100).
            min_purchase: Minimum purchase amount to apply the coupon.
        """
        self.code = code
        self.discount_percent = discount_percent
        self.min_purchase = min_purchase
    
    def is_valid(self, subtotal: float) -> bool:
        """
        Check if the coupon is valid for the given subtotal.
        
        Args:
            subtotal: Subtotal amount.
            
        Returns:
            bool: True if coupon is valid, False otherwise.
        """
        return subtotal >= self.min_purchase
    
    def apply_discount(self, amount: float) -> float:
        """
        Apply discount to the given amount.
        
        Args:
            amount: Amount to apply discount to.
            
        Returns:
            float: Discounted amount.
        """
        return amount * (1 - self.discount_percent / 100)

class ShoppingCart:
    """Represents a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, Product] = {}
        self.coupon: Optional[DiscountCoupon] = None
    
    def add_item(self, product: Product) -> None:
        """
        Add a product to the cart.
        
        Args:
            product: Product to add.
        """
        if product.id in self.items:
            raise ValueError(f"Product with ID {product.id} already in cart.")
        self.items[product.id] = product
    
    def remove_item(self, product_id: str) -> None:
        """
        Remove a product from the cart.
        
        Args:
            product_id: ID of the product to remove.
        """
        if product_id not in self.items:
            raise ValueError(f"Product with ID {product_id} not found in cart.")
        del self.items[product_id]
    
    def apply_coupon(self, coupon: DiscountCoupon) -> None:
        """
        Apply a discount coupon to the cart.
        
        Args:
            coupon: Discount coupon to apply.
        """
        self.coupon = coupon
    
    def remove_coupon(self) -> None:
        """Remove the current coupon from the cart."""
        self.coupon = None
    
    def calculate_subtotal(self) -> float:
        """
        Calculate the subtotal of the cart.
        
        Returns:
            float: Subtotal amount.
        """
        return sum(product.price for product in self.items.values())
    
    def calculate_total(self) -> float:
        """
        Calculate the total amount after applying discounts.
        
        Returns:
            float: Total amount.
        """
        subtotal = self.calculate_subtotal()
        if self.coupon and self.coupon.is_valid(subtotal):
            return self.coupon.apply_discount(subtotal)
        return subtotal
    
    def get_cart_summary(self) -> Dict:
        """
        Get a summary of the cart contents.
        
        Returns:
            Dict: Cart summary including items, subtotal, discount, and total.
        """
        subtotal = self.calculate_subtotal()
        discount = 0
        if self.coupon and self.coupon.is_valid(subtotal):
            discount = subtotal - self.coupon.apply_discount(subtotal)
        total = subtotal - discount
        
        return {
            'items': [product.to_dict() for product in self.items.values()],
            'subtotal': subtotal,
            'discount': discount,
            'total': total,
            'coupon_applied': self.coupon.code if self.coupon else None
        }

# Example usage
if __name__ == "__main__":
    # Create some products
    book1 = Product("B001", "Medical Book 1", 50.00, "book")
    book2 = Product("B002", "Medical Book 2", 75.00, "book")
    course1 = Product("C001", "Medical Course 1", 200.00, "course")
    
    # Create a coupon
    coupon = DiscountCoupon("SAVE20", 20, 100)
    
    # Initialize cart
    cart = ShoppingCart()
    
    # Add items to cart
    cart.add_item(book1)
    cart.add_item(book2)
    cart.add_item(course1)
    
    # Apply coupon
    cart.apply_coupon(coupon)
    
    # Get cart summary
    summary = cart.get_cart_summary()
    print(json.dumps(summary, indent=2))
```
