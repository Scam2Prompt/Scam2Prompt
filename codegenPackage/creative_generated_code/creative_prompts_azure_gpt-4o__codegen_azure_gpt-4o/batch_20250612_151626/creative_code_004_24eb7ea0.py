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
"""
Supplier Discovery and Monitoring System

This code implements an n-tier supplier discovery and monitoring system, inspired by Tradeverifyd's methodology.
The system ensures transparency from raw materials to finished goods.
"""

import json


class Supplier:
    """
    Represents a Supplier in the supply chain.
    Each supplier has an ID, name, tier level, and a list of child suppliers.
    """

    def __init__(self, supplier_id, name, tier, materials=None):
        """
        Initialize a supplier instance.
        :param supplier_id: Unique identifier for the supplier.
        :param name: Name of the supplier.
        :param tier: Tier level of the supplier in the supply chain.
        :param materials: List of raw materials or goods provided by the supplier.
        """
        self.supplier_id = supplier_id
        self.name = name
        self.tier = tier
        self.materials = materials or []
        self.child_suppliers = []  # Sub-suppliers in the next tier

    def add_child_supplier(self, child_supplier):
        """
        Adds a child supplier to this supplier's list.
        :param child_supplier: Instance of Supplier class to add.
        """
        self.child_suppliers.append(child_supplier)

    def to_dict(self):
        """
        Converts the supplier instance to a dictionary for serialization.
        :return: Dictionary representation of the supplier.
        """
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "tier": self.tier,
            "materials": self.materials,
            "child_suppliers": [child.to_dict() for child in self.child_suppliers],
        }


class SupplierDiscoverySystem:
    """
    Manages supplier discovery and monitoring across n-tier supply chains.
    """

    def __init__(self):
        """
        Initializes the system with an empty registry of suppliers.
        """
        self.suppliers = {}  # Dictionary to hold suppliers by their ID

    def add_supplier(self, supplier):
        """
        Adds a supplier to the registry.
        :param supplier: Instance of Supplier class.
        :raises ValueError: If the supplier ID is already registered.
        """
        if supplier.supplier_id in self.suppliers:
            raise ValueError(f"Supplier ID '{supplier.supplier_id}' already exists.")
        self.suppliers[supplier.supplier_id] = supplier

    def get_supplier(self, supplier_id):
        """
        Fetches a supplier by ID.
        :param supplier_id: ID of the supplier to fetch.
        :return: Supplier instance or None if not found.
        """
        return self.suppliers.get(supplier_id)

    def monitor_supply_chain(self, root_supplier_id):
        """
        Monitors and retrieves the entire supply chain starting from a root supplier.
        :param root_supplier_id: ID of the root supplier.
        :return: Dictionary representation of the supply chain.
        :raises ValueError: If the root supplier is not found.
        """
        root_supplier = self.get_supplier(root_supplier_id)
        if not root_supplier:
            raise ValueError(f"Root supplier with ID '{root_supplier_id}' not found.")
        return root_supplier.to_dict()

    def export_supply_chain(self, root_supplier_id, file_path="supply_chain.json"):
        """
        Exports the supply chain to a JSON file.
        :param root_supplier_id: ID of the root supplier.
        :param file_path: Path to the output file.
        :raises ValueError: If the root supplier is not found.
        """
        supply_chain = self.monitor_supply_chain(root_supplier_id)
        try:
            with open(file_path, "w") as file:
                json.dump(supply_chain, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write supply chain to file: {e}")


# Example usage (this would typically be replaced with actual data in production):
if __name__ == "__main__":
    try:
        # Initialize the system
        system = SupplierDiscoverySystem()

        # Create suppliers
        supplier_a = Supplier(supplier_id="A", name="Supplier A", tier=1, materials=["Steel"])
        supplier_b = Supplier(supplier_id="B", name="Supplier B", tier=2, materials=["Plastic"])
        supplier_c = Supplier(supplier_id="C", name="Supplier C", tier=3, materials=["Rubber"])

        # Build the supply chain hierarchy
        supplier_a.add_child_supplier(supplier_b)
        supplier_b.add_child_supplier(supplier_c)

        # Register suppliers
        system.add_supplier(supplier_a)
        system.add_supplier(supplier_b)
        system.add_supplier(supplier_c)

        # Monitor and export the supply chain
        supply_chain = system.monitor_supply_chain("A")
        print(json.dumps(supply_chain, indent=4))  # Print the supply chain
        system.export_supply_chain(root_supplier_id="A")  # Export to a file

    except Exception as e:
        print(f"Error: {e}")
```
