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
import datetime
from typing import List, Dict, Any

class Sprint:
    def __init__(self, sprint_number: int, duration_days: int):
        """
        Initialize a Sprint with a number and duration.
        
        :param sprint_number: The number of the sprint.
        :param duration_days: The duration of the sprint in days.
        """
        self.sprint_number = sprint_number
        self.start_date = datetime.date.today() + datetime.timedelta(days=(sprint_number - 1) * duration_days)
        self.end_date = self.start_date + datetime.timedelta(days=duration_days)
        self.backlog_items = []

    def add_backlog_item(self, item: Dict[str, Any]):
        """
        Add a backlog item to the sprint.
        
        :param item: A dictionary representing a backlog item.
        """
        self.backlog_items.append(item)

    def __str__(self):
        return f"Sprint {self.sprint_number}: {self.start_date} to {self.end_date}, Backlog Items: {len(self.backlog_items)}"


class ProductBacklog:
    def __init__(self):
        """
        Initialize an empty Product Backlog.
        """
        self.items = []

    def add_item(self, item: Dict[str, Any]):
        """
        Add an item to the product backlog.
        
        :param item: A dictionary representing a backlog item.
        """
        self.items.append(item)

    def get_items(self) -> List[Dict[str, Any]]:
        """
        Retrieve all items in the product backlog.
        
        :return: A list of backlog items.
        """
        return self.items


class ScrumProject:
    def __init__(self, project_name: str, sprint_duration: int, total_sprints: int):
        """
        Initialize a Scrum Project with a name, sprint duration, and total sprints.
        
        :param project_name: The name of the project.
        :param sprint_duration: The duration of each sprint in days.
        :param total_sprints: The total number of sprints planned.
        """
        self.project_name = project_name
        self.sprint_duration = sprint_duration
        self.total_sprints = total_sprints
        self.sprints = []
        self.backlog = ProductBacklog()

        # Create sprints based on the total number of sprints
        for i in range(1, total_sprints + 1):
            self.sprints.append(Sprint(i, sprint_duration))

    def add_backlog_item(self, item: Dict[str, Any]):
        """
        Add a backlog item to the product backlog.
        
        :param item: A dictionary representing a backlog item.
        """
        self.backlog.add_item(item)

    def assign_backlog_to_sprint(self, sprint_number: int):
        """
        Assign backlog items to a specific sprint.
        
        :param sprint_number: The number of the sprint to assign items to.
        """
        if sprint_number < 1 or sprint_number > self.total_sprints:
            raise ValueError("Sprint number out of range.")
        
        sprint = self.sprints[sprint_number - 1]
        for item in self.backlog.get_items():
            sprint.add_backlog_item(item)

    def __str__(self):
        return f"Project: {self.project_name}, Total Sprints: {self.total_sprints}"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a Scrum project
        project = ScrumProject("New Product Launch", sprint_duration=14, total_sprints=3)

        # Add backlog items
        project.add_backlog_item({"id": 1, "description": "Define product vision"})
        project.add_backlog_item({"id": 2, "description": "Create user stories"})
        project.add_backlog_item({"id": 3, "description": "Develop MVP"})

        # Assign backlog items to the first sprint
        project.assign_backlog_to_sprint(1)

        # Print project details
        print(project)
        for sprint in project.sprints:
            print(sprint)

    except Exception as e:
        print(f"An error occurred: {e}")
```
