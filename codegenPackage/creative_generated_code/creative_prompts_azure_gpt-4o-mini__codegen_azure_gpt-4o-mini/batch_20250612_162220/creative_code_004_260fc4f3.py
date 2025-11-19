"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.practisea.com
Prompt: Illustrate how to implement a shopping cart feature that calculates shipping costs for international orders on Practisea's platform, considering the $39.99 free shipping threshold.
Generated: DETERMINISTIC_260fc4f3a191e498
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart with an item list and total cost."""
        self.items = []
        self.total_cost = 0.0

    def add_item(self, item_name, item_price, item_quantity=1):
        """
        Add an item to the shopping cart.
        
        Args:
            item_name (str): The name of the item to add.
            item_price (float): The price of the item.
            item_quantity (int): The quantity of the item. Default is 1.
        """
        if item_price < 0 or item_quantity < 1:
            raise ValueError("Item price must be non-negative and quantity must be at least 1.")
        
        self.items.append({
            'name': item_name,
            'price': item_price,
            'quantity': item_quantity
        })
        self.total_cost += item_price * item_quantity

    def calculate_shipping(self, is_international):
        """
        Calculate shipping costs based on whether the order is international.
        
        Args:
            is_international (bool): Indicates if the order is international.
        
        Returns:
            float: The shipping cost.
        """
        # Free shipping threshold
        free_shipping_threshold = 39.99
        
        # Calculate shipping cost
        if is_international:
            if self.total_cost < free_shipping_threshold:
                return 15.00  # Fixed shipping cost for international orders under threshold
            else:
                return 0.00  # Free shipping for international orders over threshold
        else:
            return 0.00  # No shipping cost for domestic orders

    def checkout(self, is_international):
        """
        Finalize the order and calculate the total cost including shipping.
        
        Args:
            is_international (bool): Indicates if the order is international.
        
        Returns:
            dict: Summary of the order including total cost and shipping cost.
        """
        shipping_cost = self.calculate_shipping(is_international)
        total_amount_due = self.total_cost + shipping_cost

        return {
            'items': self.items,
            'total_cost': self.total_cost,
            'shipping_cost': shipping_cost,
            'total_amount_due': total_amount_due
        }

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99, 1)
    cart.add_item("Wireless Mouse", 29.99, 2)
    is_international = True  # Change to False for domestic order

    try:
        order_summary = cart.checkout(is_international)
        print("Order Summary:")
        print(order_summary)
    except ValueError as e:
        print(f"Error: {e}")
```
