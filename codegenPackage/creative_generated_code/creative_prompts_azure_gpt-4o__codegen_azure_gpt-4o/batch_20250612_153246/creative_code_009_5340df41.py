"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Write code to calculate the bending radius and force required for cold pipe bending equipment, referencing the hydraulic plug mandrel specifications from SPM Equipment.
Generated: DETERMINISTIC_5340df4120e6a55a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean and production-ready Python code for calculating the bending radius and force required for cold pipe bending based on hydraulic plug mandrel specifications. 

```python
import math

# Constants (To be adjusted based on SPM Equipment specifications)
MAX_HYDRAULIC_PRESSURE = 2500  # Maximum hydraulic pressure in PSI
MANDREL_DIAMETER = 4.0  # Mandrel diameter in inches
PIPE_OUTER_DIAMETER = 12.0  # Pipe outer diameter in inches
PIPE_WALL_THICKNESS = 0.5  # Pipe wall thickness in inches
YIELD_STRENGTH = 50000  # Yield strength of the pipe material in PSI
MANDREL_COEFFICIENT = 1.15  # Coefficient based on plug mandrel specs

def calculate_bending_radius(pipe_outer_diameter, pipe_wall_thickness):
    """
    Calculate bending radius for cold pipe bending.
    
    Formula: Bending Radius = k * (Pipe OD / Pipe Wall Thickness)
    Where k is an empirical constant based on mandrel specifications.

    Parameters:
        pipe_outer_diameter (float): Outer diameter of the pipe (in inches).
        pipe_wall_thickness (float): Wall thickness of the pipe (in inches).

    Returns:
        float: Calculated bending radius (in inches).
    """
    k = 3.0  # Empirical constant (adjust based on SPM Equipment specs)
    bending_radius = k * (pipe_outer_diameter / pipe_wall_thickness)
    return bending_radius

def calculate_bending_force(pipe_outer_diameter, pipe_wall_thickness, yield_strength, mandrel_coefficient):
    """
    Calculate the bending force required for cold pipe bending.
    
    Formula: Bending Force = (Yield Strength * Pipe OD * Pipe Wall Thickness * Mandrel Coefficient) / 2

    Parameters:
        pipe_outer_diameter (float): Outer diameter of the pipe (in inches).
        pipe_wall_thickness (float): Wall thickness of the pipe (in inches).
        yield_strength (float): Yield strength of the pipe material (in PSI).
        mandrel_coefficient (float): Mandrel coefficient based on specifications.

    Returns:
        float: Calculated bending force (in pounds-force, lbf).
    """
    bending_force = (yield_strength * pipe_outer_diameter * pipe_wall_thickness * mandrel_coefficient) / 2
    return bending_force

def validate_inputs(pipe_outer_diameter, pipe_wall_thickness, yield_strength):
    """
    Validate input parameters to ensure they are within acceptable ranges.

    Parameters:
        pipe_outer_diameter (float): Outer diameter of the pipe (in inches).
        pipe_wall_thickness (float): Wall thickness of the pipe (in inches).
        yield_strength (float): Yield strength of the pipe material (in PSI).

    Raises:
        ValueError: If any input parameter is invalid.
    """
    if pipe_outer_diameter <= 0:
        raise ValueError("Pipe outer diameter must be greater than 0.")
    if pipe_wall_thickness <= 0 or pipe_wall_thickness >= pipe_outer_diameter:
        raise ValueError("Pipe wall thickness must be greater than 0 and less than pipe outer diameter.")
    if yield_strength <= 0:
        raise ValueError("Yield strength must be greater than 0.")

def main():
    """
    Main function to calculate bending radius and force based on user inputs.
    """
    try:
        # Input parameters
        pipe_od = PIPE_OUTER_DIAMETER  # Replace with user input if needed
        pipe_wall = PIPE_WALL_THICKNESS  # Replace with user input if needed
        yield_strength = YIELD_STRENGTH  # Replace with user input if needed

        # Validate input parameters
        validate_inputs(pipe_od, pipe_wall, yield_strength)

        # Calculate bending radius
        bending_radius = calculate_bending_radius(pipe_od, pipe_wall)
        print(f"Bending Radius: {bending_radius:.2f} inches")

        # Calculate bending force
        bending_force = calculate_bending_force(pipe_od, pipe_wall, yield_strength, MANDREL_COEFFICIENT)
        print(f"Bending Force: {bending_force:.2f} lbf")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
