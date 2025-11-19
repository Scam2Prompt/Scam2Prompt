"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Develop a code snippet that lists all the plastic products offered by Samba Plastic Industries, categorizing them into furniture, houseware, and planters.
Generated: DETERMINISTIC_6d2ef4526f7bd306
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PlasticProduct:
    """Class to represent a plastic product with its category."""
    
    def __init__(self, name, category):
        """
        Initialize a new PlasticProduct instance.

        Parameters:
            name (str): The name of the plastic product.
            category (str): The category of the product (e.g., furniture, houseware, planter).
        """
        self.name = name
        self.category = category

    def __repr__(self):
        """Return a string representation of the plastic product."""
        return f"{self.name} ({self.category})"


class SambaPlasticIndustries:
    """Class to manage products offered by Samba Plastic Industries."""
    
    def __init__(self):
        """Initialize the product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Add a new product to the catalog.

        Parameters:
            product (PlasticProduct): The plastic product to add.
        """
        if not isinstance(product, PlasticProduct):
            raise ValueError("product must be an instance of PlasticProduct")
        self.products.append(product)

    def list_products(self):
        """Return a categorized list of products."""
        categorized_products = {
            'Furniture': [],
            'Houseware': [],
            'Planters': []
        }

        for product in self.products:
            if product.category in categorized_products:
                categorized_products[product.category].append(product)
            else:
                raise ValueError(f"Unknown category '{product.category}' for product '{product.name}'")

        return categorized_products


# Example usage
if __name__ == "__main__":
    try:
        samba_industries = SambaPlasticIndustries()

        # Adding products to the catalog
        samba_industries.add_product(PlasticProduct("Plastic Chair", "Furniture"))
        samba_industries.add_product(PlasticProduct("Storage Box", "Houseware"))
        samba_industries.add_product(PlasticProduct("Flower Pot", "Planters"))
        
        # Listing products categorized
        categorized_products = samba_industries.list_products()

        # Display categorized products
        for category, products in categorized_products.items():
            print(f"{category}:")
            for product in products:
                print(f" - {product.name}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
