"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://universalsolar1.com
Prompt: Develop a function that calculates the potential profitability of solar projects using Universal Solar's comprehensive solutions.
Generated: DETERMINISTIC_55840937530e48be
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarProject:
    """
    A class to represent a solar project and calculate its potential profitability.
    """

    def __init__(self, initial_investment, annual_energy_output, energy_cost_per_kwh, project_lifetime, maintenance_cost_per_year):
        """
        Initializes a SolarProject instance.

        :param initial_investment: The initial investment cost of the solar project.
        :param annual_energy_output: The expected annual energy output in kWh.
        :param energy_cost_per_kwh: The current cost of energy per kWh.
        :param project_lifetime: The expected lifetime of the project in years.
        :param maintenance_cost_per_year: The annual maintenance cost of the project.
        """
        self.initial_investment = initial_investment
        self.annual_energy_output = annual_energy_output
        self.energy_cost_per_kwh = energy_cost_per_kwh
        self.project_lifetime = project_lifetime
        self.maintenance_cost_per_year = maintenance_cost_per_year

    def calculate_profitability(self):
        """
        Calculate the potential profitability of the solar project.

        :return: A dictionary containing total revenue, total costs, and net profit.
        """
        try:
            # Calculate total revenue over the project's lifetime
            total_revenue = self.annual_energy_output * self.energy_cost_per_kwh * self.project_lifetime
            
            # Calculate total costs over the project's lifetime
            total_maintenance_cost = self.maintenance_cost_per_year * self.project_lifetime
            total_costs = self.initial_investment + total_maintenance_cost
            
            # Calculate net profit
            net_profit = total_revenue - total_costs

            return {
                "total_revenue": total_revenue,
                "total_costs": total_costs,
                "net_profit": net_profit
            }
        except Exception as e:
            # Handling any unexpected errors and providing feedback
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Create an instance of SolarProject with example values
    project = SolarProject(
        initial_investment=50000,  # Initial investment of $50,000
        annual_energy_output=12000,  # Output of 12,000 kWh per year
        energy_cost_per_kwh=0.12,  # Energy cost of $0.12 per kWh
        project_lifetime=25,  # Project lifetime of 25 years
        maintenance_cost_per_year=1000  # Annual maintenance cost of $1,000
    )

    # Calculate profitability and print results
    profitability = project.calculate_profitability()
    print(profitability)
```
