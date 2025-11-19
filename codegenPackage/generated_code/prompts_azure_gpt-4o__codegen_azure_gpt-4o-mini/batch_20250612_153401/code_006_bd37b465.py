"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Generate code to automate the generation of project reports for construction projects, including details like client name, location, and project milestones, based on the project descriptions provided by INARO S.A.S.
Generated: DETERMINISTIC_bd37b4650c26514f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class ProjectReportGenerator:
    """
    A class to generate project reports for construction projects.
    """

    def __init__(self, project_data_file):
        """
        Initializes the ProjectReportGenerator with the path to the project data file.

        :param project_data_file: Path to the JSON file containing project descriptions.
        """
        self.project_data_file = project_data_file
        self.projects = self.load_project_data()

    def load_project_data(self):
        """
        Loads project data from a JSON file.

        :return: A list of project dictionaries.
        """
        if not os.path.exists(self.project_data_file):
            raise FileNotFoundError(f"Project data file not found: {self.project_data_file}")

        with open(self.project_data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")

    def generate_report(self, project):
        """
        Generates a report for a single project.

        :param project: A dictionary containing project details.
        :return: A formatted string report for the project.
        """
        report = (
            f"Project Report\n"
            f"====================\n"
            f"Client Name: {project.get('client_name', 'N/A')}\n"
            f"Location: {project.get('location', 'N/A')}\n"
            f"Start Date: {project.get('start_date', 'N/A')}\n"
            f"End Date: {project.get('end_date', 'N/A')}\n"
            f"Milestones:\n"
        )

        milestones = project.get('milestones', [])
        for milestone in milestones:
            report += f" - {milestone.get('name', 'N/A')} (Due: {milestone.get('due_date', 'N/A')})\n"

        report += "====================\n"
        return report

    def save_report(self, report, project_name):
        """
        Saves the generated report to a text file.

        :param report: The report string to save.
        :param project_name: The name of the project for the filename.
        """
        filename = f"{project_name.replace(' ', '_')}_report.txt"
        with open(filename, 'w') as file:
            file.write(report)
        print(f"Report saved as: {filename}")

    def generate_reports(self):
        """
        Generates reports for all projects and saves them to text files.
        """
        for project in self.projects:
            try:
                report = self.generate_report(project)
                self.save_report(report, project.get('client_name', 'Unnamed Project'))
            except Exception as e:
                print(f"Error generating report for project {project.get('client_name', 'Unnamed Project')}: {e}")

if __name__ == "__main__":
    # Path to the JSON file containing project descriptions
    project_data_file = 'projects.json'

    # Create an instance of the report generator
    report_generator = ProjectReportGenerator(project_data_file)

    # Generate and save reports for all projects
    report_generator.generate_reports()
```

**Note:** Ensure that the `projects.json` file exists in the same directory as this script and contains valid JSON data structured appropriately for the project details.
