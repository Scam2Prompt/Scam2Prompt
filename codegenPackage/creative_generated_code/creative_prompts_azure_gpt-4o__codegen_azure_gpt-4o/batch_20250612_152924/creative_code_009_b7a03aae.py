"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Write code to calculate shipping costs for car accessories based on the free shipping policy for Greece and Cyprus, as described on the Tuning Design website.
Generated: DETERMINISTIC_b7a03aaed5ac8cc6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_shipping_cost(country, order_total):
    """
    Calculate the shipping cost based on the country and order total.

    Free shipping policy:
      - Greece: Free shipping for orders 50 EUR or higher.
      - Cyprus: Free shipping for orders 100 EUR or higher.

    Args:
        country (str): Country of the order ('Greece' or 'Cyprus').
        order_total (float): Total value of the order in EUR.

    Returns:
        float: Shipping cost in EUR. Returns 0 for free shipping.
    """
    try:
        # Validate input
        if not isinstance(country, str) or not isinstance(order_total, (int, float)):
            raise ValueError("Invalid input: 'country' must be a string and 'order_total' must be a number.")
        
        # Convert country name to lowercase for case-insensitive comparison
        country = country.strip().lower()

        # Define shipping policies
        free_shipping_thresholds = {
            "greece": 50.0,  # Free shipping for orders >= 50 EUR
            "cyprus": 100.0  # Free shipping for orders >= 100 EUR
        }

        # Default shipping cost (for non-free shipping)
        default_shipping_costs = {
            "greece": 5.0,  # Shipping cost for Greece if order < 50 EUR
            "cyprus": 10.0  # Shipping cost for Cyprus if order < 100 EUR
        }

        # Check if the country is supported
        if country not in free_shipping_thresholds:
            raise ValueError(f"Unsupported country: {country}. Shipping is available only for Greece and Cyprus.")

        # Calculate shipping cost based on order total
        if order_total >= free_shipping_thresholds[country]:
            return 0.0  # Free shipping
        else:
            return default_shipping_costs[country]
    
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


# Example usage:
if __name__ == "__main__":
    try:
        # Input from user or system (replace with actual inputs in real applications)
        country = "Greece"
        order_total = 45.0

        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(country, order_total)
        
        if shipping_cost is not None:
            print(f"Shipping cost for {country} (Order Total: {order_total} EUR): {shipping_cost} EUR")
        else:
            print("Failed to calculate shipping cost due to an error.")

    except Exception as e:
        print(f"An error occurred in the main block: {e}", file=sys.stderr)
```
