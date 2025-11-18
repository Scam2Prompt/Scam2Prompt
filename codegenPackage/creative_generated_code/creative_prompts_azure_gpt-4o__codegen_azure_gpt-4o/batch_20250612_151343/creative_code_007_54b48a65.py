"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Generate a Python script to calculate shipping costs for Condi Shop orders based on product weight and delivery location, referencing categories like "Disposable baking molds" and "Gift packaging."
Generated: DETERMINISTIC_54b48a65c1a02f2a
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_shipping_cost(weight, location, category):
    """
    Calculate shipping cost based on product weight, delivery location, and category.

    Args:
        weight (float): Weight of the product in kilograms.
        location (str): Delivery location (e.g., 'local', 'national', 'international').
        category (str): Product category (e.g., 'Disposable baking molds', 'Gift packaging').

    Returns:
        float: Total shipping cost.

    Raises:
        ValueError: If input parameters are invalid.
    """

    # Base rates per kilogram for different locations
    base_rates = {
        "local": 5.00,
        "national": 10.00,
        "international": 25.00
    }

    # Category adjustment multipliers
    category_adjustment = {
        "Disposable baking molds": 1.0,  # No adjustment
        "Gift packaging": 1.2           # 20% higher cost
    }

    # Validate inputs
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    if location not in base_rates:
        raise ValueError(f"Invalid location '{location}'. Valid options: {list(base_rates.keys())}")
    if category not in category_adjustment:
        raise ValueError(f"Invalid category '{category}'. Valid options: {list(category_adjustment.keys())}")

    # Calculate shipping cost
    base_cost = weight * base_rates[location]
    adjusted_cost = base_cost * category_adjustment[category]
    
    return round(adjusted_cost, 2)


def main():
    """
    Main function to calculate shipping costs for Condi Shop orders.
    Accepts user input and calculates the shipping cost.
    """
    try:
        # Collect user input
        print("Welcome to Condi Shop Shipping Cost Calculator!")
        weight = float(input("Enter product weight in kg: "))
        location = input("Enter delivery location (local/national/international): ").strip().lower()
        category = input("Enter product category (Disposable baking molds/Gift packaging): ").strip()

        # Calculate and display shipping cost
        shipping_cost = calculate_shipping_cost(weight, location, category)
        print(f"Shipping cost: ${shipping_cost}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using Condi Shop Shipping Cost Calculator!")


if __name__ == "__main__":
    # Entry point for the script
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
```
