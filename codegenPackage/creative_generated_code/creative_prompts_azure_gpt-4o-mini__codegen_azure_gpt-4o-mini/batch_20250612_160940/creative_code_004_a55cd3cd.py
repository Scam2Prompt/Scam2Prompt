"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutstudios.in
Prompt: Create a sample project plan for a CGI animation series, including milestones for concept art and animation production as practiced at Sprout Studios.
Generated: DETERMINISTIC_a55cd3cd0ef15c5c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ProjectMilestone:
    """
    A class to represent a milestone in the CGI animation project.
    """
    
    def __init__(self, name, due_date, description):
        """
        Initializes a new milestone with a name, due date, and description.
        
        :param name: The name of the milestone
        :param due_date: The due date for the milestone (datetime.date)
        :param description: A brief description of the milestone
        """
        self.name = name
        self.due_date = due_date
        self.description = description
        self.completed = False

    def complete_milestone(self):
        """Mark the milestone as completed."""
        self.completed = True

    def __str__(self):
        """Return a string representation of the milestone."""
        return f"{self.name} - Due: {self.due_date} - Completed: {self.completed}"


class ProjectPlan:
    """
    A class to manage the project plan for a CGI animation series.
    """

    def __init__(self, title):
        """
        Initializes a project plan with a title and an empty list of milestones.
        
        :param title: The title of the CGI animation project
        """
        self.title = title
        self.milestones = []

    def add_milestone(self, milestone):
        """
        Adds a milestone to the project plan.
        
        :param milestone: An instance of ProjectMilestone
        """
        if not isinstance(milestone, ProjectMilestone):
            raise ValueError("milestone must be an instance of ProjectMilestone")
        self.milestones.append(milestone)

    def show_milestones(self):
        """Display all milestones in the project plan."""
        for milestone in self.milestones:
            print(milestone)

    def get_due_milestones(self):
        """
        Returns a list of milestones that are due or overdue.
        
        :return: List of due milestones
        """
        today = datetime.date.today()
        return [milestone for milestone in self.milestones if milestone.due_date <= today and not milestone.completed]


# Example usage of the ProjectPlan class
if __name__ == "__main__":
    # Create a project plan for a CGI animation series
    project = ProjectPlan("Fantastic Adventures")

    # Define some milestones
    milestones = [
        ProjectMilestone("Concept Art", datetime.date(2024, 1, 15), "Complete concept art for main characters and settings."),
        ProjectMilestone("Storyboarding", datetime.date(2024, 2, 15), "Finish storyboarding for the first episode."),
        ProjectMilestone("Animation Production", datetime.date(2024, 4, 30), "Begin animation production for Episode 1."),
        ProjectMilestone("Final Edits", datetime.date(2024, 5, 15), "Complete final edits and sound mixing."),
    ]

    # Add milestones to the project plan
    for milestone in milestones:
        project.add_milestone(milestone)

    # Show all milestones
    print("Project Milestones:")
    project.show_milestones()

    # Check for due milestones
    due_milestones = project.get_due_milestones()
    if due_milestones:
        print("\nDue or Overdue Milestones:")
        for milestone in due_milestones:
            print(milestone)
    else:
        print("\nNo due or overdue milestones.")
```
