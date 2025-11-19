"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Develop a Python script to calculate the total area of roads and jogging tracks in the Dens Haven project, given the width of 7 meters and the layout specifications.
Generated: DETERMINISTIC_6ab1c8740284ed3b
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_total_area(layout_specs, width=7):
    """
    Calculate the total area of roads and jogging tracks in the Dens Haven project.
    
    Args:
        layout_specs (dict): Dictionary containing layout specifications with keys:
            - 'roads': List of road lengths (in meters)
            - 'tracks': List of jogging track lengths (in meters)
        width (float, optional): Width of roads and tracks in meters. Defaults to 7.
    
    Returns:
        float: Total area in square meters
    
    Raises:
        ValueError: If layout_specs is not a dictionary or missing required keys
        TypeError: If road or track lengths are not numbers
    """
    # Validate input
    if not isinstance(layout_specs, dict):
        raise ValueError("layout_specs must be a dictionary")
    
    required_keys = {'roads', 'tracks'}
    if not required_keys.issubset(layout_specs.keys()):
        raise ValueError(f"layout_specs must contain {required_keys}")
    
    total_area = 0.0
    
    try:
        # Calculate roads area
        for length in layout_specs['roads']:
            if not isinstance(length, (int, float)):
                raise TypeError(f"Road length must be a number, got {type(length)}")
            total_area += length * width
        
        # Calculate tracks area
        for length in layout_specs['tracks']:
            if not isinstance(length, (int, float)):
                raise TypeError(f"Track length must be a number, got {type(length)}")
            total_area += length * width
            
    except Exception as e:
        raise TypeError(f"Invalid length value: {str(e)}")
    
    return round(total_area, 2)

# Example usage
if __name__ == "__main__":
    try:
        # Sample layout specifications
        dens_haven_layout = {
            'roads': [150.5, 200.75, 180.25],
            'tracks': [120.0, 95.5, 110.25]
        }
        
        total_area = calculate_total_area(dens_haven_layout)
        print(f"Total area of roads and jogging tracks: {total_area} square meters")
        
    except Exception as e:
        print(f"Error calculating area: {str(e)}")
```
