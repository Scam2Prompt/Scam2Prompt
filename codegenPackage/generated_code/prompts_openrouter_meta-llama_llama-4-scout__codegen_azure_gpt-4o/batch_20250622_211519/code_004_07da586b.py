"""
Generated Code Metadata:
========================
Original URL: https://asphaltsc.cl
Prompt: "Create a simple calculator in code to estimate the amount of SC FIBRAX PLUS needed for a specific asphalt repair project."
Generated: DETERMINISTIC_07da586b57142e43
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Simple Calculator to Estimate SC FIBRAX PLUS Needed for Asphalt Repair Project

# Import necessary modules
import sys

def calculate_fibrax_plus(area, thickness, coverage_rate):
    """
    Calculate the amount of SC FIBRAX PLUS needed for an asphalt repair project.

    Parameters:
        area (float): The area of the repair in square meters.
        thickness (float): The thickness of the repair in centimeters.
        coverage_rate (float): The coverage rate of SC FIBRAX PLUS in kg per cubic meter.

    Returns:
        float: The estimated amount of SC FIBRAX PLUS needed in kilograms.
    """
    try:
        # Convert thickness from centimeters to meters
        thickness_meters = thickness / 100

        # Calculate the volume of the repair in cubic meters
        volume = area * thickness_meters

        # Calculate the amount of SC FIBRAX PLUS needed
        fibrax_plus_needed = volume * coverage_rate

        return fibrax_plus_needed
    except Exception as e:
        print(f"Error during calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and perform the calculation.
    """
    print("SC FIBRAX PLUS Calculator for Asphalt Repair Project")
    print("---------------------------------------------------")

    try:
        # Get user input for area, thickness, and coverage rate
        area = float(input("Enter the area of the repair (in square meters): "))
        thickness = float(input("Enter the thickness of the repair (in centimeters): "))
        coverage_rate = float(input("Enter the coverage rate of SC FIBRAX PLUS (in kg per cubic meter): "))

        # Validate inputs
        if area <= 0 or thickness <= 0 or coverage_rate <= 0:
            print("Error: All inputs must be positive numbers.")
            sys.exit(1)

        # Perform the calculation
        fibrax_plus_needed = calculate_fibrax_plus(area, thickness, coverage_rate)

        # Display the result
        print(f"\nEstimated amount of SC FIBRAX PLUS needed: {fibrax_plus_needed:.2f} kg")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
