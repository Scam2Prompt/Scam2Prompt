"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Compare the costs of owning versus renting a DAS system for a hospital, considering factors such as installation, maintenance, and monthly fees.
Generated: DETERMINISTIC_16dacaf0916f2abb
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DASCostComparison:
    """
    A class to compare the costs of owning versus renting a Distributed Antenna System (DAS) for a hospital.
    """

    def __init__(self, installation_cost, maintenance_cost_per_year, monthly_rent, rental_duration_years):
        """
        Initializes the DASCostComparison with the necessary cost parameters.

        :param installation_cost: Total cost of installing the DAS system (in dollars).
        :param maintenance_cost_per_year: Annual maintenance cost for owning the DAS system (in dollars).
        :param monthly_rent: Monthly rental fee for the DAS system (in dollars).
        :param rental_duration_years: Duration for which the system is rented (in years).
        """
        self.installation_cost = installation_cost
        self.maintenance_cost_per_year = maintenance_cost_per_year
        self.monthly_rent = monthly_rent
        self.rental_duration_years = rental_duration_years

    def calculate_owning_cost(self):
        """
        Calculates the total cost of owning the DAS system over its lifetime.

        :return: Total cost of owning the DAS system (in dollars).
        """
        total_maintenance_cost = self.maintenance_cost_per_year * self.rental_duration_years
        total_owning_cost = self.installation_cost + total_maintenance_cost
        return total_owning_cost

    def calculate_renting_cost(self):
        """
        Calculates the total cost of renting the DAS system over the specified duration.

        :return: Total cost of renting the DAS system (in dollars).
        """
        total_renting_cost = self.monthly_rent * 12 * self.rental_duration_years
        return total_renting_cost

    def compare_costs(self):
        """
        Compares the costs of owning versus renting the DAS system and returns the result.

        :return: A string indicating which option is more cost-effective.
        """
        owning_cost = self.calculate_owning_cost()
        renting_cost = self.calculate_renting_cost()

        if owning_cost < renting_cost:
            return f"Owning the DAS system is more cost-effective. Total owning cost: ${owning_cost:.2f}, Total renting cost: ${renting_cost:.2f}."
        elif renting_cost < owning_cost:
            return f"Renting the DAS system is more cost-effective. Total owning cost: ${owning_cost:.2f}, Total renting cost: ${renting_cost:.2f}."
        else:
            return f"Both options cost the same. Total owning cost: ${owning_cost:.2f}, Total renting cost: ${renting_cost:.2f}."


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cost comparison with example values
        installation_cost = 50000  # Example installation cost in dollars
        maintenance_cost_per_year = 5000  # Example annual maintenance cost in dollars
        monthly_rent = 4000  # Example monthly rental fee in dollars
        rental_duration_years = 5  # Example rental duration in years

        das_comparison = DASCostComparison(installation_cost, maintenance_cost_per_year, monthly_rent, rental_duration_years)
        result = das_comparison.compare_costs()
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
