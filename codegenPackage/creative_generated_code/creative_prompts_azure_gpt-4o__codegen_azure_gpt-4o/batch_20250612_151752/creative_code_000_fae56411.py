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
import time
from datetime import datetime, timedelta


class Product:
    """
    Represents a single product in the catalog.
    """

    def __init__(self, name, category, price, stock, best_offer=False, offer_expiry=None):
        """
        Initialize a product.

        :param name: Product name (string).
        :param category: Product category (string) - e.g., 'Fruit' or 'Vegetable'.
        :param price: Product price (float).
        :param stock: Available stock (integer).
        :param best_offer: Whether the product is on a "best offer" (boolean).
        :param offer_expiry: Offer expiry time (datetime object).
        """
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.best_offer = best_offer
        self.offer_expiry = offer_expiry

    def is_offer_active(self):
        """
        Check if the best offer is currently active.

        :return: True if offer is active, False otherwise.
        """
        if self.best_offer and self.offer_expiry:
            return datetime.now() < self.offer_expiry
        return False

    def time_until_offer_expires(self):
        """
        Calculate the time remaining until the offer expires.

        :return: Time remaining as a string (e.g., "2 hours, 15 minutes").
        """
        if self.is_offer_active():
            remaining = self.offer_expiry - datetime.now()
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            return f"{remaining.days} days, {hours} hours, {minutes} minutes"
        return "Offer expired"


class Catalog:
    """
    Represents the product catalog.
    """

    def __init__(self):
        """
        Initialize an empty catalog.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        :param product: An instance of Product.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Must be an instance of Product class.")
        self.products.append(product)

    def list_products(self):
        """
        List all products in the catalog with their details.

        :return: A list of formatted product details (string).
        """
        if not self.products:
            return ["No products available."]
        return [self.format_product_details(product) for product in self.products]

    def format_product_details(self, product):
        """
        Format product details for display.

        :param product: An instance of Product.
        :return: A string with product details.
        """
        details = f"Name: {product.name}\n" \
                  f"Category: {product.category}\n" \
                  f"Price: ${product.price:.2f}\n" \
                  f"Stock: {product.stock}\n"
        if product.is_offer_active():
            details += f"Offer Active! Time Remaining: {product.time_until_offer_expires()}\n"
        elif product.best_offer:
            details += "Offer Expired.\n"
        return details

    def search_by_category(self, category):
        """
        Search for products by category.

        :param category: Category name (string).
        :return: A list of formatted product details matching the category.
        """
        matching_products = [product for product in self.products if product.category.lower() == category.lower()]
        if not matching_products:
            return [f"No products found for category: {category}"]
        return [self.format_product_details(product) for product in matching_products]


# Example usage
if __name__ == "__main__":
    # Create catalog
    catalog = Catalog()

    # Add products to catalog
    catalog.add_product(Product("Apple", "Fruit", 1.50, 100, True, datetime.now() + timedelta(hours=3)))
    catalog.add_product(Product("Banana", "Fruit", 0.75, 200, False))
    catalog.add_product(Product("Carrot", "Vegetable", 0.50, 300, True, datetime.now() + timedelta(days=1)))

    # List all products
    print("All Products:")
    for product_details in catalog.list_products():
        print(product_details)

    # Search by category
    print("\nFruits:")
    for product_details in catalog.search_by_category("Fruit"):
        print(product_details)

    print("\nVegetables:")
    for product_details in catalog.search_by_category("Vegetable"):
        print(product_details)

    # Simulate passage of time for testing
    print("\nSimulating time passage...")
    time.sleep(2)  # Simulated delay
    print("All Products After Time Passage:")
    for product_details in catalog.list_products():
        print(product_details)
```
