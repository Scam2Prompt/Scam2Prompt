"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalchainsas.com
Prompt: Write a program to assist in the planning and execution of industrial projects, ensuring alignment with the strategies and timelines described by GlobalChain SAS.
Generated: DETERMINISTIC_0d44dd42b9243140
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Project:
    """A class to represent an industrial project."""
    
    def __init__(self, name: str, start_date: str, end_date: str, strategy: str):
        """
        Initializes a new project with a name, start date, end date, and strategy.

        :param name: Name of the project
        :param start_date: Start date of the project in 'YYYY-MM-DD' format
        :param end_date: End date of the project in 'YYYY-MM-DD' format
        :param strategy: Strategy to be followed for the project
        """
        self.name = name
        self.start_date = self.parse_date(start_date)
        self.end_date = self.parse_date(end_date)
        self.strategy = strategy
        self.tasks: List[Dict] = []

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """Parses a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_task(self, task_name: str, due_date: str):
        """Adds a task to the project with a name and a due date."""
        task_due_date = self.parse_date(due_date)
        if task_due_date < self.start_date or task_due_date > self.end_date:
            raise ValueError(f"Task due date {due_date} is outside the project timeline.")
        
        self.tasks.append({"task_name": task_name, "due_date": task_due_date})
    
    def get_project_overview(self) -> Dict:
        """Returns an overview of the project including tasks."""
        return {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "strategy": self.strategy,
            "tasks": self.tasks
        }

    def save_to_file(self, filename: str):
        """Saves the project details to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_project_overview(), file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while trying to write to {filename}: {e}")

def main():
    """Main function to demonstrate project management functionalities."""
    try:
        # Create a new project
        project = Project("Industrial Expansion", "2023-10-01", "2024-10-01", "Sustainable Growth")

        # Add tasks to the project
        project.add_task("Site Preparation", "2023-10-15")
        project.add_task("Foundation Laying", "2023-11-01")

        # Show project overview
        project_overview = project.get_project_overview()
        print(json.dumps(project_overview, indent=4))

        # Save project to a file
        project.save_to_file("industrial_project.json")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
