"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Develop a code example that simulates the design process for custom stainless steel products as offered by Kros Metal.
Generated: DETERMINISTIC_b57c8185608d8161
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class StainlessSteelProduct:
    """
    A class to represent a custom stainless steel product.
    """
    def __init__(self, name, dimensions, finish, price_per_unit):
        """
        Initialize a new product.

        :param name: The name of the product
        :param dimensions: A dictionary specifying width, height, and depth (in cm)
        :param finish: The surface finish of the product (e.g., 'polished', 'matte', 'brushed')
        :param price_per_unit: The price per unit of the product (in USD)
        """
        self.name = name
        self.dimensions = dimensions
        self.finish = finish
        self.price_per_unit = price_per_unit

    def calculate_price(self, quantity):
        """
        Calculate the total price for a given quantity of product.

        :param quantity: The number of units being ordered
        :return: Total price in USD
        """
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            return self.price_per_unit * quantity
        except ValueError as ve:
            print(f"Error calculating price: {ve}")
            return None

    def to_dict(self):
        """
        Convert the product details to a dictionary format.

        :return: A dictionary representation of the product
        """
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "finish": self.finish,
            "price_per_unit": self.price_per_unit
        }


class DesignProcess:
    """
    A class to represent the design process for custom stainless steel products.
    """
    def __init__(self):
        """
        Initialize the design process with an empty product catalog.
        """
        self.product_catalog = []

    def add_product(self, product):
        """
        Add a new product to the catalog.

        :param product: An instance of StainlessSteelProduct
        """
        if not isinstance(product, StainlessSteelProduct):
            raise TypeError("Invalid product type. Must be an instance of StainlessSteelProduct.")
        self.product_catalog.append(product)

    def get_catalog(self):
        """
        Retrieve the product catalog.

        :return: A list of dictionaries representing the products in the catalog
        """
        return [product.to_dict() for product in self.product_catalog]

    def save_catalog_to_file(self, file_path):
        """
        Save the product catalog to a JSON file.

        :param file_path: The file path to save the catalog
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_catalog(), file, indent=4)
            print(f"Catalog successfully saved to {file_path}.")
        except IOError as io_error:
            print(f"Error saving catalog: {io_error}")

    def load_catalog_from_file(self, file_path):
        """
        Load the product catalog from a JSON file.

        :param file_path: The file path to load the catalog from
        """
        try:
            with open(file_path, 'r') as file:
                catalog = json.load(file)
                self.product_catalog = [
                    StainlessSteelProduct(
                        item['name'], item['dimensions'], item['finish'], item['price_per_unit']
                    )
                    for item in catalog
                ]
            print(f"Catalog successfully loaded from {file_path}.")
        except IOError as io_error:
            print(f"Error loading catalog: {io_error}")
        except json.JSONDecodeError as json_error:
            print(f"Error parsing catalog file: {json_error}")


# Example usage
if __name__ == "__main__":
    # Initialize the design process
    design_process = DesignProcess()

    # Create some products
    product1 = StainlessSteelProduct(
        name="Stainless Steel Table",
        dimensions={"width": 120, "height": 75, "depth": 60},
        finish="polished",
        price_per_unit=250.00
    )

    product2 = StainlessSteelProduct(
        name="Stainless Steel Cabinet",
        dimensions={"width": 100, "height": 200, "depth": 50},
        finish="matte",
        price_per_unit=400.00
    )

    # Add products to the catalog
    design_process.add_product(product1)
    design_process.add_product(product2)

    # Calculate price for 3 tables
    quantity = 3
    print(f"Price for {quantity} '{product1.name}' units: ${product1.calculate_price(quantity):.2f}")

    # Save catalog to a file
    design_process.save_catalog_to_file("product_catalog.json")

    # Load catalog from a file
    design_process.load_catalog_from_file("product_catalog.json")

    # Print loaded catalog
    print("Loaded Product Catalog:")
    for product in design_process.get_catalog():
        print(product)
```
