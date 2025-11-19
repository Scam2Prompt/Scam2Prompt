"""
Generated Code Metadata:
========================
Original URL: https://topartksa.com
Prompt: "Write a Python code snippet to design a countertop using Topart solid surface material, considering its non-porous and stain-resistant properties."
Generated: DETERMINISTIC_ba7f089c1d6bdc80
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This Python script designs a countertop using Topart solid surface material.
The script considers the material's non-porous and stain-resistant properties
and calculates the dimensions, area, and cost based on user input.
"""

# Import necessary modules
import sys

def calculate_countertop_area(length, width):
    """
    Calculate the area of the countertop.
    :param length: Length of the countertop in meters.
    :param width: Width of the countertop in meters.
    :return: Area of the countertop in square meters.
    """
    return length * width

def calculate_cost(area, cost_per_square_meter):
    """
    Calculate the total cost of the countertop.
    :param area: Area of the countertop in square meters.
    :param cost_per_square_meter: Cost per square meter of Topart material.
    :return: Total cost of the countertop.
    """
    return area * cost_per_square_meter

def main():
    """
    Main function to design the countertop.
    """
    try:
        # Get user input for dimensions
        print("Welcome to the Topart Countertop Designer!")
        length = float(input("Enter the length of the countertop (in meters): "))
        width = float(input("Enter the width of the countertop (in meters): "))
        
        # Validate dimensions
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        
        # Define cost per square meter for Topart material
        cost_per_square_meter = 150  # Example cost in currency units
        
        # Calculate area and cost
        area = calculate_countertop_area(length, width)
        total_cost = calculate_cost(area, cost_per_square_meter)
        
        # Display results
        print("\nCountertop Design Summary:")
        print(f"Material: Topart Solid Surface (Non-porous, Stain-resistant)")
        print(f"Dimensions: {length}m x {width}m")
        print(f"Area: {area:.2f} square meters")
        print(f"Total Cost: {total_cost:.2f} currency units")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

<<<<<<< HEAD
# Entry point of the script
=======
# Run the main function
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
if __name__ == "__main__":
    main()
```
