"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Develop a roadmap tracker for a launchpad platform, incorporating BlastUP's milestones such as EasyLaunch, AI IDO Helper, and Learn-to-Earn programs.
Generated: DETERMINISTIC_e0508bb81823ade7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class Milestone:
    """Class to represent a milestone in the roadmap tracker."""
    
    def __init__(self, name: str, description: str, due_date: str, completed: bool = False):
        """
        Initialize a new milestone.

        :param name: Name of the milestone
        :param description: Detailed description of the milestone
        :param due_date: Due date for the milestone (format: 'YYYY-MM-DD')
        :param completed: Status of the milestone, default is False
        """
        self.name = name
        self.description = description
        self.due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
        self.completed = completed

    def mark_completed(self):
        """Mark the milestone as completed."""
        self.completed = True

    def is_overdue(self) -> bool:
        """Check if the milestone is overdue."""
        return datetime.date.today() > self.due_date and not self.completed
    
    def __repr__(self) -> str:
        """Represent the milestone as a string."""
        return f"Milestone(name='{self.name}', due_date='{self.due_date}', completed={self.completed})"


class RoadmapTracker:
    """Class to manage the roadmap milestones."""
    
    def __init__(self):
        """Initialize the roadmap tracker with an empty milestone list."""
        self.milestones: List[Milestone] = []

    def add_milestone(self, name: str, description: str, due_date: str):
        """
        Add a new milestone to the tracker.

        :param name: Name of the milestone
        :param description: Description of the milestone
        :param due_date: Due date for the milestone (format: 'YYYY-MM-DD')
        """
        try:
            new_milestone = Milestone(name, description, due_date)
            self.milestones.append(new_milestone)
        except ValueError as e:
            print(f"Error adding milestone: {e}")

    def complete_milestone(self, name: str):
        """
        Mark a milestone as completed by its name.

        :param name: Name of the milestone to mark as completed
        """
        for milestone in self.milestones:
            if milestone.name == name:
                milestone.mark_completed()
                return
        print(f"Milestone '{name}' not found.")

    def get_overdue_milestones(self) -> List[Milestone]:
        """Retrieve a list of overdue milestones."""
        return [m for m in self.milestones if m.is_overdue()]

    def display_roadmap(self) -> None:
        """Display all milestones in the roadmap."""
        if not self.milestones:
            print("No milestones in the roadmap.")
            return
        
        print("Roadmap Milestones:")
        for milestone in self.milestones:
            status = 'Completed' if milestone.completed else 'Pending'
            print(f"- {milestone.name} (Due: {milestone.due_date}, Status: {status})")


if __name__ == "__main__":
    # Initialize the roadmap tracker
    roadmap = RoadmapTracker()
    
    # Adding milestones specific to BlastUP's roadmap
    roadmap.add_milestone("EasyLaunch", "Launchpad for easy project launches.", "2024-01-15")
    roadmap.add_milestone("AI IDO Helper", "AI-driven tool for Initial DEX Offerings.", "2024-03-30")
    roadmap.add_milestone("Learn-to-Earn", "Educational program for participants.", "2024-05-20")
    
    # Display the current roadmap
    roadmap.display_roadmap()
    
    # Example of completing a milestone
    roadmap.complete_milestone("EasyLaunch")
    
    # Display overdue milestones
    overdue_milestones = roadmap.get_overdue_milestones()
    if overdue_milestones:
        print("Overdue Milestones:")
        for m in overdue_milestones:
            print(f"- {m.name} (Due: {m.due_date})")
    else:
        print("No overdue milestones.")
```
