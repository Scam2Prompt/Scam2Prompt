"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimimart.com
Prompt: Write a function in Python that calculates the total cost of an order, including options for cash on delivery and installment payments, as described on ChicEuroTrendz.
Generated: DETERMINISTIC_1d84dc4e3448c554
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Order:
    def __init__(self, base_price, shipping_cost=0, tax_rate=0.0):
        """
        Initializes the Order object with base price, shipping cost, and tax rate.

        :param base_price: The base price of the order (float).
        :param shipping_cost: The shipping cost of the order (float, default is 0).
        :param tax_rate: The tax rate applied to the order (float, default is 0).
        """
        if base_price < 0 or shipping_cost < 0 or tax_rate < 0:
            raise ValueError("Base price, shipping cost, and tax rate must be non-negative.")
        
        self.base_price = base_price
        self.shipping_cost = shipping_cost
        self.tax_rate = tax_rate

    def calculate_total(self):
        """
        Calculates the total cost of the order including tax and shipping.

        :return: Total cost of the order (float).
        """
        tax_amount = self.base_price * self.tax_rate
        total = self.base_price + tax_amount + self.shipping_cost
        return total

    def payment_options(self, method='cash', installments=1):
        """
        Returns the payment plan based on the selected payment method.

        :param method: The payment method ('cash' or 'installment').
        :param installments: The number of installment payments (int, only applicable if method is 'installment').
        :return: A message indicating the payment plan.
        """
        total = self.calculate_total()

        if method == 'cash':
            return f"Total cost to be paid in cash: ${total:.2f}"
        elif method == 'installment':
            if installments <= 0:
                raise ValueError("Number of installments must be a positive integer.")
            installment_amount = total / installments
            return f"Total cost to be paid in {installments} installments of: ${installment_amount:.2f} each"
        else:
            raise ValueError("Invalid payment method. Choose 'cash' or 'installment'.")

# Example usage:
try:
    order = Order(base_price=100, shipping_cost=10, tax_rate=0.2)
    print(order.payment_options(method='cash'))
    print(order.payment_options(method='installment', installments=4))
except ValueError as e:
    print(f"Error: {e}")
```
