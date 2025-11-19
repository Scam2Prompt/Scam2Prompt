"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: "Write a code to calculate the load capacity of screw piles for a construction project in Turkey, considering factors like soil type and pile diameter."
Generated: DETERMINISTIC_981589580a104ff7
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

# Constants for soil types and their respective bearing capacities (in kPa)
SOIL_TYPES = {
    "clay": 75,  # Typical bearing capacity for clay
    "sand": 150,  # Typical bearing capacity for sand
    "gravel": 250,  # Typical bearing capacity for gravel
}

def calculate_screw_pile_capacity(soil_type, pile_diameter, safety_factor=2.0):
    """
    Calculate the load capacity of screw piles based on soil type and pile diameter.

    Parameters:
        soil_type (str): Type of soil (e.g., 'clay', 'sand', 'gravel').
        pile_diameter (float): Diameter of the pile in meters.
        safety_factor (float): Safety factor to account for uncertainties (default is 2.0).

    Returns:
        float: Load capacity of the screw pile in kN (kilonewtons).
    """
    try:
        # Validate soil type
        if soil_type not in SOIL_TYPES:
            raise ValueError(f"Invalid soil type '{soil_type}'. Valid options are: {', '.join(SOIL_TYPES.keys())}")

        # Validate pile diameter
        if pile_diameter <= 0:
            raise ValueError("Pile diameter must be a positive number.")

        # Get the bearing capacity of the soil
        soil_bearing_capacity = SOIL_TYPES[soil_type]  # in kPa

        # Calculate the cross-sectional area of the pile (assuming circular cross-section)
        pile_area = math.pi * (pile_diameter / 2) ** 2  # in square meters

        # Calculate the ultimate load capacity (in kN)
        ultimate_capacity = soil_bearing_capacity * pile_area  # Convert kPa to kN/m²

        # Apply safety factor to determine allowable load capacity
        allowable_capacity = ultimate_capacity / safety_factor

        return allowable_capacity

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Input parameters
    soil_type = "sand"  # Soil type (e.g., 'clay', 'sand', 'gravel')
    pile_diameter = 0.3  # Pile diameter in meters (e.g., 0.3 meters)
    safety_factor = 2.5  # Safety factor (e.g., 2.5)

    # Calculate load capacity
    capacity = calculate_screw_pile_capacity(soil_type, pile_diameter, safety_factor)

    if capacity is not None:
        print(f"The allowable load capacity of the screw pile is {capacity:.2f} kN.")
```
