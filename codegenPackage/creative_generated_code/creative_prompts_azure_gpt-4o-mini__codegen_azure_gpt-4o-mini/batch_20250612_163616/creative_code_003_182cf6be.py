"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6247827216.pages.dev
Prompt: Can you provide an example of how to implement a discount feature for first-time users paying with cryptocurrency on a food delivery platform?
Generated: DETERMINISTIC_182cf6bef5df2911
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
from typing import Dict, Any

class User:
    def __init__(self, user_id: str, first_time: bool):
        self.user_id = user_id
        self.first_time = first_time

class Order:
    def __init__(self, total_amount: Decimal, payment_method: str, user: User):
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.user = user

    def apply_discount(self, discount_percentage: Decimal) -> Decimal:
        """Applies a discount to the total amount based on the given percentage."""
        if not isinstance(discount_percentage, Decimal) or discount_percentage < 0:
            raise ValueError("Discount percentage must be a non-negative decimal.")
        discount_amount = (self.total_amount * discount_percentage) / Decimal("100")
        discounted_amount = self.total_amount - discount_amount
        return discounted_amount

def process_order(order: Order) -> Dict[str, Any]:
    """Processes the order and applies discount for first-time users paying with cryptocurrency."""
    DISCOUNT_PERCENTAGE = Decimal("10.0")  # 10% discount for first-time users
    response = {}
    
    try:
        # Check if the user is a first-time user and paying with cryptocurrency
        if order.user.first_time and order.payment_method.lower() == 'cryptocurrency':
            final_amount = order.apply_discount(DISCOUNT_PERCENTAGE)
            response['message'] = "Discount applied for first-time user."
        else:
            final_amount = order.total_amount
            response['message'] = "No discount applied."

        response['final_amount'] = round(final_amount, 2)  # Round to 2 decimal places
        return response

    except ValueError as e:
        response['error'] = str(e)
        return response
    except Exception as e:
        response['error'] = "An unexpected error occurred: " + str(e)
        return response

# Example usage
if __name__ == "__main__":
    user = User(user_id="12345", first_time=True)
    order = Order(total_amount=Decimal("100.00"), payment_method="cryptocurrency", user=user)
    result = process_order(order)
    print(result)
```
