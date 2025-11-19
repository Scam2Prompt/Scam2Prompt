"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Develop a code snippet that lists all the plastic products offered by Samba Plastic Industries, categorizing them into furniture, houseware, and planters.
Generated: DETERMINISTIC_6d2ef4526f7bd306
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlasticProduct:
    """Class representing a plastic product."""
    
    def __init__(self, name, category):
        """
        Initialize a new plastic product.

        Args:
            name (str): The name of the product.
            category (str): The category of the product (e.g., furniture, houseware, planters).
        """
        self.name = name
        self.category = category

    def __repr__(self):
        """Return a string representation of the product."""
        return f"{self.name} ({self.category})"


class SambaPlasticIndustries:
    """Class representing Samba Plastic Industries."""

    def __init__(self):
        """Initialize the product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (PlasticProduct): The product to add.
        """
        if not isinstance(product, PlasticProduct):
            raise ValueError("Only instances of PlasticProduct can be added.")
        self.products.append(product)

    def list_products(self):
        """List all products categorized by their type."""
        categorized_products = {
            "Furniture": [],
            "Houseware": [],
            "Planters": []
        }

        for product in self.products:
            if product.category in categorized_products:
                categorized_products[product.category].append(product)
            else:
                raise ValueError(f"Unknown category: {product.category}")

        return categorized_products


def main():
    """Main function to demonstrate the functionality."""
    try:
        # Create an instance of Samba Plastic Industries
        samba_plastics = SambaPlasticIndustries()

        # Add products to the catalog
        samba_plastics.add_product(PlasticProduct("Plastic Chair", "Furniture"))
        samba_plastics.add_product(PlasticProduct("Plastic Table", "Furniture"))
        samba_plastics.add_product(PlasticProduct("Plastic Bowl", "Houseware"))
        samba_plastics.add_product(PlasticProduct("Plastic Cup", "Houseware"))
        samba_plastics.add_product(PlasticProduct("Plastic Planter", "Planters"))

        # List all products categorized
        categorized_products = samba_plastics.list_products()
        
        # Print categorized products
        for category, products in categorized_products.items():
            print(f"{category}:")
            for product in products:
                print(f"  - {product.name}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
