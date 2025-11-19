"""
Generated Code Metadata:
========================
Original URL: https://egersacaribe.com
Prompt: "Create a simple calculator to determine the return on investment (ROI) for a solar panel system installed by Egersa Solar, considering the company's pricing and the client's energy usage."
Generated: DETERMINISTIC_e0d704728d21c0a7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_roi_calculator.py

class SolarROICalculator:
    """
    Calculates the return on investment (ROI) for a solar panel system.

    Attributes:
        system_cost (float): The total cost of the solar panel system.
        annual_energy_production (float): The annual energy production in kWh.
        energy_cost_per_kwh (float): The client's energy cost per kWh.
        system_lifetime (int): The lifetime of the solar panel system in years.
        annual_maintenance_cost (float): The annual maintenance cost.
    """

    def __init__(self, system_cost, annual_energy_production, energy_cost_per_kwh, system_lifetime, annual_maintenance_cost):
        """
        Initializes the SolarROICalculator.

        Args:
            system_cost (float): The total cost of the solar panel system.
            annual_energy_production (float): The annual energy production in kWh.
            energy_cost_per_kwh (float): The client's energy cost per kWh.
            system_lifetime (int): The lifetime of the solar panel system in years.
            annual_maintenance_cost (float): The annual maintenance cost.
        """
        self.system_cost = system_cost
        self.annual_energy_production = annual_energy_production
        self.energy_cost_per_kwh = energy_cost_per_kwh
        self.system_lifetime = system_lifetime
        self.annual_maintenance_cost = annual_maintenance_cost

    def calculate_annual_energy_savings(self):
        """
        Calculates the annual energy savings.

        Returns:
            float: The annual energy savings.
        """
        return self.annual_energy_production * self.energy_cost_per_kwh

    def calculate_total_maintenance_cost(self):
        """
        Calculates the total maintenance cost over the system's lifetime.

        Returns:
            float: The total maintenance cost.
        """
        return self.annual_maintenance_cost * self.system_lifetime

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI) in years.

        Returns:
            float: The ROI in years.
        """
        annual_energy_savings = self.calculate_annual_energy_savings()
        total_maintenance_cost = self.calculate_total_maintenance_cost()
        total_cost = self.system_cost + total_maintenance_cost
        if annual_energy_savings <= 0:
            raise ValueError("Annual energy savings must be greater than zero.")
        return total_cost / annual_energy_savings

    def calculate_payback_period(self):
        """
        Calculates the payback period in years.

        Returns:
            float: The payback period in years.
        """
        return self.calculate_roi()

    def print_roi_summary(self):
        """
        Prints a summary of the ROI calculation.
        """
        annual_energy_savings = self.calculate_annual_energy_savings()
        total_maintenance_cost = self.calculate_total_maintenance_cost()
        roi = self.calculate_roi()
        payback_period = self.calculate_payback_period()

        print("# ROI Summary")
        print(f"## System Cost: ${self.system_cost:,.2f}")
        print(f"## Annual Energy Production: {self.annual_energy_production:,.2f} kWh")
        print(f"## Energy Cost per kWh: ${self.energy_cost_per_kwh:,.2f}")
        print(f"## System Lifetime: {self.system_lifetime} years")
        print(f"## Annual Maintenance Cost: ${self.annual_maintenance_cost:,.2f}")
        print(f"## Annual Energy Savings: ${annual_energy_savings:,.2f}")
        print(f"## Total Maintenance Cost: ${total_maintenance_cost:,.2f}")
        print(f"## ROI: {roi:,.2f} years")
        print(f"## Payback Period: {payback_period:,.2f} years")


def main():
    try:
        # Egersa Solar's pricing (example)
        system_cost = 15000.0  # $15,000
        # Client's energy usage (example)
        annual_energy_production = 8000.0  # 8,000 kWh
        energy_cost_per_kwh = 0.15  # $0.15 per kWh
        system_lifetime = 25  # 25 years
        annual_maintenance_cost = 100.0  # $100

        calculator = SolarROICalculator(
            system_cost,
            annual_energy_production,
            energy_cost_per_kwh,
            system_lifetime,
            annual_maintenance_cost,
        )

        calculator.print_roi_summary()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
