"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python script to simulate the checkout process, including applying discount coupons and calculating installment payments, inspired by the "Insira seu cupom de desconto na página de finalização" feature on the "Dal Cortivo Pneus" site.
Generated: DETERMINISTIC_5af9311a9fd56a00
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

# Constants
DISCOUNTS = {
    "SAVE10": 0.10,  # 10% discount
    "SAVE20": 0.20,  # 20% discount
    "FREEDELIVERY": 0.00  # No discount, just free delivery placeholder
}
MAX_INSTALLMENTS = 12

# Function to validate coupon
def validate_coupon(coupon_code):
    """
    Validate the coupon code against predefined discount coupons.
    
    Parameters:
        coupon_code (str): Coupon code entered by the user.
    
    Returns:
        float: Discount percentage if valid, otherwise None.
    """
    return DISCOUNTS.get(coupon_code.upper())

# Function to calculate total price after discount
def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the price after applying the discount.
    
    Parameters:
        original_price (float): The original price of the items.
        discount_percentage (float): Discount percentage to apply.
    
    Returns:
        float: Price after discount.
    """
    discounted_price = original_price * (1 - discount_percentage)
    return round(discounted_price, 2)

# Function to calculate installment payments
def calculate_installments(total_price, installments):
    """
    Calculate installment amounts based on the total price and number of installments.
    
    Parameters:
        total_price (float): Total price after discount.
        installments (int): Number of installment payments.
    
    Returns:
        list: List of installment amounts.
    """
    if installments > MAX_INSTALLMENTS:
        raise ValueError(f"Installments cannot exceed {MAX_INSTALLMENTS}.")
    installment_amount = round(total_price / installments, 2)
    return [installment_amount] * installments

# Main function to simulate checkout process
def checkout_process():
    """
    Simulate the checkout process. Includes discount application and installment calculation.
    """
    try:
        # Step 1: User inputs
        original_price = float(input("Enter the original price of items: "))
        coupon_code = input("Enter your discount coupon code (or press Enter to skip): ").strip()
        installments = int(input(f"Enter the number of installments (1-{MAX_INSTALLMENTS}): "))
        
        # Validate inputs
        if original_price <= 0:
            raise ValueError("Original price must be greater than zero.")
        if installments < 1 or installments > MAX_INSTALLMENTS:
            raise ValueError(f"Number of installments must be between 1 and {MAX_INSTALLMENTS}.")
        
        # Step 2: Apply coupon (if any)
        discount_percentage = validate_coupon(coupon_code) if coupon_code else None
        if discount_percentage is not None:
            print(f"Coupon applied! You get a {discount_percentage * 100:.0f}% discount.")
        else:
            print("No valid coupon applied.")
            discount_percentage = 0.0
        
        discounted_price = calculate_discounted_price(original_price, discount_percentage)
        print(f"Total price after discount: ${discounted_price:.2f}")
        
        # Step 3: Calculate installments
        installment_amounts = calculate_installments(discounted_price, installments)
        print(f"Your installment plan ({installments} payments):")
        for i, amount in enumerate(installment_amounts, 1):
            print(f"  Payment {i}: ${amount:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    print("Welcome to the Checkout System!")
    checkout_process()
```
