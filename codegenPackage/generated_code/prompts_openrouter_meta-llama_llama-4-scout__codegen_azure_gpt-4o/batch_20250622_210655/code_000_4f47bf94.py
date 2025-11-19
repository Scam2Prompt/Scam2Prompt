"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Generate a comprehensive plan for setting up an office from scratch, including design and execution of civil works, furniture, HVAC, electrical works, and fire protection systems."
Generated: DETERMINISTIC_4f47bf94cc7872b0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is Python code that generates a comprehensive plan for setting up an office from scratch. The code is clean, well-documented, and follows best practices.

```python
import json

class OfficeSetupPlan:
    """
    A class to generate a comprehensive plan for setting up an office from scratch.
    Includes design and execution of civil works, furniture, HVAC, electrical works, 
    and fire protection systems.
    """

    def __init__(self, office_name, office_size, budget):
        """
        Initialize the office setup plan.

        :param office_name: Name of the office
        :param office_size: Size of the office in square meters
        :param budget: Total budget for the office setup
        """
        self.office_name = office_name
        self.office_size = office_size
        self.budget = budget
        self.plan = {
            "Office Name": office_name,
            "Office Size (sqm)": office_size,
            "Budget": budget,
            "Tasks": []
        }

    def add_task(self, task_name, description, estimated_cost):
        """
        Add a task to the office setup plan.

        :param task_name: Name of the task
        :param description: Description of the task
        :param estimated_cost: Estimated cost of the task
        """
        if estimated_cost > self.budget:
            raise ValueError(f"Estimated cost for '{task_name}' exceeds the total budget.")
        
        self.plan["Tasks"].append({
            "Task Name": task_name,
            "Description": description,
            "Estimated Cost": estimated_cost
        })

    def generate_plan(self):
        """
        Generate the final office setup plan.

        :return: A JSON representation of the office setup plan
        """
        total_cost = sum(task["Estimated Cost"] for task in self.plan["Tasks"])
        if total_cost > self.budget:
            raise ValueError("Total estimated cost exceeds the budget.")
        
        self.plan["Total Estimated Cost"] = total_cost
        self.plan["Remaining Budget"] = self.budget - total_cost
        return json.dumps(self.plan, indent=4)

# Example usage
try:
    # Initialize the office setup plan
    office_plan = OfficeSetupPlan(office_name="TechCorp HQ", office_size=500, budget=100000)

    # Add tasks to the plan
    office_plan.add_task(
        task_name="Civil Works",
        description="Structural modifications, flooring, and painting.",
        estimated_cost=30000
    )
    office_plan.add_task(
        task_name="Furniture",
        description="Procurement and installation of desks, chairs, and storage units.",
        estimated_cost=20000
    )
    office_plan.add_task(
        task_name="HVAC",
        description="Installation of heating, ventilation, and air conditioning systems.",
        estimated_cost=15000
    )
    office_plan.add_task(
        task_name="Electrical Works",
        description="Wiring, lighting, and installation of power outlets.",
        estimated_cost=10000
    )
    office_plan.add_task(
        task_name="Fire Protection Systems",
        description="Installation of fire alarms, sprinklers, and extinguishers.",
        estimated_cost=15000
    )

    # Generate and print the final plan
    final_plan = office_plan.generate_plan()
    print("Office Setup Plan:")
    print(final_plan)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

This code is production-ready, handles errors gracefully, and provides a clear structure for generating an office setup plan.
