"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Write a script that generates quotes for custom apparel orders based on user input, reflecting the pricing model used by Bern Wears.
Generated: DETERMINISTIC_844a4689d6f0a900
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_quote(quantity, print_option, shirt_type):
    """
    Calculate the cost for custom apparel based on quantity, print option, and shirt type.

    Args:
        quantity (int): Number of shirts being ordered.
        print_option (str): Type of print ('single-color', 'multi-color', or 'full-color').
        shirt_type (str): Type of shirt ('basic', 'premium', or 'luxury').

    Returns:
        float: Total cost of the order.
    """
    # Base prices for each shirt type
    base_price = {
        'basic': 5.00,
        'premium': 8.00,
        'luxury': 12.00
    }

    # Print costs per shirt for various print options
    print_cost = {
        'single-color': 2.00,
        'multi-color': 4.00,
        'full-color': 6.00
    }

    # Validate input
    if shirt_type not in base_price:
        raise ValueError(f"Invalid shirt type: {shirt_type}. Expected 'basic', 'premium', or 'luxury'.")
    if print_option not in print_cost:
        raise ValueError(f"Invalid print option: {print_option}. Expected 'single-color', 'multi-color', or 'full-color'.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    # Calculate the total cost
    cost_per_shirt = base_price[shirt_type] + print_cost[print_option]
    total_cost = cost_per_shirt * quantity

    # Apply discount for bulk orders (10% off for orders of 100+ shirts)
    if quantity >= 100:
        total_cost *= 0.90  # 10% discount

    return round(total_cost, 2)


def main():
    """
    Main function to handle user input and generate quotes.
    """
    print("Welcome to Bern Wears Quote Generator!")

    try:
        # Get user input
        quantity = int(input("Enter the quantity of shirts: "))
        print_option = input("Enter the print option ('single-color', 'multi-color', 'full-color'): ").strip().lower()
        shirt_type = input("Enter the shirt type ('basic', 'premium', 'luxury'): ").strip().lower()

        # Calculate quote
        total_cost = calculate_quote(quantity, print_option, shirt_type)

        # Display result
        print(f"The total cost for your order is: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
