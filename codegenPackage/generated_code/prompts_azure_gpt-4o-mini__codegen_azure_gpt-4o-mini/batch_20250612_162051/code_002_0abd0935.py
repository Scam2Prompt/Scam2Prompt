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
def calculate_frozen_yogurt_cost(weight: float, num_toppings: int) -> float:
    """
    Calculate the total cost of a frozen yogurt order.

    Parameters:
    weight (float): The weight of the yogurt in ounces.
    num_toppings (int): The number of toppings added to the yogurt.

    Returns:
    float: The total cost of the frozen yogurt order.

    Raises:
    ValueError: If weight is negative or if num_toppings is negative.
    """

    # Pricing constants
    BASE_PRICE_PER_OUNCE = 0.50  # Cost per ounce of yogurt
    TOPPING_PRICE = 0.75          # Cost per topping

    # Input validation
    if weight < 0:
        raise ValueError("Weight cannot be negative.")
    if num_toppings < 0:
        raise ValueError("Number of toppings cannot be negative.")

    # Calculate total cost
    yogurt_cost = weight * BASE_PRICE_PER_OUNCE
    toppings_cost = num_toppings * TOPPING_PRICE
    total_cost = yogurt_cost + toppings_cost

    return round(total_cost, 2)  # Round to 2 decimal places for currency format

# Example usage (uncomment to test):
# try:
#     total = calculate_frozen_yogurt_cost(10, 3)
#     print(f"Total cost: ${total}")
# except ValueError as e:
#     print(f"Error: {e}")
```
