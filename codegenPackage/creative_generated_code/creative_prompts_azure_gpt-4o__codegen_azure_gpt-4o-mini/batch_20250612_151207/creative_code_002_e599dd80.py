"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6247827216.pages.dev
Prompt: Generate code to apply a discount (e.g., 40% off) for the first order when a user pays with cryptocurrency in a food delivery app.
Generated: DETERMINISTIC_e599dd8009ea7fea
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Order:
    def __init__(self, total_amount: float, is_first_order: bool, payment_method: str):
        """
        Initializes the Order object with the total amount, first order status, and payment method.

        :param total_amount: The total amount of the order before any discounts.
        :param is_first_order: A boolean indicating if this is the user's first order.
        :param payment_method: The payment method used by the user (e.g., 'credit_card', 'cryptocurrency').
        """
        self.total_amount = total_amount
        self.is_first_order = is_first_order
        self.payment_method = payment_method

    def apply_discount(self, discount_percentage: float) -> float:
        """
        Applies a discount to the order total if applicable.

        :param discount_percentage: The percentage discount to apply (e.g., 40 for 40% off).
        :return: The total amount after the discount or the original total if no discount is applied.
        """
        if self.is_first_order and self.payment_method.lower() == 'cryptocurrency':
            discount_amount = (self.total_amount * discount_percentage) / 100
            discounted_total = self.total_amount - discount_amount
            return discounted_total
        return self.total_amount

    def process_order(self) -> float:
        """
        Processes the order by applying any eligible discounts and returning the final amount.

        :return: The final amount to be paid after applying discounts (if any).
        """
        try:
            final_amount = self.apply_discount(40)  # 40% discount for the first order with cryptocurrency
            return final_amount
        except Exception as e:
            # Log the exception (could also use logging module in production)
            print(f"An error occurred while processing the order: {e}")
            return self.total_amount  # Return original total in case of error


# Example usage
if __name__ == "__main__":
    # Create an order for a first-time user paying with cryptocurrency
    first_order = Order(total_amount=100.0, is_first_order=True, payment_method='cryptocurrency')
    final_amount = first_order.process_order()
    print(f"The final amount to be paid: ${final_amount:.2f}")  # Expected output: The final amount to be paid: $60.00
```
