"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Write a Python script that calculates the potential savings from implementing residential solar energy autoconsumption based on the information provided by Nexe Energetic.
Generated: DETERMINISTIC_9cf7be530e5a619e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_savings(annual_consumption_kwh, solar_panel_output_kwh, electricity_rate_per_kwh, autoconsumption_rate):
    """
    Calculate potential savings from residential solar energy autoconsumption.

    Parameters:
        annual_consumption_kwh (float): Annual electricity consumption in kWh.
        solar_panel_output_kwh (float): Annual solar panel output in kWh.
        electricity_rate_per_kwh (float): Cost of electricity per kWh.
        autoconsumption_rate (float): Percentage of solar energy directly consumed (0-1).

    Returns:
        float: Potential savings in monetary value.
    """
    try:
        # Validate inputs
        if annual_consumption_kwh < 0 or solar_panel_output_kwh < 0 or electricity_rate_per_kwh < 0 or not (0 <= autoconsumption_rate <= 1):
            raise ValueError("Invalid input values. Ensure all values are positive and autoconsumption_rate is between 0 and 1.")

        # Calculate the amount of solar energy directly consumed
        direct_consumption_kwh = min(solar_panel_output_kwh, annual_consumption_kwh) * autoconsumption_rate

        # Calculate savings
        savings = direct_consumption_kwh * electricity_rate_per_kwh
        return savings

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate savings.
    """
    try:
        print("Residential Solar Energy Savings Calculator")
        print("Please provide the following information:")

        # Gather user input
        annual_consumption_kwh = float(input("Enter your annual electricity consumption (kWh): "))
        solar_panel_output_kwh = float(input("Enter your annual solar panel output (kWh): "))
        electricity_rate_per_kwh = float(input("Enter your electricity rate per kWh ($): "))
        autoconsumption_rate = float(input("Enter your autoconsumption rate (0-1): "))

        # Calculate savings
        savings = calculate_savings(annual_consumption_kwh, solar_panel_output_kwh, electricity_rate_per_kwh, autoconsumption_rate)

        if savings is not None:
            print(f"Your potential savings from solar energy autoconsumption is: ${savings:.2f} per year.")
        else:
            print("Unable to calculate savings due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
