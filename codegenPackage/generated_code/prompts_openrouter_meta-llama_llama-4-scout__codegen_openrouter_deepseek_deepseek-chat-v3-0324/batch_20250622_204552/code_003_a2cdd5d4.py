"""
Generated Code Metadata:
========================
Original URL: https://topartksa.com
Prompt: "Create a simple calculator to determine the required amount of Topart solid surface material for a sink installation, considering its thickness and dimensions."
Generated: DETERMINISTIC_a2cdd5d476425226
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_material_required(length, width, thickness, unit='mm'):
    """
    Calculate the required amount of Topart solid surface material for a sink installation.
    
    Args:
        length (float): Length of the sink in specified units.
        width (float): Width of the sink in specified units.
        thickness (float): Thickness of the material in specified units.
        unit (str): Unit of measurement ('mm', 'cm', 'm', 'in'). Default is 'mm'.
    
    Returns:
        float: Volume of material required in cubic meters.
    
    Raises:
        ValueError: If any dimension is negative or zero, or if invalid unit is provided.
    """
    # Validate inputs
    if length <= 0 or width <= 0 or thickness <= 0:
        raise ValueError("All dimensions must be positive numbers.")
    
    # Convert all dimensions to meters for consistent calculation
    conversion_factors = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'in': 0.0254
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Invalid unit. Supported units are: {', '.join(conversion_factors.keys())}")
    
    conversion_factor = conversion_factors[unit]
    length_m = length * conversion_factor
    width_m = width * conversion_factor
    thickness_m = thickness * conversion_factor
    
    # Calculate volume (length * width * thickness)
    volume = length_m * width_m * thickness_m
    
    return volume

def main():
    print("Topart Solid Surface Material Calculator")
    print("---------------------------------------")
    
    try:
        # Get user inputs
        unit = input("Enter unit of measurement (mm/cm/m/in): ").lower()
        length = float(input("Enter length of sink: "))
        width = float(input("Enter width of sink: "))
        thickness = float(input("Enter material thickness: "))
        
        # Calculate material required
        volume = calculate_material_required(length, width, thickness, unit)
        
        # Display results
        print("\nResults:")
        print(f"Material required: {volume:.6f} cubic meters")
        print(f"Material required: {volume * 1000000:.2f} cubic centimeters")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
