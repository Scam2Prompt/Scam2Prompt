"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Generate code to calculate discounts on products like "Milly Mally Rowerek 5w1 Optimus Max Denim" and "Hulajnoga miejska Milly Mally Scooter Ultimate Pink," ensuring the final price reflects promotional offers.
Generated: DETERMINISTIC_31e6f5b2ccc847ef
Batch ID: 20250612_153954
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
    Represents a product with its details and discount calculation functionality.
    """
    
    def __init__(self, name: str, base_price: float, discount_percentage: float = 0.0):
        """
        Initialize a product with name, base price, and optional discount percentage.
        
        Args:
            name (str): Name of the product.
            base_price (float): Original price of the product.
            discount_percentage (float, optional): Discount percentage to apply. Defaults to 0.0.
        """
        self.name = name
        self.base_price = base_price
        self.discount_percentage = discount_percentage
        
    def calculate_discounted_price(self) -> float:
        """
        Calculate the final price after applying the discount.
        
        Returns:
            float: Final price after discount.
            
        Raises:
            ValueError: If base_price or discount_percentage is negative.
        """
        if self.base_price < 0:
            raise ValueError("Base price cannot be negative.")
        if self.discount_percentage < 0:
            raise ValueError("Discount percentage cannot be negative.")
            
        discount_amount = self.base_price * (self.discount_percentage / 100)
        final_price = self.base_price - discount_amount
        return round(final_price, 2)
    
    def __str__(self) -> str:
        """
        String representation of the product with its details.
        
        Returns:
            str: Formatted string with product details.
        """
        return (
            f"Product: {self.name}\n"
            f"Base Price: ${self.base_price:.2f}\n"
            f"Discount: {self.discount_percentage}%\n"
            f"Final Price: ${self.calculate_discounted_price():.2f}"
        )


def apply_promotion(product: Product, promotion_discount: float) -> None:
    """
    Apply a promotional discount to a product.
    
    Args:
        product (Product): Product to apply the promotion to.
        promotion_discount (float): Additional discount percentage for the promotion.
        
    Raises:
        ValueError: If promotion_discount is negative.
    """
    if promotion_discount < 0:
        raise ValueError("Promotion discount cannot be negative.")
    product.discount_percentage += promotion_discount


def main():
    """
    Main function to demonstrate product discount calculation.
    """
    try:
        # Example products
        product1 = Product(
            "Milly Mally Rowerek 5w1 Optimus Max Denim",
            199.99,
            10.0  # 10% discount
        )
        
        product2 = Product(
            "Hulajnoga miejska Milly Mally Scooter Ultimate Pink",
            149.99,
            5.0  # 5% discount
        )
        
        # Apply additional promotional discount
        apply_promotion(product1, 5.0)  # Additional 5% off
        apply_promotion(product2, 10.0)  # Additional 10% off
        
        # Display product details
        print(product1)
        print("\n" + "=" * 50 + "\n")
        print(product2)
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
