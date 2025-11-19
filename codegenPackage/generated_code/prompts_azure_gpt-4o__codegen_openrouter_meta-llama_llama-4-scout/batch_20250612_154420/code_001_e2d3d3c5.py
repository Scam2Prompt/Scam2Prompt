"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Create a JSON structure to organize the food products listed on the Homefoods Ghana website, including categories like "Processed Root Grains" and "Natural Sweeteners."
Generated: DETERMINISTIC_e2d3d3c55ba354b0
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FoodProduct:
    """Represents a food product with its details."""

    def __init__(self, name, description, category, price):
        """
        Initializes a FoodProduct instance.

        Args:
            name (str): Name of the food product.
            description (str): Description of the food product.
            category (str): Category of the food product.
            price (float): Price of the food product.
        """
        self.name = name
        self.description = description
        self.category = category
        self.price = price

    def to_dict(self):
        """Converts the FoodProduct instance to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "price": self.price,
        }


class FoodProductOrganizer:
    """Organizes food products into categories."""

    def __init__(self):
        """Initializes a FoodProductOrganizer instance."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a food product to the organizer.

        Args:
            product (FoodProduct): Food product to add.
        """
        if product.category not in self.products:
            self.products[product.category] = []
        self.products[product.category].append(product.to_dict())

    def to_json(self):
        """Converts the food products to a JSON string."""
        data = {}
        for category, products in self.products.items():
            data[category] = products
        return json.dumps(data, indent=4)


def main():
    # Create food products
    product1 = FoodProduct(
        "Pounded Cassava",
        "A traditional Ghanaian dish made from cassava tubers.",
        "Processed Root Grains",
        5.99,
    )
    product2 = FoodProduct(
        "Honey",
        "A natural sweetener produced by bees.",
        "Natural Sweeteners",
        7.99,
    )
    product3 = FoodProduct(
        "Banku Mix",
        "A pre-mixed powder for making banku, a traditional Ghanaian dish.",
        "Processed Root Grains",
        3.99,
    )

    # Create food product organizer
    organizer = FoodProductOrganizer()

    # Add products to organizer
    organizer.add_product(product1)
    organizer.add_product(product2)
    organizer.add_product(product3)

    # Convert to JSON
    json_string = organizer.to_json()

    # Print JSON
    print(json_string)


if __name__ == "__main__":
    main()
```
