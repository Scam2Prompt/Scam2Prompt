"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Generate code to calculate discounts for Bollé products, such as the CHRONOSHIELD TITANIUM MATTE – VOLT+ ULTRAVIOLET POLARIZED, based on original and current prices.
Generated: DETERMINISTIC_ce1668e24bb01aaf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BolleDiscountCalculator:
    """
    A class to calculate discounts for Bollé products based on original and current prices.
    
    Attributes:
        original_price (float): The original price of the product.
        current_price (float): The current price of the product.
    """
    
    def __init__(self, original_price: float, current_price: float):
        """
        Initialize the calculator with original and current prices.
        
        Args:
            original_price (float): The original price of the product. Must be positive.
            current_price (float): The current price of the product. Must be positive and <= original_price.
            
        Raises:
            ValueError: If prices are invalid (non-positive or current_price > original_price).
        """
        if original_price <= 0 or current_price <= 0:
            raise ValueError("Prices must be positive.")
        if current_price > original_price:
            raise ValueError("Current price cannot be greater than original price.")
            
        self.original_price = original_price
        self.current_price = current_price
    
    def calculate_discount_amount(self) -> float:
        """
        Calculate the absolute discount amount.
        
        Returns:
            float: The difference between original and current price.
        """
        return self.original_price - self.current_price
    
    def calculate_discount_percentage(self) -> float:
        """
        Calculate the discount percentage.
        
        Returns:
            float: The discount percentage (0-100).
        """
        return ((self.original_price - self.current_price) / self.original_price) * 100
    
    def get_discount_details(self) -> dict:
        """
        Get a summary of discount details.
        
        Returns:
            dict: A dictionary containing original price, current price, discount amount, and discount percentage.
        """
        return {
            "original_price": self.original_price,
            "current_price": self.current_price,
            "discount_amount": self.calculate_discount_amount(),
            "discount_percentage": self.calculate_discount_percentage()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Example product: CHRONOSHIELD TITANIUM MATTE – VOLT+ ULTRAVIOLET POLARIZED
        original_price = 250.00  # Original price in USD
        current_price = 199.99   # Current discounted price in USD
        
        calculator = BolleDiscountCalculator(original_price, current_price)
        discount_details = calculator.get_discount_details()
        
        print("Discount Details:")
        print(f"Original Price: ${discount_details['original_price']:.2f}")
        print(f"Current Price: ${discount_details['current_price']:.2f}")
        print(f"Discount Amount: ${discount_details['discount_amount']:.2f}")
        print(f"Discount Percentage: {discount_details['discount_percentage']:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
