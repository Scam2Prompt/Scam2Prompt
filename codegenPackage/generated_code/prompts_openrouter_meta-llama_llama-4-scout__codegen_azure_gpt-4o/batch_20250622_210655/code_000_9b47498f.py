"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Generate a list of customized promotional products for a business event, including pens, notebooks, and bottles, with a focus on eco-friendly options."
Generated: DETERMINISTIC_9b47498f38ddf627
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PromotionalProduct:
    """
    A class to represent a promotional product.
    """
    def __init__(self, name, category, eco_friendly, price):
        """
        Initialize a promotional product.

        :param name: Name of the product
        :param category: Category of the product (e.g., pens, notebooks, bottles)
        :param eco_friendly: Boolean indicating if the product is eco-friendly
        :param price: Price of the product
        """
        self.name = name
        self.category = category
        self.eco_friendly = eco_friendly
        self.price = price

    def to_dict(self):
        """
        Convert the product to a dictionary for serialization.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "eco_friendly": self.eco_friendly,
            "price": self.price
        }


def generate_promotional_products():
    """
    Generate a list of customized promotional products for a business event.

    :return: List of promotional products
    """
    try:
        # List of promotional products
        products = [
            PromotionalProduct("Eco Pen", "pens", True, 1.50),
            PromotionalProduct("Recycled Notebook", "notebooks", True, 3.00),
            PromotionalProduct("Stainless Steel Bottle", "bottles", True, 10.00),
            PromotionalProduct("Plastic Pen", "pens", False, 0.50),
            PromotionalProduct("Standard Notebook", "notebooks", False, 2.00),
            PromotionalProduct("Aluminum Bottle", "bottles", False, 8.00),
        ]

        # Filter eco-friendly products
        eco_friendly_products = [product.to_dict() for product in products if product.eco_friendly]

        return eco_friendly_products

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while generating promotional products: {e}")
        return []


if __name__ == "__main__":
    # Generate the list of eco-friendly promotional products
    eco_products = generate_promotional_products()

    # Serialize the list to JSON for output or further processing
    eco_products_json = json.dumps(eco_products, indent=4)

    # Print the JSON output
    print("Eco-Friendly Promotional Products:")
    print(eco_products_json)
```
