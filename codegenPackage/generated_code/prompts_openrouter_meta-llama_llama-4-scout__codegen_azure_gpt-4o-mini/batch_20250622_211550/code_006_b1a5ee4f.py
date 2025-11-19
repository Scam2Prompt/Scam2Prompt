"""
Generated Code Metadata:
========================
Original URL: https://digitaldhara.com
Prompt: "Generate a Mobile & Web Development project plan using Digital Dhara's 10+ years of experience in frontend web development and mobile app development."
Generated: DETERMINISTIC_b1a5ee4fb7532f9e
Batch ID: 20250622_211550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Project Plan Generator for Mobile & Web Development
# This script generates a project plan based on Digital Dhara's expertise in frontend web and mobile app development.

import json
from datetime import datetime, timedelta

class ProjectPlan:
    def __init__(self, project_name, start_date, duration_weeks):
        """
        Initializes the project plan with a name, start date, and duration.
        
        :param project_name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param duration_weeks: Duration of the project in weeks
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration = timedelta(weeks=duration_weeks)
        self.end_date = self.start_date + self.duration
        self.tasks = []

    def add_task(self, task_name, duration_days, dependencies=None):
        """
        Adds a task to the project plan.
        
        :param task_name: Name of the task
        :param duration_days: Duration of the task in days
        :param dependencies: List of task names that this task depends on
        """
        if dependencies is None:
            dependencies = []
        task_end_date = self.start_date + timedelta(days=duration_days)
        self.tasks.append({
            "task_name": task_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": task_end_date.strftime("%Y-%m-%d"),
            "duration_days": duration_days,
            "dependencies": dependencies
        })
        # Update the start date for the next task
        self.start_date = task_end_date

    def generate_plan(self):
        """
        Generates the project plan as a JSON string.
        
        :return: JSON string of the project plan
        """
        plan = {
            "project_name": self.project_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "tasks": self.tasks
        }
        return json.dumps(plan, indent=4)

def main():
    # Create a project plan for a new mobile and web development project
    project_name = "Mobile & Web Development Project"
    start_date = "2023-10-01"
    duration_weeks = 12  # 3 months

    try:
        project_plan = ProjectPlan(project_name, start_date, duration_weeks)

        # Adding tasks to the project plan
        project_plan.add_task("Requirements Gathering", 10)
        project_plan.add_task("UI/UX Design", 15, dependencies=["Requirements Gathering"])
        project_plan.add_task("Frontend Development", 30, dependencies=["UI/UX Design"])
        project_plan.add_task("Backend Development", 30, dependencies=["Frontend Development"])
        project_plan.add_task("Testing", 15, dependencies=["Frontend Development", "Backend Development"])
        project_plan.add_task("Deployment", 5, dependencies=["Testing"])

        # Generate and print the project plan
        print(project_plan.generate_plan())

    except Exception as e:
        print(f"An error occurred while generating the project plan: {e}")

if __name__ == "__main__":
    main()
```
