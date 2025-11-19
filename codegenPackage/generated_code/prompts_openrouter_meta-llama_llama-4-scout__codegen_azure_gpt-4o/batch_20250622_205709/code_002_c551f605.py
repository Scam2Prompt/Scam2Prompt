"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Generate a product catalog for a factory producing flip-flops and shoe soles, including product descriptions for items like Ojota Infantil Estampada 3D – Niños and Suecos Hombre.
Generated: DETERMINISTIC_c551f605c57b77d5
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ProductCatalog:
    """
    A class to represent a product catalog for a factory producing flip-flops and shoe soles.
    """

    def __init__(self):
        """
        Initializes an empty product catalog.
        """
        self.products = []

    def add_product(self, name, category, description, price, stock):
        """
        Adds a product to the catalog.

        :param name: Name of the product
        :param category: Category of the product (e.g., Flip-Flops, Shoe Soles)
        :param description: Description of the product
        :param price: Price of the product (float)
        :param stock: Number of items in stock (int)
        """
        try:
            product = {
                "name": name,
                "category": category,
                "description": description,
                "price": round(price, 2),
                "stock": stock
            }
            self.products.append(product)
        except Exception as e:
            print(f"Error adding product: {e}")

    def get_catalog(self):
        """
        Returns the entire product catalog.

        :return: List of products in the catalog
        """
        return self.products

    def save_to_file(self, filename):
        """
        Saves the product catalog to a JSON file.

        :param filename: Name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.products, file, indent=4)
            print(f"Catalog saved to {filename}")
        except Exception as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename):
        """
        Loads the product catalog from a JSON file.

        :param filename: Name of the file to load the catalog from
        """
        try:
            with open(filename, 'r') as file:
                self.products = json.load(file)
            print(f"Catalog loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}.")
        except Exception as e:
            print(f"Error loading catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a product catalog instance
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(
        name="Ojota Infantil Estampada 3D – Niños",
        category="Flip-Flops",
        description="Comfortable and colorful 3D-printed flip-flops for kids.",
        price=12.99,
        stock=100
    )
    catalog.add_product(
        name="Suecos Hombre",
        category="Shoe Soles",
        description="Durable and lightweight shoe soles for men.",
        price=19.99,
        stock=50
    )

    # Display the catalog
    print("Product Catalog:")
    print(json.dumps(catalog.get_catalog(), indent=4))

    # Save the catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from a file
    catalog.load_from_file("product_catalog.json")
```
