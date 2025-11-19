"""
Generated Code Metadata:
========================
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Generate Python code to calculate and display discounted prices for products, such as the "-50% Perfume Árabe Feminino Lattafa Tharwah Gold EDP 100 ml," based on the original price listed on an e-commerce site.
Generated: DETERMINISTIC_65c573ee9df16438
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    A class to represent a product with a name, original price, and discount percentage.
    """

    def __init__(self, name: str, original_price: float, discount_percentage: float):
        """
        Initializes a new Product instance.

        :param name: The name of the product.
        :param original_price: The original price of the product.
        :param discount_percentage: The discount percentage to apply.
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price of the product.

        :return: The discounted price.
        :raises ValueError: If the original price or discount percentage is negative.
        """
        if self.original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= self.discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = (self.discount_percentage / 100) * self.original_price
        discounted_price = self.original_price - discount_amount
        return discounted_price

    def display_product_info(self) -> None:
        """
        Displays the product information including the original price and discounted price.
        """
        try:
            discounted_price = self.calculate_discounted_price()
            print(f"Product: {self.name}")
            print(f"Original Price: ${self.original_price:.2f}")
            print(f"Discount: {self.discount_percentage}%")
            print(f"Discounted Price: ${discounted_price:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """
    Main function to create a product and display its discounted price.
    """
    # Example product
    product_name = "-50% Perfume Árabe Feminino Lattafa Tharwah Gold EDP 100 ml"
    original_price = 100.00  # Original price in dollars
    discount_percentage = 50.0  # Discount percentage

    # Create a Product instance
    product = Product(product_name, original_price, discount_percentage)

    # Display product information
    product.display_product_info()


if __name__ == "__main__":
    main()
```
