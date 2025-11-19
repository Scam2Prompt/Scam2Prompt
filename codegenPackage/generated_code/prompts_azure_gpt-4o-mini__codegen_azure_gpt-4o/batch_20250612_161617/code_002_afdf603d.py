"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Write a Python script that simulates the estimation of costs for custom printed packaging based on the unique features highlighted on the Metis website.
Generated: DETERMINISTIC_afdf603dd2509f4d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_cost(dimensions, material, print_quality, quantity):
    """
    Calculate the cost of custom printed packaging based on dimensions, material, print quality, and quantity.

    Parameters:
        dimensions (tuple): Dimensions of the packaging (length, width, height) in cm.
        material (str): Type of material (e.g., 'cardboard', 'plastic', 'metal').
        print_quality (str): Print quality ('standard', 'premium', 'luxury').
        quantity (int): Number of units to be produced.

    Returns:
        float: Estimated cost of the packaging.
    """
    try:
        # Base cost per unit based on material
        material_cost = {
            'cardboard': 0.5,
            'plastic': 1.0,
            'metal': 2.0
        }
        if material not in material_cost:
            raise ValueError(f"Invalid material type: {material}. Choose from 'cardboard', 'plastic', or 'metal'.")

        # Print quality multiplier
        print_quality_multiplier = {
            'standard': 1.0,
            'premium': 1.5,
            'luxury': 2.0
        }
        if print_quality not in print_quality_multiplier:
            raise ValueError(f"Invalid print quality: {print_quality}. Choose from 'standard', 'premium', or 'luxury'.")

        # Calculate volume in cubic cm
        length, width, height = dimensions
        volume = length * width * height

        # Base cost calculation
        base_cost = volume * material_cost[material] * print_quality_multiplier[print_quality]

        # Apply quantity discount
        if quantity >= 1000:
            discount = 0.2  # 20% discount for bulk orders
        elif quantity >= 500:
            discount = 0.1  # 10% discount for medium orders
        else:
            discount = 0.0  # No discount for small orders

        total_cost = base_cost * quantity * (1 - discount)
        return round(total_cost, 2)

    except Exception as e:
        print(f"Error calculating cost: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to simulate cost estimation for custom printed packaging.
    """
    print("Custom Printed Packaging Cost Estimator")
    print("---------------------------------------")

    try:
        # Get user input
        length = float(input("Enter length of packaging (cm): "))
        width = float(input("Enter width of packaging (cm): "))
        height = float(input("Enter height of packaging (cm): "))
        material = input("Enter material type ('cardboard', 'plastic', 'metal'): ").strip().lower()
        print_quality = input("Enter print quality ('standard', 'premium', 'luxury'): ").strip().lower()
        quantity = int(input("Enter quantity of packaging: "))

        # Validate dimensions and quantity
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate cost
        cost = calculate_cost((length, width, height), material, print_quality, quantity)
        if cost is not None:
            print(f"Estimated cost for {quantity} units: ${cost}")
        else:
            print("Failed to calculate cost due to an error.")

    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
