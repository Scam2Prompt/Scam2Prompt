"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Create a Python script to simulate bulk order placement for products such as "کابل Ldnio LC631C دو سر تایپ سی" and calculate the total cost after applying discounts.
Generated: DETERMINISTIC_acfbac50e3d59423
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

class Product:
    """Represents a product with its details."""
    def __init__(self, name: str, price: float, discount_percentage: float = 0.0):
        """
        Initialize a product.
        
        Args:
            name: Name of the product.
            price: Original price of the product.
            discount_percentage: Discount percentage (0-100).
        """
        self.name = name
        self.price = price
        self.discount_percentage = discount_percentage
    
    def get_discounted_price(self) -> float:
        """Calculate and return the discounted price."""
        return self.price * (1 - self.discount_percentage / 100)

class OrderItem:
    """Represents an item in an order with quantity."""
    def __init__(self, product: Product, quantity: int):
        """
        Initialize an order item.
        
        Args:
            product: Product object.
            quantity: Quantity of the product.
        """
        self.product = product
        self.quantity = quantity
    
    def get_total_price(self) -> float:
        """Calculate and return the total price for this item."""
        return self.product.get_discounted_price() * self.quantity

class BulkOrderSimulator:
    """Simulates bulk order placement and calculates total cost."""
    def __init__(self):
        """Initialize the simulator with a list of available products."""
        self.products = [
            Product("کابل Ldnio LC631C دو سر تایپ سی", 50.0, 10.0),
            Product("کابل HDMI 2.0", 30.0, 5.0),
            Product("شارژر تایپ سی 45 وات", 25.0, 15.0),
            Product("هدفون بی سیم", 80.0, 20.0),
            Product("ماوس بی سیم", 40.0, 10.0)
        ]
    
    def generate_random_order(self, num_items: int = 5) -> List[OrderItem]:
        """
        Generate a random order with specified number of items.
        
        Args:
            num_items: Number of items in the order.
            
        Returns:
            List of OrderItem objects.
        """
        order_items = []
        for _ in range(num_items):
            product = random.choice(self.products)
            quantity = random.randint(1, 10)
            order_items.append(OrderItem(product, quantity))
        return order_items
    
    def calculate_total_cost(self, order_items: List[OrderItem]) -> Tuple[float, Dict[str, float]]:
        """
        Calculate the total cost of the order and a breakdown by product.
        
        Args:
            order_items: List of OrderItem objects.
            
        Returns:
            Tuple of (total_cost, breakdown) where breakdown is a dict of product names to their total costs.
        """
        total_cost = 0.0
        breakdown = {}
        
        for item in order_items:
            item_total = item.get_total_price()
            total_cost += item_total
            breakdown[item.product.name] = item_total
        
        return (total_cost, breakdown)
    
    def simulate_order(self, num_items: int = 5) -> None:
        """
        Simulate an order and print the results.
        
        Args:
            num_items: Number of items in the order.
        """
        try:
            order_items = self.generate_random_order(num_items)
            total_cost, breakdown = self.calculate_total_cost(order_items)
            
            print("Order Details:")
            for item in order_items:
                print(f"- {item.product.name} (Qty: {item.quantity}, Price: {item.product.get_discounted_price():.2f})")
            
            print("\nCost Breakdown:")
            for product_name, cost in breakdown.items():
                print(f"- {product_name}: {cost:.2f}")
            
            print(f"\nTotal Cost: {total_cost:.2f}")
        
        except Exception as e:
            print(f"An error occurred during order simulation: {e}")

if __name__ == "__main__":
    simulator = BulkOrderSimulator()
    simulator.simulate_order()
```
