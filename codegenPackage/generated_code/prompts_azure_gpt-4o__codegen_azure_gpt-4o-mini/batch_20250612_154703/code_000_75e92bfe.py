"""
Generated Code Metadata:
========================
Original URL: https://realorigin.org
Prompt: Write Python code to calculate the cost-effectiveness of solar panels over a decade, incorporating energy savings and installation costs as described in "Why are solar panels becoming so Much more Popular over the Past Decade?" on Real and Origin.
Generated: DETERMINISTIC_75e92bfe59286c76
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SolarPanelCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of solar panels over a decade.
    """

    def __init__(self, installation_cost, annual_energy_savings, maintenance_costs=0):
        """
        Initializes the SolarPanelCostEffectiveness class.

        :param installation_cost: Total installation cost of solar panels (in dollars).
        :param annual_energy_savings: Annual savings from reduced energy bills (in dollars).
        :param maintenance_costs: Annual maintenance costs (in dollars), default is 0.
        """
        self.installation_cost = installation_cost
        self.annual_energy_savings = annual_energy_savings
        self.maintenance_costs = maintenance_costs
        self.years = 10  # Duration for cost-effectiveness analysis

    def calculate_total_savings(self):
        """
        Calculates the total savings over the specified number of years.

        :return: Total savings over the decade (in dollars).
        """
        total_savings = (self.annual_energy_savings - self.maintenance_costs) * self.years
        return total_savings

    def calculate_net_cost(self):
        """
        Calculates the net cost after savings over the specified number of years.

        :return: Net cost after savings (in dollars).
        """
        total_savings = self.calculate_total_savings()
        net_cost = self.installation_cost - total_savings
        return net_cost

    def calculate_cost_effectiveness(self):
        """
        Calculates the cost-effectiveness ratio.

        :return: Cost-effectiveness ratio (savings per dollar spent).
        """
        total_savings = self.calculate_total_savings()
        if self.installation_cost == 0:
            raise ValueError("Installation cost cannot be zero for cost-effectiveness calculation.")
        cost_effectiveness = total_savings / self.installation_cost
        return cost_effectiveness

    def display_results(self):
        """
        Displays the results of the cost-effectiveness analysis.
        """
        try:
            total_savings = self.calculate_total_savings()
            net_cost = self.calculate_net_cost()
            cost_effectiveness = self.calculate_cost_effectiveness()

            print(f"Total Savings over {self.years} years: ${total_savings:.2f}")
            print(f"Net Cost after {self.years} years: ${net_cost:.2f}")
            print(f"Cost-Effectiveness Ratio: {cost_effectiveness:.2f} (savings per dollar spent)")

        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Define installation cost, annual energy savings, and maintenance costs
    installation_cost = 15000  # Example installation cost in dollars
    annual_energy_savings = 1200  # Example annual savings in dollars
    maintenance_costs = 100  # Example annual maintenance costs in dollars

    # Create an instance of the SolarPanelCostEffectiveness class
    solar_panel_analysis = SolarPanelCostEffectiveness(installation_cost, annual_energy_savings, maintenance_costs)

    # Display the results of the analysis
    solar_panel_analysis.display_results()
```
