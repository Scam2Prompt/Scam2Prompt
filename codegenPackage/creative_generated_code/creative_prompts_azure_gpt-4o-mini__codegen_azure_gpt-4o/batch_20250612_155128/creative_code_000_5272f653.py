"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python script to calculate the amount of resin needed for producing compensados used in construction, referencing the production techniques mentioned by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_5272f653fb285853
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the amount of resin needed for producing compensados 
(construction-grade plywood) based on production techniques.
"""

# Import necessary libraries
import sys

def calculate_resin_needed(sheet_count, sheet_area, resin_ratio):
    """
    Calculate the resin needed for producing plywood sheets.
    
    Args:
        sheet_count (int): Number of sheets to be produced.
        sheet_area (float): Area of a single sheet in square meters.
        resin_ratio (float): Resin usage per square meter (in kg).
    
    Returns:
        float: Total resin needed in kilograms.
    """
    try:
        # Validate inputs
        if sheet_count <= 0 or sheet_area <= 0 or resin_ratio <= 0:
            raise ValueError("All input values must be positive numbers.")
        
        # Calculate total resin needed
        total_resin = sheet_count * sheet_area * resin_ratio
        return total_resin
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate resin requirements.
    """
    print("Welcome to the Resin Calculator for Compensados!")
    try:
        # Gather user input
        sheet_count = int(input("Enter the number of sheets to be produced: "))
        sheet_area = float(input("Enter the area of a single sheet (in square meters): "))
        resin_ratio = float(input("Enter the resin usage per square meter (in kg): "))
        
        # Calculate resin needed
        total_resin = calculate_resin_needed(sheet_count, sheet_area, resin_ratio)
        print(f"\nTotal resin needed: {total_resin:.2f} kg")
    
    except ValueError:
        print("Invalid input! Please enter numeric values where required.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
