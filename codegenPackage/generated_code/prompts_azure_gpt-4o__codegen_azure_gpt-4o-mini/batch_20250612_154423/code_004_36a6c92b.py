"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Create a program to calculate the cost comparison between owning and renting a cellular DAS system, using the pricing models described by CellAntenna Wireless.
Generated: DETERMINISTIC_36a6c92b4a17befe
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CellularDASCostComparison:
    """
    A class to compare the costs of owning versus renting a cellular Distributed Antenna System (DAS).
    """

    def __init__(self, purchase_price, installation_cost, monthly_maintenance_cost, rental_cost_per_month, years=5):
        """
        Initializes the cost comparison parameters.

        :param purchase_price: The initial purchase price of the DAS system.
        :param installation_cost: The cost of installation for the DAS system.
        :param monthly_maintenance_cost: The monthly maintenance cost for owning the DAS system.
        :param rental_cost_per_month: The monthly rental cost for the DAS system.
        :param years: The number of years to compare costs (default is 5 years).
        """
        self.purchase_price = purchase_price
        self.installation_cost = installation_cost
        self.monthly_maintenance_cost = monthly_maintenance_cost
        self.rental_cost_per_month = rental_cost_per_month
        self.years = years

    def calculate_owning_cost(self):
        """
        Calculates the total cost of owning the DAS system over the specified number of years.

        :return: Total cost of ownership.
        """
        total_owning_cost = (self.purchase_price + self.installation_cost +
                             (self.monthly_maintenance_cost * 12 * self.years))
        return total_owning_cost

    def calculate_renting_cost(self):
        """
        Calculates the total cost of renting the DAS system over the specified number of years.

        :return: Total cost of renting.
        """
        total_renting_cost = self.rental_cost_per_month * 12 * self.years
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


def main():
    """
    Main function to execute the cost comparison program.
    """
    try:
        # Example parameters for the cost comparison
        purchase_price = 50000  # Example purchase price
        installation_cost = 10000  # Example installation cost
        monthly_maintenance_cost = 500  # Example monthly maintenance cost
        rental_cost_per_month = 2000  # Example rental cost per month
        years = 5  # Number of years for comparison

        # Create an instance of the cost comparison class
        cost_comparison = CellularDASCostComparison(purchase_price, installation_cost,
                                                    monthly_maintenance_cost, rental_cost_per_month, years)

        # Compare costs and print the result
        result = cost_comparison.compare_costs()
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
