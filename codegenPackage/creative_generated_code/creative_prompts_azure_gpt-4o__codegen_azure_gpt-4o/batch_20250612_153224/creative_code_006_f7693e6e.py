"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Develop a Python script to analyze the efficiency of VinaRoy air blowers in transporting loose materials like grains and powders.
Generated: DETERMINISTIC_f7693e6ec68aea1b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to analyze the efficiency of VinaRoy air blowers in transporting loose materials like grains and powders.

The script calculates the efficiency based on given parameters such as air pressure, flow rate, and material type.
It includes error handling for invalid inputs and ensures clean, modular, and production-ready code.
"""

import logging

# Configure logging for debugging and error reporting
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define constants for efficiency calculations
GRAVITY = 9.81  # m/s^2, acceleration due to gravity
AIR_DENSITY = 1.225  # kg/m^3, density of air at sea level, 15°C

# Supported material types
SUPPORTED_MATERIALS = {
    "grains": {"density": 0.8, "friction_coefficient": 0.4},
    "powders": {"density": 0.5, "friction_coefficient": 0.6}
}


def calculate_efficiency(air_pressure, flow_rate, material_type):
    """
    Calculate the efficiency of the air blower in transporting loose materials.

    :param air_pressure: Air pressure in Pascals (Pa).
    :param flow_rate: Flow rate in cubic meters per second (m^3/s).
    :param material_type: Type of material ('grains' or 'powders').
    :return: Efficiency score as a float.
    :raises ValueError: If inputs are invalid or unsupported material type is used.
    """
    try:
        # Validate material type
        if material_type not in SUPPORTED_MATERIALS:
            raise ValueError(f"Unsupported material type: {material_type}. "
                             f"Supported types are: {', '.join(SUPPORTED_MATERIALS.keys())}")

        # Retrieve material properties
        material_properties = SUPPORTED_MATERIALS[material_type]
        material_density = material_properties["density"]
        friction_coefficient = material_properties["friction_coefficient"]

        # Ensure inputs are positive
        if air_pressure <= 0 or flow_rate <= 0:
            raise ValueError("Air pressure and flow rate must be positive values.")

        # Efficiency calculation (simplified model for demonstration purposes)
        kinetic_energy = 0.5 * AIR_DENSITY * flow_rate ** 2
        work_done_on_material = air_pressure * flow_rate
        energy_loss_due_to_friction = friction_coefficient * material_density * GRAVITY

        efficiency = (work_done_on_material - energy_loss_due_to_friction) / kinetic_energy

        # Clamp the efficiency between 0 and 1
        efficiency = max(0, min(1, efficiency))

        logging.info(f"Efficiency calculated successfully for {material_type}.")
        return round(efficiency, 4)

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise


def main():
    """
    Main function to handle user inputs and execute the efficiency calculation.
    """
    print("VinaRoy Air Blower Efficiency Analysis")
    print("======================================")

    try:
        # Collect inputs from the user
        air_pressure = float(input("Enter air pressure in Pascals (Pa): "))
        flow_rate = float(input("Enter flow rate in cubic meters per second (m^3/s): "))
        material_type = input("Enter material type ('grains' or 'powders'): ").strip().lower()

        # Calculate efficiency
        efficiency = calculate_efficiency(air_pressure, flow_rate, material_type)

        # Display result
        print(f"\nEfficiency Score for {material_type.capitalize()}: {efficiency}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
