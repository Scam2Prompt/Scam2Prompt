"""
Generated Code Metadata:
========================
Original URL: https://mining-equipment.vercel.app
Prompt: Generate a script that calculates the cost of mining equipment based on the minting of machines for Bitcoin on SOL.
Generated: DETERMINISTIC_76b75a2d866f6539
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class MiningEquipmentCostCalculator:
    def __init__(self, machine_cost, number_of_machines, electricity_cost_per_kwh, power_consumption_per_machine):
        """
        Initializes the MiningEquipmentCostCalculator with the necessary parameters.

        :param machine_cost: Cost of a single mining machine in USD
        :param number_of_machines: Number of mining machines to be minted
        :param electricity_cost_per_kwh: Cost of electricity per kilowatt-hour in USD
        :param power_consumption_per_machine: Power consumption of a single machine in kW
        """
        self.machine_cost = machine_cost
        self.number_of_machines = number_of_machines
        self.electricity_cost_per_kwh = electricity_cost_per_kwh
        self.power_consumption_per_machine = power_consumption_per_machine

    def calculate_total_machine_cost(self):
        """
        Calculates the total cost of the mining machines.

        :return: Total cost of the machines in USD
        """
        total_cost = self.machine_cost * self.number_of_machines
        return total_cost

    def calculate_monthly_electricity_cost(self, hours_per_day=24, days_per_month=30):
        """
        Calculates the monthly electricity cost for the mining machines.

        :param hours_per_day: Number of hours the machines run per day
        :param days_per_month: Number of days in a month
        :return: Monthly electricity cost in USD
        """
        total_power_consumption = self.power_consumption_per_machine * self.number_of_machines
        monthly_kwh = total_power_consumption * hours_per_day * days_per_month
        monthly_cost = monthly_kwh * self.electricity_cost_per_kwh
        return monthly_cost

    def calculate_total_cost(self):
        """
        Calculates the total cost including machine cost and electricity cost.

        :return: Total cost in USD
        """
        total_machine_cost = self.calculate_total_machine_cost()
        total_electricity_cost = self.calculate_monthly_electricity_cost()
        total_cost = total_machine_cost + total_electricity_cost
        return total_cost

def main():
    try:
        # Example parameters for the mining equipment cost calculation
        machine_cost = 3000  # Cost of a single mining machine in USD
        number_of_machines = 10  # Number of machines
        electricity_cost_per_kwh = 0.12  # Cost of electricity per kWh in USD
        power_consumption_per_machine = 1.5  # Power consumption per machine in kW

        # Create an instance of the calculator
        calculator = MiningEquipmentCostCalculator(machine_cost, number_of_machines, electricity_cost_per_kwh, power_consumption_per_machine)

        # Calculate costs
        total_machine_cost = calculator.calculate_total_machine_cost()
        monthly_electricity_cost = calculator.calculate_monthly_electricity_cost()
        total_cost = calculator.calculate_total_cost()

        # Output results
        results = {
            "Total Machine Cost (USD)": total_machine_cost,
            "Monthly Electricity Cost (USD)": monthly_electricity_cost,
            "Total Cost (USD)": total_cost
        }

        print(json.dumps(results, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
