"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: Generate a Python script for automating project management tasks in architecture, such as tracking milestones and generating reports, as described in Études' project management services.
Generated: DETERMINISTIC_32d50de10a92c075
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Any

class Project:
    def __init__(self, name: str, milestones: List[Dict[str, Any]]):
        """
        Initialize a new project with a name and a list of milestones.

        :param name: The name of the project.
        :param milestones: A list of milestones, each represented as a dictionary.
        """
        self.name = name
        self.milestones = milestones

    def add_milestone(self, milestone: Dict[str, Any]) -> None:
        """
        Add a new milestone to the project.

        :param milestone: A dictionary representing the milestone to add.
        """
        self.milestones.append(milestone)

    def generate_report(self) -> str:
        """
        Generate a report of the project's milestones.

        :return: A string representation of the project report.
        """
        report = f"Project: {self.name}\n"
        report += "Milestones:\n"
        for milestone in self.milestones:
            report += f"- {milestone['name']} (Due: {milestone['due_date']}, Status: {milestone['status']})\n"
        return report

    def save_to_file(self, filename: str) -> None:
        """
        Save the project data to a JSON file.

        :param filename: The name of the file to save the project data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    'name': self.name,
                    'milestones': self.milestones
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving project to file: {e}")

    @staticmethod
    def load_from_file(filename: str) -> 'Project':
        """
        Load a project from a JSON file.

        :param filename: The name of the file to load the project data from.
        :return: An instance of Project.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return Project(data['name'], data['milestones'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading project from file: {e}")
            return None

def main():
    # Example usage of the Project class
    milestones = [
        {'name': 'Design Phase', 'due_date': '2023-12-01', 'status': 'In Progress'},
        {'name': 'Construction Phase', 'due_date': '2024-06-01', 'status': 'Pending'},
    ]

    project = Project("New Building Project", milestones)

    # Add a new milestone
    project.add_milestone({'name': 'Final Review', 'due_date': '2024-07-01', 'status': 'Pending'})

    # Generate and print the project report
    report = project.generate_report()
    print(report)

    # Save the project to a file
    project.save_to_file('project_data.json')

    # Load the project from a file
    loaded_project = Project.load_from_file('project_data.json')
    if loaded_project:
        print(loaded_project.generate_report())

if __name__ == "__main__":
    main()
```
