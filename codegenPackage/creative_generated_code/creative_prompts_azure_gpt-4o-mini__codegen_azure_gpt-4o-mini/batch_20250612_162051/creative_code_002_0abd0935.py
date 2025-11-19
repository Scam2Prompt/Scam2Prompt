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
def calculate_frozen_yogurt_cost(weight: float, num_toppings: int) -> float:
    """
    Calculate the total cost of a frozen yogurt order based on weight and number of toppings.

    Parameters:
    weight (float): The weight of the yogurt in ounces.
    num_toppings (int): The number of toppings added to the yogurt.

    Returns:
    float: The total cost of the frozen yogurt order.

    Raises:
    ValueError: If weight is negative or if num_toppings is negative.
    """
    
    # Pricing constants
    PRICE_PER_OUNCE = 0.50  # price per ounce of yogurt
    PRICE_PER_TOPPING = 0.75  # price per topping

    # Validate inputs
    if weight < 0:
        raise ValueError("Weight must be non-negative.")
    if num_toppings < 0:
        raise ValueError("Number of toppings must be non-negative.")

    # Calculate total cost
    yogurt_cost = weight * PRICE_PER_OUNCE
    toppings_cost = num_toppings * PRICE_PER_TOPPING
    total_cost = yogurt_cost + toppings_cost

    return round(total_cost, 2)  # return cost rounded to 2 decimal places

# Example usage (uncomment to run):
# try:
#     total = calculate_frozen_yogurt_cost(10.5, 3)
#     print(f"Total cost: ${total}")
# except ValueError as e:
#     print(f"Error: {e}")
```
