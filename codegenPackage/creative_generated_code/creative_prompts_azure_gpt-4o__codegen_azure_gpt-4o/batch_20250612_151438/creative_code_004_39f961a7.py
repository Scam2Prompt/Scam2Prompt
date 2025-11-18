"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Provide code to calculate the monthly installment amount for purchasing "04 X Junção Branca Sanfonada P/ Luminaria Circular (redonda)" with a 5% discount and 12 interest-free payments.
Generated: DETERMINISTIC_39f961a7245abaac
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Calculate the monthly installment amount for a product purchase
# with a 5% discount and 12 interest-free payments.

def calculate_monthly_installment(original_price, discount_percentage, payment_terms):
    """
    Calculate the monthly installment amount after applying a discount.
    
    Args:
        original_price (float): The original price of the product.
        discount_percentage (float): The discount percentage to be applied.
        payment_terms (int): Number of monthly payments (interest-free).
    
    Returns:
        float: Monthly installment amount after applying the discount.
    """
    try:
        # Validate inputs
        if original_price < 0 or discount_percentage < 0 or payment_terms <= 0:
            raise ValueError("Invalid input values. Ensure all inputs are positive.")

        # Calculate the discounted price
        discounted_price = original_price * ((100 - discount_percentage) / 100)

        # Calculate the monthly installment amount (interest-free)
        monthly_installment = discounted_price / payment_terms

        return round(monthly_installment, 2)  # Rounding to two decimal places for currency
    except Exception as e:
        # Log the error (production systems may use logging frameworks instead of print)
        print(f"Error calculating monthly installment: {e}")
        return None  # Return None to indicate failure


# Example usage
if __name__ == "__main__":
    # Original price of the product
    original_price = 500.00  # Change this value as needed

    # Discount percentage
    discount_percentage = 5  # 5% discount

    # Number of interest-free payments
    payment_terms = 12  # 12 months

    # Calculate the monthly installment
    monthly_payment = calculate_monthly_installment(original_price, discount_percentage, payment_terms)

    if monthly_payment is not None:
        print(f"Monthly Installment Amount: ${monthly_payment}")
    else:
        print("Failed to calculate monthly installment amount.")
```
