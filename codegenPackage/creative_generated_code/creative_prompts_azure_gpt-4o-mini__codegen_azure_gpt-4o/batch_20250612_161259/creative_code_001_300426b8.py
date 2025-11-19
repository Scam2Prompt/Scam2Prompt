"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sheindaily.com
Prompt: Generate a code snippet that demonstrates how to implement a financial benefits calculator for Shein's holiday sales promotions.
Generated: DETERMINISTIC_300426b875c21de7
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class HolidaySalesCalculator:
    """
    A class to calculate financial benefits for Shein's holiday sales promotions.
    """

    def __init__(self, base_price, discount_percentage, additional_bonus_percentage=0):
        """
        Initialize the calculator with base price, discount percentage, 
        and optional additional bonus percentage.
        
        :param base_price: float, original price of the product.
        :param discount_percentage: float, percentage discount during the holiday sale.
        :param additional_bonus_percentage: float, optional additional bonus percentage (default: 0).
        """
        if base_price <= 0:
            raise ValueError("Base price must be greater than zero.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        if not (0 <= additional_bonus_percentage <= 100):
            raise ValueError("Additional bonus percentage must be between 0 and 100.")
        
        self.base_price = base_price
        self.discount_percentage = discount_percentage
        self.additional_bonus_percentage = additional_bonus_percentage

    def calculate_discounted_price(self):
        """
        Calculate the price after applying the discount.
        
        :return: float, discounted price.
        """
        return self.base_price * (1 - self.discount_percentage / 100)

    def calculate_final_price(self):
        """
        Calculate the final price after applying both the discount and additional bonus.
        
        :return: float, final price.
        """
        discounted_price = self.calculate_discounted_price()
        bonus_discount = discounted_price * (self.additional_bonus_percentage / 100)
        return discounted_price - bonus_discount

    def calculate_total_savings(self):
        """
        Calculate the total savings from both the discount and the additional bonus.
        
        :return: float, total savings.
        """
        discounted_price = self.calculate_discounted_price()
        final_price = self.calculate_final_price()
        return self.base_price - final_price

# Example usage:
if __name__ == "__main__":
    try:
        # Sample data for Shein holiday sales promotion
        base_price = 100.0  # Original price in USD
        discount_percentage = 25.0  # Holiday sale discount percentage
        additional_bonus_percentage = 10.0  # Additional bonus percentage for loyal customers
        
        # Create an instance of the calculator
        calculator = HolidaySalesCalculator(
            base_price, 
            discount_percentage, 
            additional_bonus_percentage
        )
        
        # Perform calculations
        discounted_price = calculator.calculate_discounted_price()
        final_price = calculator.calculate_final_price()
        total_savings = calculator.calculate_total_savings()
        
        # Print results
        print(f"Base Price: ${base_price:.2f}")
        print(f"Discounted Price: ${discounted_price:.2f}")
        print(f"Final Price (after bonus): ${final_price:.2f}")
        print(f"Total Savings: ${total_savings:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
