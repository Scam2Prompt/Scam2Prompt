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
import datetime
from typing import List, Dict

# Define a Product class to represent individual products
class Product:
    def __init__(self, id: int, name: str, original_price: float, discount_percentage: float):
        """
        Initialize a product with its details.
        :param id: Unique identifier for the product
        :param name: Name of the product
        :param original_price: Original price of the product
        :param discount_percentage: Discount percentage applied to the product
        """
        self.id = id
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage
        self.discounted_price = self.calculate_discounted_price()

    def calculate_discounted_price(self) -> float:
        """
        Calculate the discounted price based on the original price and discount percentage.
        :return: Discounted price
        """
        return round(self.original_price * (1 - self.discount_percentage / 100), 2)

    def to_dict(self) -> Dict:
        """
        Convert product details to a dictionary format for easier serialization.
        :return: Product details as a dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "original_price": self.original_price,
            "discount_percentage": self.discount_percentage,
            "discounted_price": self.discounted_price
        }

# Define the DealsOfTheWeek class to manage and showcase discounted products
class DealsOfTheWeek:
    def __init__(self):
        """
        Initialize the DealsOfTheWeek section with an empty list of products.
        """
        self.products: List[Product] = []
        self.start_date: datetime.date = datetime.date.today()
        self.end_date: datetime.date = self.start_date + datetime.timedelta(days=7)

    def add_product(self, product: Product):
        """
        Add a product to the Deals of the Week section.
        :param product: Product instance to be added
        """
        if product.discount_percentage <= 0 or product.discount_percentage > 100:
            raise ValueError("Discount percentage must be between 1 and 100.")
        self.products.append(product)

    def get_deals(self) -> List[Dict]:
        """
        Retrieve all products in the Deals of the Week section as a list of dictionaries.
        :return: List of products with their details
        """
        return [product.to_dict() for product in self.products]

    def is_active(self) -> bool:
        """
        Check if the Deals of the Week section is currently active.
        :return: True if active, False otherwise
        """
        today = datetime.date.today()
        return self.start_date <= today <= self.end_date

# Example Usage
if __name__ == "__main__":
    try:
        # Instantiate the DealsOfTheWeek section
        deals_section = DealsOfTheWeek()

        # Create sample products
        product1 = Product(id=1, name="Book A", original_price=20.0, discount_percentage=30)
        product2 = Product(id=2, name="Book B", original_price=15.0, discount_percentage=40)
        
        # Add products to the Deals of the Week section
        deals_section.add_product(product1)
        deals_section.add_product(product2)

        # Display the Deals of the Week if active
        if deals_section.is_active():
            print("Deals of the Week (Active):")
            for deal in deals_section.get_deals():
                print(deal)
        else:
            print("Deals of the Week is not currently active.")
    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
```
