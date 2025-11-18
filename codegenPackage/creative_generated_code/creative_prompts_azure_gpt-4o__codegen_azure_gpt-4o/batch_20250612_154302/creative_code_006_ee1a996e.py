"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Develop a script to calculate the optimal settings for tube end facing using the TEF FA Series tools described on the DBX Tools website.
Generated: DETERMINISTIC_ee1a996e1a365289
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_optimal_tube_end_facing_settings(material_type, tube_diameter, wall_thickness):
    """
    Calculate the optimal tube end facing settings based on material type, tube diameter, and wall thickness.

    Parameters:
        material_type (str): The material type of the tube (e.g., "steel", "aluminum", "copper").
        tube_diameter (float): The outer diameter of the tube in millimeters.
        wall_thickness (float): The thickness of the tube wall in millimeters.

    Returns:
        dict: A dictionary containing the calculated settings for speed, feed rate, and cutting depth.
    """

    # Constants for TEF FA Series tools (hypothetical values based on DBX Tools specifications)
    MATERIAL_SETTINGS = {
        "steel": {"speed_factor": 0.8, "feed_rate_factor": 0.6},
        "aluminum": {"speed_factor": 1.2, "feed_rate_factor": 1.0},
        "copper": {"speed_factor": 1.0, "feed_rate_factor": 0.8},
    }

    # Validate material type
    if material_type.lower() not in MATERIAL_SETTINGS:
        raise ValueError(f"Invalid material type '{material_type}'. Supported materials: {', '.join(MATERIAL_SETTINGS.keys())}")

    # Retrieve settings for given material type
    material_settings = MATERIAL_SETTINGS[material_type.lower()]
    speed_factor = material_settings["speed_factor"]
    feed_rate_factor = material_settings["feed_rate_factor"]

    # Calculate optimal speed (RPM) based on tube diameter and material factor
    # Formula: speed = (speed_factor * 1000) / tube_diameter
    optimal_speed = (speed_factor * 1000) / tube_diameter

    # Calculate feed rate (mm/min) based on wall thickness and material factor
    # Formula: feed_rate = feed_rate_factor * wall_thickness
    feed_rate = feed_rate_factor * wall_thickness

    # Calculate cutting depth (mm) with a safety margin based on wall thickness
    # Formula: cutting_depth = max(0.1, wall_thickness * 0.2)
    cutting_depth = max(0.1, wall_thickness * 0.2)

    # Return calculated settings
    return {
        "optimal_speed_rpm": round(optimal_speed, 2),
        "feed_rate_mm_per_min": round(feed_rate, 2),
        "cutting_depth_mm": round(cutting_depth, 2),
    }


def main():
    """
    Main function to demonstrate tube end facing settings calculation.
    """

    print("Tube End Facing Settings Calculator (TEF FA Series Tools)")
    
    # Collect user input
    try:
        material_type = input("Enter material type (steel/aluminum/copper): ").strip()
        tube_diameter = float(input("Enter tube diameter (mm): "))
        wall_thickness = float(input("Enter wall thickness (mm): "))

        # Validate inputs
        if tube_diameter <= 0 or wall_thickness <= 0:
            raise ValueError("Diameter and wall thickness must be positive numbers.")

        # Perform calculations
        settings = calculate_optimal_tube_end_facing_settings(material_type, tube_diameter, wall_thickness)

        # Display results
        print("\nOptimal Tube End Facing Settings:")
        print(f"  Optimal Speed (RPM): {settings['optimal_speed_rpm']}")
        print(f"  Feed Rate (mm/min): {settings['feed_rate_mm_per_min']}")
        print(f"  Cutting Depth (mm): {settings['cutting_depth_mm']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
