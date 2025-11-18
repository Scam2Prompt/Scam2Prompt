"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Generate code to model the thermal expansion of "高压锅炉管" (high-pressure boiler pipes) under varying temperatures, using material properties mentioned on the website.
Generated: DETERMINISTIC_c7c1996fae346088
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Thermal Expansion Model for High-Pressure Boiler Pipes (高压锅炉管)

This Python program calculates the thermal expansion of high-pressure boiler pipes
based on temperature variations. The material properties, such as coefficients of
thermal expansion, are assumed based on typical values for steel used in boiler pipes.
Ensure material properties are verified against actual data before production use.

Dependencies: None (uses standard Python libraries)
"""

# Import necessary libraries
import math

# Constants (Assumed material properties for high-pressure boiler pipes)
COEFFICIENT_OF_THERMAL_EXPANSION = 11.7e-6  # in 1/°C, typical for steel
ORIGINAL_LENGTH = 1000.0  # in mm, initial length of the pipe
TEMPERATURE_RANGE = range(0, 601, 50)  # Temperature range in °C (0°C to 600°C in steps of 50°C)

# Error handling for input validation
def validate_temperature_input(temp):
    """
    Validates the temperature input to ensure it's within a realistic range.
    """
    if temp < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")

# Thermal expansion calculation function
def calculate_thermal_expansion(original_length, temp_change, coeff_thermal_expansion):
    """
    Calculates the thermal expansion of a material based on its properties.

    Parameters:
    - original_length (float): The original length of the material in mm.
    - temp_change (float): The temperature change in °C.
    - coeff_thermal_expansion (float): The coefficient of thermal expansion in 1/°C.

    Returns:
    - float: The new length after thermal expansion in mm.
    """
    try:
        # Validate temperature input
        validate_temperature_input(temp_change)

        # Calculate expanded length
        length_change = original_length * coeff_thermal_expansion * temp_change
        new_length = original_length + length_change

        return new_length
    except Exception as e:
        print(f"Error in calculating thermal expansion: {e}")
        return None

# Main function to model thermal expansion
def main():
    """
    Main function that iterates through a range of temperatures and calculates the
    thermal expansion of high-pressure boiler pipes.
    """
    print("Thermal Expansion Model for High-Pressure Boiler Pipes")
    print("----------------------------------------------------")
    print(f"Original Length: {ORIGINAL_LENGTH} mm")
    print(f"Coefficient of Thermal Expansion: {COEFFICIENT_OF_THERMAL_EXPANSION} 1/°C")
    print("----------------------------------------------------")

    # Iterate over temperature range
    for temperature in TEMPERATURE_RANGE:
        try:
            new_length = calculate_thermal_expansion(
                ORIGINAL_LENGTH, temperature, COEFFICIENT_OF_THERMAL_EXPANSION
            )
            print(
                f"At {temperature}°C, the pipe's new length is: {new_length:.2f} mm."
            )
        except ValueError as ve:
            print(f"Temperature validation error: {ve}")

# Run the main function
if __name__ == "__main__":
    main()
```
