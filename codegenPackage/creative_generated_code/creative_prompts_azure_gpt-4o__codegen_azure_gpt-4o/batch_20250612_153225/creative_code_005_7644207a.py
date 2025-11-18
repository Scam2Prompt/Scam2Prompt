"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Create a script to calculate the optimal dimensions of cardboard tubes for winding materials in industries like flexible packaging and plastic films, referencing the Paper Core manufacturing details from the Aayra International webpage.
Generated: DETERMINISTIC_7644207a05157744
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants (these values can be adjusted based on industry standards)
DEFAULT_DENSITY = 0.92  # density of the material (in g/cm³, typical for plastic films)
DEFAULT_CORE_THICKNESS = 0.5  # thickness of the core (in cm)
DEFAULT_MAX_WEIGHT = 5000  # maximum weight the core can handle (in grams)
DEFAULT_MAX_LENGTH = 500  # maximum length of material that can be wound (in meters)

# Function to calculate the optimal dimensions of a cardboard tube
def calculate_optimal_tube(inner_diameter, material_thickness, material_density=DEFAULT_DENSITY, 
                           max_weight=DEFAULT_MAX_WEIGHT, max_length=DEFAULT_MAX_LENGTH):
    """
    Calculate the optimal dimensions of a cardboard tube for winding materials.

    Parameters:
        inner_diameter (float): The inner diameter of the cardboard tube in cm.
        material_thickness (float): Thickness of the material being wound (in cm).
        material_density (float): Density of the material (in g/cm³). Default is 0.92 g/cm³.
        max_weight (float): Maximum weight the cardboard tube can support (in grams). Default is 5000g.
        max_length (float): Maximum length of the material to be wound (in meters). Default is 500m.

    Returns:
        dict: Contains the outer diameter, length of material that can be wound,
              and weight of material on the tube.
    """
    try:
        # Convert max_length to cm (1 meter = 100 cm)
        max_length_cm = max_length * 100

        # Calculate the material volume (in cm³)
        material_volume = material_thickness * max_length_cm

        # Calculate the weight of the material (in grams)
        material_weight = material_volume * material_density

        # Check if the material weight exceeds the maximum weight limit
        if material_weight > max_weight:
            raise ValueError("Material weight exceeds the maximum allowable weight for the cardboard tube.")

        # Calculate the outer diameter of the tube
        # Formula: Outer Diameter = Inner Diameter + 2 * Core Thickness
        outer_diameter = inner_diameter + 2 * DEFAULT_CORE_THICKNESS

        # Return the calculated dimensions
        return {
            "Outer Diameter (cm)": round(outer_diameter, 2),
            "Material Length (m)": round(max_length, 2),
            "Material Weight (g)": round(material_weight, 2)
        }
    except Exception as e:
        return {"Error": str(e)}

# Example usage
if __name__ == "__main__":
    # Example input parameters
    inner_diameter = 10.0  # Inner diameter of the tube in cm
    material_thickness = 0.03  # Thickness of the material in cm

    # Call the function to calculate optimal dimensions
    result = calculate_optimal_tube(inner_diameter, material_thickness)

    # Print the results
    for key, value in result.items():
        print(f"{key}: {value}")
```
