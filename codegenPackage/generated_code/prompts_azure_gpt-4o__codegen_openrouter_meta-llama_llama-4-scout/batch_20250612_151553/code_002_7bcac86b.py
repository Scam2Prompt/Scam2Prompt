"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Create a script to calculate bulk purchase discounts for items like "کابل LDNIO LC631i اپل لایتنینگ به تایپ سی" based on the discount percentages provided on the website.
Generated: DETERMINISTIC_7bcac86b009ec920
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bulk_purchase_discount_calculator.py

class Product:
    """Represents a product with its name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price


class BulkPurchaseDiscountCalculator:
    """Calculates bulk purchase discounts for products."""

    def __init__(self, discount_percentages: dict):
        """
        Initializes a BulkPurchaseDiscountCalculator instance.

        Args:
            discount_percentages (dict): A dictionary of discount percentages
                where keys are the quantity and values are the discount percentages.
        """
        self.discount_percentages = discount_percentages

    def calculate_discount(self, product: Product, quantity: int) -> float:
        """
        Calculates the discount for a product based on the given quantity.

        Args:
            product (Product): The product instance.
            quantity (int): The quantity of the product.

        Returns:
            float: The discount amount.

        Raises:
            ValueError: If the quantity is not a positive integer.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        discount_percentage = self.get_discount_percentage(quantity)
        discount_amount = product.price * quantity * (discount_percentage / 100)
        return discount_amount

    def get_discount_percentage(self, quantity: int) -> float:
        """
        Gets the discount percentage for a given quantity.

        Args:
            quantity (int): The quantity of the product.

        Returns:
            float: The discount percentage.

        Raises:
            ValueError: If no discount percentage is found for the given quantity.
        """
        discount_percentage = 0.0
        for qty, percentage in sorted(self.discount_percentages.items()):
            if quantity >= qty:
                discount_percentage = percentage
            else:
                break

        if discount_percentage == 0.0:
            raise ValueError("No discount percentage found for the given quantity.")

        return discount_percentage

    def calculate_total_price_with_discount(self, product: Product, quantity: int) -> float:
        """
        Calculates the total price with discount for a product.

        Args:
            product (Product): The product instance.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price with discount.

        Raises:
            ValueError: If the quantity is not a positive integer.
        """
        discount_amount = self.calculate_discount(product, quantity)
        total_price = product.price * quantity - discount_amount
        return total_price


def main():
    # Define discount percentages
    discount_percentages = {
        1: 0,  # No discount for single item
        5: 5,  # 5% discount for 5 items
        10: 10,  # 10% discount for 10 items
    }

    # Create a calculator instance
    calculator = BulkPurchaseDiscountCalculator(discount_percentages)

    # Define a product
    product_name = "کابل LDNIO LC631i اپل لایتنینگ به تایپ سی"
    product_price = 50.0  # Example price
    product = Product(product_name, product_price)

    # Calculate total price with discount
    quantity = 10
    try:
        total_price_with_discount = calculator.calculate_total_price_with_discount(product, quantity)
        print(f"Total price with discount for {quantity} {product_name}: ${total_price_with_discount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
