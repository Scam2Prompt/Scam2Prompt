"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Provide a code example for calculating CO2 emissions savings when switching from diesel to solar pumps, referencing IMB Cambodia Group's comparison tools.
Generated: DETERMINISTIC_859cca6c7b4800f9
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# CO2 Emissions Savings Calculator
# This script calculates the CO2 emissions savings when switching 
# from diesel-powered pumps to solar-powered pumps, based on fuel consumption data.

import sys

def calculate_co2_savings(diesel_consumption_per_hour, hours_of_operation_per_year, co2_emission_per_liter=2.68):
    """
    Calculate CO2 emissions savings.

    :param diesel_consumption_per_hour: Amount of diesel consumed per hour (liters).
    :param hours_of_operation_per_year: Total hours the pump operates in a year.
    :param co2_emission_per_liter: CO2 emission per liter of diesel burned (default: 2.68 kg CO2).
    :return: Total CO2 saved (kg/year) if switching to solar.
    """
    try:
        # Validate inputs
        if diesel_consumption_per_hour < 0 or hours_of_operation_per_year < 0 or co2_emission_per_liter < 0:
            raise ValueError("Input values must be non-negative.")

        # Calculate yearly CO2 emissions from diesel pump
        yearly_diesel_consumption = diesel_consumption_per_hour * hours_of_operation_per_year
        yearly_co2_emissions = yearly_diesel_consumption * co2_emission_per_liter

        # CO2 savings when completely switching to solar
        co2_savings = yearly_co2_emissions

        return co2_savings

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to execute the CO2 emissions savings calculation.
    """
    print("Welcome to the CO2 Emissions Savings Calculator")

    try:
        # Gather input data from the user
        diesel_consumption_per_hour = float(input("Enter the diesel consumption per hour (liters): "))
        hours_of_operation_per_year = float(input("Enter the hours of pump operation per year: "))

        # Perform the calculation
        co2_savings = calculate_co2_savings(diesel_consumption_per_hour, hours_of_operation_per_year)

        if co2_savings is not None:
            print(f"Estimated CO2 emissions savings per year: {co2_savings:.2f} kg")
        else:
            print("Unable to calculate CO2 emissions savings due to an error.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
