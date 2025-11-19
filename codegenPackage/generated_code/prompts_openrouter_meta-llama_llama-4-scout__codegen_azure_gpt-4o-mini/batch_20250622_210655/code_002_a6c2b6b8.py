"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: "Generate a cost estimation template for a custom pipeline construction project in Africa, including factors such as materials, labor, and equipment costs."
Generated: DETERMINISTIC_a6c2b6b883a010da
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class CostEstimation:
    """
    A class to estimate the costs for a custom pipeline construction project.
    """

    def __init__(self):
        """
        Initializes the CostEstimation class with empty data structures.
        """
        self.materials_cost = {}
        self.labor_cost = {}
        self.equipment_cost = {}
        self.total_cost = 0.0

    def add_material(self, material_name, unit_cost, quantity):
        """
        Adds a material cost to the estimation.

        :param material_name: Name of the material
        :param unit_cost: Cost per unit of the material
        :param quantity: Quantity of the material
        """
        if unit_cost < 0 or quantity < 0:
            raise ValueError("Unit cost and quantity must be non-negative.")
        self.materials_cost[material_name] = unit_cost * quantity

    def add_labor(self, labor_type, hourly_rate, hours):
        """
        Adds a labor cost to the estimation.

        :param labor_type: Type of labor (e.g., skilled, unskilled)
        :param hourly_rate: Cost per hour for the labor
        :param hours: Total hours of labor
        """
        if hourly_rate < 0 or hours < 0:
            raise ValueError("Hourly rate and hours must be non-negative.")
        self.labor_cost[labor_type] = hourly_rate * hours

    def add_equipment(self, equipment_name, rental_cost, duration):
        """
        Adds an equipment cost to the estimation.

        :param equipment_name: Name of the equipment
        :param rental_cost: Cost to rent the equipment
        :param duration: Duration of the rental
        """
        if rental_cost < 0 or duration < 0:
            raise ValueError("Rental cost and duration must be non-negative.")
        self.equipment_cost[equipment_name] = rental_cost * duration

    def calculate_total_cost(self):
        """
        Calculates the total cost of the project by summing materials, labor, and equipment costs.
        """
        self.total_cost = sum(self.materials_cost.values()) + \
                          sum(self.labor_cost.values()) + \
                          sum(self.equipment_cost.values())

    def generate_report(self):
        """
        Generates a cost estimation report as a DataFrame.

        :return: A pandas DataFrame containing the cost estimation report
        """
        report_data = {
            'Category': ['Materials', 'Labor', 'Equipment', 'Total'],
            'Cost': [
                sum(self.materials_cost.values()),
                sum(self.labor_cost.values()),
                sum(self.equipment_cost.values()),
                self.total_cost
            ]
        }
        report_df = pd.DataFrame(report_data)
        return report_df

# Example usage
if __name__ == "__main__":
    try:
        estimator = CostEstimation()
        estimator.add_material("Steel Pipe", 100, 50)  # 100 per unit, 50 units
        estimator.add_labor("Skilled Labor", 20, 160)   # 20 per hour, 160 hours
        estimator.add_equipment("Excavator", 500, 10)    # 500 per day, 10 days
        estimator.calculate_total_cost()
        report = estimator.generate_report()
        print(report)
    except ValueError as e:
        print(f"Error: {e}")
```
