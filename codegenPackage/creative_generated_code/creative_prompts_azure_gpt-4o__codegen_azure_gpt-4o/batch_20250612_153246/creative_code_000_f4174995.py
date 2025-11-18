"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.marodconsultores.com.pe
Prompt: Write Python code to calculate electrical system resistance values for grounding systems, referencing methodologies used in industrial audits as described by MAROD Consultores SAC.
Generated: DETERMINISTIC_f4174995998d0d5d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_resistance(soil_resistivity, electrode_length, electrode_radius, num_electrodes=1):
    """
    Calculate the electrical system resistance for grounding systems.

    Parameters:
        soil_resistivity (float): The resistivity of the soil in ohm-meters (Ω·m).
        electrode_length (float): The length of the vertical electrode in meters (m).
        electrode_radius (float): The radius of the electrode in meters (m).
        num_electrodes (int, optional): The number of electrodes in the system. Default is 1.

    Returns:
        float: The calculated grounding resistance in ohms (Ω).
    """
    try:
        # Validate input parameters
        if soil_resistivity <= 0 or electrode_length <= 0 or electrode_radius <= 0 or num_electrodes <= 0:
            raise ValueError("All input parameters must be positive numbers.")

        # Resistance calculation based on IEEE standards and MAROD Consultores SAC methodologies
        single_electrode_resistance = (
            soil_resistivity
            / (2 * math.pi * electrode_length)
        ) * math.log(4 * electrode_length / electrode_radius)

        # Adjust for multiple electrodes using approximate parallel resistance formula
        total_resistance = single_electrode_resistance / num_electrodes

        return total_resistance

    except ValueError as e:
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function for execution. Prompts user for input and calculates the resistance values.
    """
    try:
        print("Electrical System Resistance Calculator for Grounding Systems")
        print("-------------------------------------------------------------")

        # Gather input from the user
        soil_resistivity = float(input("Enter soil resistivity (Ω·m): "))
        electrode_length = float(input("Enter electrode length (m): "))
        electrode_radius = float(input("Enter electrode radius (m): "))
        num_electrodes = int(input("Enter number of electrodes: "))

        # Perform resistance calculation
        resistance = calculate_resistance(
            soil_resistivity, electrode_length, electrode_radius, num_electrodes
        )

        if resistance is not None:
            print(f"\nCalculated Grounding Resistance: {resistance:.2f} Ω")
        else:
            print("\nCould not calculate grounding resistance due to input errors.")

    except ValueError:
        print("\nInvalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
