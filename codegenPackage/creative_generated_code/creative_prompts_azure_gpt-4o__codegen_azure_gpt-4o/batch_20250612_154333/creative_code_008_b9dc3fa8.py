"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Generate a program to calculate the torque required for an earth auger drill to dig through various soil types, referencing the product details on PT. Fuji Metal Teknik's website.
Generated: DETERMINISTIC_b9dc3fa8df437b68
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code in Python:

```python
import math

# Constants for soil types (values are hypothetical; replace with real data if available)
# Torque = Force * Radius
SOIL_TYPES = {
    "sand": 5,       # N/m^2 (resistance factor)
    "clay": 8,       # N/m^2 (resistance factor)
    "gravel": 6,     # N/m^2 (resistance factor)
    "loam": 4        # N/m^2 (resistance factor)
}

# Function to calculate torque required for drilling
def calculate_torque(soil_type, auger_radius, drill_depth):
    """
    Calculate the torque required for an earth auger drill based on soil type, auger radius, and drill depth.

    Parameters:
        soil_type (str): The type of soil (e.g., sand, clay, gravel, loam).
        auger_radius (float): Radius of the auger in meters.
        drill_depth (float): Depth to drill in meters.

    Returns:
        float: Required torque in Newton-meters (Nm).
    """
    try:
        # Validate inputs
        if soil_type not in SOIL_TYPES:
            raise ValueError(f"Invalid soil type '{soil_type}'. Available types: {list(SOIL_TYPES.keys())}")
        if auger_radius <= 0:
            raise ValueError("Auger radius must be a positive number.")
        if drill_depth <= 0:
            raise ValueError("Drill depth must be a positive number.")
        
        # Soil resistance factor
        resistance_factor = SOIL_TYPES[soil_type]

        # Area of the auger blade (assuming it's circular)
        auger_area = math.pi * (auger_radius ** 2)

        # Force required to overcome soil resistance
        force_required = resistance_factor * auger_area * drill_depth

        # Torque calculation
        torque = force_required * auger_radius

        return torque
    except Exception as e:
        print(f"Error: {e}")
        return None

# Main program
if __name__ == "__main__":
    # User input
    print("Welcome to the Earth Auger Torque Calculator")
    soil_type = input("Enter soil type (sand, clay, gravel, loam): ").strip().lower()
    try:
        auger_radius = float(input("Enter auger radius in meters: "))
        drill_depth = float(input("Enter drill depth in meters: "))
    except ValueError:
        print("Invalid input. Please enter numerical values for auger radius and drill depth.")
        exit(1)

    # Calculate torque
    torque = calculate_torque(soil_type, auger_radius, drill_depth)

    if torque is not None:
        print(f"The required torque to drill through {soil_type} soil is {torque:.2f} Nm.")
    else:
        print("Failed to calculate torque due to errors.")
```

### Notes:
- Replace the `SOIL_TYPES` resistance factors with actual data from PT. Fuji Metal Teknik's website if available.
- The program includes input validation and error handling for robustness.
- Ensure proper units are used when integrating real-world data.
