"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Write a Python code snippet to calculate the total cost of purchasing solar batteries, including a 40A 12V/24V AM MPPT Solar charge controller and a 2000 Lithium Portable Power Pack, considering a 10% discount on the total price.
Generated: DETERMINISTIC_100a97bef233b0c8
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary module for decimal precision
from decimal import Decimal, ROUND_HALF_UP

def calculate_total_cost():
    """
    Calculate the total cost of purchasing solar batteries and accessories,
    including a 10% discount on the total price.
    """
    try:
        # Define the prices of items
        mppt_controller_price = Decimal("150.00")  # Price of 40A 12V/24V AM MPPT Solar charge controller
        power_pack_price = Decimal("1200.00")     # Price of 2000 Lithium Portable Power Pack

        # Calculate the total price before discount
        total_price = mppt_controller_price + power_pack_price

        # Apply a 10% discount
        discount_rate = Decimal("0.10")  # 10% discount
        discount_amount = total_price * discount_rate
        discounted_price = total_price - discount_amount

        # Round the final price to 2 decimal places for currency formatting
        final_price = discounted_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return final_price

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Calculate and display the total cost
    total_cost = calculate_total_cost()
    if total_cost is not None:
        print(f"The total cost after a 10% discount is: ${total_cost}")
    else:
        print("Failed to calculate the total cost.")
```
