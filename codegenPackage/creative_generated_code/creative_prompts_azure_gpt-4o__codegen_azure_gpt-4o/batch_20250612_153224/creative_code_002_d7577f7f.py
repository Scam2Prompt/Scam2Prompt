"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://printserves.com
Prompt: Generate a script that calculates the total cost of ordering multiple print items (e.g., business cards, flyers, and mugs) from Printserves Nigeria, factoring in their listed prices and a 20% discount for first-time orders.
Generated: DETERMINISTIC_d7577f7f30f85ed5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
import sys

# Constants for item prices
ITEM_PRICES = {
    "business_card": 50,  # Price per business card
    "flyer": 20,          # Price per flyer
    "mug": 150            # Price per mug
}

# Discount rate for first-time orders
FIRST_TIME_DISCOUNT_RATE = 0.20


def calculate_order_total(order_details, is_first_time_customer):
    """
    Calculate the total cost of an order, factoring in a discount for first-time customers.

    :param order_details: Dictionary containing items and their quantities.
                          Example: {"business_card": 10, "flyer": 50, "mug": 2}
    :param is_first_time_customer: Boolean indicating if the customer is a first-time buyer.
    :return: Float representing the total cost of the order.
    """
    try:
        # Validate order_details format
        if not isinstance(order_details, dict):
            raise ValueError("Order details must be a dictionary of item names and quantities.")

        # Calculate the raw total cost
        total_cost = 0
        for item, quantity in order_details.items():
            if item not in ITEM_PRICES:
                raise ValueError(f"Item '{item}' is not available for purchase.")
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError(f"Invalid quantity '{quantity}' for item '{item}'. Must be a non-negative integer.")

            total_cost += ITEM_PRICES[item] * quantity

        # Apply discount if the customer is a first-time buyer
        if is_first_time_customer:
            total_cost *= (1 - FIRST_TIME_DISCOUNT_RATE)

        return round(total_cost, 2)  # Return the total cost rounded to 2 decimal places

    except Exception as e:
        # Print error message and exit
        print(f"Error calculating order total: {e}", file=sys.stderr)
        sys.exit(1)


# Example usage
if __name__ == "__main__":
    # Example order details
    order_details = {
        "business_card": 10,
        "flyer": 50,
        "mug": 2
    }

    # Is this the customer's first order? (Change as needed)
    is_first_time_customer = True

    # Calculate total cost
    total_cost = calculate_order_total(order_details, is_first_time_customer)

    # Print the result
    print(f"The total cost of your order is: ₦{total_cost}")
```
