"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://andiasfrozenyogurt.com
Prompt: Write a Python function that calculates the total cost of a frozen yogurt order based on the weight of the yogurt and the number of toppings, reflecting the pricing model used by Andias Frozen Yogurt.
Generated: DETERMINISTIC_0abd0935c1da0c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_frozen_yogurt_cost(weight_oz, num_toppings):
    """
    Calculates the total cost of a frozen yogurt order.
    
    Parameters:
        weight_oz (float): Weight of the frozen yogurt in ounces.
        num_toppings (int): Number of toppings added to the yogurt.
    
    Returns:
        float: Total cost of the frozen yogurt order.
    
    Pricing Model:
        - Base cost: $0.50 per ounce of frozen yogurt.
        - Topping cost: $0.75 per topping.
    
    Raises:
        ValueError: If weight_oz or num_toppings is negative.
    """
    # Validate inputs
    if weight_oz < 0:
        raise ValueError("The weight of the yogurt cannot be negative.")
    if num_toppings < 0:
        raise ValueError("The number of toppings cannot be negative.")

    # Pricing configuration
    COST_PER_OUNCE = 0.50  # Cost per ounce of yogurt
    COST_PER_TOPPING = 0.75  # Cost per topping

    # Calculate total cost
    yogurt_cost = weight_oz * COST_PER_OUNCE
    topping_cost = num_toppings * COST_PER_TOPPING
    total_cost = yogurt_cost + topping_cost

    return round(total_cost, 2)  # Round to two decimal places for currency

# Example usage:
# Uncomment the line below to test the function:
# print(calculate_frozen_yogurt_cost(12.5, 3))
```
