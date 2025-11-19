"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Write a Python script that calculates the required number of Groundcell panels needed for a specific area based on the panel sizes EC100, EC150, and EC200.
Generated: DETERMINISTIC_1e48a339baf5fb79
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Groundcell Panel Calculator

This script calculates the number of Groundcell panels required to cover a specific area.
It supports three panel sizes: EC100, EC150, and EC200.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_panels(area, panel_size):
    """
    Calculate the number of panels required to cover the given area.

    Parameters:
        area (float): The area to be covered (in square meters).
        panel_size (str): The panel size ('EC100', 'EC150', 'EC200').

    Returns:
        int: The number of panels required.
    """
    # Define panel dimensions in square meters
    panel_dimensions = {
        'EC100': 1.0,  # 1 square meter
        'EC150': 1.5,  # 1.5 square meters
        'EC200': 2.0   # 2 square meters
    }

    # Validate panel size
    if panel_size not in panel_dimensions:
        raise ValueError(f"Invalid panel size '{panel_size}'. Valid options are: {', '.join(panel_dimensions.keys())}")

    # Calculate the number of panels (rounding up to ensure full coverage)
    panel_area = panel_dimensions[panel_size]
    num_panels = -(-area // panel_area)  # Ceiling division

    return int(num_panels)

def main():
    """
    Main function to handle user input and calculate the required panels.
    """
    try:
        # Prompt user for input
        print("Groundcell Panel Calculator")
        area = float(input("Enter the area to be covered (in square meters): "))
        panel_size = input("Enter the panel size (EC100, EC150, EC200): ").strip().upper()

        # Validate area input
        if area <= 0:
            raise ValueError("Area must be a positive number.")

        # Calculate the required number of panels
        num_panels = calculate_panels(area, panel_size)

        # Display the result
        print(f"To cover an area of {area:.2f} square meters, you will need {num_panels} {panel_size} panels.")

    except ValueError as ve:
        # Handle invalid input
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Groundcell Panel Calculator.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
