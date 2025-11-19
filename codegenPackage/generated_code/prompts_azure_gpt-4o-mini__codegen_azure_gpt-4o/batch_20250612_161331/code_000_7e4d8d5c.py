"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Generate a Python script to calculate the energy savings when switching from traditional HID lights to LED flood lights from Credible BD, considering their specifications.
Generated: DETERMINISTIC_7e4d8d5cbecfa400
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate energy savings when switching from traditional HID lights to LED flood lights.
This script assumes the user provides the wattage of HID lights, the wattage of LED flood lights, 
and the number of hours the lights are used per day.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_energy_savings(hid_wattage, led_wattage, hours_per_day, days_per_year=365):
    """
    Calculate energy savings when switching from HID lights to LED flood lights.

    Parameters:
        hid_wattage (float): Wattage of the HID lights.
        led_wattage (float): Wattage of the LED flood lights.
        hours_per_day (float): Number of hours the lights are used per day.
        days_per_year (int): Number of days the lights are used per year (default is 365).

    Returns:
        dict: A dictionary containing energy consumption of HID and LED lights, and savings.
    """
    try:
        # Calculate annual energy consumption for HID and LED lights (in kWh)
        hid_energy_consumption = (hid_wattage * hours_per_day * days_per_year) / 1000  # Convert watts to kWh
        led_energy_consumption = (led_wattage * hours_per_day * days_per_year) / 1000  # Convert watts to kWh

        # Calculate energy savings
        energy_savings = hid_energy_consumption - led_energy_consumption

        # Return results as a dictionary
        return {
            "HID Energy Consumption (kWh)": round(hid_energy_consumption, 2),
            "LED Energy Consumption (kWh)": round(led_energy_consumption, 2),
            "Energy Savings (kWh)": round(energy_savings, 2)
        }
    except Exception as e:
        print(f"Error occurred during calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate energy savings.
    """
    print("Energy Savings Calculator: HID Lights vs LED Flood Lights")
    try:
        # Get user input
        hid_wattage = float(input("Enter the wattage of HID lights (in watts): "))
        led_wattage = float(input("Enter the wattage of LED flood lights (in watts): "))
        hours_per_day = float(input("Enter the number of hours the lights are used per day: "))

        # Validate input
        if hid_wattage <= 0 or led_wattage <= 0 or hours_per_day <= 0:
            print("Error: All input values must be positive numbers.")
            sys.exit(1)

        # Calculate energy savings
        results = calculate_energy_savings(hid_wattage, led_wattage, hours_per_day)

        # Display results
        print("\nEnergy Savings Results:")
        for key, value in results.items():
            print(f"{key}: {value} kWh")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
