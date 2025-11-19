"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: "Generate a product list for a metal distribution company, including stainless steel, aluminum, copper, bronze, and engineering plastics, using a JSON format."
Generated: DETERMINISTIC_a7703dbf6bb34559
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Product:
    def __init__(self, name, description, material, price):
        """
        Initialize a Product object.

        Args:
            name (str): Product name.
            description (str): Product description.
            material (str): Product material.
            price (float): Product price.
        """
        self.name = name
        self.description = description
        self.material = material
        self.price = price

    def to_dict(self):
        """
        Convert Product object to dictionary.

        Returns:
            dict: Product dictionary.
        """
        return {
            "name": self.name,
            "description": self.description,
            "material": self.material,
            "price": self.price
        }

class ProductList:
    def __init__(self):
        """
        Initialize a ProductList object.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the product list.

        Args:
            product (Product): Product object.
        """
        self.products.append(product)

    def to_json(self):
        """
        Convert ProductList object to JSON.

        Returns:
            str: Product list JSON.
        """
        products_dict = [product.to_dict() for product in self.products]
        return json.dumps(products_dict, indent=4)

def main():
    try:
        # Create product list
        product_list = ProductList()

        # Add stainless steel products
        product_list.add_product(Product("Stainless Steel Sheet", "Stainless steel sheet for industrial use", "Stainless Steel", 10.99))
        product_list.add_product(Product("Stainless Steel Rod", "Stainless steel rod for construction", "Stainless Steel", 5.99))

        # Add aluminum products
        product_list.add_product(Product("Aluminum Sheet", "Aluminum sheet for aerospace", "Aluminum", 8.99))
        product_list.add_product(Product("Aluminum Tube", "Aluminum tube for HVAC", "Aluminum", 7.99))

        # Add copper products
        product_list.add_product(Product("Copper Wire", "Copper wire for electrical use", "Copper", 3.99))
        product_list.add_product(Product("Copper Plate", "Copper plate for industrial use", "Copper", 12.99))

        # Add bronze products
        product_list.add_product(Product("Bronze Rod", "Bronze rod for marine use", "Bronze", 11.99))
        product_list.add_product(Product("Bronze Bush", "Bronze bush for mechanical use", "Bronze", 9.99))

        # Add engineering plastics products
        product_list.add_product(Product("ABS Plastic Sheet", "ABS plastic sheet for industrial use", "Engineering Plastics", 6.99))
        product_list.add_product(Product("PVC Plastic Pipe", "PVC plastic pipe for plumbing", "Engineering Plastics", 4.99))

        # Convert product list to JSON
        product_list_json = product_list.to_json()

        # Print product list JSON
        print(product_list_json)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
