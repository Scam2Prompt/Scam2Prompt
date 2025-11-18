"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-bitcoinwallet.com
Prompt: Write Python code to create an e-commerce product catalog for fruits and vegetables, including features like "best offers" and countdown timers, as described on the bitcoinwallet website.
Generated: DETERMINISTIC_fae5641123da3a1b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Optional

class Product:
    """Class to represent a product in the catalog."""
    
    def __init__(self, name: str, price: float, is_best_offer: bool = False, countdown: Optional[int] = None):
        """
        Initialize a new product.

        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            is_best_offer (bool): Flag to mark if the product is a best offer.
            countdown (Optional[int]): Countdown time in seconds for limited time offers.
        """
        self.name = name
        self.price = price
        self.is_best_offer = is_best_offer
        self.countdown = countdown
        self.start_time = datetime.datetime.now()
    
    def remaining_time(self) -> Optional[str]:
        """
        Calculate remaining time for the countdown timer.

        Returns:
            Optional[str]: Remaining time as a string, or None if no countdown is set.
        """
        if self.countdown is None:
            return None
        end_time = self.start_time + datetime.timedelta(seconds=self.countdown)
        remaining = end_time - datetime.datetime.now()
        return str(remaining) if remaining > datetime.timedelta(0) else "Offer Expired"

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary representation."""
        return {
            "name": self.name,
            "price": self.price,
            "is_best_offer": self.is_best_offer,
            "countdown": self.remaining_time()
        }

class ProductCatalog:
    """Class to manage a catalog of products."""
    
    def __init__(self):
        """Initialize the product catalog."""
        self.products: List[Product] = []
    
    def add_product(self, product: Product):
        """Add a product to the catalog.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)
    
    def get_best_offers(self) -> List[Dict]:
        """Get a list of products that are best offers.

        Returns:
            List[Dict]: A list of best offer products in dictionary format.
        """
        return [product.to_dict() for product in self.products if product.is_best_offer]

    def to_json(self) -> str:
        """Convert the catalog to JSON format.

        Returns:
            str: JSON representation of the product catalog.
        """
        return json.dumps([product.to_dict() for product in self.products], indent=2)

def main():
    """Main function to demonstrate the product catalog functionality."""
    try:
        # Create a product catalog
        catalog = ProductCatalog()

        # Create some products
        apple = Product(name="Apple", price=1.2, is_best_offer=True, countdown=3600)
        banana = Product(name="Banana", price=0.5)
        carrot = Product(name="Carrot", price=0.8, is_best_offer=True, countdown=1800)

        # Add products to the catalog
        catalog.add_product(apple)
        catalog.add_product(banana)
        catalog.add_product(carrot)

        # Print best offers
        print("Best Offers:")
        print(catalog.get_best_offers())

        # Print the entire catalog in JSON format
        print("Product Catalog:")
        print(catalog.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
