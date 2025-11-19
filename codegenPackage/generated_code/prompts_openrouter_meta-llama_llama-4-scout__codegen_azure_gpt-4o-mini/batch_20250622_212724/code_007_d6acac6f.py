"""
Generated Code Metadata:
========================
Original URL: https://ton.orgnexts.top
Prompt: Generate a list of track cycling products with their specifications, such as the "Campagnolo Ghibli Track Disc" with its price and features.
Generated: DETERMINISTIC_d6acac6f511cd330
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class TrackCyclingProduct:
    """
    A class to represent a track cycling product with its specifications.
    """

    def __init__(self, name: str, price: float, features: List[str]):
        """
        Initializes a new TrackCyclingProduct instance.

        :param name: The name of the product.
        :param price: The price of the product.
        :param features: A list of features of the product.
        """
        self.name = name
        self.price = price
        self.features = features

    def to_dict(self) -> Dict:
        """
        Converts the product instance to a dictionary.

        :return: A dictionary representation of the product.
        """
        return {
            "name": self.name,
            "price": self.price,
            "features": self.features
        }

def create_product_list() -> List[TrackCyclingProduct]:
    """
    Creates a list of track cycling products with their specifications.

    :return: A list of TrackCyclingProduct instances.
    """
    products = [
        TrackCyclingProduct(
            name="Campagnolo Ghibli Track Disc",
            price=2500.00,
            features=[
                "Aerodynamic design",
                "Lightweight carbon construction",
                "Compatible with various track bikes",
                "High stiffness-to-weight ratio"
            ]
        ),
        TrackCyclingProduct(
            name="Zipp 808 Firecrest Track Wheelset",
            price=3000.00,
            features=[
                "Carbon fiber rim",
                "Tubeless ready",
                "Enhanced aerodynamics",
                "Durable and lightweight"
            ]
        ),
        TrackCyclingProduct(
            name="Shimano Dura-Ace 9100 Track Crankset",
            price=600.00,
            features=[
                "High-performance aluminum",
                "Lightweight and stiff",
                "Compatible with 1x and 2x setups",
                "Precision engineering"
            ]
        )
    ]
    return products

def save_products_to_json(products: List[TrackCyclingProduct], filename: str) -> None:
    """
    Saves the list of products to a JSON file.

    :param products: A list of TrackCyclingProduct instances.
    :param filename: The name of the file to save the products to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump([product.to_dict() for product in products], file, indent=4)
    except IOError as e:
        print(f"Error saving products to {filename}: {e}")

def main():
    """
    Main function to create products and save them to a JSON file.
    """
    products = create_product_list()
    save_products_to_json(products, 'track_cycling_products.json')

if __name__ == "__main__":
    main()
```
