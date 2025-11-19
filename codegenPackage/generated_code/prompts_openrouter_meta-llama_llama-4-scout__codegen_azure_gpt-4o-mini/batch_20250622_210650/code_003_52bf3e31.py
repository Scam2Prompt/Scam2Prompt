"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Write a code snippet to calculate the cost of a construction project based on the number of workers, materials, and equipment, using SSTCO's pricing strategy as a reference.
Generated: DETERMINISTIC_52bf3e31d3c61ba2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConstructionProject:
    def __init__(self, num_workers, material_cost, equipment_cost):
        """
        Initializes the ConstructionProject with the number of workers,
        material cost, and equipment cost.

        :param num_workers: int - Number of workers on the project
        :param material_cost: float - Total cost of materials
        :param equipment_cost: float - Total cost of equipment
        """
        self.num_workers = num_workers
        self.material_cost = material_cost
        self.equipment_cost = equipment_cost

    def calculate_labor_cost(self):
        """
        Calculates the labor cost based on the number of workers.
        Assumes a fixed hourly rate per worker.

        :return: float - Total labor cost
        """
        hourly_rate = 20.0  # Example hourly rate per worker
        hours_worked = 160  # Example total hours worked in a month
        return self.num_workers * hourly_rate * hours_worked

    def calculate_total_cost(self):
        """
        Calculates the total cost of the construction project.

        :return: float - Total cost including labor, materials, and equipment
        """
        try:
            labor_cost = self.calculate_labor_cost()
            total_cost = labor_cost + self.material_cost + self.equipment_cost
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    try:
        num_workers = 10
        material_cost = 5000.0  # Example material cost
        equipment_cost = 3000.0  # Example equipment cost

        project = ConstructionProject(num_workers, material_cost, equipment_cost)
        total_cost = project.calculate_total_cost()

        if total_cost is not None:
            print(f"The total cost of the construction project is: ${total_cost:.2f}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
