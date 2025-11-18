"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgnexts.top
Prompt: Write code to create a product catalog for track cycling equipment, including categories like "Track Bikes/Frames," "Track Wheels/Tyres," and "Track Chainsets," using data structures in Python.
Generated: DETERMINISTIC_e112e543fa34e765
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to create a product catalog for track cycling equipment.
# The catalog is organized into categories with subcategories and products.

# Import necessary modules
import json

class ProductCatalog:
    """
    A class to represent a product catalog for track cycling equipment.
    """

    def __init__(self):
        """
        Initializes the ProductCatalog with predefined categories and an empty product list.
        """
        self.catalog = {
            "Track Bikes/Frames": [],
            "Track Wheels/Tyres": [],
            "Track Chainsets": []
        }

    def add_product(self, category, product_details):
        """
        Adds a product to a specific category in the catalog.

        Args:
            category (str): The category to which the product belongs.
            product_details (dict): A dictionary containing details of the product (name, price, etc.).
        Returns:
            None
        """
        if category not in self.catalog:
            raise ValueError(f"Invalid category. Available categories are: {', '.join(self.catalog.keys())}")
        
        # Validate product details
        if not isinstance(product_details, dict):
            raise ValueError("Product details must be a dictionary.")
        if "name" not in product_details or "price" not in product_details:
            raise ValueError("Product details must include 'name' and 'price'.")

        self.catalog[category].append(product_details)

    def view_catalog(self):
        """
        Returns the entire catalog in JSON format.

        Returns:
            str: Catalog in JSON string format.
        """
        return json.dumps(self.catalog, indent=4)

    def search_products(self, search_term):
        """
        Searches for products containing the given term in their name across all categories.

        Args:
            search_term (str): The term to search for in product names.
        Returns:
            list: A list of matching products.
        """
        matching_products = []
        for category, products in self.catalog.items():
            for product in products:
                if search_term.lower() in product["name"].lower():
                    matching_products.append({"category": category, **product})
        return matching_products


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the catalog
        catalog = ProductCatalog()

        # Add products to the catalog
        catalog.add_product("Track Bikes/Frames", {"name": "High-Speed Track Frame", "price": 1500.00, "brand": "Speedster"})
        catalog.add_product("Track Wheels/Tyres", {"name": "Aerodynamic Track Wheelset", "price": 800.00, "brand": "WheelCo"})
        catalog.add_product("Track Chainsets", {"name": "Lightweight Chainset", "price": 300.00, "brand": "CycleGear"})

        # View the entire catalog
        print("Product Catalog:")
        print(catalog.view_catalog())

        # Search for products
        search_results = catalog.search_products("track")
        print("\nSearch Results for 'track':")
        print(json.dumps(search_results, indent=4))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
