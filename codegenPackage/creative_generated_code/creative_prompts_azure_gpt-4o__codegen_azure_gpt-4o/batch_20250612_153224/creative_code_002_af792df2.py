"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Generate a Python script for calculating energy savings achieved through thermal insulation, using materials like polyurethane foam, as highlighted on the "شمس المملكة" website.
Generated: DETERMINISTIC_af792df269d74d6e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class ThermalInsulationCalculator:
    """
    A class to calculate energy savings achieved through thermal insulation using materials like polyurethane foam.
    """

    def __init__(self, area, temperature_difference, insulation_material_r_value):
        """
        Initialize the calculator with necessary parameters.

        :param area: The area of the insulated surface (in square meters).
        :param temperature_difference: The temperature difference across the insulation material (in degrees Celsius).
        :param insulation_material_r_value: The R-value (thermal resistance) of the insulation material (in m²·°C/W).
        """
        self.area = area
        self.temperature_difference = temperature_difference
        self.insulation_material_r_value = insulation_material_r_value

    def calculate_energy_savings(self, hours, energy_cost_per_kwh):
        """
        Calculate the energy savings achieved through thermal insulation.

        :param hours: The number of hours the insulation is in use.
        :param energy_cost_per_kwh: The cost of energy per kilowatt-hour (in local currency).
        :return: Energy savings in kWh and monetary savings in local currency.
        """
        try:
            # Heat loss prevented (in watts)
            heat_loss_prevented_w = self.area * self.temperature_difference / self.insulation_material_r_value

            # Convert heat loss prevented to kilowatts
            heat_loss_prevented_kw = heat_loss_prevented_w / 1000

            # Total energy savings (in kWh)
            energy_savings_kwh = heat_loss_prevented_kw * hours

            # Monetary savings
            monetary_savings = energy_savings_kwh * energy_cost_per_kwh

            return energy_savings_kwh, monetary_savings
        except ZeroDivisionError:
            raise ValueError("Insulation material R-value must be greater than zero to calculate savings.")
        except Exception as e:
            raise ValueError(f"An error occurred while calculating energy savings: {e}")


def main():
    """
    Entry point for the script.
    Collects user input and calculates energy and monetary savings.
    """
    print("Thermal Insulation Energy Savings Calculator")
    print("------------------------------------------------")

    try:
        # User inputs
        area = float(input("Enter the insulated surface area (in square meters): "))
        temperature_difference = float(input("Enter the temperature difference across the insulation material (in °C): "))
        insulation_material_r_value = float(input("Enter the R-value of the insulation material (in m²·°C/W): "))
        hours = float(input("Enter the number of hours insulation is in use: "))
        energy_cost_per_kwh = float(input("Enter the cost of energy per kWh (in your local currency): "))

        # Initialize the calculator
        calculator = ThermalInsulationCalculator(
            area, temperature_difference, insulation_material_r_value
        )

        # Calculate energy savings
        energy_savings_kwh, monetary_savings = calculator.calculate_energy_savings(
            hours, energy_cost_per_kwh
        )

        # Display the results
        print("\nResults:")
        print(f"Energy savings: {energy_savings_kwh:.2f} kWh")
        print(f"Monetary savings: {monetary_savings:.2f} (local currency)")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
