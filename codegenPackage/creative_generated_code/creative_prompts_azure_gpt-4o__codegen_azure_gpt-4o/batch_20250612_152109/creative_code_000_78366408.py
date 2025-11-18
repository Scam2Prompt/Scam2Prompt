"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Write Python code to calculate the optimal dimensions for a Caja China based on user input for meat capacity (in kg) and material type (e.g., acero inoxidable or madera laqueada), referencing the product specifications on Meat Master.
Generated: DETERMINISTIC_7836640838889378
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to calculate the optimal dimensions for a Caja China
# based on user input for meat capacity and material type.

# Import necessary modules
import math

def calculate_optimal_dimensions(meat_capacity_kg, material_type):
    """
    Calculate optimal dimensions for a Caja China based on meat capacity and material type.

    Parameters:
    meat_capacity_kg (float): The desired meat capacity in kilograms.
    material_type (str): The type of material (e.g., "acero inoxidable", "madera laqueada").

    Returns:
    dict: Dictionary containing optimal dimensions (length, width, height) in centimeters.
    """
    # Validate inputs
    if meat_capacity_kg <= 0:
        raise ValueError("Meat capacity must be greater than 0 kg.")
    if material_type not in ["acero inoxidable", "madera laqueada"]:
        raise ValueError("Invalid material type. Please choose 'acero inoxidable' or 'madera laqueada'.")

    # Define base specifications for Caja China
    # These factors are derived from Meat Master's typical product specifications.
    material_factors = {
        "acero inoxidable": 1.1,  # Slightly more space-efficient due to thinner walls
        "madera laqueada": 1.25  # Slightly less space-efficient due to thicker insulation
    }

    # Calculate base dimensions using meat capacity
    # Assume a density factor for meat capacity to volume conversion (approx. 60 kg/m³ for packed meat)
    meat_density = 60  # kg/m³
    internal_volume_m3 = meat_capacity_kg / meat_density

    # Convert internal volume to external dimensions (accounting for material type)
    # Assume a rectangular box, with length, width, and height proportional to the cube root of the volume
    efficiency_factor = material_factors[material_type]
    external_volume_m3 = internal_volume_m3 * efficiency_factor
    cube_root = math.pow(external_volume_m3, 1 / 3)
    
    # Calculate dimensions in cm (scaled proportions: length:width:height = 3:2:1)
    length_cm = round(cube_root * 3 * 100, 2)
    width_cm = round(cube_root * 2 * 100, 2)
    height_cm = round(cube_root * 1 * 100, 2)

    # Return dimensions as a dictionary
    return {
        "length_cm": length_cm,
        "width_cm": width_cm,
        "height_cm": height_cm
    }

def main():
    """
    Main function to interact with the user and display optimal Caja China dimensions.
    """
    try:
        # Get user input
        meat_capacity_kg = float(input("Enter the desired meat capacity in kilograms: "))
        material_type = input("Enter the material type ('acero inoxidable' or 'madera laqueada'): ").strip().lower()

        # Calculate optimal dimensions
        dimensions = calculate_optimal_dimensions(meat_capacity_kg, material_type)

        # Display the result
        print("\nOptimal Caja China Dimensions:")
        print(f"Length: {dimensions['length_cm']} cm")
        print(f"Width: {dimensions['width_cm']} cm")
        print(f"Height: {dimensions['height_cm']} cm")
    except ValueError as e:
        # Handle input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
