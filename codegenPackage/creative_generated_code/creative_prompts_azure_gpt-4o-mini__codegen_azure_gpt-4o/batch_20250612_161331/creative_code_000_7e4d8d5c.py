"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Generate a Python script to calculate the energy savings when switching from traditional HID lights to LED flood lights from Credible BD, considering their specifications.
Generated: DETERMINISTIC_7e4d8d5cbecfa400
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate energy savings when switching from HID lights to LED flood lights.
HID: High Intensity Discharge lights
LED: Light Emitting Diode flood lights
"""

# Import necessary libraries
import sys

def calculate_energy_savings(hid_wattage, led_wattage, hours_per_day, days_per_year, num_lights):
    """
    Calculate energy savings when switching from HID lights to LED lights.
    
    Args:
        hid_wattage (float): Wattage of the HID lights.
        led_wattage (float): Wattage of the LED lights.
        hours_per_day (float): Average hours the lights are used per day.
        days_per_year (int): Number of days the lights are used per year.
        num_lights (int): Number of lights being replaced.
    
    Returns:
        dict: A dictionary containing energy consumption for HID and LED,
              energy savings in kWh, and percentage reduction.
    """
    try:
        # Calculate energy consumption for HID lights (kWh/year)
        hid_consumption = hid_wattage * hours_per_day * days_per_year * num_lights / 1000  # Convert watts to kilowatts
        
        # Calculate energy consumption for LED lights (kWh/year)
        led_consumption = led_wattage * hours_per_day * days_per_year * num_lights / 1000  # Convert watts to kilowatts
        
        # Calculate energy savings
        energy_savings_kwh = hid_consumption - led_consumption
        percentage_reduction = (energy_savings_kwh / hid_consumption) * 100 if hid_consumption > 0 else 0
        
        # Return the computed values
        return {
            "HID Energy Consumption (kWh/year)": hid_consumption,
            "LED Energy Consumption (kWh/year)": led_consumption,
            "Energy Savings (kWh/year)": energy_savings_kwh,
            "Percentage Reduction (%)": percentage_reduction
        }
    except Exception as error:
        print(f"An error occurred during calculation: {error}")
        sys.exit(1)


def main():
    """
    Main function to get user input and display energy savings information.
    """
    print("Energy Savings Calculator: HID to LED")

    try:
        # Get user input
        hid_wattage = float(input("Enter HID wattage (in watts): "))
        led_wattage = float(input("Enter LED wattage (in watts): "))
        hours_per_day = float(input("Enter hours of operation per day: "))
        days_per_year = int(input("Enter number of operational days per year: "))
        num_lights = int(input("Enter number of lights being replaced: "))
        
        # Validate input
        if any(value <= 0 for value in [hid_wattage, led_wattage, hours_per_day, days_per_year, num_lights]):
            print("Error: All input values must be greater than zero.")
            sys.exit(1)

        # Perform the calculation
        savings = calculate_energy_savings(hid_wattage, led_wattage, hours_per_day, days_per_year, num_lights)
        
        # Display results
        print("\nEnergy Savings Summary:")
        for key, value in savings.items():
            print(f"{key}: {value:.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```
