"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Write a program to simulate the extrusion process for polypropylene yarn and PP spun-bound fabrics, incorporating the use of stainless steel wire mesh filters as described by Aayra International.
Generated: DETERMINISTIC_154df3ed2f47b07a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a simulation program in Python for the described process:

```python
import logging

# Configure logging for debugging and production use
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define custom exceptions for error handling
class ExtrusionProcessError(Exception):
    """Custom exception for errors during the extrusion process."""
    pass

class MaterialError(Exception):
    """Custom exception for unsupported materials."""
    pass

# Constants for simulation
SUPPORTED_MATERIALS = ["polypropylene"]
STAINLESS_STEEL_MESH_FILTERS = ["Mesh_100", "Mesh_200", "Mesh_400"]  # Example filter grades
TEMPERATURE_RANGE = (200, 250)  # Acceptable temperature range in Celsius
PRESSURE_RANGE = (50, 100)  # Acceptable pressure range in Bars

# Functions for the extrusion process
def validate_material(material):
    """
    Validates the material for extrusion.

    :param material: Material to be validated.
    :raises MaterialError: If the material is not supported.
    """
    if material.lower() not in SUPPORTED_MATERIALS:
        raise MaterialError(f"Material '{material}' is not supported for extrusion.")
    logging.info(f"Material '{material}' validated successfully.")

def validate_temperature(temperature):
    """
    Validates the extrusion temperature.

    :param temperature: Temperature in Celsius.
    :raises ExtrusionProcessError: If the temperature is out of range.
    """
    if not (TEMPERATURE_RANGE[0] <= temperature <= TEMPERATURE_RANGE[1]):
        raise ExtrusionProcessError(f"Temperature {temperature}C is out of the acceptable range {TEMPERATURE_RANGE}.")
    logging.info(f"Temperature {temperature}C validated successfully.")

def validate_pressure(pressure):
    """
    Validates the extrusion pressure.

    :param pressure: Pressure in Bars.
    :raises ExtrusionProcessError: If the pressure is out of range.
    """
    if not (PRESSURE_RANGE[0] <= pressure <= PRESSURE_RANGE[1]):
        raise ExtrusionProcessError(f"Pressure {pressure} Bars is out of the acceptable range {PRESSURE_RANGE}.")
    logging.info(f"Pressure {pressure} Bars validated successfully.")

def simulate_extrusion(material, temperature, pressure, filter_grade):
    """
    Simulates the extrusion process.

    :param material: Material to be extruded.
    :param temperature: Extrusion temperature in Celsius.
    :param pressure: Extrusion pressure in Bars.
    :param filter_grade: Stainless steel wire mesh filter grade.
    :return: Simulation result as a string.
    :raises ExtrusionProcessError: If any validation fails.
    """
    try:
        # Validate inputs
        validate_material(material)
        validate_temperature(temperature)
        validate_pressure(pressure)
        
        if filter_grade not in STAINLESS_STEEL_MESH_FILTERS:
            raise ExtrusionProcessError(f"Filter grade '{filter_grade}' is not supported.")

        # Simulate extrusion process
        logging.info(f"Starting extrusion process for {material} with filter '{filter_grade}'...")
        simulated_result = (
            f"Extrusion of '{material}' successful at {temperature}C and {pressure} Bars using filter '{filter_grade}'."
        )
        logging.info("Extrusion process completed successfully.")
        return simulated_result

    except Exception as e:
        # Handle any exceptions and log them
        logging.error(f"Error during extrusion process: {e}")
        raise

# Main function for execution
def main():
    """
    Entry point for the simulation program.
    """
    try:
        # Example input parameters
        material = "Polypropylene"
        temperature = 230  # Celsius
        pressure = 75  # Bars
        filter_grade = "Mesh_200"

        # Run simulation
        result = simulate_extrusion(material, temperature, pressure, filter_grade)
        print(result)

    except ExtrusionProcessError as e:
        print(f"Simulation failed: {e}")
    except MaterialError as e:
        print(f"Material validation failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
