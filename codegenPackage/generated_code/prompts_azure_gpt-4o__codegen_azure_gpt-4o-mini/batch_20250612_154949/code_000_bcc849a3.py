"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write Python code to calculate a discount of 5% for purchases made via Pix payment, as described on the ebrasilbrazz website.
Generated: DETERMINISTIC_bcc849a3d89daf54
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PaymentProcessor:
    """
    A class to handle payment processing and apply discounts based on payment methods.
    """

    DISCOUNT_RATE = 0.05  # 5% discount for Pix payments

    def __init__(self):
        pass

    def calculate_discounted_price(self, original_price: float, payment_method: str) -> float:
        """
        Calculate the discounted price based on the payment method.

        :param original_price: The original price of the purchase.
        :param payment_method: The payment method used (e.g., 'Pix', 'Credit Card').
        :return: The price after applying the discount if applicable.
        :raises ValueError: If the original price is negative or payment method is invalid.
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        
        if payment_method not in ['Pix', 'Credit Card']:
            raise ValueError("Invalid payment method. Use 'Pix' or 'Credit Card'.")

        # Calculate the discounted price if payment is made via Pix
        if payment_method == 'Pix':
            discounted_price = original_price * (1 - self.DISCOUNT_RATE)
        else:
            discounted_price = original_price

        return round(discounted_price, 2)  # Round to 2 decimal places for currency

def main():
    """
    Main function to demonstrate the discount calculation.
    """
    processor = PaymentProcessor()

    # Example usage
    try:
        original_price = 100.00  # Example original price
        payment_method = 'Pix'   # Example payment method

        discounted_price = processor.calculate_discounted_price(original_price, payment_method)
        print(f"The discounted price for {payment_method} payment is: ${discounted_price}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
