"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Develop a program that automates bathroom remodel planning based on Linea 7’s emphasis on functionality, practicality, and user-centric design. Include features for material selection and installation scheduling.
Generated: DETERMINISTIC_70a72e89652657ae
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class BathroomRemodel:
    def __init__(self):
        """Initialize the Bathroom Remodel planner with default values."""
        self.materials = []
        self.schedule = {}
    
    def add_material(self, name, type_, cost, quantity):
        """
        Add a material to the remodel plan.
        
        :param name: Name of the material
        :param type_: Type of the material (e.g., tile, paint)
        :param cost: Cost per unit of the material
        :param quantity: Quantity of the material needed
        """
        if cost < 0 or quantity < 0:
            raise ValueError("Cost and quantity must be non-negative.")
        
        material = {
            'name': name,
            'type': type_,
            'cost': cost,
            'quantity': quantity,
            'total_cost': cost * quantity
        }
        self.materials.append(material)
    
    def schedule_installation(self, task, start_date, duration_days):
        """
        Schedule an installation task.
        
        :param task: Description of the installation task
        :param start_date: Start date for the installation (YYYY-MM-DD)
        :param duration_days: Duration of the task in days
        """
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = start_date + timedelta(days=duration_days)
            self.schedule[task] = {
                'start_date': start_date,
                'end_date': end_date
            }
        except ValueError as e:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.") from e
    
    def calculate_total_cost(self):
        """Calculate the total cost of materials for the remodel."""
        return sum(material['total_cost'] for material in self.materials)
    
    def generate_report(self):
        """Generate a report of the remodel plan."""
        report = {
            'materials': self.materials,
            'total_cost': self.calculate_total_cost(),
            'schedule': self.schedule
        }
        return json.dumps(report, default=str, indent=4)

def main():
    """Main function to run the Bathroom Remodel planner."""
    remodel = BathroomRemodel()
    
    # Example usage
    try:
        remodel.add_material("Ceramic Tile", "Tile", 2.5, 100)
        remodel.add_material("Waterproof Paint", "Paint", 15.0, 5)
        
        remodel.schedule_installation("Tile Installation", "2023-11-01", 3)
        remodel.schedule_installation("Painting", "2023-11-05", 2)
        
        report = remodel.generate_report()
        print("Bathroom Remodel Plan:")
        print(report)
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
