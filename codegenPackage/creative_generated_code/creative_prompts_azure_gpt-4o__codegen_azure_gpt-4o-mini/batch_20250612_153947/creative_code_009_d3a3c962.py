"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write code to implement a "Deals of the Week" section for an e-commerce platform, showcasing discounted products like those on medebooks.shop.
Generated: DETERMINISTIC_d3a3c962517df7e0
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict

class Product:
    def __init__(self, id: int, name: str, price: float, discount: float, start_date: datetime, end_date: datetime):
        """
        Initializes a Product instance.

        :param id: Unique identifier for the product.
        :param name: Name of the product.
        :param price: Original price of the product.
        :param discount: Discount percentage (0-100).
        :param start_date: Date when the deal starts.
        :param end_date: Date when the deal ends.
        """
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self) -> bool:
        """
        Checks if the product's deal is currently active.

        :return: True if the deal is active, otherwise False.
        """
        current_date = datetime.now()
        return self.start_date <= current_date <= self.end_date

    def get_discounted_price(self) -> float:
        """
        Calculates the price after applying the discount.

        :return: Discounted price of the product.
        """
        return self.price * (1 - self.discount / 100)

class DealsOfTheWeek:
    def __init__(self):
        """
        Initializes the DealsOfTheWeek instance with an empty product list.
        """
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Adds a product to the Deals of the Week.

        :param product: The Product instance to add.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Must be an instance of Product.")
        self.products.append(product)

    def get_active_deals(self) -> List[Dict]:
        """
        Retrieves a list of currently active deals.

        :return: A list of dictionaries containing active product deals.
        """
        active_deals = []
        for product in self.products:
            if product.is_active():
                active_deals.append({
                    'id': product.id,
                    'name': product.name,
                    'original_price': product.price,
                    'discounted_price': product.get_discounted_price(),
                    'discount_percentage': product.discount,
                    'deal_validity': {
                        'start_date': product.start_date.strftime("%Y-%m-%d"),
                        'end_date': product.end_date.strftime("%Y-%m-%d")
                    }
                })
        return active_deals

# Example usage:
if __name__ == "__main__":
    # Initialize deals section
    deals_section = DealsOfTheWeek()

    # Sample products
    try:
        product1 = Product(1, "Wireless Mouse", 29.99, 20, datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=7))
        product2 = Product(2, "Bluetooth Headphones", 59.99, 15, datetime.now() - timedelta(days=2), datetime.now() + timedelta(days=5))
        product3 = Product(3, "Mechanical Keyboard", 89.99, 25, datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=10))

        # Add products to the Deals of the Week
        deals_section.add_product(product1)
        deals_section.add_product(product2)
        deals_section.add_product(product3)

        # Fetch active deals
        active_deals = deals_section.get_active_deals()
        
        # Output active deals
        for deal in active_deals:
            print(f"Deal: {deal['name']} - Original Price: ${deal['original_price']:.2f}, "
                  f"Discounted Price: ${deal['discounted_price']:.2f}, "
                  f"Discount: {deal['discount_percentage']}%, "
                  f"Valid from: {deal['deal_validity']['start_date']} to {deal['deal_validity']['end_date']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
