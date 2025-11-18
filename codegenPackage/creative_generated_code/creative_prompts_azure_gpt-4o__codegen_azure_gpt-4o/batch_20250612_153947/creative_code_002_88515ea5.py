"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Generate code to calculate shipping costs and apply free shipping for orders over $400, as specified on BioLongevity Labs.
Generated: DETERMINISTIC_88515ea550b64498
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script calculates shipping costs for BioLongevity Labs orders.
# Free shipping is applied for orders over $400.

def calculate_shipping_cost(order_total, shipping_rate=10.0):
    """
    Calculate the shipping cost based on the order total.
    If the order total exceeds $400, free shipping is applied.

    Args:
        order_total (float): Total cost of the order.
        shipping_rate (float): Flat shipping rate (default is $10.0).

    Returns:
        float: The applicable shipping cost.
    """
    try:
        if order_total < 0:
            raise ValueError("Order total cannot be negative.")
        
        # Apply free shipping for orders over $400
        if order_total > 400:
            return 0.0
        else:
            return shipping_rate
    except TypeError:
        raise TypeError("Order total must be a number.")
    except ValueError as ve:
        print(f"Error: {ve}")
        raise

def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    try:
        # Example order totals
        orders = [150.00, 420.50, 390.00, 500.00, -10.00]  # Includes a negative value for testing
        
        print("Shipping Costs:")
        for order_total in orders:
            try:
                shipping_cost = calculate_shipping_cost(order_total)
                print(f"Order Total: ${order_total:.2f}, Shipping Cost: ${shipping_cost:.2f}")
            except Exception as e:
                print(f"Failed to calculate shipping for order total ${order_total}: {e}")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
