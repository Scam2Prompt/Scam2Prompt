"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Write Python code to calculate the optimal dimensions for a Caja China based on user input for meat capacity (in kg) and material type (e.g., acero inoxidable or madera laqueada), referencing the product specifications on Meat Master.
Generated: DETERMINISTIC_7836640838889378
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

# Constants for material properties (thermal conductivity in W/mK)
MATERIAL_PROPERTIES = {
    'acero inoxidable': 16.3,
    'madera laqueada': 0.13
}

# Constants for meat density (kg/m³) and cooking parameters
MEAT_DENSITY = 970  # Average density of pork in kg/m³
COOKING_THICKNESS = 0.15  # Recommended thickness of meat layer in meters
HEAT_TRANSFER_RATE = 0.85  # Efficiency factor for heat transfer

def calculate_caja_dimensions(meat_capacity_kg, material_type):
    """
    Calculate optimal dimensions for a Caja China based on meat capacity and material.
    
    Args:
        meat_capacity_kg (float): Amount of meat to be cooked in kilograms
        material_type (str): Type of material ('acero inoxidable' or 'madera laqueada')
    
    Returns:
        dict: Dictionary containing calculated dimensions (length, width, height) in meters
              and material properties
    
    Raises:
        ValueError: If invalid inputs are provided
    """
    # Input validation
    if meat_capacity_kg <= 0:
        raise ValueError("Meat capacity must be positive")
    
    material_type = material_type.lower()
    if material_type not in MATERIAL_PROPERTIES:
        raise ValueError(f"Invalid material type. Must be one of: {list(MATERIAL_PROPERTIES.keys())}")
    
    # Calculate required volume for meat
    meat_volume = meat_capacity_kg / MEAT_DENSITY
    
    # Calculate base area based on recommended cooking thickness
    base_area = meat_volume / COOKING_THICKNESS
    
    # Calculate length and width (assuming square base for optimal heat distribution)
    side_length = math.sqrt(base_area)
    
    # Calculate height (cooking thickness + clearance)
    height = COOKING_THICKNESS * 1.5  # 50% clearance
    
    # Adjust dimensions based on material properties
    material_factor = MATERIAL_PROPERTIES[material_type] / 10  # Scaling factor
    side_length *= (1 + material_factor)
    height *= (1 + material_factor)
    
    return {
        'length_m': round(side_length, 2),
        'width_m': round(side_length, 2),
        'height_m': round(height, 2),
        'material': material_type,
        'thermal_conductivity': f"{MATERIAL_PROPERTIES[material_type]} W/mK",
        'max_meat_capacity_kg': round(meat_capacity_kg, 1)
    }

def main():
    """Main function to get user input and display results."""
    print("Caja China Dimension Calculator")
    print("-------------------------------")
    
    try:
        # Get user input
        meat_capacity = float(input("Enter meat capacity (kg): "))
        material = input("Enter material type (acero inoxidable/madera laqueada): ")
        
        # Calculate dimensions
        dimensions = calculate_caja_dimensions(meat_capacity, material)
        
        # Display results
        print("\nOptimal Caja China Dimensions:")
        print(f"Material: {dimensions['material'].title()}")
        print(f"Length: {dimensions['length_m']} m")
        print(f"Width: {dimensions['width_m']} m")
        print(f"Height: {dimensions['height_m']} m")
        print(f"Thermal Conductivity: {dimensions['thermal_conductivity']}")
        print(f"Max Meat Capacity: {dimensions['max_meat_capacity_kg']} kg")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
