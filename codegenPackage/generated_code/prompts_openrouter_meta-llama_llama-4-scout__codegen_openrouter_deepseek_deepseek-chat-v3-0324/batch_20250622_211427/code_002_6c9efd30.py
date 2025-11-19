"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Generate a product catalog for a cooking oil company that prioritizes health-conscious and sustainable practices, including descriptions of extra virgin olive oils and specialty cooking oils.
Generated: DETERMINISTIC_6c9efd30a6096052
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class ProductCatalog:
    """
    A product catalog for a cooking oil company specializing in health-conscious and sustainable products.
    """

    def __init__(self):
        self.products = []
        self._initialize_catalog()

    def _initialize_catalog(self) -> None:
        """Initialize the catalog with default products."""
        self.products = [
            {
                "id": 1,
                "name": "Extra Virgin Olive Oil",
                "description": "Cold-pressed from organic olives, rich in antioxidants and healthy monounsaturated fats.",
                "category": "Olive Oil",
                "health_benefits": ["Heart health", "Anti-inflammatory", "High in polyphenols"],
                "sustainability": ["Organic farming", "Carbon-neutral packaging"],
                "price": 12.99,
                "size": "500ml"
            },
            {
                "id": 2,
                "name": "Avocado Oil",
                "description": "High smoke point oil extracted from ripe avocados, perfect for high-heat cooking.",
                "category": "Specialty Oil",
                "health_benefits": ["Rich in vitamin E", "Supports skin health", "Low in saturated fat"],
                "sustainability": ["Sustainably sourced", "Eco-friendly processing"],
                "price": 15.99,
                "size": "500ml"
            },
            {
                "id": 3,
                "name": "Coconut Oil",
                "description": "Unrefined, cold-pressed coconut oil with a rich aroma and flavor.",
                "category": "Specialty Oil",
                "health_benefits": ["Supports metabolism", "Contains lauric acid", "Dairy-free butter alternative"],
                "sustainability": ["Fair trade certified", "Biodegradable packaging"],
                "price": 10.99,
                "size": "500ml"
            }
        ]

    def get_all_products(self) -> List[Dict]:
        """Return all products in the catalog."""
        return self.products

    def get_product_by_id(self, product_id: int) -> Optional[Dict]:
        """
        Retrieve a product by its ID.
        
        Args:
            product_id: The ID of the product to retrieve.
        
        Returns:
            The product dictionary if found, otherwise None.
        """
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None

    def add_product(self, product: Dict) -> bool:
        """
        Add a new product to the catalog.
        
        Args:
            product: A dictionary containing product details.
        
        Returns:
            True if the product was added successfully, False otherwise.
        """
        try:
            # Validate required fields
            required_fields = ["name", "description", "category", "price", "size"]
            for field in required_fields:
                if field not in product:
                    raise ValueError(f"Missing required field: {field}")

            # Generate a new ID
            new_id = max(p["id"] for p in self.products) + 1 if self.products else 1
            product["id"] = new_id

            self.products.append(product)
            return True
        except Exception as e:
            print(f"Error adding product: {e}")
            return False

    def to_json(self) -> str:
        """Return the catalog as a JSON string."""
        return json.dumps(self.products, indent=2)

    def save_to_file(self, filename: str) -> bool:
        """
        Save the catalog to a JSON file.
        
        Args:
            filename: The name of the file to save to.
        
        Returns:
            True if the file was saved successfully, False otherwise.
        """
        try:
            with open(filename, "w") as f:
                json.dump(self.products, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving catalog: {e}")
            return False

    @classmethod
    def load_from_file(cls, filename: str) -> Optional['ProductCatalog']:
        """
        Load a catalog from a JSON file.
        
        Args:
            filename: The name of the file to load from.
        
        Returns:
            A ProductCatalog instance if successful, None otherwise.
        """
        try:
            with open(filename, "r") as f:
                products = json.load(f)
            catalog = cls()
            catalog.products = products
            return catalog
        except Exception as e:
            print(f"Error loading catalog: {e}")
            return None


# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Print all products
    print("All Products:")
    print(catalog.to_json())

    # Get a specific product
    product = catalog.get_product_by_id(1)
    print("\nProduct with ID 1:")
    print(json.dumps(product, indent=2))

    # Add a new product
    new_product = {
        "name": "Flaxseed Oil",
        "description": "Rich in omega-3 fatty acids, ideal for dressings and low-heat cooking.",
        "category": "Specialty Oil",
        "health_benefits": ["Omega-3 source", "Supports brain health", "Vegan-friendly"],
        "sustainability": ["Non-GMO", "Recyclable packaging"],
        "price": 14.99,
        "size": "250ml"
    }
    success = catalog.add_product(new_product)
    print(f"\nProduct added successfully: {success}")

    # Save catalog to file
    catalog.save_to_file("product_catalog.json")
    print("\nCatalog saved to 'product_catalog.json'")
```
