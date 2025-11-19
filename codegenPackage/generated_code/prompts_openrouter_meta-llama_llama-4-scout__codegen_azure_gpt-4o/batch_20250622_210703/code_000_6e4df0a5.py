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
import math

def calculate_soil_resistivity(voltage, current, electrode_spacing):
    """
    Calculate the electrical resistivity of a soil sample using the Wenner method.

    Parameters:
        voltage (float): Measured voltage in volts (V).
        current (float): Measured current in amperes (A).
        electrode_spacing (float): Distance between electrodes in meters (m).

    Returns:
        float: Soil resistivity in ohm-meters (Ω·m).
    """
    try:
        # Validate inputs
        if voltage <= 0 or current <= 0 or electrode_spacing <= 0:
            raise ValueError("Voltage, current, and electrode spacing must be positive values.")

        # Wenner method formula: ρ = 2 * π * a * (V / I)
        resistivity = 2 * math.pi * electrode_spacing * (voltage / current)
        return resistivity

    except ZeroDivisionError:
        raise ValueError("Current cannot be zero to avoid division by zero.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating soil resistivity: {e}")


def main():
    """
    Main function to interact with the user and calculate soil resistivity.
    """
    print("Soil Resistivity Calculator (Wenner Method)")
    print("Follow the guidelines provided by Marod Consultores for accurate measurements.\n")

    try:
        # Gather user input
        voltage = float(input("Enter the measured voltage (V): "))
        current = float(input("Enter the measured current (A): "))
        electrode_spacing = float(input("Enter the electrode spacing (m): "))

        # Calculate resistivity
        resistivity = calculate_soil_resistivity(voltage, current, electrode_spacing)

        # Display the result
        print(f"\nThe calculated soil resistivity is: {resistivity:.2f} Ω·m")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
