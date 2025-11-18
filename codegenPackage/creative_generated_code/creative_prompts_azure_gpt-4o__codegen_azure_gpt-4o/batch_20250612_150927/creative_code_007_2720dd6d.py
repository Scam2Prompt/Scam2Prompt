"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Write code to generate product listings with detailed descriptions, including items like "гидрокостюм AquaDiscovery VOEVODA" and "сумка Beuchat Voyager XL," as featured on acula.com.ua.
Generated: DETERMINISTIC_2720dd6dd7cce611
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class Product:
    """
    A class to represent a product listing with detailed descriptions.
    """
    def __init__(self, name, description, price, stock_quantity):
        """
        Initialize a Product instance.
        
        :param name: Name of the product
        :param description: Detailed description of the product
        :param price: Price of the product in USD
        :param stock_quantity: Quantity of the product in stock
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID for the product
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        """
        String representation of a product instance.
        """
        return (f"Product ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price:.2f}\n"
                f"Stock Quantity: {self.stock_quantity}")


class ProductGenerator:
    """
    A class to generate and manage a collection of product listings.
    """
    def __init__(self):
        """
        Initialize a ProductGenerator instance with an empty list of products.
        """
        self.products = []

    def add_product(self, name, description, price, stock_quantity):
        """
        Add a new product to the collection.
        
        :param name: Name of the product
        :param description: Detailed description of the product
        :param price: Price of the product in USD
        :param stock_quantity: Quantity of the product in stock
        """
        if price < 0 or stock_quantity < 0:
            raise ValueError("Price and stock quantity cannot be negative.")
        
        product = Product(name, description, price, stock_quantity)
        self.products.append(product)

    def list_products(self):
        """
        List all products in the collection.
        
        :return: A list of product string representations
        """
        return [str(product) for product in self.products]


# Main script
if __name__ == "__main__":
    try:
        # Initialize the product generator
        product_generator = ProductGenerator()

        # Add products to the collection
        product_generator.add_product(
            name="гидрокостюм AquaDiscovery VOEVODA",
            description="Гидрокостюм AquaDiscovery VOEVODA - идеальный выбор для подводной охоты и дайвинга.",
            price=249.99,
            stock_quantity=10
        )
        product_generator.add_product(
            name="сумка Beuchat Voyager XL",
            description="Сумка Beuchat Voyager XL - вместительная и удобная сумка для оборудования.",
            price=89.99,
            stock_quantity=5
        )

        # List all products
        for product_listing in product_generator.list_products():
            print(product_listing)
            print("-" * 40)  # Separator for readability

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
