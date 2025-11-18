"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumaipce.com
Prompt: Provide a Python example for managing project logistics and procurement in industrial engineering, inspired by Puma Ipce's technical-administrative support services.
Generated: DETERMINISTIC_3c1a302f7d5e600e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ProcurementManager:
    """Class to manage procurement for project logistics."""

    def __init__(self, project_name: str):
        """
        Initializes the ProcurementManager with a project name.

        Args:
            project_name (str): Name of the project for which procurement is managed.
        """
        self.project_name = project_name
        self.suppliers: List[Dict[str, Any]] = []
        self.orders: List[Dict[str, Any]] = []

    def add_supplier(self, name: str, contact_info: str) -> None:
        """
        Adds a supplier to the procurement list.

        Args:
            name (str): Name of the supplier.
            contact_info (str): Contact information of the supplier.
        """
        supplier = {'name': name, 'contact_info': contact_info}
        self.suppliers.append(supplier)
        logging.info(f"Supplier added: {supplier}")

    def place_order(self, supplier_name: str, item: str, quantity: int, price_per_unit: float) -> None:
        """
        Places an order with a specified supplier.

        Args:
            supplier_name (str): Name of the supplier to place the order with.
            item (str): Name of the item being ordered.
            quantity (int): Quantity of the item.
            price_per_unit (float): Price per unit of the item.

        Raises:
            ValueError: If the supplier is not found or if quantity/price is invalid.
        """
        if quantity <= 0 or price_per_unit <= 0:
            raise ValueError("Quantity and price per unit must be greater than zero.")

        supplier = next((s for s in self.suppliers if s['name'] == supplier_name), None)
        if not supplier:
            raise ValueError(f"Supplier '{supplier_name}' not found.")

        order = {
            'supplier_name': supplier_name,
            'item': item,
            'quantity': quantity,
            'total_price': quantity * price_per_unit
        }
        self.orders.append(order)
        logging.info(f"Order placed: {order}")

    def get_orders(self) -> List[Dict[str, Any]]:
        """Returns a list of all orders placed."""
        return self.orders

    def save_to_file(self, filename: str) -> None:
        """
        Saves the current state of suppliers and orders to a JSON file.

        Args:
            filename (str): Name of the file to save the data.
        """
        data = {
            'project_name': self.project_name,
            'suppliers': self.suppliers,
            'orders': self.orders
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            logging.info(f"Data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save data to file: {e}")
            raise

    def load_from_file(self, filename: str) -> None:
        """
        Loads suppliers and orders from a JSON file.

        Args:
            filename (str): Name of the file to load the data from.

        Raises:
            IOError: If the file cannot be read.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.project_name = data['project_name']
            self.suppliers = data['suppliers']
            self.orders = data['orders']
            logging.info(f"Data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load data from file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    pm = ProcurementManager("Industrial Project A")
    pm.add_supplier("Supplier A", "contact@supplierA.com")
    pm.place_order("Supplier A", "Cement", 100, 5.0)
    pm.save_to_file("procurement_data.json")

    # Load from file example
    new_pm = ProcurementManager("New Project")
    new_pm.load_from_file("procurement_data.json")
    logging.info(f"Loaded orders: {new_pm.get_orders()}")
```
