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
# Python script to generate a sample project plan for a CGI animation series
# Project milestones include concept art and animation production 
# This script summarizes the project plan using Python's built-in data structures

import json

class ProjectPlan:
    """
    Represents a project plan for a CGI animation series.
    Includes milestones, deadlines, and deliverables.
    """

    def __init__(self, project_name, studio_name, start_date, end_date):
        """
        Initialize the project plan with basic details.

        :param project_name: Name of the animation series
        :param studio_name: Name of the animation studio
        :param start_date: Project start date (YYYY-MM-DD format)
        :param end_date: Project end date (YYYY-MM-DD format)
        """
        self.project_name = project_name
        self.studio_name = studio_name
        self.start_date = start_date
        self.end_date = end_date
        self.milestones = []

    def add_milestone(self, milestone_name, due_date, description):
        """
        Add a milestone to the project plan.

        :param milestone_name: Name of the milestone
        :param due_date: Due date of the milestone (YYYY-MM-DD format)
        :param description: Details about the milestone
        """
        milestone = {
            "milestone_name": milestone_name,
            "due_date": due_date,
            "description": description
        }
        self.milestones.append(milestone)

    def generate_plan(self):
        """
        Generate the complete project plan.

        :return: JSON representation of the project plan
        """
        project_plan = {
            "project_name": self.project_name,
            "studio_name": self.studio_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "milestones": self.milestones
        }
        return json.dumps(project_plan, indent=4)

# Error handling example
def validate_date(date_string):
    """
    Validate that a given date string is in the correct format.

    :param date_string: Date string to validate (YYYY-MM-DD format)
    :return: True if valid, False otherwise
    """
    try:
        year, month, day = map(int, date_string.split('-'))
        assert 1 <= month <= 12
        assert 1 <= day <= 31
        return True
    except (ValueError, AssertionError):
        return False


# Main script to create and display the project plan
if __name__ == "__main__":
    # Define project details
    project_name = "Mystic Adventures"
    studio_name = "Sprout Studios"
    start_date = "2024-01-01"
    end_date = "2025-12-31"

    # Validate project dates
    if not validate_date(start_date) or not validate_date(end_date):
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        exit(1)

    # Create a project plan
    plan = ProjectPlan(project_name, studio_name, start_date, end_date)

    # Add milestones
    plan.add_milestone("Concept Art Completion", "2024-03-01", "All concept art for characters and environments finalized.")
    plan.add_milestone("Storyboarding Completion", "2024-06-01", "Storyboard for all episodes created and approved.")
    plan.add_milestone("Animation Production Start", "2024-07-01", "Begin production of CGI animation.")
    plan.add_milestone("First Episode Completion", "2025-01-01", "Complete animation and post-production for the first episode.")
    plan.add_milestone("Series Completion", "2025-12-01", "Finalize animation, post-production, and sound design for all episodes.")

    # Generate and display the project plan
    project_plan_json = plan.generate_plan()
    print("Generated Project Plan:")
    print(project_plan_json)
```
