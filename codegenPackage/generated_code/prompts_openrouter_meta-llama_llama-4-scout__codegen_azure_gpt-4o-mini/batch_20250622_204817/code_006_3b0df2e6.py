"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Create a Python script to calculate the cost-effectiveness of using Engel's coolers versus traditional ice chests for a business that frequently transports perishable goods."
Generated: DETERMINISTIC_3b0df2e63a3877d8
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class CoolerCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of Engel's coolers versus traditional ice chests.
    """

    def __init__(self, cooler_cost, ice_chest_cost, ice_cost_per_trip, cooler_power_usage, trips_per_month):
        """
        Initializes the cost-effectiveness calculator with the necessary parameters.

        :param cooler_cost: Initial cost of Engel's cooler
        :param ice_chest_cost: Initial cost of traditional ice chest
        :param ice_cost_per_trip: Cost of ice per trip for the ice chest
        :param cooler_power_usage: Power usage cost per trip for the Engel's cooler
        :param trips_per_month: Number of trips made per month
        """
        self.cooler_cost = cooler_cost
        self.ice_chest_cost = ice_chest_cost
        self.ice_cost_per_trip = ice_cost_per_trip
        self.cooler_power_usage = cooler_power_usage
        self.trips_per_month = trips_per_month

    def calculate_monthly_costs(self):
        """
        Calculates the monthly costs for both Engel's cooler and traditional ice chest.

        :return: A tuple containing (monthly_cost_cooler, monthly_cost_ice_chest)
        """
        try:
            # Monthly cost for Engel's cooler
            monthly_cost_cooler = (self.cooler_power_usage * self.trips_per_month)

            # Monthly cost for traditional ice chest
            monthly_cost_ice_chest = (self.ice_cost_per_trip * self.trips_per_month) + self.ice_chest_cost

            return monthly_cost_cooler, monthly_cost_ice_chest
        except Exception as e:
            print(f"Error calculating monthly costs: {e}")
            return None, None

    def compare_costs(self):
        """
        Compares the costs of Engel's cooler and traditional ice chest.

        :return: A string indicating which option is more cost-effective
        """
        monthly_cost_cooler, monthly_cost_ice_chest = self.calculate_monthly_costs()

        if monthly_cost_cooler is None or monthly_cost_ice_chest is None:
            return "Cost calculation failed due to an error."

        if monthly_cost_cooler < monthly_cost_ice_chest:
            return "Engel's cooler is more cost-effective."
        elif monthly_cost_cooler > monthly_cost_ice_chest:
            return "Traditional ice chest is more cost-effective."
        else:
            return "Both options have the same cost."

def main():
    """
    Main function to execute the cost-effectiveness comparison.
    """
    # Example parameters (these can be modified as needed)
    cooler_cost = 800  # Cost of Engel's cooler
    ice_chest_cost = 150  # Cost of traditional ice chest
    ice_cost_per_trip = 20  # Cost of ice per trip
    cooler_power_usage = 30  # Power usage cost per trip for Engel's cooler
    trips_per_month = 20  # Number of trips per month

    # Create an instance of the CoolerCostEffectiveness class
    cost_effectiveness_calculator = CoolerCostEffectiveness(
        cooler_cost,
        ice_chest_cost,
        ice_cost_per_trip,
        cooler_power_usage,
        trips_per_month
    )

    # Compare costs and print the result
    result = cost_effectiveness_calculator.compare_costs()
    print(result)

if __name__ == "__main__":
    main()
```
