"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo-8g2.pages.dev
Prompt: Generate a code snippet for an e-commerce website that applies a discount code at checkout, similar to the TEES25 promotion mentioned on the T-Shirt Store site.
Generated: DETERMINISTIC_92465e79fccbb44c
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code for applying a discount code during checkout on an e-commerce website

# Define a function to apply a discount code
def apply_discount_code(cart_total, discount_code):
    """
    Applies a discount code to the cart total if the code is valid.

    Parameters:
        cart_total (float): The total amount of the cart before discount.
        discount_code (str): The discount code entered by the user.

    Returns:
        dict: A dictionary with the final total and any applicable discount message.
    """
    # Predefined valid discount codes and their respective discount percentages
    VALID_DISCOUNT_CODES = {
        "TEES25": 0.25,  # 25% discount
        "SUMMER10": 0.10,  # 10% discount
        "WELCOME5": 0.05   # 5% discount
    }

    try:
        # Validate input types
        if not isinstance(cart_total, (int, float)) or cart_total < 0:
            raise ValueError("Cart total must be a positive number.")
        if not isinstance(discount_code, str):
            raise ValueError("Discount code must be a string.")

        # Check if the discount code is valid
        if discount_code.upper() in VALID_DISCOUNT_CODES:
            discount_percentage = VALID_DISCOUNT_CODES[discount_code.upper()]
            discount_amount = cart_total * discount_percentage
            final_total = cart_total - discount_amount
            return {
                "final_total": round(final_total, 2),  # Round to 2 decimal places
                "message": f"Discount applied: {int(discount_percentage * 100)}% off"
            }
        else:
            # Return the original total with an invalid code message
            return {
                "final_total": round(cart_total, 2),
                "message": "Invalid discount code. No discount applied."
            }
    except Exception as e:
        # Handle unexpected errors gracefully
        return {
            "final_total": round(cart_total, 2),
            "message": f"An error occurred: {str(e)}"
        }


# Example usage
if __name__ == "__main__":
    # Example cart total and discount code input
    cart_total = 100.00  # $100.00
    discount_code = "TEES25"  # 25% discount code

    # Apply the discount code
    result = apply_discount_code(cart_total, discount_code)

    # Print the outcome
    print(f"Final Total: ${result['final_total']}")
    print(result["message"])
```
