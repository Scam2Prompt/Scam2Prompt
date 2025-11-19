"""
Generated Code Metadata:
========================
Original URL: https://sevalcikolata.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for Seval Çikolata's chocolate products, including their names, descriptions, and prices.
Generated: DETERMINISTIC_7406fd67e769eab0
Batch ID: 20250622_210650
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

# Define a class for the product catalog
class ProductCatalog:
    """
    A class to represent an e-commerce product catalog for Seval Çikolata's chocolate products.
    """
    def __init__(self):
        # Initialize an empty catalog
        self.catalog = []

    def add_product(self, name, description, price):
        """
        Add a product to the catalog.

        :param name: str - Name of the product
        :param description: str - Description of the product
        :param price: float - Price of the product
        """
        try:
            # Validate input types
            if not isinstance(name, str) or not isinstance(description, str) or not isinstance(price, (int, float)):
                raise ValueError("Invalid input types. 'name' and 'description' must be strings, 'price' must be a number.")
            
            # Validate price
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            # Create a product dictionary
            product = {
                "name": name,
                "description": description,
                "price": round(price, 2)  # Ensure price is rounded to two decimal places
            }
            
            # Add the product to the catalog
            self.catalog.append(product)
        except ValueError as e:
            print(f"Error adding product: {e}")

    def display_catalog(self):
        """
        Display the product catalog in a readable format.
        """
        if not self.catalog:
            print("The catalog is empty.")
            return
        
        print("Seval Çikolata Product Catalog:")
        for idx, product in enumerate(self.catalog, start=1):
            print(f"{idx}. {product['name']}")
            print(f"   Description: {product['description']}")
            print(f"   Price: ${product['price']:.2f}")
            print()

    def save_catalog_to_file(self, filename):
        """
        Save the product catalog to a JSON file.

        :param filename: str - Name of the file to save the catalog
        """
        try:
            # Validate filename
            if not isinstance(filename, str):
                raise ValueError("Filename must be a string.")
            
            # Save the catalog to a file
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.catalog, file, ensure_ascii=False, indent=4)
            print(f"Catalog successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving catalog to file: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the ProductCatalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product("Milk Chocolate", "Smooth and creamy milk chocolate.", 4.99)
    catalog.add_product("Dark Chocolate", "Rich and intense dark chocolate.", 5.49)
    catalog.add_product("Hazelnut Chocolate", "Milk chocolate with crunchy hazelnuts.", 6.99)

    # Display the catalog
    catalog.display_catalog()

    # Save the catalog to a file
    catalog.save_catalog_to_file("seval_cikolata_catalog.json")
```
