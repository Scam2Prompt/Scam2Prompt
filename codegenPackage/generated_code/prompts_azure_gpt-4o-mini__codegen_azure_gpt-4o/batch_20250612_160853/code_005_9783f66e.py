"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: How do I obtain an Energy Performance Certificate (ΠΕΑ) for a building, and what are the energy categories it can fall into?
Generated: DETERMINISTIC_9783f66efb5140a2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to simulate obtaining an Energy Performance Certificate (ΠΕΑ) for a building
and determining its energy category based on input parameters.

This script is a simulation and does not replace the official process of obtaining
an Energy Performance Certificate. For official certification, consult a licensed energy inspector.
"""

# Import necessary modules
import sys

def get_energy_category(energy_consumption):
    """
    Determine the energy category of a building based on its energy consumption.

    Parameters:
        energy_consumption (float): Annual energy consumption in kWh/m².

    Returns:
        str: Energy category of the building.
    """
    try:
        if energy_consumption < 0:
            raise ValueError("Energy consumption cannot be negative.")

        # Energy categories based on consumption thresholds
        if energy_consumption <= 50:
            return "A+ (Very High Energy Efficiency)"
        elif energy_consumption <= 75:
            return "A (High Energy Efficiency)"
        elif energy_consumption <= 100:
            return "B+ (Above Average Energy Efficiency)"
        elif energy_consumption <= 150:
            return "B (Average Energy Efficiency)"
        elif energy_consumption <= 200:
            return "C (Below Average Energy Efficiency)"
        elif energy_consumption <= 300:
            return "D (Low Energy Efficiency)"
        elif energy_consumption <= 450:
            return "E (Very Low Energy Efficiency)"
        elif energy_consumption <= 600:
            return "F (Poor Energy Efficiency)"
        else:
            return "G (Very Poor Energy Efficiency)"
    except ValueError as e:
        return f"Error: {e}"


def obtain_energy_certificate(building_name, energy_consumption):
    """
    Simulate the process of obtaining an Energy Performance Certificate (ΠΕΑ) for a building.

    Parameters:
        building_name (str): Name of the building.
        energy_consumption (float): Annual energy consumption in kWh/m².

    Returns:
        dict: Details of the Energy Performance Certificate.
    """
    try:
        if not building_name or not isinstance(building_name, str):
            raise ValueError("Building name must be a non-empty string.")
        if not isinstance(energy_consumption, (int, float)):
            raise ValueError("Energy consumption must be a numeric value.")

        # Determine the energy category
        energy_category = get_energy_category(energy_consumption)

        # Generate the certificate details
        certificate = {
            "Building Name": building_name,
            "Energy Consumption (kWh/m²)": energy_consumption,
            "Energy Category": energy_category
        }

        return certificate
    except ValueError as e:
        return {"Error": str(e)}


def main():
    """
    Main function to interact with the user and simulate obtaining an Energy Performance Certificate.
    """
    try:
        print("Welcome to the Energy Performance Certificate (ΠΕΑ) Simulator!")
        
        # Get user input for building name
        building_name = input("Enter the name of the building: ").strip()
        
        # Get user input for energy consumption
        energy_consumption_input = input("Enter the annual energy consumption (kWh/m²): ").strip()
        
        # Validate and convert energy consumption input
        try:
            energy_consumption = float(energy_consumption_input)
        except ValueError:
            print("Error: Energy consumption must be a numeric value.")
            sys.exit(1)
        
        # Obtain the certificate
        certificate = obtain_energy_certificate(building_name, energy_consumption)
        
        # Display the certificate details
        print("\nEnergy Performance Certificate (ΠΕΑ):")
        for key, value in certificate.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    main()
```
