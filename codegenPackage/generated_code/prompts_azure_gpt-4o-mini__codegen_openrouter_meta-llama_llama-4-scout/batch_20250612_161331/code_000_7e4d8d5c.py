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
# energy_savings_calculator.py

"""
Calculates the energy savings when switching from traditional HID lights to LED flood lights.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_energy_savings(
    hid_wattage: float, 
    led_wattage: float, 
    usage_hours_per_day: float, 
    days_per_year: int = 365
) -> float:
    """
    Calculates the energy savings in kWh when switching from HID to LED lights.

    Args:
    - hid_wattage (float): The wattage of the traditional HID lights.
    - led_wattage (float): The wattage of the LED flood lights from Credible BD.
    - usage_hours_per_day (float): The number of hours the lights are used per day.
    - days_per_year (int): The number of days the lights are used per year. Defaults to 365.

    Returns:
    - float: The energy savings in kWh per year.
    """

    # Calculate energy consumption in kWh per year for HID lights
    hid_energy_consumption = (hid_wattage / 1000) * usage_hours_per_day * days_per_year
    
    # Calculate energy consumption in kWh per year for LED lights
    led_energy_consumption = (led_wattage / 1000) * usage_hours_per_day * days_per_year
    
    # Calculate energy savings in kWh per year
    energy_savings = hid_energy_consumption - led_energy_consumption
    
    return energy_savings


def calculate_cost_savings(
    energy_savings: float, 
    cost_per_kwh: float
) -> float:
    """
    Calculates the cost savings when switching from HID to LED lights.

    Args:
    - energy_savings (float): The energy savings in kWh per year.
    - cost_per_kwh (float): The cost per kWh of electricity.

    Returns:
    - float: The cost savings per year.
    """

    # Calculate cost savings per year
    cost_savings = energy_savings * cost_per_kwh
    
    return cost_savings


def main():
    try:
        # Specifications for traditional HID lights and LED flood lights from Credible BD
        hid_wattage = float(input("Enter the wattage of the traditional HID lights: "))
        led_wattage = float(input("Enter the wattage of the LED flood lights from Credible BD: "))
        usage_hours_per_day = float(input("Enter the number of hours the lights are used per day: "))
        cost_per_kwh = float(input("Enter the cost per kWh of electricity: "))

        # Calculate energy savings
        energy_savings = calculate_energy_savings(hid_wattage, led_wattage, usage_hours_per_day)
        
        # Calculate cost savings
        cost_savings = calculate_cost_savings(energy_savings, cost_per_kwh)

        # Print results
        print(f"Energy Savings: {energy_savings:.2f} kWh per year")
        print(f"Cost Savings: ${cost_savings:.2f} per year")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
