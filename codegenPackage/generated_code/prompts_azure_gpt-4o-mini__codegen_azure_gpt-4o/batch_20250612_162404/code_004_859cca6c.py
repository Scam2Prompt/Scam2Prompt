"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Provide a code example for calculating CO2 emissions savings when switching from diesel to solar pumps, referencing IMB Cambodia Group's comparison tools.
Generated: DETERMINISTIC_859cca6c7b4800f9
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sys

def calculate_co2_savings(diesel_usage_liters, co2_emission_per_liter=2.68):
    """
    Calculate CO2 emissions savings when switching from diesel to solar pumps.

    Parameters:
        diesel_usage_liters (float): The amount of diesel used in liters.
        co2_emission_per_liter (float): CO2 emissions per liter of diesel (default is 2.68 kg CO2/liter).

    Returns:
        float: The total CO2 emissions saved in kilograms.
    """
    try:
        # Validate input
        if diesel_usage_liters < 0:
            raise ValueError("Diesel usage cannot be negative.")

        # Calculate CO2 emissions savings
        co2_savings = diesel_usage_liters * co2_emission_per_liter
        return co2_savings

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to demonstrate CO2 savings calculation.
    """
    print("Welcome to the CO2 Emissions Savings Calculator!")
    try:
        # Get user input for diesel usage
        diesel_usage = float(input("Enter the amount of diesel used in liters: "))

        # Calculate savings
        savings = calculate_co2_savings(diesel_usage)

        if savings is not None:
            print(f"By switching to solar pumps, you save approximately {savings:.2f} kg of CO2 emissions.")
        else:
            print("Could not calculate CO2 savings due to an error.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for diesel usage.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
