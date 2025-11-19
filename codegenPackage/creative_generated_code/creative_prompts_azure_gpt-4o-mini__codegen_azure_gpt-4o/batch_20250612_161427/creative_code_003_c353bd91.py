"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trekk.com
Prompt: Generate a sample project plan for a complete rebranding and website migration similar to what Trekk has done for their clients.
Generated: DETERMINISTIC_c353bd911bb48e2b
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime


class ProjectPlan:
    """Class to generate and manage a project plan for rebranding and website migration."""

    def __init__(self, project_name, client_name, start_date, end_date):
        """
        Initializes the project plan instance.
        
        Args:
            project_name (str): Name of the project.
            client_name (str): Name of the client.
            start_date (str): Start date of the project (YYYY-MM-DD).
            end_date (str): End date of the project (YYYY-MM-DD).
        """
        self.project_name = project_name
        self.client_name = client_name
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.task_list = []

    def validate_date(self, date_str):
        """
        Validates the format of the provided date.
        
        Args:
            date_str (str): Date string in YYYY-MM-DD format.
        
        Returns:
            datetime.date: A valid date object.
        
        Raises:
            ValueError: If the date is not in the correct format or is invalid.
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format is YYYY-MM-DD.") from e

    def add_task(self, task_name, description, assignee, due_date):
        """
        Adds a task to the project plan.
        
        Args:
            task_name (str): Name of the task.
            description (str): A brief description of the task.
            assignee (str): Person responsible for the task.
            due_date (str): Due date of the task (YYYY-MM-DD).
        """
        due_date_obj = self.validate_date(due_date)
        if due_date_obj > self.end_date:
            raise ValueError(f"Task due date {due_date} cannot be after the project end date {self.end_date}.")
        
        task = {
            "task_name": task_name,
            "description": description,
            "assignee": assignee,
            "due_date": due_date_obj.strftime("%Y-%m-%d")
        }
        self.task_list.append(task)

    def generate_plan(self):
        """
        Generates the project plan as a dictionary.
        
        Returns:
            dict: A dictionary representation of the project plan.
        """
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "tasks": self.task_list
        }

    def export_plan_to_json(self, file_path):
        """
        Exports the project plan to a JSON file.
        
        Args:
            file_path (str): Path to the JSON file where the project plan will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.generate_plan(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file: {file_path}. Details: {e}") from e


# Example usage of the ProjectPlan class
if __name__ == "__main__":
    try:
        # Initialize the project plan
        project = ProjectPlan(
            project_name="Rebranding and Website Migration",
            client_name="Trekk Client XYZ",
            start_date="2023-10-01",
            end_date="2024-03-31"
        )

        # Add tasks to the plan
        project.add_task(
            task_name="Brand Strategy Development",
            description="Define new brand identity and guidelines.",
            assignee="Marketing Team",
            due_date="2023-10-15"
        )
        project.add_task(
            task_name="Website Content Audit",
            description="Identify content to migrate, remove, or rewrite.",
            assignee="Content Team",
            due_date="2023-11-01"
        )
        project.add_task(
            task_name="Website Design Mockups",
            description="Create mockups for the new website design.",
            assignee="Design Team",
            due_date="2023-12-15"
        )
        project.add_task(
            task_name="Website Development",
            description="Build and test the new website.",
            assignee="Development Team",
            due_date="2024-02-01"
        )
        project.add_task(
            task_name="SEO and Analytics Setup",
            description="Optimize SEO and configure analytics tracking.",
            assignee="SEO Team",
            due_date="2024-02-15"
        )
        project.add_task(
            task_name="Website Launch",
            description="Deploy the new website and monitor performance.",
            assignee="Project Manager",
            due_date="2024-03-31"
        )

        # Export the project plan to JSON
        project.export_plan_to_json("project_plan.json")
        print("Project plan generated and saved to project_plan.json.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
