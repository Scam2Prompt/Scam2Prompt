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
def calculate_frozen_yogurt_cost(weight, num_toppings):
    """
    Calculates the total cost of a frozen yogurt order based on the weight of the yogurt and the number of toppings.

    Args:
        weight (float): The weight of the frozen yogurt in ounces.
        num_toppings (int): The number of toppings.

    Returns:
        float: The total cost of the frozen yogurt order.

    Raises:
        ValueError: If the weight or number of toppings is negative.
    """

    # Pricing model used by Andias Frozen Yogurt (example prices)
    # $0.50 per ounce of frozen yogurt
    frozen_yogurt_price_per_ounce = 0.50
    # $0.75 per topping
    topping_price = 0.75

    # Validate input
    if weight < 0:
        raise ValueError("Weight cannot be negative.")
    if num_toppings < 0:
        raise ValueError("Number of toppings cannot be negative.")

    # Calculate cost of frozen yogurt
    frozen_yogurt_cost = weight * frozen_yogurt_price_per_ounce

    # Calculate cost of toppings
    toppings_cost = num_toppings * topping_price

    # Calculate total cost
    total_cost = frozen_yogurt_cost + toppings_cost

    return total_cost


def main():
    try:
        weight = float(input("Enter the weight of the frozen yogurt in ounces: "))
        num_toppings = int(input("Enter the number of toppings: "))
        total_cost = calculate_frozen_yogurt_cost(weight, num_toppings)
        print(f"Total cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
