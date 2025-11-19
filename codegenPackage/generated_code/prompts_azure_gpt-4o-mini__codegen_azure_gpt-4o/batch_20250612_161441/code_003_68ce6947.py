"""
Generated Code Metadata:
========================
Original URL: https://support.godaddysites.com
Prompt: Provide an example of a project plan that includes timelines and cost analysis for a financial services marketing campaign based on Uphold's support framework.
Generated: DETERMINISTIC_68ce69472b982e8f
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ProjectPlan:
    """
    A class to represent a project plan for a financial services marketing campaign.
    Includes timelines and cost analysis based on Uphold's support framework.
    """

    def __init__(self, project_name, start_date, end_date, budget):
        """
        Initialize the project plan.

        :param project_name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        :param budget: Total budget for the project
        """
        self.project_name = project_name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.budget = budget
        self.tasks = []

    def add_task(self, task_name, start_date, end_date, cost):
        """
        Add a task to the project plan.

        :param task_name: Name of the task
        :param start_date: Start date of the task (YYYY-MM-DD)
        :param end_date: End date of the task (YYYY-MM-DD)
        :param cost: Cost associated with the task
        :raises ValueError: If task cost exceeds the remaining budget
        """
        task_start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        task_end = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        if cost > self.get_remaining_budget():
            raise ValueError("Task cost exceeds the remaining budget.")

        self.tasks.append({
            "task_name": task_name,
            "start_date": task_start,
            "end_date": task_end,
            "cost": cost
        })

    def get_remaining_budget(self):
        """
        Calculate the remaining budget for the project.

        :return: Remaining budget
        """
        total_spent = sum(task["cost"] for task in self.tasks)
        return self.budget - total_spent

    def generate_report(self):
        """
        Generate a report of the project plan.

        :return: A dictionary containing project details, tasks, and budget analysis
        """
        report = {
            "project_name": self.project_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "total_budget": self.budget,
            "remaining_budget": self.get_remaining_budget(),
            "tasks": [
                {
                    "task_name": task["task_name"],
                    "start_date": task["start_date"].strftime("%Y-%m-%d"),
                    "end_date": task["end_date"].strftime("%Y-%m-%d"),
                    "cost": task["cost"]
                }
                for task in self.tasks
            ]
        }
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create a project plan
        project = ProjectPlan(
            project_name="Financial Services Marketing Campaign",
            start_date="2023-11-01",
            end_date="2023-12-31",
            budget=50000
        )

        # Add tasks to the project plan
        project.add_task("Market Research", "2023-11-01", "2023-11-15", 10000)
        project.add_task("Content Creation", "2023-11-16", "2023-11-30", 15000)
        project.add_task("Ad Campaigns", "2023-12-01", "2023-12-15", 20000)

        # Generate and print the project report
        report = project.generate_report()
        print("Project Report:")
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
