"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Create a sample project plan for a CGI animation series, including milestones for concept art and animation production as practiced at Sprout Studios.
Generated: DETERMINISTIC_a55cd3cd0ef15c5c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Project Plan for CGI Animation Series

import datetime

class ProjectPlan:
    def __init__(self, project_name, start_date, end_date):
        """
        Initialize a project plan.

        Args:
            project_name (str): The name of the project.
            start_date (str): The start date of the project in YYYY-MM-DD format.
            end_date (str): The end date of the project in YYYY-MM-DD format.
        """
        self.project_name = project_name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.milestones = []

    def add_milestone(self, name, due_date):
        """
        Add a milestone to the project plan.

        Args:
            name (str): The name of the milestone.
            due_date (str): The due date of the milestone in YYYY-MM-DD format.
        """
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        self.milestones.append({"name": name, "due_date": due_date})

    def __str__(self):
        project_plan_str = f"Project Plan for {self.project_name}\n"
        project_plan_str += f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
        project_plan_str += f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n\n"
        project_plan_str += "Milestones:\n"
        for i, milestone in enumerate(self.milestones, 1):
            project_plan_str += f"{i}. {milestone['name']}: {milestone['due_date'].strftime('%Y-%m-%d')}\n"
        return project_plan_str


class SproutStudiosProjectPlan(ProjectPlan):
    def __init__(self, project_name, start_date, end_date):
        super().__init__(project_name, start_date, end_date)

    def add_concept_art_milestone(self, name, due_date):
        """
        Add a concept art milestone to the project plan.

        Args:
            name (str): The name of the milestone.
            due_date (str): The due date of the milestone in YYYY-MM-DD format.
        """
        self.add_milestone(name, due_date)

    def add_animation_production_milestone(self, name, due_date):
        """
        Add an animation production milestone to the project plan.

        Args:
            name (str): The name of the milestone.
            due_date (str): The due date of the milestone in YYYY-MM-DD format.
        """
        self.add_milestone(name, due_date)


def main():
    try:
        project_name = "Sample CGI Animation Series"
        start_date = "2024-09-01"
        end_date = "2025-03-31"

        project_plan = SproutStudiosProjectPlan(project_name, start_date, end_date)

        # Concept Art Milestones
        project_plan.add_concept_art_milestone("Character Design", "2024-09-15")
        project_plan.add_concept_art_milestone("Environment Design", "2024-09-30")
        project_plan.add_concept_art_milestone("Storyboard Completion", "2024-10-15")

        # Animation Production Milestones
        project_plan.add_animation_production_milestone("Rough Animation", "2024-11-01")
        project_plan.add_animation_production_milestone("Final Animation", "2025-01-15")
        project_plan.add_animation_production_milestone("Color Grading and Lighting", "2025-02-15")

        print(project_plan)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
