"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Develop a supply chain management system for PDC Brush, taking into account their commitment to sustainable practices and responsible sourcing.
Generated: DETERMINISTIC_0bcfbd702fee93a4
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python implementation of a supply chain management system for PDC Brush, focusing on sustainable practices and responsible sourcing.

```python
import json
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    filename='supply_chain.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SupplyChainManagement:
    """
    A class to manage the supply chain for PDC Brush, ensuring sustainable practices and responsible sourcing.
    """

    def __init__(self):
        """
        Initialize the supply chain management system with empty data structures.
        """
        self.suppliers = {}  # Dictionary to store supplier information
        self.inventory = {}  # Dictionary to store inventory details
        self.orders = []     # List to store orders

    def add_supplier(self, supplier_id, name, sustainability_score, materials):
        """
        Add a new supplier to the system.

        :param supplier_id: Unique identifier for the supplier
        :param name: Name of the supplier
        :param sustainability_score: A score representing the supplier's commitment to sustainability
        :param materials: List of materials provided by the supplier
        """
        if supplier_id in self.suppliers:
            logging.warning(f"Supplier ID {supplier_id} already exists.")
            raise ValueError("Supplier ID already exists.")
        
        self.suppliers[supplier_id] = {
            "name": name,
            "sustainability_score": sustainability_score,
            "materials": materials
        }
        logging.info(f"Added supplier: {name} with ID {supplier_id}.")

    def add_inventory_item(self, item_id, name, quantity, supplier_id):
        """
        Add a new inventory item to the system.

        :param item_id: Unique identifier for the inventory item
        :param name: Name of the inventory item
        :param quantity: Quantity of the item in stock
        :param supplier_id: ID of the supplier providing the item
        """
        if item_id in self.inventory:
            logging.warning(f"Item ID {item_id} already exists in inventory.")
            raise ValueError("Item ID already exists in inventory.")
        
        if supplier_id not in self.suppliers:
            logging.warning(f"Supplier ID {supplier_id} does not exist.")
            raise ValueError("Supplier ID does not exist.")
        
        self.inventory[item_id] = {
            "name": name,
            "quantity": quantity,
            "supplier_id": supplier_id
        }
        logging.info(f"Added inventory item: {name} with ID {item_id}.")

    def place_order(self, order_id, item_id, quantity):
        """
        Place an order for an inventory item.

        :param order_id: Unique identifier for the order
        :param item_id: ID of the inventory item to order
        :param quantity: Quantity of the item to order
        """
        if item_id not in self.inventory:
            logging.warning(f"Item ID {item_id} does not exist in inventory.")
            raise ValueError("Item ID does not exist in inventory.")
        
        if self.inventory[item_id]["quantity"] < quantity:
            logging.warning(f"Insufficient stock for item ID {item_id}.")
            raise ValueError("Insufficient stock for the requested quantity.")
        
        self.inventory[item_id]["quantity"] -= quantity
        order = {
            "order_id": order_id,
            "item_id": item_id,
            "quantity": quantity,
            "timestamp": datetime.now().isoformat()
        }
        self.orders.append(order)
        logging.info(f"Placed order ID {order_id} for item ID {item_id}.")

    def generate_report(self):
        """
        Generate a report of suppliers, inventory, and orders.

        :return: A dictionary containing the report data
        """
        report = {
            "suppliers": self.suppliers,
            "inventory": self.inventory,
            "orders": self.orders
        }
        logging.info("Generated supply chain report.")
        return report

    def save_report_to_file(self, filename):
        """
        Save the supply chain report to a JSON file.

        :param filename: Name of the file to save the report
        """
        report = self.generate_report()
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            logging.info(f"Report saved to file: {filename}.")
        except Exception as e:
            logging.error(f"Failed to save report to file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Add suppliers
    scm.add_supplier("S001", "EcoBrush Supplies", 95, ["Bamboo", "Recycled Plastic"])
    scm.add_supplier("S002", "Green Materials Co.", 90, ["Wood", "Biodegradable Fibers"])

    # Add inventory items
    scm.add_inventory_item("I001", "Bamboo Handle", 100, "S001")
    scm.add_inventory_item("I002", "Recycled Plastic Bristles", 200, "S001")
    scm.add_inventory_item("I003", "Wood Handle", 150, "S002")

    # Place orders
    scm.place_order("O001", "I001", 20)
    scm.place_order("O002", "I002", 50)

    # Generate and save report
    report = scm.generate_report()
    print(json.dumps(report, indent=4))  # Print report to console
    scm.save_report_to_file("supply_chain_report.json")
```

This code is production-ready, adheres to best practices, and includes error handling and logging for traceability.
