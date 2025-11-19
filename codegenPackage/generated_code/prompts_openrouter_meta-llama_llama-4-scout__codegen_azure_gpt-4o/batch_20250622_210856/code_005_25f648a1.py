"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write a short program to determine the optimal storage and transportation conditions for cosmetic products, based on Fabricare Cosmeticos' logistics and quality control procedures.
Generated: DETERMINISTIC_25f648a1329bb591
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CosmeticProduct:
    """
    Class to represent a cosmetic product and its storage/transportation conditions.
    """
    def __init__(self, name, temperature_range, humidity_range, fragile):
        """
        Initialize a cosmetic product with its properties.

        :param name: Name of the product
        :param temperature_range: Tuple indicating optimal temperature range (min, max) in Celsius
        :param humidity_range: Tuple indicating optimal humidity range (min, max) in percentage
        :param fragile: Boolean indicating if the product is fragile
        """
        self.name = name
        self.temperature_range = temperature_range
        self.humidity_range = humidity_range
        self.fragile = fragile

    def get_optimal_conditions(self):
        """
        Returns a dictionary of optimal storage and transportation conditions for the product.

        :return: Dictionary containing optimal conditions
        """
        return {
            "temperature_range": self.temperature_range,
            "humidity_range": self.humidity_range,
            "fragile": self.fragile
        }


def load_products_from_file(file_path):
    """
    Load cosmetic products from a JSON file.

    :param file_path: Path to the JSON file containing product data
    :return: List of CosmeticProduct objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            products = [
                CosmeticProduct(
                    name=item['name'],
                    temperature_range=tuple(item['temperature_range']),
                    humidity_range=tuple(item['humidity_range']),
                    fragile=item['fragile']
                )
                for item in data
            ]
            return products
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file")
        return []
    except KeyError as e:
        print(f"Error: Missing key in product data - {e}")
        return []


def display_optimal_conditions(products):
    """
    Display optimal storage and transportation conditions for a list of products.

    :param products: List of CosmeticProduct objects
    """
    if not products:
        print("No products available to display.")
        return

    print("Optimal Storage and Transportation Conditions:")
    for product in products:
        conditions = product.get_optimal_conditions()
        print(f"Product: {product.name}")
        print(f"  Temperature Range: {conditions['temperature_range'][0]}°C to {conditions['temperature_range'][1]}°C")
        print(f"  Humidity Range: {conditions['humidity_range'][0]}% to {conditions['humidity_range'][1]}%")
        print(f"  Fragile: {'Yes' if conditions['fragile'] else 'No'}")
        print()


if __name__ == "__main__":
    # File path to the JSON data (replace with actual file path)
    file_path = "cosmetic_products.json"

    # Load products from file
    products = load_products_from_file(file_path)

    # Display optimal conditions
    display_optimal_conditions(products)
```

### Example JSON File (`cosmetic_products.json`):
```json
[
    {
        "name": "Moisturizing Cream",
        "temperature_range": [5, 25],
        "humidity_range": [30, 50],
        "fragile": true
    },
    {
        "name": "Lipstick",
        "temperature_range": [10, 30],
        "humidity_range": [20, 60],
        "fragile": false
    }
]
```
