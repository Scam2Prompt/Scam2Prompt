"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Generate a product catalogue for a food packaging company that offers microwavable containers, dessert containers, drinking cups, and plastic cutlery."
Generated: DETERMINISTIC_7f79faf505524be0
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ProductCatalogue:
    """
    A class to represent a product catalogue for a food packaging company.
    """

    def __init__(self):
        """
        Initializes the product catalogue with predefined categories and products.
        """
        self.catalogue = {
            "Microwavable Containers": [
                {"id": 1, "name": "Round Container 500ml", "price": 0.50, "material": "Plastic"},
                {"id": 2, "name": "Square Container 750ml", "price": 0.75, "material": "Plastic"},
            ],
            "Dessert Containers": [
                {"id": 3, "name": "Small Dessert Cup 200ml", "price": 0.30, "material": "Plastic"},
                {"id": 4, "name": "Large Dessert Cup 400ml", "price": 0.50, "material": "Plastic"},
            ],
            "Drinking Cups": [
                {"id": 5, "name": "Cold Drink Cup 300ml", "price": 0.20, "material": "Plastic"},
                {"id": 6, "name": "Hot Drink Cup 250ml", "price": 0.25, "material": "Paper"},
            ],
            "Plastic Cutlery": [
                {"id": 7, "name": "Plastic Fork", "price": 0.10, "material": "Plastic"},
                {"id": 8, "name": "Plastic Spoon", "price": 0.10, "material": "Plastic"},
                {"id": 9, "name": "Plastic Knife", "price": 0.10, "material": "Plastic"},
            ],
        }

    def get_catalogue(self):
        """
        Returns the entire product catalogue.
        """
        return self.catalogue

    def get_category(self, category_name):
        """
        Returns products in a specific category.

        Args:
            category_name (str): The name of the category to retrieve.

        Returns:
            list: A list of products in the specified category.
        """
        try:
            return self.catalogue[category_name]
        except KeyError:
            raise ValueError(f"Category '{category_name}' does not exist in the catalogue.")

    def add_product(self, category_name, product):
        """
        Adds a new product to a specific category.

        Args:
            category_name (str): The name of the category to add the product to.
            product (dict): A dictionary containing product details (id, name, price, material).

        Raises:
            ValueError: If the category does not exist or the product format is invalid.
        """
        if category_name not in self.catalogue:
            raise ValueError(f"Category '{category_name}' does not exist.")
        if not all(key in product for key in ["id", "name", "price", "material"]):
            raise ValueError("Product must contain 'id', 'name', 'price', and 'material' fields.")
        self.catalogue[category_name].append(product)

    def save_to_file(self, file_name):
        """
        Saves the product catalogue to a JSON file.

        Args:
            file_name (str): The name of the file to save the catalogue to.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.catalogue, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save catalogue to file: {e}")

    def load_from_file(self, file_name):
        """
        Loads the product catalogue from a JSON file.

        Args:
            file_name (str): The name of the file to load the catalogue from.

        Raises:
            IOError: If the file cannot be read or the content is invalid.
        """
        try:
            with open(file_name, "r") as file:
                self.catalogue = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load catalogue from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the product catalogue
    catalogue = ProductCatalogue()

    # Print the entire catalogue
    print("Product Catalogue:")
    print(json.dumps(catalogue.get_catalogue(), indent=4))

    # Get products in a specific category
    print("\nMicrowavable Containers:")
    print(json.dumps(catalogue.get_category("Microwavable Containers"), indent=4))

    # Add a new product to a category
    new_product = {"id": 10, "name": "Round Container 1000ml", "price": 1.00, "material": "Plastic"}
    catalogue.add_product("Microwavable Containers", new_product)

    # Save the updated catalogue to a file
    catalogue.save_to_file("product_catalogue.json")

    # Load the catalogue from a file
    catalogue.load_from_file("product_catalogue.json")
    print("\nLoaded Catalogue:")
    print(json.dumps(catalogue.get_catalogue(), indent=4))
```
