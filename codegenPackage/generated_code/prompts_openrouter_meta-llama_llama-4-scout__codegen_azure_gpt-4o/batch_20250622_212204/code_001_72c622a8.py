"""
Generated Code Metadata:
========================
Original URL: https://pancakefarm.com
Prompt: Generate a product list for a farm that specializes in naturally reared meat, similar to Pancake Farm's offerings.
Generated: DETERMINISTIC_72c622a80e6dd055
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FarmProduct:
    """
    Represents a product offered by the farm.
    """
    def __init__(self, name, category, price_per_unit, unit):
        """
        Initialize a farm product.

        :param name: Name of the product (e.g., "Grass-fed Beef")
        :param category: Category of the product (e.g., "Meat")
        :param price_per_unit: Price per unit of the product (e.g., 12.99)
        :param unit: Unit of measurement (e.g., "lb")
        """
        self.name = name
        self.category = category
        self.price_per_unit = price_per_unit
        self.unit = unit

    def to_dict(self):
        """
        Convert the product to a dictionary for serialization.

        :return: Dictionary representation of the product.
        """
        return {
            "name": self.name,
            "category": self.category,
            "price_per_unit": self.price_per_unit,
            "unit": self.unit
        }


class FarmProductList:
    """
    Manages a list of farm products.
    """
    def __init__(self):
        """
        Initialize an empty product list.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the list.

        :param product: Instance of FarmProduct to add.
        """
        if not isinstance(product, FarmProduct):
            raise TypeError("Expected a FarmProduct instance.")
        self.products.append(product)

    def generate_product_list(self):
        """
        Generate a list of products in JSON format.

        :return: JSON string representing the product list.
        """
        return json.dumps([product.to_dict() for product in self.products], indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Create a farm product list
        farm_product_list = FarmProductList()

        # Add products to the list
        farm_product_list.add_product(FarmProduct("Grass-fed Beef", "Meat", 12.99, "lb"))
        farm_product_list.add_product(FarmProduct("Free-range Chicken", "Meat", 8.99, "lb"))
        farm_product_list.add_product(FarmProduct("Pasture-raised Pork", "Meat", 10.99, "lb"))
        farm_product_list.add_product(FarmProduct("Farm Fresh Eggs", "Eggs", 4.99, "dozen"))

        # Generate and print the product list in JSON format
        print(farm_product_list.generate_product_list())
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
