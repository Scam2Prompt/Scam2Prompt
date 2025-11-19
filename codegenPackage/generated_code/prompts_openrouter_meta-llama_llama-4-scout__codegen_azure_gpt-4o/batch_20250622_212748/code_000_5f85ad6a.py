"""
Generated Code Metadata:
========================
Original URL: https://weco.fi
Prompt: "Generate a Python code snippet for an e-commerce product categorization system similar to WEco's, with categories like Beverages, Creams, and Snacks & Nuts."
Generated: DETERMINISTIC_5f85ad6a8ac98e98
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a class for the Product Categorization System
class ProductCategorizationSystem:
    """
    A system to categorize e-commerce products into predefined categories.
    Categories include Beverages, Creams, and Snacks & Nuts.
    """
    
    def __init__(self):
        # Initialize predefined categories
        self.categories = {
            "Beverages": [],
            "Creams": [],
            "Snacks & Nuts": []
        }

    def add_product(self, product_name, category):
        """
        Add a product to a specific category.
        
        Args:
            product_name (str): Name of the product.
            category (str): Category to which the product belongs.
        
        Raises:
            ValueError: If the category is invalid.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.categories.keys())}")
        
        self.categories[category].append(product_name)
        print(f"Product '{product_name}' added to category '{category}'.")

    def get_products_by_category(self, category):
        """
        Retrieve all products in a specific category.
        
        Args:
            category (str): Category to retrieve products from.
        
        Returns:
            list: List of products in the specified category.
        
        Raises:
            ValueError: If the category is invalid.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.categories.keys())}")
        
        return self.categories[category]

    def export_categories_to_json(self, file_path):
        """
        Export the categories and their products to a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.categories, json_file, indent=4)
            print(f"Categories successfully exported to '{file_path}'.")
        except Exception as e:
            print(f"An error occurred while exporting categories: {e}")

    def import_categories_from_json(self, file_path):
        """
        Import categories and their products from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(file_path, 'r') as json_file:
                self.categories = json.load(json_file)
            print(f"Categories successfully imported from '{file_path}'.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except json.JSONDecodeError:
            print(f"File '{file_path}' is not a valid JSON file.")
        except Exception as e:
            print(f"An error occurred while importing categories: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the categorization system
    system = ProductCategorizationSystem()

    # Add products to categories
    system.add_product("Coca-Cola", "Beverages")
    system.add_product("Pepsi", "Beverages")
    system.add_product("Almond Cream", "Creams")
    system.add_product("Cashews", "Snacks & Nuts")

    # Retrieve products by category
    print("Beverages:", system.get_products_by_category("Beverages"))
    print("Creams:", system.get_products_by_category("Creams"))
    print("Snacks & Nuts:", system.get_products_by_category("Snacks & Nuts"))

    # Export categories to a JSON file
    system.export_categories_to_json("categories.json")

    # Import categories from a JSON file
    system.import_categories_from_json("categories.json")
```
