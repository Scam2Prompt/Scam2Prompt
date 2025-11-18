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
class Payment:
    def __init__(self, amount: float, payment_method: str):
        """
        Initializes the Payment class with the amount and payment method.

        :param amount: The total amount for the purchase
        :param payment_method: The method of payment (e.g., 'Pix', 'Credit Card', etc.)
        """
        self.amount = amount
        self.payment_method = payment_method

    def apply_discount(self) -> float:
        """
        Applies a discount if the payment method is 'Pix'.

        :return: The final amount after applying the discount, if applicable
        :raises ValueError: If the amount is negative
        """
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
        
        discount_rate = 0.05  # 5% discount
        if self.payment_method.lower() == 'pix':
            discount = self.amount * discount_rate
            final_amount = self.amount - discount
            return final_amount
        return self.amount  # No discount applied

def main():
    """
    Main function to execute the discount calculation.
    """
    try:
        # Example usage
        amount = float(input("Enter the purchase amount: "))
        payment_method = input("Enter the payment method (e.g., 'Pix'): ")

        payment = Payment(amount, payment_method)
        final_amount = payment.apply_discount()

        print(f"The final amount after applying discounts (if applicable) is: {final_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
