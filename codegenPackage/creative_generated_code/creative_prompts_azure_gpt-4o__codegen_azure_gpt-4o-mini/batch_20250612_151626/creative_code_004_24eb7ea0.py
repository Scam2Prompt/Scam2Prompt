"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade-verified.com
Prompt: Write code to implement n-tier supplier discovery and monitoring, ensuring transparency from raw materials to finished goods, inspired by Tradeverifyd's methodology.
Generated: DETERMINISTIC_24eb7ea0d7377cd5
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Supplier Discovery and Monitoring System

# Import necessary libraries
import logging
from typing import List, Dict, Any

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Supplier:
    def __init__(self, supplier_id: str, name: str, materials: List[str]):
        """
        Initialize a Supplier object.

        :param supplier_id: Unique identifier for the supplier
        :param name: Name of the supplier
        :param materials: List of raw materials supplied
        """
        self.supplier_id = supplier_id
        self.name = name
        self.materials = materials

    def __repr__(self):
        return f"Supplier({self.supplier_id}, {self.name})"


class SupplyChain:
    def __init__(self):
        """
        Initialize the SupplyChain with an empty supplier list.
        """
        self.suppliers: List[Supplier] = []

    def add_supplier(self, supplier: Supplier) -> None:
        """
        Add a new supplier to the supply chain.

        :param supplier: Supplier object to be added
        """
        if not isinstance(supplier, Supplier):
            logging.error("Invalid supplier object.")
            raise ValueError("Invalid supplier object.")

        self.suppliers.append(supplier)
        logging.info(f"Supplier {supplier.name} added to the supply chain.")

    def monitor_suppliers(self) -> Dict[str, Any]:
        """
        Monitor suppliers and return their details.

        :return: Dictionary containing supplier details for monitoring
        """
        try:
            supplier_info = {supplier.supplier_id: {
                'name': supplier.name,
                'materials': supplier.materials
            } for supplier in self.suppliers}
            logging.info("Supplier monitoring completed successfully.")
            return supplier_info
        except Exception as e:
            logging.error(f"Error while monitoring suppliers: {e}")
            raise


class Product:
    def __init__(self, product_id: str, name: str, suppliers: List[Supplier]):
        """
        Initialize a Product object.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param suppliers: List of suppliers for the raw materials used
        """
        self.product_id = product_id
        self.name = name
        self.suppliers = suppliers

    def __repr__(self):
        return f"Product({self.product_id}, {self.name})"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize supply chain
        supply_chain = SupplyChain()

        # Create suppliers
        supplier1 = Supplier("S001", "Supplier A", ["Steel", "Plastic"])
        supplier2 = Supplier("S002", "Supplier B", ["Rubber", "Glass"])

        # Add suppliers to the supply chain
        supply_chain.add_supplier(supplier1)
        supply_chain.add_supplier(supplier2)

        # Monitor suppliers and print their details
        monitored_suppliers = supply_chain.monitor_suppliers()
        print(monitored_suppliers)

        # Create a product
        product = Product("P001", "Product X", [supplier1, supplier2])
        print(product)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
