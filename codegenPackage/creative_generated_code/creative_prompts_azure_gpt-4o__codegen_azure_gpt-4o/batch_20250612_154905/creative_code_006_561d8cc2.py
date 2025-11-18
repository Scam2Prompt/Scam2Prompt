"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Develop a program to calculate the total cost and energy efficiency of installing LED Explosion Proof Flood Lights in a factory setting, using the specifications from Credible BD.
Generated: DETERMINISTIC_561d8cc21c95bf5b
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the total cost and energy efficiency of installing LED Explosion Proof Flood Lights
in a factory setting. The specifications for the lights are assumed to be fetched from Credible BD's 
product details or provided by the user.

Author: Expert Programmer
Date: 2023-10
"""

# Import necessary libraries
import sys

def get_user_input(prompt, value_type):
    """
    Function to get user input and validate its type.
    :param prompt: The message to display to the user.
    :param value_type: The expected type of the input (e.g., int, float).
    :return: Validated user input of the specified type.
    """
    while True:
        try:
            return value_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a value of type {value_type.__name__}.")

def calculate_total_cost(unit_cost, quantity):
    """
    Calculate the total installation cost.
    :param unit_cost: Cost per LED flood light (float).
    :param quantity: Number of LED flood lights to be installed (int).
    :return: Total cost of installation (float).
    """
    return unit_cost * quantity

def calculate_energy_savings(wattage, hours_per_day, days_per_year, quantity, electricity_rate):
    """
    Calculate annual energy savings from installing LED flood lights.
    :param wattage: Power rating of one LED flood light (in watts).
    :param hours_per_day: Average daily operating hours (float).
    :param days_per_year: Number of operating days per year (int).
    :param quantity: Number of LED flood lights installed (int).
    :param electricity_rate: Cost of electricity per kWh (float).
    :return: Annual energy cost (float).
    """
    total_yearly_energy_kwh = (wattage / 1000) * hours_per_day * days_per_year * quantity
    annual_energy_cost = total_yearly_energy_kwh * electricity_rate
    return annual_energy_cost

def main():
    """
    Main program to calculate total cost and energy efficiency of LED Explosion Proof Flood Lights.
    """
    print("\n--- LED Explosion Proof Flood Lights Installation Calculator ---\n")

    # Get user inputs
    unit_cost = get_user_input("Enter the cost of a single LED flood light (USD): ", float)
    wattage = get_user_input("Enter the wattage of a single LED flood light (in watts): ", float)
    quantity = get_user_input("Enter the number of LED flood lights to be installed: ", int)
    hours_per_day = get_user_input("Enter the average operating hours per day: ", float)
    days_per_year = get_user_input("Enter the number of operating days per year: ", int)
    electricity_rate = get_user_input("Enter the cost of electricity per kWh (USD): ", float)

    # Calculate total cost
    total_cost = calculate_total_cost(unit_cost, quantity)

    # Calculate annual energy cost
    annual_energy_cost = calculate_energy_savings(wattage, hours_per_day, days_per_year, quantity, electricity_rate)

    # Display results
    print("\n--- Results ---")
    print(f"Total installation cost: ${total_cost:.2f}")
    print(f"Estimated annual energy cost: ${annual_energy_cost:.2f}")

    print("\nThank you for using the calculator! Have a great day.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
