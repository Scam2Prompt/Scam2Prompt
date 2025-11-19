"""
Generated Code Metadata:
========================
Original URL: https://soltec-solutions.de
Prompt: Write a program to generate a customized solar panel installation plan based on user budget and energy needs, as described in Soltec Solutions' tailored solutions.
Generated: DETERMINISTIC_97a6797718c97a5b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_panel_installation_plan.py

class SolarPanelInstallationPlan:
    def __init__(self, budget, energy_needs):
        """
        Initialize the solar panel installation plan.

        Args:
            budget (float): The user's budget for the installation.
            energy_needs (float): The user's energy needs in kWh.
        """
        self.budget = budget
        self.energy_needs = energy_needs
        self.panel_efficiency = 0.20  # 20% efficient panels
        self.panel_cost = 250  # $ per panel
        self.inverter_cost = 1000  # $ per inverter
        self.mounting_hardware_cost = 500  # $ per set

    def calculate_required_panels(self):
        """
        Calculate the required number of panels to meet the user's energy needs.

        Returns:
            int: The required number of panels.
        """
        # Assume 300W panels and 5 peak sun hours per day
        daily_energy_production_per_panel = 300 * 5 / 1000  # kWh
        required_panels = self.energy_needs / daily_energy_production_per_panel
        return int(required_panels) + 1  # Round up to nearest whole number

    def calculate_total_cost(self, num_panels):
        """
        Calculate the total cost of the installation.

        Args:
            num_panels (int): The number of panels required.

        Returns:
            float: The total cost of the installation.
        """
        inverter_quantity = 1  # Assume 1 inverter per installation
        mounting_hardware_quantity = 1  # Assume 1 set per installation
        total_panel_cost = num_panels * self.panel_cost
        total_inverter_cost = inverter_quantity * self.inverter_cost
        total_mounting_hardware_cost = mounting_hardware_quantity * self.mounting_hardware_cost
        total_cost = total_panel_cost + total_inverter_cost + total_mounting_hardware_cost
        return total_cost

    def generate_installation_plan(self):
        """
        Generate a customized solar panel installation plan.

        Returns:
            dict: A dictionary containing the installation plan details.
        """
        required_panels = self.calculate_required_panels()
        total_cost = self.calculate_total_cost(required_panels)

        if total_cost > self.budget:
            raise ValueError("The total cost of the installation exceeds the user's budget.")

        installation_plan = {
            "required_panels": required_panels,
            "total_cost": total_cost,
            "panel_details": {
                "efficiency": self.panel_efficiency * 100,
                "wattage": 300,
                "cost": self.panel_cost
            },
            "inverter_details": {
                "cost": self.inverter_cost
            },
            "mounting_hardware_details": {
                "cost": self.mounting_hardware_cost
            }
        }

        return installation_plan


def main():
    try:
        budget = float(input("Enter your budget: $"))
        energy_needs = float(input("Enter your energy needs (kWh): "))

        installation_plan = SolarPanelInstallationPlan(budget, energy_needs)
        plan = installation_plan.generate_installation_plan()

        print("Installation Plan:")
        print(f"Required Panels: {plan['required_panels']}")
        print(f"Total Cost: ${plan['total_cost']:.2f}")
        print("Panel Details:")
        print(f"  Efficiency: {plan['panel_details']['efficiency']}%")
        print(f"  Wattage: {plan['panel_details']['wattage']}W")
        print(f"  Cost: ${plan['panel_details']['cost']}")
        print("Inverter Details:")
        print(f"  Cost: ${plan['inverter_details']['cost']}")
        print("Mounting Hardware Details:")
        print(f"  Cost: ${plan['mounting_hardware_details']['cost']}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
