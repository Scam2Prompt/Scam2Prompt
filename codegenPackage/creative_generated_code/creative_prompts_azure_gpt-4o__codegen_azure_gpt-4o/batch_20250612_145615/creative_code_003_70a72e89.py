"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-7.webflow.io
Prompt: Develop a program that automates bathroom remodel planning based on Linea 7’s emphasis on functionality, practicality, and user-centric design. Include features for material selection and installation scheduling.
Generated: DETERMINISTIC_70a72e89652657ae
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class BathroomRemodelPlanner:
    """
    Bathroom Remodel Planner
    Automates planning for bathroom remodeling with a focus on functionality, practicality,
    and user-centric design. Includes material selection and installation scheduling features.
    """

    def __init__(self):
        self.materials = []
        self.schedule = []

    def add_material(self, name, category, cost_per_unit):
        """
        Add a material to the selection list.

        :param name: Name of the material (e.g., "Tile", "Faucet").
        :param category: Category of the material (e.g., "Flooring", "Plumbing").
        :param cost_per_unit: Cost per unit of material.
        """
        material = {
            "name": name,
            "category": category,
            "cost_per_unit": cost_per_unit
        }
        self.materials.append(material)
        print(f"Material '{name}' has been added.")

    def view_materials(self):
        """
        View the list of selected materials.
        """
        if not self.materials:
            print("No materials selected yet.")
            return

        print("Selected Materials:")
        for idx, material in enumerate(self.materials, 1):
            print(f"{idx}. {material['name']} (Category: {material['category']}, Cost/Unit: ${material['cost_per_unit']:.2f})")

    def schedule_installation(self, task_name, start_date, duration_days):
        """
        Schedule an installation task.

        :param task_name: Name of the task (e.g., "Install Tiles").
        :param start_date: Start date for the task in 'YYYY-MM-DD' format.
        :param duration_days: Estimated duration in days.
        """
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = start_date_obj + timedelta(days=duration_days)
            task = {
                "task_name": task_name,
                "start_date": start_date,
                "end_date": end_date_obj.strftime("%Y-%m-%d")
            }
            self.schedule.append(task)
            print(f"Task '{task_name}' scheduled from {start_date} to {end_date_obj.strftime('%Y-%m-%d')}.")
        except ValueError as e:
            print(f"Error: {e}. Ensure the date is in 'YYYY-MM-DD' format.")

    def view_schedule(self):
        """
        View the installation schedule.
        """
        if not self.schedule:
            print("No tasks scheduled yet.")
            return

        print("Installation Schedule:")
        for idx, task in enumerate(self.schedule, 1):
            print(f"{idx}. {task['task_name']} (Start: {task['start_date']}, End: {task['end_date']})")

    def save_plan(self, filename="bathroom_remodel_plan.json"):
        """
        Save the remodel plan (materials and schedule) to a JSON file.

        :param filename: Name of the output file (default: "bathroom_remodel_plan.json").
        """
        try:
            plan = {
                "materials": self.materials,
                "schedule": self.schedule
            }
            with open(filename, "w") as file:
                json.dump(plan, file, indent=4)
            print(f"Plan saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving plan: {e}")

    def load_plan(self, filename="bathroom_remodel_plan.json"):
        """
        Load a remodel plan (materials and schedule) from a JSON file.

        :param filename: Name of the input file (default: "bathroom_remodel_plan.json").
        """
        try:
            with open(filename, "r") as file:
                plan = json.load(file)
                self.materials = plan.get("materials", [])
                self.schedule = plan.get("schedule", [])
            print(f"Plan loaded successfully from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading plan: {e}")


# Example usage (comment out in production if integrating into a larger system):
if __name__ == "__main__":
    remodel_planner = BathroomRemodelPlanner()

    # Add materials
    remodel_planner.add_material("Ceramic Tiles", "Flooring", 5.5)
    remodel_planner.add_material("Rain Showerhead", "Plumbing", 120.0)

    # View materials
    remodel_planner.view_materials()

    # Schedule tasks
    remodel_planner.schedule_installation("Tile Installation", "2023-11-01", 5)
    remodel_planner.schedule_installation("Shower Installation", "2023-11-07", 3)

    # View schedule
    remodel_planner.view_schedule()

    # Save and load plan
    remodel_planner.save_plan()
    remodel_planner.load_plan()
```
