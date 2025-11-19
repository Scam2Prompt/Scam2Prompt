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
# discounted_price_calculator.py

class Product:
    """Represents a product with an original price and discount."""

    def __init__(self, name: str, original_price: float, discount_percentage: float):
        """
        Initializes a Product instance.

        Args:
        - name (str): The product name.
        - original_price (float): The original price of the product.
        - discount_percentage (float): The discount percentage.

        Raises:
        - ValueError: If the original price or discount percentage is invalid.
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price.

        Returns:
        - float: The discounted price.
        """
        discount_amount = self.original_price * (self.discount_percentage / 100)
        return self.original_price - discount_amount

    def __str__(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
        - str: The product details.
        """
        discounted_price = self.calculate_discounted_price()
        return f"{self.name}\nOriginal Price: R${self.original_price:.2f}\nDiscount: -{self.discount_percentage}%\nDiscounted Price: R${discounted_price:.2f}"


def main():
    try:
        # Example usage:
        product_name = "-50% Perfume Árabe Feminino Lattafa Tharwah Gold EDP 100 ml"
        original_price = 200.00  # Original price in local currency (e.g., Brazilian Real)
        discount_percentage = 50.0  # Discount percentage

        product = Product(product_name, original_price, discount_percentage)
        print(product)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
