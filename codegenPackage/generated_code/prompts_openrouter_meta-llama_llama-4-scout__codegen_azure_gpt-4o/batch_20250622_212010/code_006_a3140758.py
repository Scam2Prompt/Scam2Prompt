"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Create a data structure to store information about masterbatch products, including their chemical composition, applications, and market segments."
Generated: DETERMINISTIC_a3140758abbc0b95
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict, Optional

class MasterbatchProduct:
    """
    A class to represent a masterbatch product.
    """

    def __init__(self, name: str, chemical_composition: Dict[str, float], 
                 applications: List[str], market_segments: List[str]):
        """
        Initialize a MasterbatchProduct instance.

        :param name: Name of the masterbatch product.
        :param chemical_composition: A dictionary representing the chemical composition 
                                     (key: chemical name, value: percentage by weight).
        :param applications: A list of applications where the product is used.
        :param market_segments: A list of market segments targeted by the product.
        """
        self.name = name
        self.chemical_composition = chemical_composition
        self.applications = applications
        self.market_segments = market_segments

    def __str__(self) -> str:
        """
        Return a string representation of the masterbatch product.

        :return: A string describing the product.
        """
        return (f"MasterbatchProduct(name={self.name}, "
                f"chemical_composition={self.chemical_composition}, "
                f"applications={self.applications}, "
                f"market_segments={self.market_segments})")

    def add_application(self, application: str) -> None:
        """
        Add a new application to the product.

        :param application: The application to add.
        """
        if application not in self.applications:
            self.applications.append(application)

    def add_market_segment(self, segment: str) -> None:
        """
        Add a new market segment to the product.

        :param segment: The market segment to add.
        """
        if segment not in self.market_segments:
            self.market_segments.append(segment)

    def update_chemical_composition(self, chemical: str, percentage: float) -> None:
        """
        Update the chemical composition of the product.

        :param chemical: The chemical to update.
        :param percentage: The percentage by weight of the chemical.
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.chemical_composition[chemical] = percentage


class MasterbatchCatalog:
    """
    A class to manage a catalog of masterbatch products.
    """

    def __init__(self):
        """
        Initialize an empty catalog.
        """
        self.products: List[MasterbatchProduct] = []

    def add_product(self, product: MasterbatchProduct) -> None:
        """
        Add a new product to the catalog.

        :param product: The MasterbatchProduct instance to add.
        """
        if not isinstance(product, MasterbatchProduct):
            raise TypeError("Only MasterbatchProduct instances can be added.")
        self.products.append(product)

    def find_product_by_name(self, name: str) -> Optional[MasterbatchProduct]:
        """
        Find a product in the catalog by its name.

        :param name: The name of the product to find.
        :return: The MasterbatchProduct instance if found, else None.
        """
        for product in self.products:
            if product.name == name:
                return product
        return None

    def remove_product_by_name(self, name: str) -> bool:
        """
        Remove a product from the catalog by its name.

        :param name: The name of the product to remove.
        :return: True if the product was removed, False if not found.
        """
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return True
        return False

    def list_all_products(self) -> List[str]:
        """
        List the names of all products in the catalog.

        :return: A list of product names.
        """
        return [product.name for product in self.products]


# Example usage (can be removed in production code)
if __name__ == "__main__":
    # Create a catalog
    catalog = MasterbatchCatalog()

    # Create a masterbatch product
    product1 = MasterbatchProduct(
        name="MB-001",
        chemical_composition={"Polyethylene": 60.0, "Carbon Black": 40.0},
        applications=["Packaging", "Automotive"],
        market_segments=["Plastics", "Construction"]
    )

    # Add the product to the catalog
    catalog.add_product(product1)

    # List all products
    print("All Products:", catalog.list_all_products())

    # Find a product by name
    found_product = catalog.find_product_by_name("MB-001")
    print("Found Product:", found_product)

    # Update chemical composition
    if found_product:
        found_product.update_chemical_composition("Titanium Dioxide", 5.0)

    # Remove a product by name
    catalog.remove_product_by_name("MB-001")
    print("All Products after removal:", catalog.list_all_products())
```
