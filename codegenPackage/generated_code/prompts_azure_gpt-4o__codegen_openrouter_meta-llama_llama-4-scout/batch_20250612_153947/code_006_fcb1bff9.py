"""
Generated Code Metadata:
========================
Original URL: https://medebooks.shop
Prompt: Write a script to manage and display discounted prices for products, ensuring discounts are applied dynamically based on the original price, as seen on medebooks.shop.
Generated: DETERMINISTIC_fcb1bff9494a9ddd
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product.py

class Product:
    """
    Represents a product with an original price and a discount.
    """

    def __init__(self, name: str, original_price: float, discount_percentage: float = 0):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            original_price (float): The original price of the product.
            discount_percentage (float, optional): The discount percentage. Defaults to 0.
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    @property
    def discounted_price(self) -> float:
        """
        Calculates the discounted price dynamically.

        Returns:
            float: The discounted price.
        """
        return self.original_price * (1 - self.discount_percentage / 100)

    def __str__(self):
        return f"{self.name}: ${self.original_price:.2f} (Discount: {self.discount_percentage}%)"


class ProductManager:
    """
    Manages a collection of products and displays their discounted prices.
    """

    def __init__(self):
        """
        Initializes a ProductManager instance.
        """
        self.products = []

    def add_product(self, product: Product):
        """
        Adds a product to the collection.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def display_products(self):
        """
        Displays the products with their discounted prices.
        """
        for product in self.products:
            print(f"Original Price: ${product.original_price:.2f}")
            print(f"Discounted Price: ${product.discounted_price:.2f}")
            print(product)
            print("------------------------")

    def update_discount(self, product_name: str, new_discount_percentage: float):
        """
        Updates the discount percentage for a specific product.

        Args:
            product_name (str): The name of the product to update.
            new_discount_percentage (float): The new discount percentage.

        Raises:
            ValueError: If the product is not found.
        """
        for product in self.products:
            if product.name == product_name:
                product.discount_percentage = new_discount_percentage
                return
        raise ValueError("Product not found")


def main():
    # Create a product manager
    manager = ProductManager()

    # Create products
    product1 = Product("Book 1", 100, 20)
    product2 = Product("Book 2", 200, 10)

    # Add products to the manager
    manager.add_product(product1)
    manager.add_product(product2)

    # Display products with discounted prices
    manager.display_products()

    # Update discount for a product
    manager.update_discount("Book 1", 30)

    # Display updated products with discounted prices
    print("After updating discount:")
    manager.display_products()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
