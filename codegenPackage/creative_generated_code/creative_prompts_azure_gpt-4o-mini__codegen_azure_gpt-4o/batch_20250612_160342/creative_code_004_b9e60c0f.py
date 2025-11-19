"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xxcw51.com
Prompt: Develop a monthly work plan template that reflects the recommendations from the 月工作计划模板汇总 on 账云范文网.
Generated: DETERMINISTIC_b9e60c0f063230d8
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python code that generates a monthly work plan template based on general recommendations. The code is designed to be clean, efficient, and production-ready.

```python
import datetime
import json

class MonthlyWorkPlan:
    """
    A class to represent a Monthly Work Plan.
    Provides functionality for creating, updating, and exporting a work plan.
    """
    def __init__(self, month: str, year: int):
        """
        Initialize the MonthlyWorkPlan instance.

        :param month: Month for the work plan (e.g., "January").
        :param year: Year for the work plan.
        """
        self.month = month
        self.year = year
        self.tasks = []  # List to store tasks for the month

    def add_task(self, task_name: str, description: str, priority: str, deadline: str):
        """
        Add a task to the work plan.

        :param task_name: Name of the task.
        :param description: Description of the task.
        :param priority: Priority level (High, Medium, Low).
        :param deadline: Deadline for the task (format: YYYY-MM-DD).
        """
        try:
            # Validate deadline format
            datetime.datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid deadline format. Use YYYY-MM-DD.")

        if priority not in ['High', 'Medium', 'Low']:
            raise ValueError("Invalid priority. Use 'High', 'Medium', or 'Low'.")

        task = {
            "task_name": task_name,
            "description": description,
            "priority": priority,
            "deadline": deadline
        }
        self.tasks.append(task)

    def get_plan_summary(self) -> str:
        """
        Get a summary of the work plan.

        :return: Formatted summary string.
        """
        summary = f"Monthly Work Plan - {self.month} {self.year}\n"
        summary += "=" * 40 + "\n"
        for idx, task in enumerate(self.tasks, start=1):
            summary += (
                f"Task {idx}:\n"
                f"  Name       : {task['task_name']}\n"
                f"  Description: {task['description']}\n"
                f"  Priority   : {task['priority']}\n"
                f"  Deadline   : {task['deadline']}\n"
                f"-" * 40 + "\n"
            )
        return summary

    def export_to_json(self, filepath: str):
        """
        Export the work plan to a JSON file.

        :param filepath: Path to save the JSON file.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump({
                    "month": self.month,
                    "year": self.year,
                    "tasks": self.tasks
                }, f, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")

    def load_from_json(self, filepath: str):
        """
        Load the work plan from a JSON file.

        :param filepath: Path to the JSON file.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.month = data.get("month", self.month)
                self.year = data.get("year", self.year)
                self.tasks = data.get("tasks", [])
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to load work plan: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create a work plan for January 2024
        plan = MonthlyWorkPlan(month="January", year=2024)

        # Add tasks to the work plan
        plan.add_task(
            task_name="Complete Project Proposal",
            description="Draft and submit the project proposal for Q1 initiatives.",
            priority="High",
            deadline="2024-01-10"
        )
        plan.add_task(
            task_name="Team Meeting",
            description="Hold a monthly meeting to discuss goals and progress.",
            priority="Medium",
            deadline="2024-01-15"
        )

        # Display the work plan summary
        print(plan.get_plan_summary())

        # Export the work plan to a JSON file
        plan.export_to_json(filepath="work_plan_january_2024.json")

        # Load the work plan back from the JSON file (optional)
        loaded_plan = MonthlyWorkPlan(month="Dummy", year=2000)
        loaded_plan.load_from_json(filepath="work_plan_january_2024.json")
        print("\nLoaded Plan Summary:")
        print(loaded_plan.get_plan_summary())

    except Exception as e:
        print(f"Error: {e}")
```

This script defines a `MonthlyWorkPlan` class with methods for adding tasks, summarizing the plan, exporting it to a JSON file, and loading it from a JSON file. It includes robust error handling and adheres to clean coding principles.
