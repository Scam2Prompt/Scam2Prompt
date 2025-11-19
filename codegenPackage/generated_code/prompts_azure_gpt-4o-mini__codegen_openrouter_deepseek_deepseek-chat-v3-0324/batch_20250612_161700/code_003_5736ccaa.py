"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: Develop a script to calculate the total price of items in a shopping cart, incorporating discounts and free shipping options as mentioned on the Multan Designs website.
Generated: DETERMINISTIC_5736ccaa49676ffc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Union

class ShoppingCart:
    """
    A class to represent a shopping cart with items, discounts, and shipping options.
    
    Attributes:
        items (List[Dict]): List of items in the cart, each with 'name', 'price', and 'quantity'.
        discount_code (str): Discount code applied to the cart.
        shipping_option (str): Shipping option selected ('standard', 'express', 'free').
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
        self.discount_code = None
        self.shipping_option = 'standard'
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the shopping cart.
        
        Args:
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int, optional): Quantity of the item. Defaults to 1.
            
        Raises:
            ValueError: If price or quantity is not positive.
        """
        if price <= 0:
            raise ValueError("Price must be positive.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def apply_discount(self, discount_code: str) -> None:
        """
        Apply a discount code to the cart.
        
        Args:
            discount_code (str): Discount code to apply.
        """
        self.discount_code = discount_code
    
    def set_shipping_option(self, shipping_option: str) -> None:
        """
        Set the shipping option for the cart.
        
        Args:
            shipping_option (str): Shipping option ('standard', 'express', 'free').
            
        Raises:
            ValueError: If shipping option is invalid.
        """
        valid_options = ['standard', 'express', 'free']
        if shipping_option not in valid_options:
            raise ValueError(f"Invalid shipping option. Must be one of: {valid_options}")
        self.shipping_option = shipping_option
    
    def calculate_subtotal(self) -> float:
        """
        Calculate the subtotal of all items in the cart.
        
        Returns:
            float: Subtotal before discounts and shipping.
        """
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def calculate_discount(self, subtotal: float) -> float:
        """
        Calculate the discount amount based on the discount code.
        
        Args:
            subtotal (float): Subtotal before discounts.
            
        Returns:
            float: Discount amount.
        """
        if not self.discount_code:
            return 0.0
        
        # Define discount rules (could be loaded from a database or config file)
        discount_rules = {
            'SAVE10': 0.10,  # 10% off
            'SAVE20': 0.20,  # 20% off
            'FREESHIP': 0.0,  # Free shipping only
        }
        
        discount_percent = discount_rules.get(self.discount_code, 0.0)
        return subtotal * discount_percent
    
    def calculate_shipping(self, subtotal: float) -> float:
        """
        Calculate the shipping cost based on the shipping option and subtotal.
        
        Args:
            subtotal (float): Subtotal before shipping.
            
        Returns:
            float: Shipping cost.
        """
        if self.shipping_option == 'free':
            return 0.0
        
        # Free shipping for orders over $50
        if subtotal >= 50.0:
            return 0.0
        
        shipping_costs = {
            'standard': 5.0,
            'express': 10.0,
        }
        return shipping_costs.get(self.shipping_option, 0.0)
    
    def calculate_total(self) -> Dict[str, Union[float, str]]:
        """
        Calculate the total price of the cart including discounts and shipping.
        
        Returns:
            Dict[str, Union[float, str]]: A dictionary containing subtotal, discount, shipping, and total.
        """
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        
        # Apply discount to subtotal
        discounted_subtotal = subtotal - discount
        
        shipping = self.calculate_shipping(discounted_subtotal)
        total = discounted_subtotal + shipping
        
        return {
            'subtotal': subtotal,
            'discount': discount,
            'shipping': shipping,
            'total': total,
            'discount_code': self.discount_code,
            'shipping_option': self.shipping_option
        }
    
    def to_json(self) -> str:
        """
        Convert the cart and its calculations to a JSON string.
        
        Returns:
            str: JSON representation of the cart and totals.
        """
        cart_data = {
            'items': self.items,
            'discount_code': self.discount_code,
            'shipping_option': self.shipping_option,
            'totals': self.calculate_total()
        }
        return json.dumps(cart_data, indent=2)

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("T-Shirt", 25.0, 2)
    cart.add_item("Jeans", 45.0)
    cart.apply_discount("SAVE10")
    cart.set_shipping_option("standard")
    
    print(cart.to_json())
```
