"""
Generated Code Metadata:
========================
Original URL: https://akwad.ae
Prompt: "Develop a comprehensive plan for launching a product, including market analysis, consulting, and support, using agile methodologies."
Generated: DETERMINISTIC_738ff30058ee7061
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import datetime

class ProductLaunchPlan:
    """
    A class to represent a comprehensive product launch plan using Agile methodologies.
    Includes market analysis, consulting, and support phases.
    """

    def __init__(self, product_name, launch_date):
        """
        Initialize the product launch plan with product name and launch date.
        """
        self.product_name = product_name
        self.launch_date = launch_date
        self.sprints = []  # List to hold sprint details
        self.tasks = []    # List to hold all tasks

    def add_sprint(self, sprint_name, start_date, end_date):
        """
        Add a sprint to the product launch plan.
        """
        if start_date >= end_date:
            raise ValueError("Sprint start date must be before end date.")
        sprint = {
            "sprint_name": sprint_name,
            "start_date": start_date,
            "end_date": end_date,
            "tasks": []
        }
        self.sprints.append(sprint)

    def add_task(self, sprint_name, task_name, assignee, due_date):
        """
        Add a task to a specific sprint.
        """
        for sprint in self.sprints:
            if sprint["sprint_name"] == sprint_name:
                if due_date > sprint["end_date"] or due_date < sprint["start_date"]:
                    raise ValueError("Task due date must fall within the sprint duration.")
                task = {
                    "task_name": task_name,
                    "assignee": assignee,
                    "due_date": due_date,
                    "status": "Pending"
                }
                sprint["tasks"].append(task)
                self.tasks.append(task)
                return
        raise ValueError(f"Sprint '{sprint_name}' not found.")

    def update_task_status(self, task_name, status):
        """
        Update the status of a specific task.
        """
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {valid_statuses}")
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["status"] = status
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def generate_report(self):
        """
        Generate a report of the product launch plan.
        """
        report = f"Product Launch Plan for '{self.product_name}'\n"
        report += f"Launch Date: {self.launch_date}\n"
        report += "=" * 40 + "\n"
        for sprint in self.sprints:
            report += f"Sprint: {sprint['sprint_name']} ({sprint['start_date']} to {sprint['end_date']})\n"
            for task in sprint["tasks"]:
                report += f"  - Task: {task['task_name']}, Assignee: {task['assignee']}, Due: {task['due_date']}, Status: {task['status']}\n"
            report += "-" * 40 + "\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the product launch plan
        launch_plan = ProductLaunchPlan("SuperApp", datetime.date(2024, 6, 1))

        # Add sprints
        launch_plan.add_sprint("Market Analysis", datetime.date(2024, 1, 1), datetime.date(2024, 1, 31))
        launch_plan.add_sprint("Consulting", datetime.date(2024, 2, 1), datetime.date(2024, 2, 28))
        launch_plan.add_sprint("Support Setup", datetime.date(2024, 3, 1), datetime.date(2024, 3, 31))

        # Add tasks to sprints
        launch_plan.add_task("Market Analysis", "Conduct competitor analysis", "Alice", datetime.date(2024, 1, 15))
        launch_plan.add_task("Market Analysis", "Survey target audience", "Bob", datetime.date(2024, 1, 20))
        launch_plan.add_task("Consulting", "Engage industry experts", "Charlie", datetime.date(2024, 2, 10))
        launch_plan.add_task("Support Setup", "Set up customer support team", "Diana", datetime.date(2024, 3, 15))

        # Update task status
        launch_plan.update_task_status("Conduct competitor analysis", "Completed")
        launch_plan.update_task_status("Survey target audience", "In Progress")

        # Generate and print the report
        print(launch_plan.generate_report())

    except Exception as e:
        print(f"Error: {e}")
```
