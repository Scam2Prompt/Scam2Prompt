"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Generate a code snippet for a product catalog that includes various sizes and types of "Cajas Chinas" and "Cilindros" as described on the Meat Master website.
Generated: DETERMINISTIC_857f93878a20e6eb
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

# Import necessary modules
import json

# Define a class for Product
class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, name, category, sizes, price):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param category: Category of the product (e.g., "Cajas Chinas", "Cilindros")
        :param sizes: List of available sizes for the product
        :param price: Base price of the product
        """
        self.name = name
        self.category = category
        self.sizes = sizes
        self.price = price

    def to_dict(self):
        """
        Convert the Product instance to a dictionary.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "sizes": self.sizes,
            "price": self.price
        }

# Define a function to create the product catalog
def create_product_catalog():
    """
    Create a product catalog with predefined products.

    :return: List of Product instances
    """
    try:
        # Define products
        products = [
            Product(
                name="Caja China Classic",
                category="Cajas Chinas",
                sizes=["Small", "Medium", "Large"],
                price=299.99
            ),
            Product(
                name="Caja China Pro",
                category="Cajas Chinas",
                sizes=["Medium", "Large", "Extra Large"],
                price=499.99
            ),
            Product(
                name="Cilindro BBQ",
                category="Cilindros",
                sizes=["Compact", "Standard", "Deluxe"],
                price=199.99
            ),
            Product(
                name="Cilindro Smoker",
                category="Cilindros",
                sizes=["Standard", "Deluxe"],
                price=349.99
            )
        ]
        return products
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error creating product catalog: {e}")
        return []

# Define a function to display the product catalog
def display_catalog(products):
    """
    Display the product catalog in a readable format.

    :param products: List of Product instances
    """
    try:
        print("Product Catalog:")
        print("================")
        for product in products:
            print(f"Name: {product.name}")
            print(f"Category: {product.category}")
            print(f"Available Sizes: {', '.join(product.sizes)}")
            print(f"Base Price: ${product.price:.2f}")
            print("----------------")
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error displaying product catalog: {e}")

# Define a function to save the catalog to a JSON file
def save_catalog_to_file(products, filename="product_catalog.json"):
    """
    Save the product catalog to a JSON file.

    :param products: List of Product instances
    :param filename: Name of the file to save the catalog
    """
    try:
        # Convert products to a list of dictionaries
        product_dicts = [product.to_dict() for product in products]
        
        # Write to a JSON file
        with open(filename, "w") as file:
            json.dump(product_dicts, file, indent=4)
        print(f"Product catalog saved to {filename}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error saving product catalog to file: {e}")

# Main function to execute the script
if __name__ == "__main__":
    # Create the product catalog
    catalog = create_product_catalog()
    
    # Display the catalog
    display_catalog(catalog)
    
    # Save the catalog to a file
    save_catalog_to_file(catalog)
```
