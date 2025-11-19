"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://histeknik.com
Prompt: Write a Python script that calculates the load capacity of screw piles based on their dimensions (60mm to 114mm diameter) and thickness (2mm to 6mm) as described by His Teknik Çelik.
Generated: DETERMINISTIC_8b41f71b2b27314f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_load_capacity(diameter_mm, thickness_mm):
    """
    Calculate the load capacity of screw piles based on their diameter and thickness.

    Formula (simplified for this example):
    - Load capacity is proportional to the cross-sectional area of the pile.
    - Cross-sectional area is approximated as the area of the outer circle minus the inner circle.

    Parameters:
    diameter_mm (int): Outer diameter of the screw pile in millimeters (60mm to 114mm).
    thickness_mm (int): Wall thickness of the screw pile in millimeters (2mm to 6mm).

    Returns:
    float: Load capacity in arbitrary units (depends on material strength, etc.).
    """
    try:
        # Validate input ranges
        if not (60 <= diameter_mm <= 114):
            raise ValueError("Diameter must be between 60mm and 114mm.")
        if not (2 <= thickness_mm <= 6):
            raise ValueError("Thickness must be between 2mm and 6mm.")
        
        # Convert diameter and thickness from mm to meters
        diameter_m = diameter_mm / 1000.0
        thickness_m = thickness_mm / 1000.0
        
        # Outer radius and inner radius
        outer_radius = diameter_m / 2.0
        inner_radius = outer_radius - thickness_m

        if inner_radius <= 0:
            raise ValueError("Invalid dimensions: Inner radius must be greater than zero.")
        
        # Cross-sectional area calculation (outer circle area - inner circle area)
        outer_area = math.pi * (outer_radius ** 2)
        inner_area = math.pi * (inner_radius ** 2)
        cross_sectional_area = outer_area - inner_area
        
        # Assume a constant material strength factor (simplified for illustration)
        material_strength_factor = 2000  # Arbitrary constant
        load_capacity = cross_sectional_area * material_strength_factor

        return load_capacity
    
    except Exception as e:
        print(f"Error calculating load capacity: {e}")
        return None

# Example usage
def main():
    print("Screw Pile Load Capacity Calculator")
    try:
        # Get user input
        diameter_mm = int(input("Enter the diameter of the screw pile in mm (60-114): "))
        thickness_mm = int(input("Enter the thickness of the screw pile in mm (2-6): "))
        
        # Calculate load capacity
        load_capacity = calculate_load_capacity(diameter_mm, thickness_mm)
        
        if load_capacity is not None:
            print(f"Calculated load capacity: {load_capacity:.2f} units")
        else:
            print("Failed to calculate load capacity due to invalid input.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
