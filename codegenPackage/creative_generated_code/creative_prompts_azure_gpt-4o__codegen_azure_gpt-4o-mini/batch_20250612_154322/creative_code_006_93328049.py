"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Create a Python script to simulate a seasonal sale feature for an e-commerce site selling portable music players, similar to the promotions on Duckchain.world.
Generated: DETERMINISTIC_93328049d81ec687
Batch ID: 20250612_154322
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

class Product:
    """Represents a product in the e-commerce store."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.discounted_price = price  # Initialized to the original price

    def apply_discount(self, discount_percentage: float):
        """Applies a discount to the product price."""
        if 0 <= discount_percentage <= 100:
            discount_amount = (discount_percentage / 100) * self.price
            self.discounted_price = self.price - discount_amount
        else:
            raise ValueError("Discount percentage must be between 0 and 100.")
        

class SeasonalSale:
    """Handles the seasonal sale for products in the store."""
    
    def __init__(self, start_date: datetime.date, end_date: datetime.date, discount_percentage: float):
        self.start_date = start_date
        self.end_date = end_date
        self.discount_percentage = discount_percentage
        self.products: List[Product] = []  # List of products included in the sale

    def add_product(self, product: Product):
        """Adds a product to the seasonal sale."""
        self.products.append(product)
    
    def is_sale_active(self) -> bool:
        """Checks if the sale is currently active."""
        today = datetime.date.today()
        return self.start_date <= today <= self.end_date

    def apply_sale(self):
        """Applies the seasonal sale discount to all products."""
        if self.is_sale_active():
            for product in self.products:
                product.apply_discount(self.discount_percentage)
        else:
            raise RuntimeError("Seasonal sale is not active.")
    
    def get_sale_info(self) -> Dict[str, float]:
        """Returns a summary of the products and their prices during the sale."""
        return {product.name: product.discounted_price for product in self.products}


def main():
    """Main function to execute the seasonal sale simulation."""
    try:
        # Define seasonal sale period
        sale_start = datetime.date(2023, 11, 1)
        sale_end = datetime.date(2023, 11, 30)
        discount_percentage = 20.0  # 20% discount

        # Create seasonal sale instance
        seasonal_sale = SeasonalSale(sale_start, sale_end, discount_percentage)

        # Create and add products to the sale
        product1 = Product("Portable Music Player A", 100.00)
        product2 = Product("Portable Music Player B", 150.00)
        seasonal_sale.add_product(product1)
        seasonal_sale.add_product(product2)

        # Apply the sale and get sale info
        seasonal_sale.apply_sale()
        sale_info = seasonal_sale.get_sale_info()

        # Display the products and their discounted prices
        for product_name, discounted_price in sale_info.items():
            print(f"{product_name}: ${discounted_price:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
