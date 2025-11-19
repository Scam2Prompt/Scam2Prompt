"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Create a script to calculate the optimal dimensions of cardboard tubes for winding materials in industries like flexible packaging and plastic films, referencing the Paper Core manufacturing details from the Aayra International webpage.
Generated: DETERMINISTIC_7644207a05157744
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_optimal_dimensions(
    material_thickness: float,
    material_width: float,
    material_length: float,
    max_outer_diameter: float,
    core_inner_diameter: float,
    safety_factor: float = 1.1
) -> dict:
    """
    Calculate optimal cardboard tube dimensions for winding materials.
    
    Args:
        material_thickness: Thickness of the material in mm
        material_width: Width of the material in mm
        material_length: Total length of material to be wound in meters
        max_outer_diameter: Maximum allowed outer diameter of wound roll in mm
        core_inner_diameter: Inner diameter of the cardboard core in mm
        safety_factor: Safety factor to account for material compression (default: 1.1)
        
    Returns:
        Dictionary containing calculated dimensions and other parameters:
        {
            'core_outer_diameter': Optimal core outer diameter in mm,
            'layers': Number of material layers,
            'actual_outer_diameter': Actual outer diameter achieved in mm,
            'core_length': Required core length in mm,
            'material_volume': Volume of material in mm³,
            'is_within_limit': Boolean indicating if within max diameter
        }
        
    Raises:
        ValueError: If any input parameter is invalid
    """
    
    # Validate input parameters
    if any(param <= 0 for param in [material_thickness, material_width, material_length, 
                                   max_outer_diameter, core_inner_diameter]):
        raise ValueError("All dimensions must be positive values")
    
    if safety_factor < 1:
        raise ValueError("Safety factor must be >= 1")
    
    # Convert material length from meters to mm for consistent units
    material_length_mm = material_length * 1000
    
    # Calculate material volume (approximate)
    material_volume = material_thickness * material_width * material_length_mm
    
    # Calculate optimal core outer diameter (based on industry standards)
    # Minimum core OD is typically 1.5x ID for structural integrity
    min_core_od = core_inner_diameter * 1.5
    core_outer_diameter = min_core_od
    
    # Calculate number of layers that can be wound
    max_material_radius = (max_outer_diameter - core_outer_diameter) / 2
    layers = int(max_material_radius / (material_thickness * safety_factor))
    
    # Calculate actual outer diameter achieved
    actual_outer_diameter = core_outer_diameter + (2 * layers * material_thickness * safety_factor)
    
    # Core length should match material width with some tolerance
    core_length = material_width * 1.05  # 5% extra for edge protection
    
    # Check if within maximum diameter limit
    is_within_limit = actual_outer_diameter <= max_outer_diameter
    
    return {
        'core_outer_diameter': round(core_outer_diameter, 2),
        'layers': layers,
        'actual_outer_diameter': round(actual_outer_diameter, 2),
        'core_length': round(core_length, 2),
        'material_volume': round(material_volume, 2),
        'is_within_limit': is_within_limit
    }

def main():
    """Example usage of the dimension calculator."""
    try:
        # Example parameters (values in mm except length in meters)
        params = {
            'material_thickness': 0.05,
            'material_width': 1000,
            'material_length': 5000,
            'max_outer_diameter': 500,
            'core_inner_diameter': 76,
            'safety_factor': 1.15
        }
        
        results = calculate_optimal_dimensions(**params)
        
        print("Optimal Cardboard Tube Dimensions:")
        print(f"Core Inner Diameter: {params['core_inner_diameter']} mm")
        print(f"Core Outer Diameter: {results['core_outer_diameter']} mm")
        print(f"Core Length: {results['core_length']} mm")
        print(f"Number of Material Layers: {results['layers']}")
        print(f"Actual Outer Diameter: {results['actual_outer_diameter']} mm")
        print(f"Material Volume: {results['material_volume']} mm³")
        print(f"Within Maximum Diameter: {'Yes' if results['is_within_limit'] else 'No'}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
