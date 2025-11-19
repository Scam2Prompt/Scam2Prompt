"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Generate a project plan for a product management initiative that incorporates Scrum Master principles and practices, as taught in the PDMA Technologies' Scrum Master course.
Generated: DETERMINISTIC_0ccf352b6d85f20a
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Project Plan Generator for Product Management Initiative

import datetime

class ProjectPlan:
    def __init__(self, project_name, product_manager, scrum_master):
        """
        Initialize a project plan with the given project name, product manager, and Scrum Master.

        Args:
            project_name (str): The name of the project.
            product_manager (str): The name of the product manager.
            scrum_master (str): The name of the Scrum Master.
        """
        self.project_name = project_name
        self.product_manager = product_manager
        self.scrum_master = scrum_master
        self.sprint_plans = []

    def add_sprint_plan(self, sprint_name, start_date, end_date, goals):
        """
        Add a sprint plan to the project plan.

        Args:
            sprint_name (str): The name of the sprint.
            start_date (str): The start date of the sprint in YYYY-MM-DD format.
            end_date (str): The end date of the sprint in YYYY-MM-DD format.
            goals (list): A list of goals for the sprint.
        """
        sprint_plan = {
            "sprint_name": sprint_name,
            "start_date": datetime.datetime.strptime(start_date, "%Y-%m-%d").date(),
            "end_date": datetime.datetime.strptime(end_date, "%Y-%m-%d").date(),
            "goals": goals,
            "tasks": []
        }
        self.sprint_plans.append(sprint_plan)

    def add_task(self, sprint_name, task_name, task_description, assignee):
        """
        Add a task to a sprint plan.

        Args:
            sprint_name (str): The name of the sprint.
            task_name (str): The name of the task.
            task_description (str): The description of the task.
            assignee (str): The assignee of the task.

        Raises:
            ValueError: If the sprint plan is not found.
        """
        for sprint_plan in self.sprint_plans:
            if sprint_plan["sprint_name"] == sprint_name:
                task = {
                    "task_name": task_name,
                    "task_description": task_description,
                    "assignee": assignee,
                    "status": "To-Do"
                }
                sprint_plan["tasks"].append(task)
                return
        raise ValueError("Sprint plan not found")

    def update_task_status(self, sprint_name, task_name, status):
        """
        Update the status of a task.

        Args:
            sprint_name (str): The name of the sprint.
            task_name (str): The name of the task.
            status (str): The new status of the task.

        Raises:
            ValueError: If the sprint plan or task is not found.
        """
        for sprint_plan in self.sprint_plans:
            if sprint_plan["sprint_name"] == sprint_name:
                for task in sprint_plan["tasks"]:
                    if task["task_name"] == task_name:
                        task["status"] = status
                        return
                raise ValueError("Task not found")
        raise ValueError("Sprint plan not found")

    def print_project_plan(self):
        """
        Print the project plan.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Product Manager: {self.product_manager}")
        print(f"Scrum Master: {self.scrum_master}")
        for sprint_plan in self.sprint_plans:
            print(f"\nSprint Name: {sprint_plan['sprint_name']}")
            print(f"Start Date: {sprint_plan['start_date']}")
            print(f"End Date: {sprint_plan['end_date']}")
            print("Goals:")
            for goal in sprint_plan["goals"]:
                print(f"- {goal}")
            print("Tasks:")
            for task in sprint_plan["tasks"]:
                print(f"- {task['task_name']}: {task['status']}")

def main():
    project_name = "Product Management Initiative"
    product_manager = "John Doe"
    scrum_master = "Jane Smith"

    project_plan = ProjectPlan(project_name, product_manager, scrum_master)

    project_plan.add_sprint_plan(
        "Sprint 1",
        "2024-09-01",
        "2024-09-14",
        ["Goal 1", "Goal 2", "Goal 3"]
    )

    project_plan.add_task("Sprint 1", "Task 1", "Task 1 description", "John Doe")
    project_plan.add_task("Sprint 1", "Task 2", "Task 2 description", "Jane Smith")

    project_plan.update_task_status("Sprint 1", "Task 1", "In Progress")

    project_plan.print_project_plan()

if __name__ == "__main__":
    main()
```
