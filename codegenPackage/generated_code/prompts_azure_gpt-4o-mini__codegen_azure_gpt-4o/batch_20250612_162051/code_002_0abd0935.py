"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Write a Python function that calculates the total cost of a frozen yogurt order based on the weight of the yogurt and the number of toppings, reflecting the pricing model used by Andias Frozen Yogurt.
Generated: DETERMINISTIC_0abd0935c1da0c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_frozen_yogurt_cost(weight_oz, num_toppings):
    """
    Calculate the total cost of a frozen yogurt order.

    Pricing model:
    - Base cost: $0.50 per ounce of yogurt
    - Topping cost: $0.75 per topping

    Args:
        weight_oz (float): The weight of the frozen yogurt in ounces.
        num_toppings (int): The number of toppings added.

    Returns:
        float: The total cost of the frozen yogurt order.

    Raises:
        ValueError: If weight_oz is negative or num_toppings is negative.
    """
    # Validate inputs
    if weight_oz < 0:
        raise ValueError("Weight of yogurt cannot be negative.")
    if num_toppings < 0:
        raise ValueError("Number of toppings cannot be negative.")

    # Pricing constants
    COST_PER_OUNCE = 0.50
    COST_PER_TOPPING = 0.75

    # Calculate total cost
    yogurt_cost = weight_oz * COST_PER_OUNCE
    topping_cost = num_toppings * COST_PER_TOPPING
    total_cost = yogurt_cost + topping_cost

    return round(total_cost, 2)  # Round to 2 decimal places for currency formatting


# Example usage:
try:
    weight = 10.5  # Weight in ounces
    toppings = 3   # Number of toppings
    total = calculate_frozen_yogurt_cost(weight, toppings)
    print(f"Total cost: ${total}")
except ValueError as e:
    print(f"Error: {e}")
```
