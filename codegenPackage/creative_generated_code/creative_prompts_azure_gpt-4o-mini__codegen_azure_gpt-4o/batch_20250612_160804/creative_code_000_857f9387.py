"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Generate a code snippet for a product catalog that includes various sizes and types of "Cajas Chinas" and "Cilindros" as described on the Meat Master website.
Generated: DETERMINISTIC_857f93878a20e6eb
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


# Define a class for Product, which can be used for product catalog entries
class Product:
    """
    A class representing a product in the catalog.

    Attributes:
        name (str): The name of the product.
        category (str): The category of the product (e.g., 'Cajas Chinas' or 'Cilindros').
        size (str): The size of the product (e.g., 'Small', 'Medium', 'Large').
        price (float): The price of the product.
    """

    def __init__(self, name, category, size, price):
        try:
            self.name = name
            self.category = category
            self.size = size
            self.price = price
        except Exception as e:
            raise ValueError(f"Error initializing product: {e}")

    def to_dict(self):
        """
        Convert the product instance to a dictionary.
        Returns:
            dict: Dictionary representation of the product.
        """
        return {
            "name": self.name,
            "category": self.category,
            "size": self.size,
            "price": self.price,
        }


# Function to generate the product catalog
def generate_product_catalog():
    """
    Generate a catalog of products.

    Returns:
        dict: A dictionary containing the catalog of products.
    """
    try:
        # List of products
        products = [
            Product("Caja China Classic", "Cajas Chinas", "Small", 299.99),
            Product("Caja China Pro", "Cajas Chinas", "Medium", 399.99),
            Product("Caja China XL", "Cajas Chinas", "Large", 499.99),
            Product("Cilindro Basic", "Cilindros", "Small", 199.99),
            Product("Cilindro Advanced", "Cilindros", "Medium", 299.99),
            Product("Cilindro XL", "Cilindros", "Large", 399.99),
        ]

        # Convert each product to dictionary format for easier handling
        catalog = [product.to_dict() for product in products]
        return catalog
    except Exception as e:
        raise RuntimeError(f"Error generating product catalog: {e}")


# Function to save the catalog to a JSON file
def save_catalog_to_json(catalog, filename="product_catalog.json"):
    """
    Save the product catalog to a JSON file.

    Args:
        catalog (list): The product catalog to save.
        filename (str): The filename for the JSON file (default: 'product_catalog.json').
    """
    try:
        with open(filename, "w") as json_file:
            json.dump(catalog, json_file, indent=4)
        print(f"Product catalog saved to {filename}")
    except Exception as e:
        raise RuntimeError(f"Error saving catalog to JSON file: {e}")


# Main function to demonstrate functionality
def main():
    """
    Main function to generate and save the product catalog.
    """
    try:
        # Generate the catalog
        catalog = generate_product_catalog()

        # Save the catalog to a JSON file
        save_catalog_to_json(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point
if __name__ == "__main__":
    main()
```
