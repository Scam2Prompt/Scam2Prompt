"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Provide a code example to implement a feature that calculates cost savings for businesses using renting solutions compared to owning a fleet, as highlighted by Innova Renting.
Generated: DETERMINISTIC_e04e70650e9f6bab
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FleetCostCalculator:
    """
    A class to calculate cost savings for businesses using renting solutions
    compared to owning a fleet.
    """

    def __init__(self, ownership_costs, rental_costs, maintenance_costs, lifespan_years):
        """
        Initializes the FleetCostCalculator with the necessary cost parameters.

        :param ownership_costs: Total cost of owning the fleet (purchase price).
        :param rental_costs: Total cost of renting the fleet per year.
        :param maintenance_costs: Annual maintenance costs for owning the fleet.
        :param lifespan_years: Expected lifespan of the fleet in years.
        """
        self.ownership_costs = ownership_costs
        self.rental_costs = rental_costs
        self.maintenance_costs = maintenance_costs
        self.lifespan_years = lifespan_years

    def calculate_ownership_total(self):
        """
        Calculates the total cost of owning the fleet over its lifespan.

        :return: Total ownership cost.
        """
        total_ownership_cost = self.ownership_costs + (self.maintenance_costs * self.lifespan_years)
        return total_ownership_cost

    def calculate_rental_total(self):
        """
        Calculates the total cost of renting the fleet over the same period.

        :return: Total rental cost.
        """
        total_rental_cost = self.rental_costs * self.lifespan_years
        return total_rental_cost

    def calculate_savings(self):
        """
        Calculates the cost savings of renting compared to owning.

        :return: Savings amount if renting is cheaper, otherwise a message indicating no savings.
        """
        try:
            total_ownership = self.calculate_ownership_total()
            total_rental = self.calculate_rental_total()

            savings = total_ownership - total_rental

            if savings > 0:
                return f"Savings by renting: ${savings:.2f}"
            else:
                return "No savings by renting; owning is more cost-effective."
        except Exception as e:
            return f"An error occurred while calculating savings: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define cost parameters
    ownership_costs = 50000  # Total cost of owning the fleet
    rental_costs = 12000     # Annual rental cost
    maintenance_costs = 2000  # Annual maintenance cost
    lifespan_years = 5       # Expected lifespan in years

    # Create an instance of FleetCostCalculator
    calculator = FleetCostCalculator(ownership_costs, rental_costs, maintenance_costs, lifespan_years)

    # Calculate and print the savings
    print(calculator.calculate_savings())
```
