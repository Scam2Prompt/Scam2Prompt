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
import json
from typing import Dict, List, Optional

class SambaPlasticProducts:
    """
    A class to represent and categorize plastic products offered by Samba Plastic Industries.
    Products are categorized into furniture, houseware, and planters.
    """

    def __init__(self, products_data: Optional[Dict[str, List[str]]] = None):
        """
        Initialize the SambaPlasticProducts with optional predefined product data.
        
        Args:
            products_data (Optional[Dict[str, List[str]]]): A dictionary with categories as keys
                and lists of products as values. Defaults to None.
        """
        self.categories = ["furniture", "houseware", "planters"]
        self.products = products_data or {
            "furniture": [],
            "houseware": [],
            "planters": []
        }

    def add_product(self, category: str, product_name: str) -> None:
        """
        Add a product to the specified category.
        
        Args:
            category (str): The category to which the product belongs.
            product_name (str): The name of the product to add.
            
        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category. Available categories: {', '.join(self.categories)}")
        self.products[category].append(product_name)

    def get_products_by_category(self, category: str) -> List[str]:
        """
        Retrieve all products in the specified category.
        
        Args:
            category (str): The category to retrieve products from.
            
        Returns:
            List[str]: A list of product names in the category.
            
        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category. Available categories: {', '.join(self.categories)}")
        return self.products[category]

    def list_all_products(self) -> Dict[str, List[str]]:
        """
        Retrieve all products categorized by their respective categories.
        
        Returns:
            Dict[str, List[str]]: A dictionary with categories as keys and lists of products as values.
        """
        return self.products

    def save_to_json(self, file_path: str) -> None:
        """
        Save the product data to a JSON file.
        
        Args:
            file_path (str): The path to the JSON file to save the data.
            
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.products, f, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

    @classmethod
    def load_from_json(cls, file_path: str) -> 'SambaPlasticProducts':
        """
        Load product data from a JSON file and create a SambaPlasticProducts instance.
        
        Args:
            file_path (str): The path to the JSON file to load the data from.
            
        Returns:
            SambaPlasticProducts: An instance with the loaded product data.
            
        Raises:
            IOError: If there is an issue reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as f:
                products_data = json.load(f)
            return cls(products_data)
        except IOError as e:
            raise IOError(f"Error reading file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file: {e}", e.doc, e.pos)


# Example usage
if __name__ == "__main__":
    # Initialize with some sample data
    samba_products = SambaPlasticProducts({
        "furniture": ["Plastic Chair", "Plastic Table"],
        "houseware": ["Plastic Bowl", "Plastic Tray"],
        "planters": ["Small Planter", "Large Planter"]
    })

    # Add a new product
    samba_products.add_product("furniture", "Plastic Stool")

    # List all products by category
    print("All Products:")
    for category, products in samba_products.list_all_products().items():
        print(f"{category.capitalize()}: {', '.join(products)}")

    # Save to a JSON file
    samba_products.save_to_json("samba_products.json")

    # Load from the JSON file
    loaded_products = SambaPlasticProducts.load_from_json("samba_products.json")
    print("\nLoaded Products:")
    for category, products in loaded_products.list_all_products().items():
        print(f"{category.capitalize()}: {', '.join(products)}")
```
