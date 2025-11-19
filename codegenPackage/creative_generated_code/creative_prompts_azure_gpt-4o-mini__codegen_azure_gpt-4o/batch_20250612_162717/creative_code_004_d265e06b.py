"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: What are the best practices for using PDC Brush's private label services in a retail setting? Provide a code example.
Generated: DETERMINISTIC_d265e06bd65bbd2e
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates best practices for managing products from PDC Brush's 
private label services in a retail setting.

Key functionalities:
1. Inventory Management
2. Product Labeling
3. Sales Tracking

The script adheres to production-ready standards with error handling, 
clean documentation, and scalability in mind.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="pdc_brush_retail.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class PDCBrushRetail:
    """
    Class to manage PDC Brush private label products in a retail setting.
    """

    def __init__(self):
        """
        Initialize the inventory dictionary and sales records.
        """
        self.inventory = {}  # {product_id: {'name': str, 'stock': int, 'price': float}}
        self.sales_records = []  # [{'product_id': str, 'quantity': int, 'total_price': float, 'timestamp': str}]

    def add_product(self, product_id, name, stock, price):
        """
        Add or update a product in the inventory.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            stock (int): Initial stock quantity.
            price (float): Price per unit.

        Raises:
            ValueError: If stock or price are negative.
        """
        if stock < 0 or price < 0:
            raise ValueError("Stock and price must be non-negative.")
        
        self.inventory[product_id] = {
            "name": name,
            "stock": stock,
            "price": price
        }
        logging.info(f"Product {name} (ID: {product_id}) added/updated in inventory.")

    def sell_product(self, product_id, quantity):
        """
        Sell a product and update inventory and sales records.

        Args:
            product_id (str): ID of the product to sell.
            quantity (int): Quantity to sell.

        Raises:
            ValueError: If the product does not exist or if there is insufficient stock.
        """
        if product_id not in self.inventory:
            raise ValueError("Product not found in inventory.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if self.inventory[product_id]["stock"] < quantity:
            raise ValueError("Insufficient stock available.")

        # Update inventory
        self.inventory[product_id]["stock"] -= quantity
        total_price = self.inventory[product_id]["price"] * quantity

        # Record the sale
        self.sales_records.append({
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price,
            "timestamp": datetime.now().isoformat()
        })

        logging.info(f"Sold {quantity} units of {self.inventory[product_id]['name']} (ID: {product_id}).")
        return total_price

    def generate_sales_report(self):
        """
        Generate a sales report in JSON format.

        Returns:
            str: Sales report as a JSON string.
        """
        report = json.dumps(self.sales_records, indent=4)
        logging.info("Sales report generated.")
        return report

    def check_inventory(self):
        """
        Check the current inventory.

        Returns:
            dict: Current inventory.
        """
        logging.info("Inventory checked.")
        return self.inventory


# Example usage
if __name__ == "__main__":
    try:
        # Initialize PDC Brush retail system
        retail_system = PDCBrushRetail()

        # Add products
        retail_system.add_product("BR001", "Premium Hair Brush", 100, 15.99)
        retail_system.add_product("BR002", "Detangling Brush", 50, 12.49)

        # Sell products
        total_price = retail_system.sell_product("BR001", 2)
        print(f"Total price for sale: ${total_price:.2f}")

        # Check inventory
        inventory = retail_system.check_inventory()
        print("Current Inventory:")
        print(json.dumps(inventory, indent=4))

        # Generate sales report
        report = retail_system.generate_sales_report()
        print("Sales Report:")
        print(report)

    except ValueError as e:
        logging.error(f"ValueError: {str(e)}")
        print(f"Error: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        print(f"Unexpected error occurred: {str(e)}")
```
