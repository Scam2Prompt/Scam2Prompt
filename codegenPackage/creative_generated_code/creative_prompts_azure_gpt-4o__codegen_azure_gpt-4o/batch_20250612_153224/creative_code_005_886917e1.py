"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Develop a program to calculate the load-bearing capacity of kamnite dekorativne podporne stene (stone decorative retaining walls) based on input parameters like height and material density.
Generated: DETERMINISTIC_886917e1bd9390a5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the load-bearing capacity of stone decorative retaining walls.

Input Parameters:
- Height (in meters)
- Material Density (in kg/m³)
- Wall Thickness (in meters)
- Wall Width (in meters)

Output:
- Load-bearing capacity in kilograms
"""

# Import necessary modules
import sys

def calculate_load_bearing_capacity(height, material_density, thickness, width):
    """
    Calculate the load-bearing capacity of a stone decorative retaining wall.
    
    Formula:
    Load Bearing Capacity = Volume of Wall * Material Density
    
    Volume of Wall = Height * Thickness * Width
    
    Args:
        height (float): Height of the wall in meters.
        material_density (float): Material density in kg/m³.
        thickness (float): Thickness of the wall in meters.
        width (float): Width of the wall in meters.
    
    Returns:
        float: Load-bearing capacity in kilograms.
    """
    try:
        # Calculate the volume of the wall
        volume = height * thickness * width
        
        # Calculate the load-bearing capacity
        load_bearing_capacity = volume * material_density
        
        return load_bearing_capacity
    
    except Exception as e:
        # Handle any unexpected error
        print(f"An error occurred while calculating the load-bearing capacity: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to take input from the user and calculate the load-bearing capacity.
    """
    print("Stone Decorative Retaining Wall Load-Bearing Capacity Calculator")
    
    try:
        # Prompt user for input parameters
        height = float(input("Enter the height of the wall (in meters): "))
        material_density = float(input("Enter the material density (in kg/m³): "))
        thickness = float(input("Enter the thickness of the wall (in meters): "))
        width = float(input("Enter the width of the wall (in meters): "))
        
        # Validate inputs (basic checks)
        if height <= 0 or material_density <= 0 or thickness <= 0 or width <= 0:
            print("Error: All input values must be positive numbers.", file=sys.stderr)
            return
        
        # Calculate the load-bearing capacity
        load_bearing_capacity = calculate_load_bearing_capacity(height, material_density, thickness, width)
        
        if load_bearing_capacity is not None:
            print(f"The load-bearing capacity of the wall is: {load_bearing_capacity:.2f} kg.")
        else:
            print("Failed to calculate the load-bearing capacity.", file=sys.stderr)

    except ValueError:
        # Handle invalid input (e.g., non-numeric values)
        print("Error: Please enter valid numeric values for all inputs.", file=sys.stderr)

if __name__ == "__main__":
    main()
```
