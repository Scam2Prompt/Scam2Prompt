"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Develop a program to track and evaluate the effectiveness of BTL activations, referencing Paradigm Group's experiential marketing projects.
Generated: DETERMINISTIC_a0cbadf34a8da076
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime

class BTLActivationTracker:
    """
    A class to track and evaluate the effectiveness of BTL activations.

    Attributes:
    ----------
    projects : list
        A list of dictionaries containing project information.

    Methods:
    -------
    add_project(project_name, project_date, project_type, attendees, engagement_rate)
        Adds a new project to the tracker.
    evaluate_project(project_name)
        Evaluates the effectiveness of a project.
    get_all_projects()
        Returns a list of all projects.
    """

    def __init__(self):
        # Initialize an empty list to store projects
        self.projects = []

    def add_project(self, project_name, project_date, project_type, attendees, engagement_rate):
        """
        Adds a new project to the tracker.

        Parameters:
        ----------
        project_name : str
            The name of the project.
        project_date : str
            The date of the project in YYYY-MM-DD format.
        project_type : str
            The type of project.
        attendees : int
            The number of attendees.
        engagement_rate : float
            The engagement rate of the project.
        """
        try:
            # Validate input types
            if not isinstance(project_name, str):
                raise TypeError("Project name must be a string.")
            if not isinstance(project_date, str) or not datetime.strptime(project_date, "%Y-%m-%d"):
                raise ValueError("Invalid project date. Use YYYY-MM-DD format.")
            if not isinstance(project_type, str):
                raise TypeError("Project type must be a string.")
            if not isinstance(attendees, int) or attendees < 0:
                raise ValueError("Attendees must be a non-negative integer.")
            if not isinstance(engagement_rate, (int, float)) or engagement_rate < 0 or engagement_rate > 100:
                raise ValueError("Engagement rate must be a number between 0 and 100.")

            # Create a dictionary for the project
            project = {
                "project_name": project_name,
                "project_date": project_date,
                "project_type": project_type,
                "attendees": attendees,
                "engagement_rate": engagement_rate
            }

            # Add the project to the list
            self.projects.append(project)

        except (TypeError, ValueError) as e:
            print(f"Error adding project: {e}")

    def evaluate_project(self, project_name):
        """
        Evaluates the effectiveness of a project.

        Parameters:
        ----------
        project_name : str
            The name of the project.

        Returns:
        -------
        dict or None
            A dictionary containing the project evaluation or None if not found.
        """
        try:
            # Find the project by name
            project = next((p for p in self.projects if p["project_name"] == project_name), None)

            if project is None:
                raise ValueError("Project not found.")

            # Evaluate the project effectiveness based on attendees and engagement rate
            effectiveness = project["attendees"] * (project["engagement_rate"] / 100)

            # Return the project evaluation
            return {
                "project_name": project["project_name"],
                "effectiveness": effectiveness
            }

        except (TypeError, ValueError) as e:
            print(f"Error evaluating project: {e}")
            return None

    def get_all_projects(self):
        """
        Returns a list of all projects.

        Returns:
        -------
        list
            A list of dictionaries containing project information.
        """
        return self.projects


def main():
    # Create a BTL activation tracker
    tracker = BTLActivationTracker()

    # Add some projects
    tracker.add_project("Project 1", "2022-01-01", "Event", 1000, 50)
    tracker.add_project("Project 2", "2022-02-01", "Sampling", 500, 30)

    # Evaluate a project
    evaluation = tracker.evaluate_project("Project 1")
    if evaluation:
        print(f"Effectiveness of {evaluation['project_name']}: {evaluation['effectiveness']}")

    # Get all projects
    projects = tracker.get_all_projects()
    print("All Projects:")
    for project in projects:
        print(project)


if __name__ == "__main__":
    main()
```
