"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python script to calculate the amount of resin needed for producing compensados used in construction, referencing the production techniques mentioned by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_5272f653fb285853
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the amount of resin needed for producing compensados (plywood) used in construction.
This script is based on general production techniques and allows customization of parameters.
"""

# Import necessary modules
import sys

def calculate_resin_needed(sheet_area, resin_ratio):
    """
    Calculate the amount of resin needed for plywood production.

    Parameters:
        sheet_area (float): Total area of plywood sheets in square meters (m²).
        resin_ratio (float): Resin required per square meter (kg/m²).

    Returns:
        float: Total resin needed in kilograms (kg).
    """
    try:
        # Ensure inputs are valid
        if sheet_area <= 0 or resin_ratio <= 0:
            raise ValueError("Sheet area and resin ratio must be positive numbers.")
        
        # Calculate resin needed
        resin_needed = sheet_area * resin_ratio
        return resin_needed
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

def main():
    """
    Main function to execute the resin calculation.
    """
    try:
        # Input: Total area of plywood sheets (m²)
        sheet_area = float(input("Enter the total area of plywood sheets (m²): "))
        
        # Input: Resin required per square meter (kg/m²)
        resin_ratio = float(input("Enter the resin required per square meter (kg/m²): "))
        
        # Calculate resin needed
        resin_needed = calculate_resin_needed(sheet_area, resin_ratio)
        
        # Output the result
        print(f"Total resin needed: {resin_needed:.2f} kg")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
