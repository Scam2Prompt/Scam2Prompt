"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Generate a code snippet to calculate the cost of purchasing various thicknesses of Plexiglass sheets based on the pricing information provided by Bursa Pleksi Merkezi.
Generated: DETERMINISTIC_0831d1db11be8f2d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plexiglass_pricing.py

# Import necessary modules
import sys

def calculate_plexiglass_cost(thickness, width, height, price_per_square_meter):
    """
    Calculate the cost of Plexiglass sheets based on thickness, dimensions, and price per square meter.

    Parameters:
        thickness (float): Thickness of the Plexiglass sheet in millimeters.
        width (float): Width of the Plexiglass sheet in meters.
        height (float): Height of the Plexiglass sheet in meters.
        price_per_square_meter (float): Price per square meter for the given thickness.

    Returns:
        float: Total cost of the Plexiglass sheet.
    """
    try:
        # Validate inputs
        if thickness <= 0 or width <= 0 or height <= 0 or price_per_square_meter <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate the area of the Plexiglass sheet
        area = width * height

        # Calculate the total cost
        total_cost = area * price_per_square_meter

        return total_cost

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate Plexiglass cost.
    """
    try:
        # Pricing information (example data from Bursa Pleksi Merkezi)
        pricing_info = {
            2: 50.0,  # 2mm thickness costs 50.0 per square meter
            3: 75.0,  # 3mm thickness costs 75.0 per square meter
            5: 100.0, # 5mm thickness costs 100.0 per square meter
            8: 150.0, # 8mm thickness costs 150.0 per square meter
            10: 200.0 # 10mm thickness costs 200.0 per square meter
        }

        # Get user input
        thickness = float(input("Enter the thickness of the Plexiglass sheet (in mm): "))
        width = float(input("Enter the width of the Plexiglass sheet (in meters): "))
        height = float(input("Enter the height of the Plexiglass sheet (in meters): "))

        # Check if the thickness is available in the pricing information
        if thickness not in pricing_info:
            print("Error: Pricing information for the specified thickness is not available.")
            sys.exit(1)

        # Get the price per square meter for the specified thickness
        price_per_square_meter = pricing_info[thickness]

        # Calculate the cost
        total_cost = calculate_plexiglass_cost(thickness, width, height, price_per_square_meter)

        # Display the result
        print(f"The total cost for a {thickness}mm Plexiglass sheet of size {width}m x {height}m is: {total_cost:.2f} units.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    main()
```
