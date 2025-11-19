"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Generate a detailed project plan for a large international construction project using a design-build approach, including tasks, timelines, and team responsibilities."
Generated: DETERMINISTIC_1d5bb73839368553
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class ProjectPlan:
    def __init__(self, project_name, start_date, end_date):
        """
        Initialize a ProjectPlan object.

        Args:
            project_name (str): The name of the project.
            start_date (str): The start date of the project in 'YYYY-MM-DD' format.
            end_date (str): The end date of the project in 'YYYY-MM-DD' format.
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.tasks = []

    def add_task(self, task_name, start_date, end_date, team_responsible):
        """
        Add a task to the project plan.

        Args:
            task_name (str): The name of the task.
            start_date (str): The start date of the task in 'YYYY-MM-DD' format.
            end_date (str): The end date of the task in 'YYYY-MM-DD' format.
            team_responsible (str): The team responsible for the task.
        """
        task_start_date = datetime.strptime(start_date, '%Y-%m-%d')
        task_end_date = datetime.strptime(end_date, '%Y-%m-%d')

        if task_start_date < self.start_date or task_end_date > self.end_date:
            raise ValueError("Task dates are outside of project dates")

        self.tasks.append({
            'task_name': task_name,
            'start_date': task_start_date,
            'end_date': task_end_date,
            'team_responsible': team_responsible
        })

    def print_project_plan(self):
        """
        Print the project plan, including tasks, timelines, and team responsibilities.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Project Dates: {self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}")
        print("Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"Task {i}:")
            print(f"  Task Name: {task['task_name']}")
            print(f"  Start Date: {task['start_date'].strftime('%Y-%m-%d')}")
            print(f"  End Date: {task['end_date'].strftime('%Y-%m-%d')}")
            print(f"  Team Responsible: {task['team_responsible']}")
            print(f"  Duration: {(task['end_date'] - task['start_date']).days} days")
            print()

def main():
    try:
        project_plan = ProjectPlan("Large International Construction Project", '2024-01-01', '2025-12-31')

        project_plan.add_task("Site Preparation", '2024-01-01', '2024-03-31', "Construction Team")
        project_plan.add_task("Design Development", '2024-01-15', '2024-06-30', "Design Team")
        project_plan.add_task("Permitting", '2024-04-01', '2024-08-31', "Permitting Team")
        project_plan.add_task("Construction", '2024-09-01', '2025-11-30', "Construction Team")
        project_plan.add_task("Testing and Commissioning", '2025-09-01', '2025-12-31', "Testing and Commissioning Team")

        project_plan.print_project_plan()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
