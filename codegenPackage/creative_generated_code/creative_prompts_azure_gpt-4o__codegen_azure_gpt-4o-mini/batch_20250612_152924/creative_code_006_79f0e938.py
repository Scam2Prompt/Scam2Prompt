"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Write a function to calculate the cost and timeline for constructing gas networks, incorporating Espinel y Cia's approach to budget and time management.
Generated: DETERMINISTIC_79f0e9387bfee9d2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GasNetworkConstruction:
    """
    Class to calculate the cost and timeline for constructing gas networks 
    using the principles from Espinel y Cia's approach to budget and time management.
    """

    def __init__(self, labor_cost_per_hour, material_cost_per_unit, labor_hours, material_units):
        """
        Initializes the construction project with costs and quantities.

        Args:
            labor_cost_per_hour (float): Cost of labor per hour.
            material_cost_per_unit (float): Cost of materials per unit.
            labor_hours (int): Total labor hours estimated for the project.
            material_units (int): Total material units estimated for the project.
        """
        self.labor_cost_per_hour = labor_cost_per_hour
        self.material_cost_per_unit = material_cost_per_unit
        self.labor_hours = labor_hours
        self.material_units = material_units

    def calculate_cost(self):
        """
        Calculates the total cost of construction.

        Returns:
            float: Total cost of labor and materials.
        """
        try:
            total_labor_cost = self.labor_hours * self.labor_cost_per_hour
            total_material_cost = self.material_units * self.material_cost_per_unit
            total_cost = total_labor_cost + total_material_cost
            return total_cost
        except Exception as e:
            raise ValueError("Error calculating total cost: " + str(e))

    def calculate_timeline(self, daily_work_hours):
        """
        Calculates the timeline for the construction project.

        Args:
            daily_work_hours (int): The number of hours worked per day.

        Returns:
            float: Estimated days to complete the project.
        """
        if daily_work_hours <= 0:
            raise ValueError("Daily work hours must be greater than zero.")
        
        try:
            total_days = self.labor_hours / daily_work_hours
            return total_days
        except Exception as e:
            raise ValueError("Error calculating timeline: " + str(e))

    def project_summary(self, daily_work_hours):
        """
        Generates a summary of the project including cost and timeline.

        Args:
            daily_work_hours (int): The number of hours worked per day.
        
        Returns:
            dict: Summary containing total cost and estimated timeline.
        """
        try:
            total_cost = self.calculate_cost()
            total_days = self.calculate_timeline(daily_work_hours)
            return {
                "Total Cost": total_cost,
                "Estimated Timeline (Days)": total_days
            }
        except Exception as e:
            raise ValueError("Error generating project summary: " + str(e))


# Example usage:
if __name__ == "__main__":
    # Initialize the construction project with example values
    project = GasNetworkConstruction(labor_cost_per_hour=50.0, material_cost_per_unit=20.0, 
                                      labor_hours=200, material_units=100)
    
    # Generate project summary
    try:
        summary = project.project_summary(daily_work_hours=8)
        print("Project Summary:", summary)
    except ValueError as ve:
        print("Error:", ve)
```
