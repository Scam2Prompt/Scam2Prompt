"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Write a Python script to calculate the cost estimation for glass and aluminum materials based on the specifications provided by CristalesGraf, including dimensions and material type.
Generated: DETERMINISTIC_88396d3ecf1e0850
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# glass_aluminum_estimator.py
# This script calculates the cost estimation for glass and aluminum materials based on user-provided dimensions and material type.

# Import necessary modules
import sys

def calculate_cost(material_type, width, height, thickness):
    """
    Calculate cost based on material type, dimensions, and thickness.

    Args:
        material_type (str): Type of material ("glass" or "aluminum").
        width (float): Width of the material in meters.
        height (float): Height of the material in meters.
        thickness (float): Thickness of the material in millimeters.

    Returns:
        float: Total cost of the material.
    """
    # Define cost rates (these values can be adjusted based on real pricing data)
    COST_PER_SQ_M_GLASS = 50.0  # Cost per square meter for glass in USD
    COST_PER_SQ_M_ALUMINUM = 80.0  # Cost per square meter for aluminum in USD
    THICKNESS_COST_FACTOR_GLASS = 0.5  # Additional cost per mm of thickness for glass
    THICKNESS_COST_FACTOR_ALUMINUM = 1.0  # Additional cost per mm of thickness for aluminum

    # Validate material type
    if material_type.lower() not in ["glass", "aluminum"]:
        raise ValueError("Invalid material type. Please choose 'glass' or 'aluminum'.")

    # Calculate area in square meters
    area = width * height

    # Calculate cost based on material type
    if material_type.lower() == "glass":
        base_cost = area * COST_PER_SQ_M_GLASS
        thickness_cost = thickness * THICKNESS_COST_FACTOR_GLASS
    else:
        base_cost = area * COST_PER_SQ_M_ALUMINUM
        thickness_cost = thickness * THICKNESS_COST_FACTOR_ALUMINUM

    # Total cost calculation
    total_cost = base_cost + thickness_cost
    return total_cost

def main():
    """
    Main function to handle user input and display the cost estimation.
    """
    try:
        # Prompt user for input
        print("Welcome to CristalesGraf Material Cost Estimator!")
        material_type = input("Enter material type (glass/aluminum): ").strip()
        width = float(input("Enter width in meters: "))
        height = float(input("Enter height in meters: "))
        thickness = float(input("Enter thickness in millimeters: "))

        # Validate dimensions
        if width <= 0 or height <= 0 or thickness <= 0:
            raise ValueError("Dimensions must be positive numbers.")

        # Calculate cost
        total_cost = calculate_cost(material_type, width, height, thickness)

        # Display result
        print(f"The estimated cost for {material_type} is: ${total_cost:.2f} USD")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using CristalesGraf Material Cost Estimator!")

# Entry point for the script
if __name__ == "__main__":
    main()
```
