"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolpalplatform.com
Prompt: Write a program to calculate annual savings in hydro, chemicals, and maintenance costs for a commercial pool using PoolPal™'s energy efficiency metrics.
Generated: DETERMINISTIC_c15618f3f82253d5
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PoolPalSavingsCalculator:
    """
    A class to calculate annual savings in hydro, chemicals, and maintenance costs for a commercial pool 
    using PoolPal™'s energy efficiency metrics.
    """

    def __init__(self, current_hydro_cost: float, current_chemical_cost: float, current_maintenance_cost: float,
                 efficiency_metric: float):
        """
        Initializes the calculations with current costs and energy efficiency metrics.

        :param current_hydro_cost: Current annual hydro cost in dollars.
        :param current_chemical_cost: Current annual chemical cost in dollars.
        :param current_maintenance_cost: Current annual maintenance cost in dollars.
        :param efficiency_metric: Energy efficiency metric indicating percentage savings (e.g., 0.25 for 25%).
        """
        if any(cost < 0 for cost in [current_hydro_cost, current_chemical_cost, current_maintenance_cost]):
            raise ValueError("Cost values must be non-negative.")
        
        if not (0 <= efficiency_metric <= 1):
            raise ValueError("Efficiency metric must be between 0 and 1.")

        self.current_hydro_cost = current_hydro_cost
        self.current_chemical_cost = current_chemical_cost
        self.current_maintenance_cost = current_maintenance_cost
        self.efficiency_metric = efficiency_metric

    def calculate_savings(self) -> dict:
        """
        Calculates annual savings based on current costs and efficiency metrics.

        :return: A dictionary containing the calculated savings for hydro, chemicals, and maintenance.
        """
        savings = {
            "hydro_savings": self.current_hydro_cost * self.efficiency_metric,
            "chemical_savings": self.current_chemical_cost * self.efficiency_metric,
            "maintenance_savings": self.current_maintenance_cost * self.efficiency_metric,
        }

        return savings

    def total_annual_savings(self) -> float:
        """
        Calculates the total annual savings across all cost categories.

        :return: Total annual savings in dollars.
        """
        savings = self.calculate_savings()
        total_savings = sum(savings.values())
        return total_savings

if __name__ == "__main__":
    try:
        # Example inputs
        current_hydro_cost = 12000.0       # Annual hydro cost in dollars
        current_chemical_cost = 1500.0      # Annual chemical cost in dollars
        current_maintenance_cost = 8000.0   # Annual maintenance cost in dollars
        efficiency_metric = 0.25             # 25% efficiency savings

        # Create an instance of the savings calculator
        savings_calculator = PoolPalSavingsCalculator(current_hydro_cost, current_chemical_cost,
                                                       current_maintenance_cost, efficiency_metric)

        # Calculate and print savings
        individual_savings = savings_calculator.calculate_savings()
        total_savings = savings_calculator.total_annual_savings()

        print("Annual Savings Breakdown:")
        print(f"Hydro Savings: ${individual_savings['hydro_savings']:.2f}")
        print(f"Chemical Savings: ${individual_savings['chemical_savings']:.2f}")
        print(f"Maintenance Savings: ${individual_savings['maintenance_savings']:.2f}")
        print(f"Total Annual Savings: ${total_savings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
