"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Generate code to automate the selection of industrial belts from KOVE INDUSTRIAL's product categories, including anti-abrasive and FDA food-grade options.
Generated: DETERMINISTIC_cb03e8e9065d639c
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BeltSelector:
    """
    A class to automate the selection of industrial belts from KOVE INDUSTRIAL's product categories.
    Includes support for anti-abrasive and FDA food-grade options.
    """

    def __init__(self, product_catalog_path):
        """
        Initializes the BeltSelector with the product catalog.

        :param product_catalog_path: Path to the JSON file containing belt product categories.
        """
        self.product_catalog_path = product_catalog_path
        self.products = self.load_product_catalog()

    def load_product_catalog(self):
        """
        Loads the product catalog from a JSON file.

        :return: Dictionary of products.
        :raises FileNotFoundError: If the file doesn't exist.
        :raises json.JSONDecodeError: If the JSON file is invalid.
        """
        try:
            with open(self.product_catalog_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Product catalog file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in product catalog file.")

    def select_belt(self, belt_type):
        """
        Selects a belt based on the specified type.

        :param belt_type: Type of belt to select ('anti-abrasive' or 'FDA food-grade').
        :return: List of belts matching the given type.
        :raises ValueError: If the belt type is invalid or no matching belts are found.
        """
        if belt_type not in ['anti-abrasive', 'FDA food-grade']:
            raise ValueError("Invalid belt type. Choose either 'anti-abrasive' or 'FDA food-grade'.")

        matching_belts = [product for product in self.products if product.get('category') == belt_type]

        if not matching_belts:
            raise ValueError(f"No belts found for the category: {belt_type}")

        return matching_belts


def main():
    """
    Main function to demonstrate the belt selection process.
    """
    # Path to the product catalog file (JSON format)
    product_catalog_path = "product_catalog.json"

    try:
        # Initialize the BeltSelector
        selector = BeltSelector(product_catalog_path)

        # Example: Select anti-abrasive belts
        anti_abrasive_belts = selector.select_belt('anti-abrasive')
        print("Anti-abrasive belts:")
        for belt in anti_abrasive_belts:
            print(f"- {belt['name']}: {belt['description']}")

        # Example: Select FDA food-grade belts
        fda_food_grade_belts = selector.select_belt('FDA food-grade')
        print("\nFDA food-grade belts:")
        for belt in fda_food_grade_belts:
            print(f"- {belt['name']}: {belt['description']}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

**Note**: You need to provide a JSON file named `product_catalog.json` with structured data containing belt products and their categories (`anti-abrasive`, `FDA food-grade`, etc.). Example:

```json
[
    {
        "name": "Anti-Abrasive Belt A",
        "category": "anti-abrasive",
        "description": "High durability belt suitable for abrasive environments."
    },
    {
        "name": "FDA Food-Grade Belt B",
        "category": "FDA food-grade",
        "description": "Safe for food processing applications."
    }
]
```
