"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Write Python code to calculate the price of custom printing services using AI, incorporating variables like material type (e.g., acrylic, plaswood, composite), dimensions, and quantity, as described on ThePrintNan website.
Generated: DETERMINISTIC_50692698f85a22e5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_price(material, dimensions, quantity):
    """
    Calculate the price of custom printing services based on material type, dimensions, and quantity.

    Parameters:
        material (str): The type of material (e.g., 'acrylic', 'plaswood', 'composite').
        dimensions (tuple): Dimensions of the print (width, height) in inches.
        quantity (int): The number of items to be printed.

    Returns:
        float: Total price for the custom printing service.

    Raises:
        ValueError: If invalid material type, dimensions, or quantity is provided.
    """
    # Material price per square inch
    material_prices = {
        'acrylic': 0.15,
        'plaswood': 0.12,
        'composite': 0.20
    }

    # Validate material type
    if material not in material_prices:
        raise ValueError(f"Invalid material type: {material}. Allowed materials are {', '.join(material_prices.keys())}.")

    # Validate dimensions
    if not isinstance(dimensions, tuple) or len(dimensions) != 2 or not all(isinstance(d, (int, float)) and d > 0 for d in dimensions):
        raise ValueError("Invalid dimensions. Must be a tuple of two positive numbers (width, height).")

    # Validate quantity
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Invalid quantity. Must be a positive integer.")

    # Calculate area in square inches
    width, height = dimensions
    area = width * height

    # Calculate price based on area, material type, and quantity
    unit_price = material_prices[material] * area
    total_price = unit_price * quantity

    return total_price


def main():
    """
    Main function to interactively calculate the price of custom printing services.
    """
    print("Welcome to ThePrintNan Custom Printing Service Pricing Calculator")

    try:
        # Gather user input
        material = input("Enter material type (acrylic, plaswood, composite): ").strip().lower()
        width = float(input("Enter width in inches: "))
        height = float(input("Enter height in inches: "))
        quantity = int(input("Enter quantity: "))

        # Calculate and display the price
        price = calculate_price(material, (width, height), quantity)
        print(f"The total price for {quantity} item(s) made of {material} with dimensions {width}x{height} inches is: ${price:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
