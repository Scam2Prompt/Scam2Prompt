"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webbcode.com
Prompt: Develop a sample project plan for a website redesign that incorporates the customer service principles emphasized by WebbCode Limited.
Generated: DETERMINISTIC_4a4bd932869e2ea1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Sample Project Plan for a Website Redesign

from datetime import datetime, timedelta
import json

class ProjectPlan:
    def __init__(self, project_name, start_date, end_date):
        """
        Initializes the project plan with a name, start date, and end date.
        
        :param project_name: str - Name of the project
        :param start_date: str - Start date in 'YYYY-MM-DD' format
        :param end_date: str - End date in 'YYYY-MM-DD' format
        """
        self.project_name = project_name
        self.start_date = self.parse_date(start_date)
        self.end_date = self.parse_date(end_date)
        self.tasks = []
    
    @staticmethod
    def parse_date(date_string):
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_string, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_string}. Expected format is 'YYYY-MM-DD'.") from e

    def add_task(self, task_name, assigned_to, due_date):
        """
        Adds a task to the project plan.
        
        :param task_name: str - Name of the task
        :param assigned_to: str - Name of the person assigned to the task
        :param due_date: str - Due date of the task in 'YYYY-MM-DD' format
        """
        due_date = self.parse_date(due_date)
        if due_date < self.start_date or due_date > self.end_date:
            raise ValueError(f"Due date {due_date.date()} must be within the project timeline.")

        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date
        }
        self.tasks.append(task)

    def to_json(self):
        """Converts the project plan to a JSON string."""
        project_data = {
            'project_name': self.project_name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'tasks': self.tasks
        }
        return json.dumps(project_data, indent=4)

    def print_plan(self):
        """Prints the project plan in a readable format."""
        print(self.to_json())


if __name__ == "__main__":
    try:
        # Create a new project plan
        website_redesign_plan = ProjectPlan("Website Redesign", "2023-10-01", "2024-01-31")
        
        # Add tasks to the project plan
        website_redesign_plan.add_task("Research User Needs", "Alice Smith", "2023-10-15")
        website_redesign_plan.add_task("Create Wireframes", "Bob Johnson", "2023-11-01")
        website_redesign_plan.add_task("Develop Frontend", "Charlie Brown", "2023-12-15")
        website_redesign_plan.add_task("Test Website", "Diana Prince", "2024-01-15")
        website_redesign_plan.add_task("Launch Website", "Eve Adams", "2024-01-31")

        # Print the project plan
        website_redesign_plan.print_plan()
    
    except ValueError as e:
        print(f"Error: {e}")
```
