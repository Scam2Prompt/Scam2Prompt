"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Create a function to calculate the material requirements for producing adhesive tapes used in oil transport infrastructure.
Generated: DETERMINISTIC_5e7bebf9f9128983
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

def calculate_material_requirements(tape_length_meters, tape_width_cm, tape_thickness_mm, roll_efficiency=0.95):
    """
    Calculate the material requirements for producing adhesive tapes.

    Parameters:
        tape_length_meters (float): Length of the tape in meters.
        tape_width_cm (float): Width of the tape in centimeters.
        tape_thickness_mm (float): Thickness of the tape in millimeters.
        roll_efficiency (float): Efficiency of material usage (default: 0.95).

    Returns:
        dict: A dictionary containing the material requirements (in cubic meters)
              and waste (in cubic meters).
    """
    try:
        # Input validation
        if tape_length_meters <= 0 or tape_width_cm <= 0 or tape_thickness_mm <= 0:
            raise ValueError("Tape dimensions must be positive values.")
        if not (0 < roll_efficiency <= 1):
            raise ValueError("Roll efficiency must be between 0 and 1.")

        # Convert dimensions to meters
        tape_width_meters = tape_width_cm / 100
        tape_thickness_meters = tape_thickness_mm / 1000

        # Calculate the total material required (volume in cubic meters)
        total_volume = tape_length_meters * tape_width_meters * tape_thickness_meters

        # Adjust for roll efficiency
        usable_material = total_volume * roll_efficiency
        waste_material = total_volume * (1 - roll_efficiency)

        # Return results as a dictionary
        return {
            "usable_material_cubic_meters": usable_material,
            "waste_material_cubic_meters": waste_material,
            "total_material_cubic_meters": total_volume
        }

    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Example tape dimensions
    tape_length = 100  # in meters
    tape_width = 10    # in centimeters
    tape_thickness = 2 # in millimeters
    
    result = calculate_material_requirements(tape_length, tape_width, tape_thickness)
    print(result)
```
