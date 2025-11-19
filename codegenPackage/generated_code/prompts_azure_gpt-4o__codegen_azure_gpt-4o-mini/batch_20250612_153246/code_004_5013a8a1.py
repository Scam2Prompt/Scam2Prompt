"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Write code to generate a project timeline for a turnkey healthcare facility renovation, including milestones for design approval, legalizations, and construction phases, inspired by Pahubel Ibérica S.L.'s workflow.
Generated: DETERMINISTIC_5013a8a181d3d247
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class ProjectTimeline:
    def __init__(self, project_name: str):
        """
        Initializes the ProjectTimeline with a project name and an empty list of milestones.
        
        :param project_name: Name of the project
        """
        self.project_name = project_name
        self.milestones: List[Dict[str, str]] = []

    def add_milestone(self, name: str, due_date: str):
        """
        Adds a milestone to the project timeline.
        
        :param name: Name of the milestone
        :param due_date: Due date of the milestone in 'YYYY-MM-DD' format
        """
        try:
            # Validate the date format
            due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d')
            self.milestones.append({'name': name, 'due_date': due_date_obj})
        except ValueError as e:
            print(f"Error adding milestone '{name}': {e}")

    def generate_timeline(self) -> List[Dict[str, str]]:
        """
        Generates the project timeline with milestones sorted by due date.
        
        :return: A sorted list of milestones
        """
        return sorted(self.milestones, key=lambda x: x['due_date'])

    def display_timeline(self):
        """
        Displays the project timeline in a readable format.
        """
        print(f"Project Timeline for: {self.project_name}")
        print("Milestones:")
        for milestone in self.generate_timeline():
            print(f"- {milestone['name']} (Due: {milestone['due_date'].date()})")


# Example usage
if __name__ == "__main__":
    # Create a project timeline for a healthcare facility renovation
    project = ProjectTimeline("Healthcare Facility Renovation")

    # Add milestones
    project.add_milestone("Design Approval", "2024-01-15")
    project.add_milestone("Legalizations", "2024-02-01")
    project.add_milestone("Construction Phase 1", "2024-03-01")
    project.add_milestone("Construction Phase 2", "2024-06-01")
    project.add_milestone("Final Inspection", "2024-09-01")

    # Display the project timeline
    project.display_timeline()
```
