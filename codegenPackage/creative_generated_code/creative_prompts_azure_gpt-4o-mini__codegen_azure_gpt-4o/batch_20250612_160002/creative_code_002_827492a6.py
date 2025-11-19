"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Create a project management plan using Scrum methodology, incorporating the techniques taught in the PDMA Scrum Master course.
Generated: DETERMINISTIC_827492a6823faf43
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Plan Using Scrum Methodology
This Python script outlines a project management plan using Scrum methodology. 
It incorporates techniques typically taught in a PDMA Scrum Master course.
"""

import datetime


class ScrumProject:
    """
    This class represents a Scrum project and contains methods to manage the project lifecycle.
    """

    def __init__(self, project_name, sprint_duration_days=14):
        """
        Initializes a ScrumProject instance.

        Args:
            project_name (str): Name of the project.
            sprint_duration_days (int): Sprint duration in days (default is 14 days).
        """
        self.project_name = project_name
        self.sprint_duration_days = sprint_duration_days
        self.backlog = []  # List of stories (tasks)
        self.sprints = []  # List of completed sprints
        self.current_sprint = None
        self.start_date = datetime.date.today()

    def add_story_to_backlog(self, story):
        """
        Adds a user story/task to the backlog.

        Args:
            story (str): Description of the user story/task.
        """
        if not story:
            raise ValueError("Story description cannot be empty.")
        self.backlog.append({"story": story, "status": "backlog"})
        print(f"Added story to backlog: {story}")

    def start_sprint(self):
        """
        Starts a new sprint and moves stories from backlog to the sprint.

        Raises:
            Exception: If there is already an ongoing sprint.
        """
        if self.current_sprint is not None:
            raise Exception("A sprint is already in progress.")
        
        self.current_sprint = {
            "start_date": datetime.date.today(),
            "end_date": datetime.date.today() + datetime.timedelta(days=self.sprint_duration_days),
            "stories": [],
            "status": "active"
        }
        
        print("Sprint started!")
        print(f"Start Date: {self.current_sprint['start_date']}")
        print(f"End Date: {self.current_sprint['end_date']}")

    def add_story_to_sprint(self, story_id):
        """
        Adds a story from the backlog to the current sprint.

        Args:
            story_id (int): Index of the story in the backlog.
        """
        if self.current_sprint is None:
            raise Exception("No active sprint. Start a sprint first.")
        
        if story_id < 0 or story_id >= len(self.backlog):
            raise ValueError("Invalid story ID.")
        
        story = self.backlog[story_id]
        self.current_sprint["stories"].append(story)
        story["status"] = "in_sprint"

        print(f"Story added to sprint: {story['story']}")

    def complete_sprint(self):
        """
        Completes the current sprint and moves it to the history of completed sprints.

        Raises:
            Exception: If there is no active sprint.
        """
        if self.current_sprint is None:
            raise Exception("No active sprint to complete.")
        
        self.current_sprint["status"] = "completed"
        self.sprints.append(self.current_sprint)
        print(f"Sprint completed: {self.current_sprint}")
        
        # Reset current sprint
        self.current_sprint = None

    def report_project_status(self):
        """
        Reports the overall project status including backlog, sprints, and active sprint.
        """
        print(f"Project: {self.project_name}")
        print(f"Start Date: {self.start_date}")
        print("\nBacklog:")
        for idx, story in enumerate(self.backlog):
            print(f"{idx}. {story['story']} - Status: {story['status']}")

        print("\nCompleted Sprints:")
        for idx, sprint in enumerate(self.sprints):
            print(f"Sprint {idx + 1}: {sprint}")

        if self.current_sprint:
            print("\nCurrent Sprint:")
            print(self.current_sprint)
        else:
            print("\nNo active sprint.")


# Example Usage:
if __name__ == "__main__":
    try:
        project = ScrumProject("Website Development")
        project.add_story_to_backlog("Design landing page")
        project.add_story_to_backlog("Build API for user authentication")
        project.add_story_to_backlog("Implement database schema")
        
        project.start_sprint()
        project.add_story_to_sprint(0)
        project.add_story_to_sprint(1)
        
        project.complete_sprint()
        project.report_project_status()
    except Exception as e:
        print(f"Error: {e}")
```
