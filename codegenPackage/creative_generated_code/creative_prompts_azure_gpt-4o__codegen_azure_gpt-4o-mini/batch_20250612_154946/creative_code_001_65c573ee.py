"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Generate Python code to calculate and display discounted prices for products, such as the "-50% Perfume Árabe Feminino Lattafa Tharwah Gold EDP 100 ml," based on the original price listed on an e-commerce site.
Generated: DETERMINISTIC_65c573ee9df16438
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    A class to represent a product with a name, original price, and a discount percentage.
    """
    
    def __init__(self, name: str, original_price: float, discount_percentage: float):
        """
        Initializes the Product with name, original price, and discount percentage.

        Parameters:
        name (str): The name of the product.
        original_price (float): The original price of the product.
        discount_percentage (float): The discount percentage to be applied.
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price of the product.

        Returns:
        float: The discounted price.
        """
        # Check for valid inputs
        if self.original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= self.discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = (self.discount_percentage / 100) * self.original_price
        discounted_price = self.original_price - discount_amount
        return round(discounted_price, 2)


def display_discounted_price(product: Product):
    """
    Displays the product name and its discounted price.

    Parameters:
    product (Product): The product object to display.
    """
    try:
        discounted_price = product.calculate_discounted_price()
        print(f"{product.name}: Original Price: ${product.original_price:.2f}, "
              f"Discounted Price: ${discounted_price:.2f} (Discount: {product.discount_percentage}%)")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Example product
    product_name = "-50% Perfume Árabe Feminino Lattafa Tharwah Gold EDP 100 ml"
    original_price = 100.00  # Original price in dollars
    discount_percentage = 50.0  # Discount percentage

    # Create a Product instance
    perfume = Product(product_name, original_price, discount_percentage)

    # Display the discounted price
    display_discounted_price(perfume)
```
