"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperland.com.ar
Prompt: Write a Python script to generate a catalog of customizable paper and cardboard products, including categories like artistic materials, packaging, and stationery, inspired by Paperland's offerings.
Generated: DETERMINISTIC_eca6bffd6c1ea433
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to generate a catalog of customizable paper and cardboard products.
Categories include:
- Artistic materials
- Packaging
- Stationery

This script is inspired by Paperland's offerings. The catalog is stored as a JSON
file and allows users to customize product details interactively.
"""

import json
import sys

# Constants
CATALOG_FILE = "paperland_catalog.json"
DEFAULT_CATEGORIES = ["Artistic Materials", "Packaging", "Stationery"]

class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, name, category, description, price, custom_options=None):
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.custom_options = custom_options or []

    def to_dict(self):
        """
        Convert the product object to a dictionary for JSON serialization.
        """
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "price": self.price,
            "custom_options": self.custom_options
        }


class Catalog:
    """
    Represents the catalog that stores paper and cardboard products.
    """
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product object.")
        self.products.append(product)

    def save_to_file(self, filename):
        """
        Save the catalog to a JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except Exception as e:
            print(f"Error saving catalog to file: {e}", file=sys.stderr)

    def load_from_file(self, filename):
        """
        Load the catalog from a JSON file.
        """
        try:
            with open(filename, "r") as file:
                product_dicts = json.load(file)
                self.products = [
                    Product(
                        name=prod["name"],
                        category=prod["category"],
                        description=prod["description"],
                        price=prod["price"],
                        custom_options=prod.get("custom_options", [])
                    )
                    for prod in product_dicts
                ]
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty catalog.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'. Starting with an empty catalog.")
        except Exception as e:
            print(f"Error loading catalog from file: {e}", file=sys.stderr)


def create_custom_product():
    """
    Interactively create a custom product.
    """
    print("\nCreate a new product:")
    name = input("Enter product name: ").strip()
    category = input(f"Enter product category ({', '.join(DEFAULT_CATEGORIES)}): ").strip()
    description = input("Enter product description: ").strip()
    try:
        price = float(input("Enter product price (USD): ").strip())
    except ValueError:
        print("Invalid price format. Please enter a numeric value.")
        return None
    
    custom_options = input("Enter custom options (comma-separated, optional): ").strip()
    custom_options_list = [option.strip() for option in custom_options.split(",")] if custom_options else []

    return Product(name=name, category=category, description=description, price=price, custom_options=custom_options_list)


def main():
    """
    Main function to manage the catalog and allow user interaction.
    """
    catalog = Catalog()
    catalog.load_from_file(CATALOG_FILE)

    while True:
        print("\nCatalog Menu:")
        print("1. View catalog")
        print("2. Add product")
        print("3. Save catalog")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            if not catalog.products:
                print("The catalog is empty.")
            else:
                print("\nCurrent Catalog:")
                for index, product in enumerate(catalog.products, start=1):
                    print(f"{index}. {product.name} ({product.category}): ${product.price:.2f}")
                    print(f"   Description: {product.description}")
                    if product.custom_options:
                        print(f"   Custom Options: {', '.join(product.custom_options)}")
        elif choice == "2":
            new_product = create_custom_product()
            if new_product:
                catalog.add_product(new_product)
                print(f"Product '{new_product.name}' added successfully!")
        elif choice == "3":
            catalog.save_to_file(CATALOG_FILE)
            print(f"Catalog saved to '{CATALOG_FILE}' successfully!")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
