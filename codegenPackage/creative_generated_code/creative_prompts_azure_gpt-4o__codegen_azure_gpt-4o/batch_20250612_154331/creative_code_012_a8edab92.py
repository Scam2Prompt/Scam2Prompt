"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fstq.lol
Prompt: Create a Python script to track FastIQ's "вне блога" (outside the blog) projects and categorize them based on their risk levels and payout histories.
Generated: DETERMINISTIC_a8edab9294a99b66
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to track FastIQ's "вне блога" (outside the blog) projects, categorize them based on risk levels 
and payout histories, and display a summary report.

Author: [Your Name]
Date: [Current Date]
"""

import logging

# Setup logging for debugging and error messages
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("project_tracker.log"),
        logging.StreamHandler()
    ]
)

class Project:
    """
    Represents a FastIQ 'вне блога' project.
    Attributes:
        name (str): Name of the project.
        risk_level (str): Risk level of the project (e.g., Low, Medium, High).
        payout_history (list): List of past payouts (monetary amounts).
    """
    def __init__(self, name, risk_level, payout_history):
        self.name = name
        self.risk_level = risk_level
        self.payout_history = payout_history

    def average_payout(self):
        """
        Calculates the average payout of the project.

        Returns:
            float: Average payout amount. Returns 0 if no payouts exist.
        """
        if not self.payout_history:
            return 0.0
        return sum(self.payout_history) / len(self.payout_history)


class ProjectTracker:
    """
    A class to manage and categorize FastIQ's 'вне блога' projects.
    """
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        """
        Adds a new project to the tracker.

        Args:
            project (Project): The project to add.
        """
        if not isinstance(project, Project):
            raise TypeError("Expected a Project instance.")
        self.projects.append(project)
        logging.info(f"Project '{project.name}' added successfully.")

    def categorize_projects(self):
        """
        Categorizes projects based on their risk levels.

        Returns:
            dict: A dictionary where keys are risk levels and values are lists of project names.
        """
        categories = {}
        for project in self.projects:
            categories.setdefault(project.risk_level, []).append(project.name)
        return categories

    def generate_report(self):
        """
        Generates a summary report of all projects, including their average payouts.

        Returns:
            str: A formatted string report of all projects.
        """
        report = ["FastIQ 'вне блога' Projects Report:\n"]
        for project in self.projects:
            report.append(
                f"Project: {project.name}\n"
                f"  Risk Level: {project.risk_level}\n"
                f"  Average Payout: ${project.average_payout():.2f}\n"
            )
        return "\n".join(report)


def main():
    """
    Main function to execute the project tracker script.
    """
    # Initialize the ProjectTracker
    tracker = ProjectTracker()

    # Example: Adding projects manually (replace with dynamic data input for production use)
    try:
        tracker.add_project(Project("Project Alpha", "Low", [100, 120, 130]))
        tracker.add_project(Project("Project Beta", "High", [50, 60]))
        tracker.add_project(Project("Project Gamma", "Medium", [200, 180, 220]))
    except Exception as e:
        logging.error(f"Error adding project: {str(e)}")
        return

    # Categorize projects
    categories = tracker.categorize_projects()
    logging.info("Project Categorization:")
    for risk_level, projects in categories.items():
        logging.info(f"  {risk_level}: {', '.join(projects)}")

    # Generate and display the report
    report = tracker.generate_report()
    print(report)

if __name__ == "__main__":
    main()
```
