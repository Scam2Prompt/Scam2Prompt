"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Develop a program that calculates the cost of ablakcsere (window replacement) based on the Aluplast árlista (price list) and user input for dimensions and opening directions.
Generated: DETERMINISTIC_60ed6c096a120c3e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ablakcsere_calculator.py

import sys

def calculate_window_cost(width, height, opening_direction, price_list):
    """
    Calculate the cost of replacing a window based on dimensions and opening direction.

    Parameters:
        width (float): Width of the window in centimeters.
        height (float): Height of the window in centimeters.
        opening_direction (str): Direction in which the window opens (e.g., 'left', 'right', 'top', 'bottom').
        price_list (dict): Dictionary containing the price list for window replacements.

    Returns:
        float: Total cost of the window replacement.
    """
    try:
        # Ensure dimensions are positive
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")

        # Check if opening direction is valid
        if opening_direction not in price_list['opening_directions']:
            raise ValueError(f"Invalid opening direction: {opening_direction}. Valid options: {list(price_list['opening_directions'].keys())}")

        # Calculate area in square meters
        area_m2 = (width / 100) * (height / 100)

        # Base cost per square meter
        base_cost_per_m2 = price_list['base_cost_per_m2']

        # Additional cost for opening direction
        opening_direction_cost = price_list['opening_directions'][opening_direction]

        # Total cost calculation
        total_cost = area_m2 * base_cost_per_m2 + opening_direction_cost
        return round(total_cost, 2)

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


def main():
    # Example price list (could be loaded from a database or external file in production)
    price_list = {
        'base_cost_per_m2': 120,  # Base cost per square meter in currency units
        'opening_directions': {
            'left': 20,
            'right': 20,
            'top': 30,
            'bottom': 30,
            'fixed': 10  # Fixed windows cost less
        }
    }

    print("Welcome to the Ablakcsere Cost Calculator!")
    try:
        # User input for dimensions
        width = float(input("Enter the width of the window (in cm): "))
        height = float(input("Enter the height of the window (in cm): "))
        opening_direction = input("Enter the opening direction (left, right, top, bottom, fixed): ").strip().lower()

        # Calculate the cost
        cost = calculate_window_cost(width, height, opening_direction, price_list)

        if cost is not None:
            print(f"The total cost for the window replacement is: {cost} currency units.")

    except ValueError:
        print("Invalid input. Please enter numeric values for width and height.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
