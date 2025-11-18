"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Create a script to calculate the carbon footprint of a green building project, incorporating sustainability principles outlined by Bismillah Traders.
Generated: DETERMINISTIC_845a2f57fdd4f00a
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
Script to calculate the carbon footprint of a green building project.
This script incorporates sustainability principles outlined by Bismillah Traders.
The calculation includes material carbon emissions, energy consumption, and other factors.
"""

import json

def calculate_material_emissions(materials):
    """
    Calculate the carbon emissions based on the materials used.
    :param materials: List of materials with their quantity and emission factors.
                      Example: [{"name": "Concrete", "quantity": 100, "emission_factor": 0.1}]
    :return: Total material emissions in kilograms of CO2.
    """
    total_emissions = 0
    for material in materials:
        try:
            total_emissions += material["quantity"] * material["emission_factor"]
        except KeyError as e:
            print(f"Error processing material data: Missing key {e}")
    return total_emissions


def calculate_energy_emissions(energy_usage):
    """
    Calculate the carbon emissions based on energy consumption.
    :param energy_usage: Dictionary with energy sources and their emission factors.
                         Example: {"electricity_kwh": 500, "emission_factor": 0.5}
    :return: Total energy emissions in kilograms of CO2.
    """
    try:
        return energy_usage["electricity_kwh"] * energy_usage["emission_factor"]
    except KeyError as e:
        print(f"Error processing energy data: Missing key {e}")
        return 0


def calculate_transport_emissions(transport_data):
    """
    Calculate the carbon emissions based on transportation during the project.
    :param transport_data: List of transport methods with distances and emission factors.
                           Example: [{"method": "Truck", "distance_km": 200, "emission_factor": 3}]
    :return: Total transport emissions in kilograms of CO2.
    """
    total_emissions = 0
    for transport in transport_data:
        try:
            total_emissions += transport["distance_km"] * transport["emission_factor"]
        except KeyError as e:
            print(f"Error processing transport data: Missing key {e}")
    return total_emissions


def calculate_carbon_footprint(data):
    """
    Calculate the total carbon footprint of the green building project.
    :param data: Dictionary containing materials, energy usage, and transport data.
                 Example:
                 {
                     "materials": [{"name": "Concrete", "quantity": 100, "emission_factor": 0.1}],
                     "energy_usage": {"electricity_kwh": 500, "emission_factor": 0.5},
                     "transport": [{"method": "Truck", "distance_km": 200, "emission_factor": 3}]
                 }
    :return: Total carbon footprint in kilograms of CO2.
    """
    materials_emissions = calculate_material_emissions(data.get("materials", []))
    energy_emissions = calculate_energy_emissions(data.get("energy_usage", {}))
    transport_emissions = calculate_transport_emissions(data.get("transport", []))

    total_emissions = materials_emissions + energy_emissions + transport_emissions
    return total_emissions


def main():
    """
    Main function to execute the script.
    Reads input from a JSON file (bismillah_traders_data.json) containing project data,
    calculates the carbon footprint, and prints the results.
    """
    # Load project data from JSON file
    try:
        with open("bismillah_traders_data.json", "r") as file:
            project_data = json.load(file)
    except FileNotFoundError:
        print("Error: Project data file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in project data file.")
        return

    # Calculate the carbon footprint
    total_carbon_footprint = calculate_carbon_footprint(project_data)

    # Print results
    print(f"Total Carbon Footprint of the Green Building Project: {total_carbon_footprint:.2f} kg CO2")


# Run the script
if __name__ == "__main__":
    main()
```
