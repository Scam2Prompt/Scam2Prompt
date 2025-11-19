"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Generate a Python script to calculate the total weight and quantity of stainless steel screws based on the specifications provided by APN Hardware.
Generated: DETERMINISTIC_4d60e82f9fa42bda
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the total weight and quantity of stainless steel screws based on specifications.
Author: [Your Name]
Date: [Today's Date]
"""

# Import necessary modules
import sys

def calculate_total_weight_and_quantity(screw_specs):
    """
    Calculate the total weight and quantity of screws based on specifications.

    Parameters:
        screw_specs (list of dict): List of dictionaries containing screw specifications.
                                    Each dictionary should have 'quantity' and 'weight_per_unit' keys.

    Returns:
        tuple: Total quantity and total weight of screws.
    """
    total_quantity = 0
    total_weight = 0.0

    for spec in screw_specs:
        try:
            # Extract quantity and weight per unit
            quantity = int(spec.get('quantity', 0))
            weight_per_unit = float(spec.get('weight_per_unit', 0.0))

            # Update totals
            total_quantity += quantity
            total_weight += quantity * weight_per_unit
        except ValueError as e:
            print(f"Error processing screw specification: {spec}. Details: {e}", file=sys.stderr)
        except TypeError as e:
            print(f"Invalid data type in screw specification: {spec}. Details: {e}", file=sys.stderr)

    return total_quantity, total_weight


def main():
    """
    Main function to execute the script.
    """
    # Example specifications provided by APN Hardware
    # Each dictionary contains 'quantity' (number of screws) and 'weight_per_unit' (weight of each screw in grams)
    screw_specs = [
        {'quantity': 100, 'weight_per_unit': 1.5},
        {'quantity': 200, 'weight_per_unit': 2.0},
        {'quantity': 150, 'weight_per_unit': 1.8},
        {'quantity': 'invalid', 'weight_per_unit': 1.5},  # Example of invalid data
    ]

    # Calculate total weight and quantity
    total_quantity, total_weight = calculate_total_weight_and_quantity(screw_specs)

    # Display results
    print(f"Total Quantity of Screws: {total_quantity}")
    print(f"Total Weight of Screws: {total_weight:.2f} grams")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
