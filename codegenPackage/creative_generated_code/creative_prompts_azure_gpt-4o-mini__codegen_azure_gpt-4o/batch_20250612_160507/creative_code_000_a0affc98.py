"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acess-sushi-swap.blogspot.com
Prompt: Generate a Python script to calculate shipping costs based on user inputs for a stationery store checkout process.
Generated: DETERMINISTIC_a0affc981bb47718
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_shipping_cost(weight, delivery_speed):
    """
    Calculate shipping cost based on weight and delivery speed.

    Args:
        weight (float): Weight of the package in kilograms.
        delivery_speed (str): Delivery option ('standard', 'express').

    Returns:
        float: Calculated shipping cost.
    """
    # Define base rates and per kilogram rates
    BASE_RATE_STANDARD = 5.00
    BASE_RATE_EXPRESS = 10.00
    RATE_PER_KG_STANDARD = 1.50
    RATE_PER_KG_EXPRESS = 3.00

    # Validate delivery speed input
    if delivery_speed not in ['standard', 'express']:
        raise ValueError("Invalid delivery speed. Choose 'standard' or 'express'.")

    # Calculate shipping cost based on delivery speed
    if delivery_speed == 'standard':
        return BASE_RATE_STANDARD + (RATE_PER_KG_STANDARD * weight)
    elif delivery_speed == 'express':
        return BASE_RATE_EXPRESS + (RATE_PER_KG_EXPRESS * weight)


def main():
    """
    Main function to handle user input and calculate shipping costs.
    """
    try:
        # Get user input for weight
        weight = float(input("Enter the weight of the package in kg (e.g., 2.5): "))
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Get user input for delivery speed
        delivery_speed = input("Enter delivery speed ('standard' or 'express'): ").strip().lower()

        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(weight, delivery_speed)

        # Display the calculated cost
        print(f"The shipping cost for your package is: ${shipping_cost:.2f}")

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any other exceptions
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
