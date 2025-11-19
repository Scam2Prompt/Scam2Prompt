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
# plastic_products.py

class PlasticProduct:
    """Represents a plastic product offered by Samba Plastic Industries."""

    def __init__(self, name, category):
        """
        Initializes a PlasticProduct instance.

        Args:
            name (str): The name of the product.
            category (str): The category of the product (furniture, houseware, or planters).
        """
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category})"


class SambaPlasticIndustries:
    """Represents Samba Plastic Industries and their product offerings."""

    def __init__(self):
        """
        Initializes a SambaPlasticIndustries instance with a list of products.
        """
        self.products = [
            PlasticProduct("Plastic Chair", "furniture"),
            PlasticProduct("Plastic Table", "furniture"),
            PlasticProduct("Dinner Plate", "houseware"),
            PlasticProduct("Water Bottle", "houseware"),
            PlasticProduct("Flower Pot", "planters"),
            PlasticProduct("Garden Planter", "planters"),
            # Add more products as needed...
        ]

    def list_products_by_category(self):
        """
        Lists all products categorized by furniture, houseware, and planters.

        Returns:
            dict: A dictionary with categories as keys and lists of products as values.
        """
        categorized_products = {"furniture": [], "houseware": [], "planters": []}

        for product in self.products:
            if product.category in categorized_products:
                categorized_products[product.category].append(product)
            else:
                print(f"Warning: Unknown category '{product.category}' for product '{product.name}'")

        return categorized_products


def main():
    try:
        samba_plastics = SambaPlasticIndustries()
        categorized_products = samba_plastics.list_products_by_category()

        for category, products in categorized_products.items():
            print(f"\n{category.capitalize()}:")
            for product in products:
                print(product)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
