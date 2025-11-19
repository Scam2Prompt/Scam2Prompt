"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: "What are some popular fabric types used for yoga wear and leggings, and how can I source them from a supplier like Shaoxing Eagles Textile Co., Ltd.?"
Generated: DETERMINISTIC_b5ba0ad2e711bbcf
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fabric_info.py

class Fabric:
    """Represents a fabric type with its properties."""

    def __init__(self, name, description, supplier, price_per_unit):
        """
        Initializes a Fabric object.

        Args:
            name (str): The name of the fabric.
            description (str): A brief description of the fabric.
            supplier (str): The supplier of the fabric.
            price_per_unit (float): The price per unit of the fabric.
        """
        self.name = name
        self.description = description
        self.supplier = supplier
        self.price_per_unit = price_per_unit

    def __str__(self):
        return f"{self.name}: {self.description}, Supplier: {self.supplier}, Price: ${self.price_per_unit:.2f}/unit"


class FabricSupplier:
    """Represents a fabric supplier with their available fabrics."""

    def __init__(self, name):
        """
        Initializes a FabricSupplier object.

        Args:
            name (str): The name of the supplier.
        """
        self.name = name
        self.fabrics = {}

    def add_fabric(self, fabric):
        """
        Adds a fabric to the supplier's catalog.

        Args:
            fabric (Fabric): The fabric to add.
        """
        self.fabrics[fabric.name] = fabric

    def get_fabric(self, name):
        """
        Retrieves a fabric from the supplier's catalog.

        Args:
            name (str): The name of the fabric.

        Returns:
            Fabric: The fabric object if found, None otherwise.
        """
        return self.fabrics.get(name)

    def list_fabrics(self):
        """
        Lists all fabrics in the supplier's catalog.

        Returns:
            list: A list of fabric objects.
        """
        return list(self.fabrics.values())


def main():
    try:
        # Create a supplier
        eagles_textile = FabricSupplier("Shaoxing Eagles Textile Co., Ltd.")

        # Create popular fabrics for yoga wear and leggings
        fabrics = [
            Fabric("Spandex", "Stretchy and breathable fabric.", eagles_textile.name, 5.99),
            Fabric("Nylon", "Durable and moisture-wicking fabric.", eagles_textile.name, 4.99),
            Fabric("Polyester", "Soft and quick-drying fabric.", eagles_textile.name, 3.99),
            Fabric("Cotton", "Natural and breathable fabric.", eagles_textile.name, 2.99),
            Fabric("Lycra", "Stretchy and flexible fabric.", eagles_textile.name, 6.99),
        ]

        # Add fabrics to the supplier's catalog
        for fabric in fabrics:
            eagles_textile.add_fabric(fabric)

        # List popular fabrics
        print("Popular Fabrics for Yoga Wear and Leggings:")
        for fabric in eagles_textile.list_fabrics():
            print(fabric)

        # Source a specific fabric from the supplier
        fabric_name = "Spandex"
        sourced_fabric = eagles_textile.get_fabric(fabric_name)
        if sourced_fabric:
            print(f"\nSourced {fabric_name} from {eagles_textile.name}:")
            print(sourced_fabric)
        else:
            print(f"\n{fabric_name} not found in {eagles_textile.name}'s catalog.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
