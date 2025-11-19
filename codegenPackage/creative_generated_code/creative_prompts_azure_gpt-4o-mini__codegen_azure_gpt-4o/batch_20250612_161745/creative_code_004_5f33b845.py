"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Illustrate how to implement a discount feature in a shopping cart application, taking cues from the 5% discount offer mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_5f33b8453faf8005
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

# Import required libraries
from typing import List

class Item:
    """
    Represents an item in the shopping cart.
    """
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class ShoppingCart:
    """
    Represents a shopping cart that can calculate total cost and apply discounts.
    """
    def __init__(self):
        # Initialize an empty cart
        self.items: List[Item] = []
    
    def add_item(self, name: str, price: float, quantity: int):
        """
        Adds an item to the shopping cart.
        
        :param name: Name of the item.
        :param price: Price of the item.
        :param quantity: Quantity of the item.
        :raises ValueError: If price or quantity is invalid.
        """
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be non-negative and quantity must be positive.")
        
        self.items.append(Item(name, price, quantity))
    
    def calculate_total(self) -> float:
        """
        Calculates the total cost of all items in the cart.
        
        :return: Total cost.
        """
        return sum(item.price * item.quantity for item in self.items)
    
    def apply_discount(self, discount_percentage: float) -> float:
        """
        Applies discount to the total cost.
        
        :param discount_percentage: Discount percentage to be applied.
        :return: Total cost after applying discount.
        :raises ValueError: If discount percentage is invalid.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        total = self.calculate_total()
        discount = total * (discount_percentage / 100)
        return total - discount
    
    def print_receipt(self):
        """
        Prints a detailed receipt of the shopping cart.
        """
        print("Receipt:")
        print("---------")
        for item in self.items:
            print(f"{item.name} - ${item.price:.2f} x {item.quantity} = ${item.price * item.quantity:.2f}")
        
        total = self.calculate_total()
        print(f"Subtotal: ${total:.2f}")
        
        # Apply a 5% discount (specific to request)
        discounted_total = self.apply_discount(5)
        print(f"Discounted Total (5% off): ${discounted_total:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()
        
        # Add items to the cart
        cart.add_item("Laptop", 1000.00, 1)
        cart.add_item("Headphones", 50.00, 2)
        cart.add_item("Mouse", 25.00, 1)
        
        # Print the receipt
        cart.print_receipt()
    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
```
