"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Generate code to calculate the shipping cost for an order of electronic components, considering free shipping rules and conditions.
Generated: DETERMINISTIC_d6369433967d5251
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_cost_calculator.py

def calculate_shipping_cost(order_total, free_shipping_threshold, base_shipping_cost):
    """
    Calculate the shipping cost for an order based on the total order value and free shipping rules.

    Parameters:
        order_total (float): The total value of the order.
        free_shipping_threshold (float): The minimum order value for free shipping.
        base_shipping_cost (float): The default shipping cost if free shipping is not applicable.

    Returns:
        float: The calculated shipping cost.
    """
    try:
        # Validate input types
        if not isinstance(order_total, (int, float)) or order_total < 0:
            raise ValueError("Order total must be a non-negative number.")
        if not isinstance(free_shipping_threshold, (int, float)) or free_shipping_threshold < 0:
            raise ValueError("Free shipping threshold must be a non-negative number.")
        if not isinstance(base_shipping_cost, (int, float)) or base_shipping_cost < 0:
            raise ValueError("Base shipping cost must be a non-negative number.")

        # Determine shipping cost
        if order_total >= free_shipping_threshold:
            return 0.0  # Free shipping
        else:
            return base_shipping_cost  # Base shipping cost applies

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define shipping parameters
    FREE_SHIPPING_THRESHOLD = 100.0  # Free shipping for orders >= $100
    BASE_SHIPPING_COST = 10.0        # $10 shipping cost for orders below the threshold

    # Example order totals
    order_totals = [50.0, 120.0, -10.0, "invalid"]

    for order_total in order_totals:
        print(f"Order Total: ${order_total}")
        shipping_cost = calculate_shipping_cost(order_total, FREE_SHIPPING_THRESHOLD, BASE_SHIPPING_COST)
        if shipping_cost is not None:
            print(f"Shipping Cost: ${shipping_cost:.2f}")
        print("-" * 30)
```
