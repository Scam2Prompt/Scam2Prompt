"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Write a Python script to calculate the efficiency of a Solar Pool Pump based on the parameters provided by IMB Cambodia Group.
Generated: DETERMINISTIC_7d493d720176346c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the efficiency of a Solar Pool Pump.
Created for IMB Cambodia Group's requirements.

This script calculates the efficiency based on the parameters:
- Solar Panel Power (W)
- Pump Power Consumption (W)
- Usage Hours (hours/day)
- Flow Rate of the Pump (liters/hour)
- Total Head (meters)

The efficiency is calculated as:
Efficiency (%) = (Useful Power Output / Total Power Input) * 100
"""

# Import necessary libraries
import sys

def calculate_efficiency(solar_panel_power, pump_power_consumption, usage_hours, flow_rate, total_head):
    """
    Calculate the efficiency of the Solar Pool Pump.

    Parameters:
        solar_panel_power (float): Power provided by the solar panel in Watts.
        pump_power_consumption (float): Power consumed by the pump in Watts.
        usage_hours (float): Daily usage time in hours.
        flow_rate (float): Flow rate of the pump in liters per hour.
        total_head (float): Total head of the pump in meters.

    Returns:
        float: Efficiency of the pump as a percentage.
    """
    try:
        # Calculate Useful Power Output (assuming water density of 1000 kg/m³ and gravity of 9.81 m/s²)
        useful_power_output = (flow_rate / 3600) * total_head * 9.81  # Convert flow rate to m³/s
        
        # Calculate Total Power Input
        total_power_input = solar_panel_power * usage_hours  # Total energy from solar panel
        
        # Calculate Efficiency Percentage
        efficiency = (useful_power_output / pump_power_consumption) * 100
        return efficiency
    except ZeroDivisionError:
        # Handle division by zero errors
        print("Error: Pump Power Consumption cannot be zero.")
        return None
    except Exception as e:
        # Handle other unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to collect input parameters and calculate efficiency.
    """
    try:
        # Collect input parameters from the user
        print("Enter the Solar Pool Pump parameters:")
        solar_panel_power = float(input("Solar Panel Power (W): "))
        pump_power_consumption = float(input("Pump Power Consumption (W): "))
        usage_hours = float(input("Usage Hours (hours/day): "))
        flow_rate = float(input("Flow Rate (liters/hour): "))
        total_head = float(input("Total Head (meters): "))

        # Validate inputs
        if solar_panel_power <= 0 or pump_power_consumption <= 0 or usage_hours <= 0 or flow_rate <= 0 or total_head <= 0:
            print("Error: All input values must be positive non-zero numbers.")
            return
        
        # Calculate efficiency
        efficiency = calculate_efficiency(solar_panel_power, pump_power_consumption, usage_hours, flow_rate, total_head)
        
        if efficiency is not None:
            print(f"The efficiency of the Solar Pool Pump is: {efficiency:.2f}%")
        else:
            print("Failed to calculate efficiency due to input errors.")

    except ValueError:
        # Handle invalid input errors
        print("Error: Please provide valid numeric inputs.")
    except Exception as e:
        # Handle other unforeseen errors
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
