"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Develop a program to calculate the heat output and energy efficiency of bioethanol fireplaces using Planika BEV Technology™.
Generated: DETERMINISTIC_0b5ded63d116ecda
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_heat_output(fuel_consumption_rate, energy_value):
    """
    Calculate the heat output of the bioethanol fireplace.

    Parameters:
        fuel_consumption_rate (float): The rate of fuel consumption in liters per hour.
        energy_value (float): The energy value of bioethanol in MJ per liter.

    Returns:
        float: Heat output in MJ per hour.
    """
    return fuel_consumption_rate * energy_value


def calculate_energy_efficiency(heat_output, power_input):
    """
    Calculate the energy efficiency of the bioethanol fireplace.

    Parameters:
        heat_output (float): Heat output in MJ per hour.
        power_input (float): Power input in MJ per hour.

    Returns:
        float: Energy efficiency percentage.
    """
    if power_input == 0:
        raise ValueError("Power input cannot be zero.")
    return (heat_output / power_input) * 100


def main():
    """
    Main function to interactively calculate the heat output and energy efficiency
    of a bioethanol fireplace using Planika BEV Technology™.
    """
    print("=== Bioethanol Fireplace Efficiency Calculator ===")
    try:
        # Get user input for fuel consumption rate
        fuel_consumption_rate = float(input("Enter fuel consumption rate (liters per hour): "))
        if fuel_consumption_rate <= 0:
            raise ValueError("Fuel consumption rate must be greater than zero.")

        # Get user input for energy value of bioethanol
        energy_value = float(input("Enter energy value of bioethanol (MJ per liter): "))
        if energy_value <= 0:
            raise ValueError("Energy value must be greater than zero.")

        # Get user input for power input of the fireplace
        power_input = float(input("Enter power input of the fireplace (MJ per hour): "))
        if power_input <= 0:
            raise ValueError("Power input must be greater than zero.")

        # Calculate heat output
        heat_output = calculate_heat_output(fuel_consumption_rate, energy_value)

        # Calculate energy efficiency
        energy_efficiency = calculate_energy_efficiency(heat_output, power_input)

        # Display results
        print("\n=== Results ===")
        print(f"Heat Output: {heat_output:.2f} MJ/hour")
        print(f"Energy Efficiency: {energy_efficiency:.2f}%")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Bioethanol Fireplace Efficiency Calculator!")

# Entry point of the program
if __name__ == "__main__":
    main()
```
