"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Generate a script to calculate the energy savings of a solar pool pump system using the "Solar Pool Pump Calculator" provided by IMB Cambodia Group.
Generated: DETERMINISTIC_cd9636deb7d1fbe7
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class SolarPoolPumpCalculator:
    def __init__(self, pump_power_watts, hours_of_operation, electricity_cost_per_kwh, solar_panel_efficiency):
        """
        Initialize the SolarPoolPumpCalculator with the necessary parameters.

        :param pump_power_watts: Power of the pool pump in watts
        :param hours_of_operation: Number of hours the pump operates per day
        :param electricity_cost_per_kwh: Cost of electricity per kilowatt-hour
        :param solar_panel_efficiency: Efficiency of the solar panels (0 to 1)
        """
        self.pump_power_watts = pump_power_watts
        self.hours_of_operation = hours_of_operation
        self.electricity_cost_per_kwh = electricity_cost_per_kwh
        self.solar_panel_efficiency = solar_panel_efficiency

    def calculate_energy_consumption(self):
        """
        Calculate the daily energy consumption of the pool pump in kWh.

        :return: Daily energy consumption in kWh
        """
        energy_consumed_kwh = (self.pump_power_watts / 1000) * self.hours_of_operation
        return energy_consumed_kwh

    def calculate_cost_savings(self):
        """
        Calculate the cost savings from using a solar pool pump system.

        :return: Daily cost savings in currency
        """
        energy_consumed_kwh = self.calculate_energy_consumption()
        cost_savings = energy_consumed_kwh * self.electricity_cost_per_kwh
        return cost_savings

    def calculate_solar_panel_output(self):
        """
        Calculate the daily output of the solar panels in kWh.

        :return: Daily solar panel output in kWh
        """
        # Assuming 5 hours of effective sunlight per day
        effective_sunlight_hours = 5
        solar_panel_output = effective_sunlight_hours * self.solar_panel_efficiency * (self.pump_power_watts / 1000)
        return solar_panel_output

    def calculate_net_savings(self):
        """
        Calculate the net savings after accounting for solar panel output.

        :return: Net daily savings in currency
        """
        cost_savings = self.calculate_cost_savings()
        solar_output = self.calculate_solar_panel_output()
        net_savings = cost_savings - (solar_output * self.electricity_cost_per_kwh)
        return net_savings

def main():
    try:
        # Example parameters (these can be modified as needed)
        pump_power_watts = 1500  # Power of the pool pump in watts
        hours_of_operation = 8    # Number of hours the pump operates per day
        electricity_cost_per_kwh = 0.15  # Cost of electricity per kWh
        solar_panel_efficiency = 0.8  # Efficiency of the solar panels (80%)

        # Create an instance of the calculator
        calculator = SolarPoolPumpCalculator(pump_power_watts, hours_of_operation, electricity_cost_per_kwh, solar_panel_efficiency)

        # Calculate and display results
        print(f"Daily Energy Consumption: {calculator.calculate_energy_consumption():.2f} kWh")
        print(f"Daily Cost Savings: ${calculator.calculate_cost_savings():.2f}")
        print(f"Daily Solar Panel Output: {calculator.calculate_solar_panel_output():.2f} kWh")
        print(f"Net Daily Savings: ${calculator.calculate_net_savings():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
