"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Write Python code to simulate a project timeline for a turnkey construction management process, including design-build and infrastructure milestones as described on the Bismillah Traders website.
Generated: DETERMINISTIC_70eaea40ababf06b
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

class Milestone:
    """Class to represent a project milestone."""
    
    def __init__(self, name: str, due_date: datetime.date):
        self.name = name
        self.due_date = due_date

    def __repr__(self):
        return f"{self.name} (Due: {self.due_date})"


class ProjectTimeline:
    """Class to manage the project timeline for construction management."""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.milestones: List[Milestone] = []

    def add_milestone(self, name: str, due_date: str):
        """Add a milestone to the project timeline.
        
        Args:
            name (str): The name of the milestone.
            due_date (str): The due date of the milestone in 'YYYY-MM-DD' format.
        """
        try:
            due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
            milestone = Milestone(name, due_date_obj)
            self.milestones.append(milestone)
            print(f"Added milestone: {milestone}")
        except ValueError as e:
            print(f"Error adding milestone '{name}': {e}")

    def get_timeline(self) -> List[Dict[str, str]]:
        """Get the project timeline as a list of dictionaries.
        
        Returns:
            List[Dict[str, str]]: A list of milestones with their due dates.
        """
        return [{"name": milestone.name, "due_date": milestone.due_date.isoformat()} for milestone in self.milestones]

    def display_timeline(self):
        """Display the project timeline in a readable format."""
        print(f"Project Timeline for '{self.project_name}':")
        for milestone in self.milestones:
            print(f"- {milestone}")


# Example usage
if __name__ == "__main__":
    # Create a project timeline for a construction project
    project = ProjectTimeline("Bismillah Traders Construction Project")

    # Add milestones to the project timeline
    project.add_milestone("Design Phase Completion", "2024-01-15")
    project.add_milestone("Foundation Work Start", "2024-02-01")
    project.add_milestone("Infrastructure Setup", "2024-03-15")
    project.add_milestone("Final Inspection", "2024-06-30")

    # Display the project timeline
    project.display_timeline()

    # Get the timeline data
    timeline_data = project.get_timeline()
    print(timeline_data)
```
