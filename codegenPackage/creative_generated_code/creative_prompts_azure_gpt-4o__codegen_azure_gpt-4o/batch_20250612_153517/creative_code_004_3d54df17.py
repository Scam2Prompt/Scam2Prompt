"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Provide a Python script to calculate shipping costs for an online store based on product categories such as "Bicicleta," "ATV," and "Roaba," and their weights.
Generated: DETERMINISTIC_3d54df176b723929
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shipping Cost Calculator for an Online Store

This script calculates shipping costs based on product categories and weights.
Supported categories: 'Bicicleta', 'ATV', 'Roaba'.
Each category has specific pricing rules.
"""

import sys

def calculate_shipping_cost(category, weight):
    """
    Calculates the shipping cost based on the product category and its weight.

    Args:
        category (str): Product category ('Bicicleta', 'ATV', 'Roaba').
        weight (float): Weight of the product in kilograms.

    Returns:
        float: Shipping cost in currency units.

    Raises:
        ValueError: If the category is invalid.
    """
    if weight <= 0:
        raise ValueError("Weight must be greater than 0.")

    # Define the pricing rules for each category
    pricing_rules = {
        'Bicicleta': lambda w: 10 + (5 * w),  # Base cost: 10, Rate per kg: 5
        'ATV': lambda w: 20 + (8 * w),       # Base cost: 20, Rate per kg: 8
        'Roaba': lambda w: 15 + (6 * w)      # Base cost: 15, Rate per kg: 6
    }

    if category not in pricing_rules:
        raise ValueError(f"Invalid category '{category}'. Supported categories: 'Bicicleta', 'ATV', 'Roaba'.")

    # Calculate and return the shipping cost
    return pricing_rules[category](weight)

def main():
    """
    Main function to interact with the user and calculate shipping costs.
    """
    print("Welcome to the Shipping Cost Calculator!")
    print("Supported categories: Bicicleta, ATV, Roaba")

    try:
        # Prompt user for input
        category = input("Enter the product category: ").strip()
        weight = float(input("Enter the weight of the product (in kilograms): "))

        # Calculate shipping cost
        cost = calculate_shipping_cost(category, weight)
        print(f"The shipping cost for a {category} weighing {weight} kg is: {cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
