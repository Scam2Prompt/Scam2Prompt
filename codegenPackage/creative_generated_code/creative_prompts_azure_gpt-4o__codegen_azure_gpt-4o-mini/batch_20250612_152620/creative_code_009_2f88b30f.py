"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Write a script to calculate the cost savings from switching to solar energy, incorporating Big Sky Energy's "custom system design" and "battery storage options."
Generated: DETERMINISTIC_2f88b30ff5f8ef8d
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SolarEnergySavingsCalculator:
    def __init__(self, current_energy_cost, solar_system_cost, battery_storage_cost, annual_energy_usage):
        """
        Initializes the calculator with the necessary parameters.

        :param current_energy_cost: Current cost of energy per kWh
        :param solar_system_cost: Total cost of the solar energy system
        :param battery_storage_cost: Total cost of battery storage options
        :param annual_energy_usage: Annual energy usage in kWh
        """
        self.current_energy_cost = current_energy_cost
        self.solar_system_cost = solar_system_cost
        self.battery_storage_cost = battery_storage_cost
        self.annual_energy_usage = annual_energy_usage

    def calculate_annual_savings(self):
        """
        Calculates the annual savings from switching to solar energy.

        :return: Annual savings in monetary units
        """
        try:
            # Calculate annual cost of current energy usage
            annual_current_cost = self.current_energy_cost * self.annual_energy_usage

            # Calculate annual cost of solar energy (assuming 100% usage)
            annual_solar_cost = 0  # Assuming zero cost for solar energy after installation

            # Annual savings calculation
            annual_savings = annual_current_cost - annual_solar_cost
            return annual_savings
        except Exception as e:
            print(f"Error calculating annual savings: {e}", file=sys.stderr)
            return None

    def calculate_break_even_time(self):
        """
        Calculates the break-even time in years for the solar system investment.

        :return: Break-even time in years
        """
        try:
            total_investment = self.solar_system_cost + self.battery_storage_cost
            annual_savings = self.calculate_annual_savings()
            
            if annual_savings is None or annual_savings <= 0:
                print("Annual savings must be greater than zero to calculate break-even time.", file=sys.stderr)
                return None

            # Calculate break-even time
            break_even_time = total_investment / annual_savings
            return break_even_time
        except Exception as e:
            print(f"Error calculating break-even time: {e}", file=sys.stderr)
            return None

    def display_results(self):
        """
        Displays the results of the savings and break-even calculation.
        """
        annual_savings = self.calculate_annual_savings()
        break_even_time = self.calculate_break_even_time()

        if annual_savings is not None:
            print(f"Annual Savings: ${annual_savings:.2f}")

        if break_even_time is not None:
            print(f"Break-even Time: {break_even_time:.2f} years")


def main():
    # Example inputs (these could be replaced with user inputs or configuration)
    current_energy_cost = 0.12           # Cost per kWh
    solar_system_cost = 20000              # Total solar system cost
    battery_storage_cost = 5000            # Total battery storage cost
    annual_energy_usage = 10000            # Annual energy usage in kWh

    # Create an instance of the calculator
    calculator = SolarEnergySavingsCalculator(current_energy_cost, solar_system_cost, battery_storage_cost, annual_energy_usage)

    # Display the results
    calculator.display_results()


if __name__ == "__main__":
    main()
```
