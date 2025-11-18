"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Create code to calculate the vulcanization temperature for industrial belts, specifically referencing the "SERVICIO VULCANIZADOS LAMINADOS" offered by KOVE Industrial.
Generated: DETERMINISTIC_abe02a8e40efb54a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: vulcanization_temperature_calculator.py
# Description: This script calculates the vulcanization temperature for industrial belts
# for the service "SERVICIO VULCANIZADOS LAMINADOS" offered by KOVE Industrial.
# Author: [Your Name]
# Created on: [Today's Date]

# Required Libraries
import sys

def calculate_vulcanization_temperature(material_type, belt_thickness):
    """
    Calculate the vulcanization temperature based on the material type and belt thickness.

    Parameters:
        material_type (str): The type of belt material (e.g., "Rubber", "Polyurethane").
        belt_thickness (float): The thickness of the belt in millimeters (mm).

    Returns:
        float: The calculated vulcanization temperature in degrees Celsius.
    """
    try:
        # Define base temperatures for different material types
        base_temperatures = {
            "Rubber": 140.0,           # Base temperature for rubber belts in Celsius
            "Polyurethane": 160.0      # Base temperature for polyurethane belts in Celsius
        }

        # Validate input parameters
        if material_type not in base_temperatures:
            raise ValueError(f"Unsupported material type '{material_type}'. Supported types are: {', '.join(base_temperatures.keys())}")

        if belt_thickness <= 0:
            raise ValueError("Belt thickness must be a positive number.")

        # Calculate vulcanization temperature based on material and thickness
        # Formula: Base temperature + (0.5 * belt thickness)
        vulcanization_temperature = base_temperatures[material_type] + (0.5 * belt_thickness)

        return vulcanization_temperature
    except Exception as e:
        # Handle errors gracefully and provide useful feedback
        print(f"Error: {e}")
        return None

def main():
    """
    Main function to execute the vulcanization temperature calculator.
    """
    print("Welcome to the KOVE Industrial Vulcanization Temperature Calculator!")
    print("Servicio: SERVICIO VULCANIZADOS LAMINADOS")

    # Prompt user for material type and belt thickness
    try:
        material_type = input("Enter the belt material type (Rubber/Polyurethane): ").strip()
        belt_thickness = float(input("Enter the belt thickness (in mm): ").strip())

        # Calculate the vulcanization temperature
        vulcanization_temperature = calculate_vulcanization_temperature(material_type, belt_thickness)

        if vulcanization_temperature is not None:
            print(f"The vulcanization temperature for a {material_type} belt with thickness {belt_thickness} mm is: {vulcanization_temperature:.2f} °C")
        else:
            print("Failed to calculate the vulcanization temperature due to input errors.")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
        sys.exit(0)
```
