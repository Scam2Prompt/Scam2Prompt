"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Write a Python script to simulate the energy efficiency benefits of UPVC windows and doors, referencing the features described on the Dexodoor website.
Generated: DETERMINISTIC_541c29339af63ca5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class UPVCWindowsAndDoors:
    """
    Class to model and simulate energy efficiency benefits of UPVC windows and doors.
    """
    
    def __init__(self, area, u_value, external_temp, internal_temp, heating_cost_per_kwh):
        """
        Initializes the UPVC windows and doors simulation with relevant parameters.

        :param area: Total surface area of the windows/doors in square meters.
        :param u_value: Thermal transmittance of UPVC windows/doors (lower is better).
        :param external_temp: Average external temperature in Celsius.
        :param internal_temp: Desired indoor temperature in Celsius.
        :param heating_cost_per_kwh: Cost of heating per kilowatt-hour in currency units.
        """
        self.area = area
        self.u_value = u_value
        self.external_temp = external_temp
        self.internal_temp = internal_temp
        self.heating_cost_per_kwh = heating_cost_per_kwh

    def calculate_heat_loss(self):
        """
        Calculates heat loss through UPVC windows/doors based on U-value and temperature difference.

        :return: Heat loss in kilowatt-hours (kWh).
        """
        temperature_difference = abs(self.internal_temp - self.external_temp)
        # Heat loss formula: Q = U * A * ΔT
        heat_loss_watts = self.u_value * self.area * temperature_difference
        # Convert watts to kilowatt-hours assuming 1 hour duration
        heat_loss_kwh = heat_loss_watts / 1000
        return heat_loss_kwh

    def calculate_heating_cost(self):
        """
        Calculates the heating cost due to the heat loss.

        :return: Heating cost in currency units.
        """
        heat_loss_kwh = self.calculate_heat_loss()
        return heat_loss_kwh * self.heating_cost_per_kwh

    def simulate_efficiency(self):
        """
        Simulates the energy efficiency benefits of UPVC windows and doors.

        :return: A dictionary containing heat loss and heating cost.
        """
        heat_loss_kwh = self.calculate_heat_loss()
        heating_cost = self.calculate_heating_cost()
        return {
            "Heat Loss (kWh)": heat_loss_kwh,
            "Heating Cost (currency)": heating_cost
        }


# Main entry point of the script
def main():
    """
    Main function to simulate the energy efficiency of UPVC windows and doors.
    """
    try:
        # Example feature parameters (can be customized based on Dexodoor website data)
        area = float(input("Enter total surface area of windows/doors (in m²): "))
        u_value = float(input("Enter the U-value of UPVC windows/doors: "))
        external_temp = float(input("Enter the average external temperature (in °C): "))
        internal_temp = float(input("Enter the desired indoor temperature (in °C): "))
        heating_cost_per_kwh = float(input("Enter the heating cost per kilowatt-hour (in currency units): "))

        # Initialize simulation object
        upvc_simulation = UPVCWindowsAndDoors(area, u_value, external_temp, internal_temp, heating_cost_per_kwh)
        
        # Simulate efficiency
        results = upvc_simulation.simulate_efficiency()
        
        # Output results
        print("\n### Energy Efficiency Simulation Results ###")
        print(f"Heat Loss: {results['Heat Loss (kWh)']} kWh")
        print(f"Heating Cost: {results['Heating Cost (currency)']} currency units")

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: Invalid input. Please enter numeric values. Details: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Run the script if executed directly
if __name__ == "__main__":
    main()
```
