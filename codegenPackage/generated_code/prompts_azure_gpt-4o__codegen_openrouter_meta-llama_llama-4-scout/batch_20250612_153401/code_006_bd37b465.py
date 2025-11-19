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
# project_report_generator.py

import json
from datetime import datetime

class ProjectReport:
    def __init__(self, client_name, location, project_milestones):
        """
        Initialize a ProjectReport object.

        Args:
            client_name (str): The name of the client.
            location (str): The location of the project.
            project_milestones (list): A list of project milestones.
        """
        self.client_name = client_name
        self.location = location
        self.project_milestones = project_milestones

    def generate_report(self):
        """
        Generate a project report.

        Returns:
            str: A formatted project report.
        """
        report = f"Project Report for {self.client_name} at {self.location}\n"
        report += "-----------------------------------------------\n"
        report += "Project Milestones:\n"

        for milestone in self.project_milestones:
            report += f"- {milestone['name']}: {milestone['due_date']}\n"

        return report


class ProjectReportGenerator:
    def __init__(self, project_descriptions):
        """
        Initialize a ProjectReportGenerator object.

        Args:
            project_descriptions (list): A list of project descriptions.
        """
        self.project_descriptions = project_descriptions

    def generate_reports(self):
        """
        Generate project reports for a list of project descriptions.

        Returns:
            list: A list of project reports.
        """
        reports = []

        for project_description in self.project_descriptions:
            try:
                client_name = project_description['client_name']
                location = project_description['location']
                project_milestones = project_description['project_milestones']

                project_report = ProjectReport(client_name, location, project_milestones)
                report = project_report.generate_report()

                reports.append(report)
            except KeyError as e:
                print(f"Error: Missing key {e} in project description.")
            except Exception as e:
                print(f"An error occurred: {e}")

        return reports


def load_project_descriptions(file_path):
    """
    Load project descriptions from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of project descriptions.
    """
    try:
        with open(file_path, 'r') as file:
            project_descriptions = json.load(file)
            return project_descriptions
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return []


def save_reports_to_file(reports, file_path):
    """
    Save project reports to a text file.

    Args:
        reports (list): A list of project reports.
        file_path (str): The path to the output file.
    """
    try:
        with open(file_path, 'w') as file:
            for report in reports:
                file.write(report + "\n\n")
        print(f"Reports saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    project_descriptions_file = 'project_descriptions.json'
    output_file = 'project_reports.txt'

    project_descriptions = load_project_descriptions(project_descriptions_file)

    generator = ProjectReportGenerator(project_descriptions)
    reports = generator.generate_reports()

    save_reports_to_file(reports, output_file)


if __name__ == "__main__":
    main()
```

```json
// project_descriptions.json

[
  {
    "client_name": "Client A",
    "location": "New York",
    "project_milestones": [
      {"name": "Milestone 1", "due_date": "2024-01-01"},
      {"name": "Milestone 2", "due_date": "2024-06-01"}
    ]
  },
  {
    "client_name": "Client B",
    "location": "Los Angeles",
    "project_milestones": [
      {"name": "Milestone 3", "due_date": "2024-03-01"},
      {"name": "Milestone 4", "due_date": "2024-09-01"}
    ]
  }
]
```
