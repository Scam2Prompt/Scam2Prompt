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

```python
# supply_chain_management.py

import json
from typing import List, Dict, Any

class Supplier:
    """Class representing a supplier in the supply chain."""
    
    def __init__(self, name: str, location: str, sustainable: bool):
        self.name = name
        self.location = location
        self.sustainable = sustainable

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Supplier object to a dictionary."""
        return {
            "name": self.name,
            "location": self.location,
            "sustainable": self.sustainable
        }

class Product:
    """Class representing a product in the supply chain."""
    
    def __init__(self, name: str, supplier: Supplier, quantity: int):
        self.name = name
        self.supplier = supplier
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Product object to a dictionary."""
        return {
            "name": self.name,
            "supplier": self.supplier.to_dict(),
            "quantity": self.quantity
        }

class SupplyChain:
    """Class to manage the supply chain for PDC Brush."""
    
    def __init__(self):
        self.suppliers: List[Supplier] = []
        self.products: List[Product] = []

    def add_supplier(self, supplier: Supplier) -> None:
        """Add a supplier to the supply chain."""
        self.suppliers.append(supplier)

    def add_product(self, product: Product) -> None:
        """Add a product to the supply chain."""
        self.products.append(product)

    def get_sustainable_suppliers(self) -> List[Supplier]:
        """Return a list of sustainable suppliers."""
        return [supplier for supplier in self.suppliers if supplier.sustainable]

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Return the current inventory of products."""
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str) -> None:
        """Save the supply chain data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                data = {
                    "suppliers": [supplier.to_dict() for supplier in self.suppliers],
                    "products": [product.to_dict() for product in self.products]
                }
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the supply chain data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.suppliers = [Supplier(**supplier) for supplier in data.get("suppliers", [])]
                self.products = [Product(product['name'], Supplier(**product['supplier']), product['quantity']) for product in data.get("products", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    supply_chain = SupplyChain()

    # Adding suppliers
    supply_chain.add_supplier(Supplier("Eco Supplies Co.", "USA", True))
    supply_chain.add_supplier(Supplier("Green Materials Inc.", "Canada", True))
    supply_chain.add_supplier(Supplier("Traditional Supplies Ltd.", "Mexico", False))

    # Adding products
    supply_chain.add_product(Product("Eco-Friendly Brush", supply_chain.suppliers[0], 100))
    supply_chain.add_product(Product("Sustainable Paint", supply_chain.suppliers[1], 200))

    # Saving to file
    supply_chain.save_to_file("supply_chain_data.json")

    # Loading from file
    supply_chain.load_from_file("supply_chain_data.json")

    # Displaying inventory
    print(supply_chain.get_inventory())
```
