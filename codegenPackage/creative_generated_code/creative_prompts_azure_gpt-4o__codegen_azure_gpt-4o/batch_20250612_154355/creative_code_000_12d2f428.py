"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Write code to create a product catalog for replica championship belts, including categories like WWE, NBA, NFL, NHL, and MLB, with features for filtering by price and design.
Generated: DETERMINISTIC_12d2f428a2e6829e
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ProductCatalog:
    def __init__(self):
        """
        Initializes the product catalog with an empty list of products.
        """
        self.products = []

    def add_product(self, name, category, price, design):
        """
        Adds a new product to the catalog.

        Args:
            name (str): Name of the product.
            category (str): Category of the product (e.g., WWE, NBA, NFL, NHL, MLB).
            price (float): Price of the product.
            design (str): Design description of the product.
        """
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number.")
        
        product = {
            "name": name,
            "category": category,
            "price": price,
            "design": design
        }
        self.products.append(product)

    def filter_by_price(self, min_price=None, max_price=None):
        """
        Filters products by price range.

        Args:
            min_price (float, optional): Minimum price filter. Defaults to None.
            max_price (float, optional): Maximum price filter. Defaults to None.

        Returns:
            list: List of products within the specified price range.
        """
        filtered_products = [
            product for product in self.products
            if (min_price is None or product["price"] >= min_price) and
               (max_price is None or product["price"] <= max_price)
        ]
        return filtered_products

    def filter_by_design(self, keyword):
        """
        Filters products by design keyword.

        Args:
            keyword (str): Keyword to search in the product design.

        Returns:
            list: List of products whose design contains the keyword.
        """
        keyword_lower = keyword.lower()
        filtered_products = [
            product for product in self.products
            if keyword_lower in product["design"].lower()
        ]
        return filtered_products

    def filter_by_category(self, category):
        """
        Filters products by category.

        Args:
            category (str): The category to filter by.

        Returns:
            list: List of products in the specified category.
        """
        filtered_products = [
            product for product in self.products
            if product["category"].lower() == category.lower()
        ]
        return filtered_products

    def to_json(self):
        """
        Converts the product catalog to JSON format.

        Returns:
            str: JSON string representation of the catalog.
        """
        return json.dumps(self.products, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        catalog = ProductCatalog()
        
        # Adding products
        catalog.add_product("WWE Championship Belt", "WWE", 199.99, "Gold-plated design with leather strap")
        catalog.add_product("NBA Championship Belt", "NBA", 249.99, "Basketball-themed design in silver")
        catalog.add_product("NFL Championship Belt", "NFL", 299.99, "Football-themed design with team logos")
        catalog.add_product("NHL Championship Belt", "NHL", 199.99, "Hockey-themed design with ice texture")
        catalog.add_product("MLB Championship Belt", "MLB", 229.99, "Baseball-themed design with classic stitching")
        
        # Filtering examples
        print("Products priced between $200 and $300:")
        print(catalog.filter_by_price(min_price=200, max_price=300))
        
        print("\nProducts with 'Football' in design:")
        print(catalog.filter_by_design("Football"))
        
        print("\nProducts in the 'NBA' category:")
        print(catalog.filter_by_category("NBA"))
        
        print("\nFull catalog in JSON format:")
        print(catalog.to_json())
    except Exception as e:
        print(f"An error occurred: {e}")
```
