"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write Python code to calculate a discount of 5% for purchases made via Pix payment, as described on the ebrasilbrazz website.
Generated: DETERMINISTIC_bcc849a3d89daf54
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# eBrasilBrazz Discount Calculator
# This program calculates a 5% discount for purchases made via Pix payment.

def calculate_discounted_price(original_price, payment_method):
    """
    Calculate the discounted price based on the payment method.

    :param original_price: float - The original price of the item
    :param payment_method: str - The payment method ("pix" for Pix payment)
    :return: float - The final price after applying any applicable discounts
    """
    try:
        # Validate the input types
        if not isinstance(original_price, (int, float)) or original_price < 0:
            raise ValueError("Original price must be a positive number.")
        if not isinstance(payment_method, str):
            raise ValueError("Payment method must be a string.")

        # Define the discount rate for Pix payments
        PIX_DISCOUNT_RATE = 0.05  # 5% discount

        # Check if the payment method qualifies for a discount
        if payment_method.lower() == "pix":
            discount = original_price * PIX_DISCOUNT_RATE
            final_price = original_price - discount
        else:
            # No discount for other payment methods
            final_price = original_price

        return round(final_price, 2)  # Return the price rounded to 2 decimal places

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Prompt user for inputs
        original_price = float(input("Enter the original price of the item: "))
        payment_method = input("Enter the payment method (e.g., 'Pix'): ")

        # Calculate the final price
        final_price = calculate_discounted_price(original_price, payment_method)

        # Display the result
        if final_price is not None:
            print(f"The final price after discount (if applicable) is: R${final_price:.2f}")
    except Exception as e:
        print(f"An error occurred during execution: {e}")
```
