"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Write a Python script that calculates the load capacity of screw piles based on their dimensions (60mm to 114mm diameter) and thickness (2mm to 6mm) as described by His Teknik Çelik.
Generated: DETERMINISTIC_8b41f71b2b27314f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_load_capacity(diameter, thickness, material_yield_strength=235, safety_factor=1.5):
    """
    Calculate the load capacity of screw piles based on dimensions and material properties.
    
    Args:
        diameter (float): Diameter of the screw pile in mm (60mm to 114mm).
        thickness (float): Thickness of the screw pile wall in mm (2mm to 6mm).
        material_yield_strength (float, optional): Yield strength of the material in MPa. Defaults to 235 MPa (standard for structural steel).
        safety_factor (float, optional): Safety factor for design. Defaults to 1.5.
        
    Returns:
        float: Load capacity in kN.
        
    Raises:
        ValueError: If diameter or thickness are outside specified ranges.
    """
    # Validate input parameters
    if not (60 <= diameter <= 114):
        raise ValueError("Diameter must be between 60mm and 114mm")
    if not (2 <= thickness <= 6):
        raise ValueError("Thickness must be between 2mm and 6mm")
    if material_yield_strength <= 0:
        raise ValueError("Material yield strength must be positive")
    if safety_factor <= 0:
        raise ValueError("Safety factor must be positive")
    
    # Calculate cross-sectional area (mm²)
    outer_radius = diameter / 2
    inner_radius = outer_radius - thickness
    cross_sectional_area = math.pi * (outer_radius**2 - inner_radius**2)
    
    # Calculate load capacity (N)
    load_capacity_N = (material_yield_strength * cross_sectional_area) / safety_factor
    
    # Convert to kN and return
    return load_capacity_N / 1000

def main():
    """Main function to demonstrate the load capacity calculation."""
    try:
        # Example usage
        diameter = float(input("Enter screw pile diameter (mm, 60-114): "))
        thickness = float(input("Enter wall thickness (mm, 2-6): "))
        
        load_capacity = calculate_load_capacity(diameter, thickness)
        print(f"Load capacity: {load_capacity:.2f} kN")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
