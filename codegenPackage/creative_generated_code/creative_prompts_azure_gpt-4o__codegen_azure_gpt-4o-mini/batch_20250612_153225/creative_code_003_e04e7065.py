"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Provide a code example to implement a feature that calculates cost savings for businesses using renting solutions compared to owning a fleet, as highlighted by Innova Renting.
Generated: DETERMINISTIC_e04e70650e9f6bab
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FleetCostCalculator:
    """
    A class to calculate the cost savings of renting solutions
    compared to owning a fleet for businesses.
    """

    def __init__(self, ownership_costs, rental_costs, maintenance_costs, duration_years):
        """
        Initializes the FleetCostCalculator with the necessary costs.
        
        :param ownership_costs: Total costs of owning the fleet (initial + operational).
        :param rental_costs: Total rental costs over the specified duration.
        :param maintenance_costs: Total maintenance costs for owned fleet over the duration.
        :param duration_years: Duration for comparison in years.
        """
        self.ownership_costs = ownership_costs
        self.rental_costs = rental_costs
        self.maintenance_costs = maintenance_costs
        self.duration_years = duration_years

    def calculate_total_ownership_cost(self):
        """
        Calculates the total cost of ownership for the given duration.
        
        :return: Total ownership cost.
        """
        return self.ownership_costs + self.maintenance_costs

    def calculate_total_rental_cost(self):
        """
        Calculates the total rental cost over the specified duration.
        
        :return: Total rental cost.
        """
        return self.rental_costs

    def calculate_savings(self):
        """
        Calculates the cost savings when opting for renting over ownership.
        
        :return: Savings amount.
        """
        total_ownership_cost = self.calculate_total_ownership_cost()
        total_rental_cost = self.calculate_total_rental_cost()

        # Calculate savings
        savings = total_ownership_cost - total_rental_cost
        return savings

    def get_savings_report(self):
        """
        Generates a report of the savings from renting vs owning.
        
        :return: A formatted savings report.
        """
        savings = self.calculate_savings()
        report = (
            f"Total Ownership Cost over {self.duration_years} years: ${self.calculate_total_ownership_cost():,.2f}\n"
            f"Total Rental Cost over {self.duration_years} years: ${self.calculate_total_rental_cost():,.2f}\n"
            f"Total Savings by Renting: ${savings:,.2f}"
        )
        return report


def main():
    try:
        # Example values to initialize the calculator
        ownership_costs = 50000  # Example: total cost of ownership
        rental_costs = 30000      # Example: total cost of renting
        maintenance_costs = 10000  # Example: maintenance costs for owned fleet
        duration_years = 3         # Duration for comparison in years

        # Create the FleetCostCalculator instance
        calculator = FleetCostCalculator(
            ownership_costs,
            rental_costs,
            maintenance_costs,
            duration_years
        )

        # Generate and print the savings report
        savings_report = calculator.get_savings_report()
        print(savings_report)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
