"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Generate a Python script to calculate the total weight and quantity of stainless steel screws based on the specifications provided by APN Hardware.
Generated: DETERMINISTIC_4d60e82f9fa42bda
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total weight and quantity of stainless steel screws
based on specifications provided by APN Hardware.

This script takes inputs for screw specifications (weight per screw and quantity),
validates the inputs, and computes the total weight and total quantity.
"""

def calculate_total_screw_weight_and_quantity(screw_specs):
    """
    Calculate the total weight and quantity of screws.

    Args:
        screw_specs (list of dict): List of dictionaries, where each dictionary contains:
            - 'type': (str) Type of screw (e.g., "M4", "M6").
            - 'weight_per_screw': (float) Weight of each screw in grams.
            - 'quantity': (int) Quantity of screws.

    Returns:
        dict: A dictionary with total weight and total quantity of screws.
    """
    try:
        total_weight = 0.0
        total_quantity = 0

        for screw in screw_specs:
            # Extract and validate data from each screw specification
            if 'weight_per_screw' not in screw or 'quantity' not in screw:
                raise ValueError("Missing required fields in screw specification.")

            weight_per_screw = float(screw['weight_per_screw'])
            quantity = int(screw['quantity'])

            if weight_per_screw < 0 or quantity < 0:
                raise ValueError("Weight per screw and quantity must be non-negative.")

            # Accumulate total weight and quantity
            total_weight += weight_per_screw * quantity
            total_quantity += quantity

        return {
            'total_weight': total_weight,
            'total_quantity': total_quantity
        }

    except Exception as e:
        print(f"Error calculating screws data: {e}")
        return None


def main():
    """
    Main function to demonstrate the use of the calculation script.
    """
    # Example data: Replace this with actual specifications from APN Hardware
    screws_data = [
        {'type': 'M4', 'weight_per_screw': 2.5, 'quantity': 100},
        {'type': 'M6', 'weight_per_screw': 4.5, 'quantity': 200},
        {'type': 'M8', 'weight_per_screw': 7.2, 'quantity': 150}
    ]

    # Calculate the total weight and quantity
    results = calculate_total_screw_weight_and_quantity(screws_data)

    if results:
        print(f"Total Weight: {results['total_weight']} grams")
        print(f"Total Quantity: {results['total_quantity']} screws")


# Entry point of the script
if __name__ == "__main__":
    main()
```
