"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Create a function that calculates the cost of custom golf grips, taking into account the variables mentioned on the Longhui Golf site, such as logo and shipping.
Generated: DETERMINISTIC_748cc394f0c2280e
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python implementation to calculate the cost of custom golf grips
# based on logo, shipping, and base costs.

def calculate_golf_grip_cost(base_cost, quantity, logo_cost=0, shipping_cost=0):
    """
    Calculate the total cost of custom golf grips.

    Parameters:
    base_cost (float): The cost of a single golf grip.
    quantity (int): The number of golf grips being ordered.
    logo_cost (float): The additional cost for adding a logo per grip. Default is 0.
    shipping_cost (float): The shipping cost for the entire order. Default is 0.

    Returns:
    float: The total cost for the order.
    """
    try:
        # Validate input types
        if not isinstance(base_cost, (int, float)) or base_cost < 0:
            raise ValueError("Base cost must be a non-negative number.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not isinstance(logo_cost, (int, float)) or logo_cost < 0:
            raise ValueError("Logo cost must be a non-negative number.")
        if not isinstance(shipping_cost, (int, float)) or shipping_cost < 0:
            raise ValueError("Shipping cost must be a non-negative number.")
        
        # Calculate total cost
        grip_cost = (base_cost + logo_cost) * quantity
        total_cost = grip_cost + shipping_cost
        
        return round(total_cost, 2)  # Return the total cost rounded to 2 decimal places
    
    except ValueError as e:
        # Handle input validation errors
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example input
    base_cost = 10.50       # Cost per grip
    quantity = 4            # Number of grips
    logo_cost = 2.75        # Additional logo cost per grip
    shipping_cost = 15.00   # Shipping cost for the entire order
    
    total = calculate_golf_grip_cost(base_cost, quantity, logo_cost, shipping_cost)
    if total is not None:
        print(f"The total cost for the order is: ${total}")
```
