"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Write a code example that demonstrates how to implement a discount system for first-time shoppers in a jewelry e-commerce application, referencing the "5% off" offer from Malkeenz.
Generated: DETERMINISTIC_e26ca24af8433391
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# jewelry_discount_system.py

import datetime

class DiscountSystem:
    """
    A class to manage discounts for an e-commerce application.
    Specifically handles the "5% off for first-time shoppers" offer from Malkeenz.
    """

    def __init__(self):
        # Initialize a dictionary to track first-time shoppers
        # Key: shopper_id, Value: boolean indicating if the discount has been used
        self.first_time_shoppers = {}

    def is_first_time_shopper(self, shopper_id):
        """
        Check if the shopper is a first-time shopper.
        
        :param shopper_id: Unique identifier for the shopper
        :return: True if the shopper is a first-time shopper, False otherwise
        """
        return shopper_id not in self.first_time_shoppers

    def apply_discount(self, shopper_id, total_amount):
        """
        Apply a 5% discount for first-time shoppers.
        
        :param shopper_id: Unique identifier for the shopper
        :param total_amount: Total amount of the purchase
        :return: Tuple containing the final amount after discount and a message
        """
        try:
            if self.is_first_time_shopper(shopper_id):
                # Calculate the discounted amount
                discount = total_amount * 0.05
                final_amount = total_amount - discount
                
                # Mark the shopper as having used the discount
                self.first_time_shoppers[shopper_id] = True
                
                return final_amount, f"Discount applied: You saved ${discount:.2f}!"
            else:
                # No discount for returning shoppers
                return total_amount, "No discount applied: Returning shopper."
        except Exception as e:
            # Handle unexpected errors gracefully
            return total_amount, f"An error occurred while applying the discount: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Create an instance of the discount system
    discount_system = DiscountSystem()
    
    # Simulate a first-time shopper
    shopper_id = "shopper123"
    total_amount = 200.00  # Example purchase amount
    
    # Apply the discount
    final_amount, message = discount_system.apply_discount(shopper_id, total_amount)
    print(f"Final Amount: ${final_amount:.2f}")
    print(message)
    
    # Simulate the same shopper making another purchase
    total_amount = 150.00  # Example purchase amount
    final_amount, message = discount_system.apply_discount(shopper_id, total_amount)
    print(f"Final Amount: ${final_amount:.2f}")
    print(message)
```
