"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gendis.energia.misiones.gob.ar
Prompt: Create a program to estimate the cost savings of a solar photovoltaic installation based on energy tariffs in Misiones, Argentina.
Generated: DETERMINISTIC_918db16105d2eea8
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_float_input(prompt):
    """
    Safely get float input from the user. Ensures valid input.
    :param prompt: The message to display for the input.
    :return: A float value provided by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_monthly_savings(solar_energy_production, energy_tariff, percentage_self_consumption):
    """
    Calculate the estimated monthly savings based on solar energy production and consumption.
    :param solar_energy_production: Monthly solar energy production in kWh.
    :param energy_tariff: Energy tariff in ARS per kWh.
    :param percentage_self_consumption: Percentage of solar energy used directly (self-consumption).
    :return: Estimated monthly savings in ARS.
    """
    self_consumed_energy = solar_energy_production * (percentage_self_consumption / 100)
    savings = self_consumed_energy * energy_tariff
    return savings

def main():
    """
    Main function to estimate cost savings of a solar photovoltaic installation.
    """
    print("Welcome to Solar Cost Savings Estimator (Misiones, Argentina).")

    try:
        # Input: Monthly solar energy production in kWh
        solar_energy_production = get_float_input("Enter the estimated monthly solar energy production (kWh): ")
        
        # Input: Energy tariff in ARS per kWh
        energy_tariff = get_float_input("Enter the current energy tariff (ARS/kWh): ")
        
        # Input: Percentage of solar energy consumed directly by the user
        percentage_self_consumption = get_float_input(
            "What percentage of the solar energy will be used directly (self-consumption)? (e.g., 30 for 30%): "
        )

        # Validate inputs
        if solar_energy_production < 0 or energy_tariff < 0 or not (0 <= percentage_self_consumption <= 100):
            print("Error: Inputs must be non-negative, and percentage self-consumption must be between 0 and 100.")
            sys.exit(1)

        # Calculate savings
        monthly_savings = calculate_monthly_savings(
            solar_energy_production, energy_tariff, percentage_self_consumption
        )

        # Output results
        print(f"\nEstimated Monthly Cost Savings: ARS {monthly_savings:.2f}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the program
    main()
```
