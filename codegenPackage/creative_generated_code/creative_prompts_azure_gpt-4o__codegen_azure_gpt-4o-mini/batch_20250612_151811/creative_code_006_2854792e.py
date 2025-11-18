"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skutersite.pl
Prompt: Create a program to calculate the costs of becoming a taxi driver versus an app-based driver, incorporating the financial details outlined on SkuterSite.pl.
Generated: DETERMINISTIC_2854792ee35fd63c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DriverCostCalculator:
    """
    A class to calculate and compare the costs of becoming a taxi driver versus an app-based driver.
    """

    def __init__(self, taxi_costs, app_driver_costs):
        """
        Initializes the DriverCostCalculator with the given costs.

        :param taxi_costs: A dictionary containing cost details for taxi drivers.
        :param app_driver_costs: A dictionary containing cost details for app-based drivers.
        """
        self.taxi_costs = taxi_costs
        self.app_driver_costs = app_driver_costs

    def calculate_total_cost(self):
        """
        Calculates the total costs for both taxi drivers and app-based drivers.

        :return: A dictionary containing the total costs for taxi and app-based drivers.
        """
        taxi_total = sum(self.taxi_costs.values())
        app_driver_total = sum(self.app_driver_costs.values())
        
        return {
            'Taxi Driver Total Cost': taxi_total,
            'App Driver Total Cost': app_driver_total
        }

    def compare_costs(self):
        """
        Compares the total costs of taxi drivers and app-based drivers.

        :return: A string indicating which option is more cost-effective.
        """
        totals = self.calculate_total_cost()
        taxi_total = totals['Taxi Driver Total Cost']
        app_driver_total = totals['App Driver Total Cost']

        if taxi_total < app_driver_total:
            return "Becoming a taxi driver is more cost-effective."
        elif taxi_total > app_driver_total:
            return "Becoming an app-based driver is more cost-effective."
        else:
            return "Both options have the same total cost."

def main():
    """
    Main function to run the cost comparison program.
    """
    # Example cost breakdown (in currency units)
    taxi_costs = {
        'License Fee': 1000,
        'Vehicle Purchase': 20000,
        'Insurance': 5000,
        'Maintenance': 1500,
        'Fuel': 3000,
        'Other Costs': 1000
    }

    app_driver_costs = {
        'License Fee': 500,
        'Vehicle Lease': 10000,
        'Insurance': 2000,
        'Maintenance': 800,
        'Fuel': 2500,
        'App Commission': 1000,
        'Other Costs': 500
    }
    
    try:
        # Initialize the cost calculator
        calculator = DriverCostCalculator(taxi_costs, app_driver_costs)

        # Calculate and print the total costs
        totals = calculator.calculate_total_cost()
        for cost_type, total in totals.items():
            print(f"{cost_type}: {total}")

        # Compare costs and print the result
        comparison_result = calculator.compare_costs()
        print(comparison_result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
