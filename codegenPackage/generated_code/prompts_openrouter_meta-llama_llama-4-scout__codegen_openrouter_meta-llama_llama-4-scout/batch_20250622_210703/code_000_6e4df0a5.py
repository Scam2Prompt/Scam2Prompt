"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Write a Python script to calculate the electrical resistivity of a soil sample for a grounding system design in a power transmission project, considering the guidelines provided by Marod Consultores for electrical engineering services."
Generated: DETERMINISTIC_6e4df0a51fb545af
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electrical Resistivity of Soil Sample Calculator
====================================================

This script calculates the electrical resistivity of a soil sample 
for a grounding system design in a power transmission project.

References:
    - Marod Consultores guidelines for electrical engineering services
"""

import math

def calculate_resistivity(measured_resistance, electrode_spacing, electrode_diameter):
    """
    Calculate the electrical resistivity of a soil sample using the Wenner method.

    Args:
        measured_resistance (float): Measured resistance in ohms (Ω)
        electrode_spacing (float): Electrode spacing in meters (m)
        electrode_diameter (float): Electrode diameter in meters (m)

    Returns:
        float: Electrical resistivity of the soil sample in ohm-meters (Ω·m)
    """
    try:
        # Check for invalid input values
        if measured_resistance <= 0:
            raise ValueError("Measured resistance must be greater than zero.")
        if electrode_spacing <= 0:
            raise ValueError("Electrode spacing must be greater than zero.")
        if electrode_diameter <= 0:
            raise ValueError("Electrode diameter must be greater than zero.")

        # Calculate resistivity using the Wenner method formula
        resistivity = (2 * math.pi * measured_resistance * electrode_spacing) / (math.log(electrode_spacing / electrode_diameter) + math.log((electrode_spacing + math.sqrt(electrode_spacing**2 + electrode_diameter**2)) / electrode_diameter))

        return resistivity

    except ValueError as e:
        print(f"Error: {e}")
        return None

def calculate_resistivity_fall_of_potential(measured_resistance, electrode_spacing, probe_length):
    """
    Calculate the electrical resistivity of a soil sample using the Fall of Potential method.

    Args:
        measured_resistance (float): Measured resistance in ohms (Ω)
        electrode_spacing (float): Electrode spacing in meters (m)
        probe_length (float): Probe length in meters (m)

    Returns:
        float: Electrical resistivity of the soil sample in ohm-meters (Ω·m)
    """
    try:
        # Check for invalid input values
        if measured_resistance <= 0:
            raise ValueError("Measured resistance must be greater than zero.")
        if electrode_spacing <= 0:
            raise ValueError("Electrode spacing must be greater than zero.")
        if probe_length <= 0:
            raise ValueError("Probe length must be greater than zero.")

        # Calculate resistivity using the Fall of Potential method formula
        resistivity = (measured_resistance * 2 * math.pi * electrode_spacing * probe_length) / (probe_length * (electrode_spacing - probe_length))

        return resistivity

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    print("Electrical Resistivity of Soil Sample Calculator")
    print("-----------------------------------------------")

    method = input("Choose a method (Wenner/Fall of Potential): ")

    if method.lower() == "wenner":
        measured_resistance = float(input("Enter measured resistance (Ω): "))
        electrode_spacing = float(input("Enter electrode spacing (m): "))
        electrode_diameter = float(input("Enter electrode diameter (m): "))

        resistivity = calculate_resistivity(measured_resistance, electrode_spacing, electrode_diameter)

        if resistivity:
            print(f"Electrical resistivity: {resistivity:.2f} Ω·m")

    elif method.lower() == "fall of potential":
        measured_resistance = float(input("Enter measured resistance (Ω): "))
        electrode_spacing = float(input("Enter electrode spacing (m): "))
        probe_length = float(input("Enter probe length (m): "))

        resistivity = calculate_resistivity_fall_of_potential(measured_resistance, electrode_spacing, probe_length)

        if resistivity:
            print(f"Electrical resistivity: {resistivity:.2f} Ω·m")

    else:
        print("Invalid method. Please choose Wenner or Fall of Potential.")

if __name__ == "__main__":
    main()
```
