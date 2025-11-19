"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: "Generate a list of electrical conduit and accessories products as per the catalog of Miraya Electric S.A.C. and describe their use cases."
Generated: DETERMINISTIC_2802de732aeb8fba
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class ElectricalConduit:
    """
    A class to represent an electrical conduit product.
    """

    def __init__(self, name: str, diameter: float, material: str, use_case: str):
        """
        Initializes an ElectricalConduit instance.

        :param name: Name of the conduit
        :param diameter: Diameter of the conduit in inches
        :param material: Material of the conduit (e.g., PVC, EMT)
        :param use_case: Description of the use case for the conduit
        """
        self.name = name
        self.diameter = diameter
        self.material = material
        self.use_case = use_case

    def to_dict(self) -> Dict:
        """
        Converts the ElectricalConduit instance to a dictionary.

        :return: Dictionary representation of the conduit
        """
        return {
            "name": self.name,
            "diameter": self.diameter,
            "material": self.material,
            "use_case": self.use_case
        }


class ElectricalCatalog:
    """
    A class to manage a catalog of electrical conduits and accessories.
    """

    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.products: List[ElectricalConduit] = []

    def add_product(self, product: ElectricalConduit):
        """
        Adds a product to the catalog.

        :param product: An instance of ElectricalConduit to add
        """
        if not isinstance(product, ElectricalConduit):
            raise ValueError("Product must be an instance of ElectricalConduit")
        self.products.append(product)

    def to_json(self) -> str:
        """
        Converts the catalog to a JSON string.

        :return: JSON string representation of the catalog
        """
        return json.dumps([product.to_dict() for product in self.products], indent=4)


def main():
    """
    Main function to create a catalog of electrical conduits and accessories.
    """
    try:
        catalog = ElectricalCatalog()

        # Sample products
        catalog.add_product(ElectricalConduit("PVC Conduit", 2.0, "PVC", "Used for protecting electrical wiring in residential applications."))
        catalog.add_product(ElectricalConduit("EMT Conduit", 1.5, "Steel", "Used for commercial and industrial applications where durability is required."))
        catalog.add_product(ElectricalConduit("Flexible Conduit", 1.0, "PVC", "Used in areas where flexibility is needed, such as in tight spaces or around corners."))

        # Output the catalog in JSON format
        print(catalog.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
