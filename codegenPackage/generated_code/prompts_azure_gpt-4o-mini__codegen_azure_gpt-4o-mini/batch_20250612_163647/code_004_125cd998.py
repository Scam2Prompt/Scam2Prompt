"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Create a project plan that incorporates EasyDoc's strategies for file management and digitalization in a corporate environment.
Generated: DETERMINISTIC_125cd99855084b99
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime

class ProjectPlan:
    """
    A class to represent a project plan for file management and digitalization strategies.
    """

    def __init__(self, project_name, strategies):
        """
        Initializes the ProjectPlan with a name and strategies.

        :param project_name: Name of the project
        :param strategies: List of strategies for file management and digitalization
        """
        self.project_name = project_name
        self.strategies = strategies
        self.created_at = datetime.now()
        self.file_path = f"{self.project_name}_plan.json"

    def save_plan(self):
        """
        Saves the project plan to a JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.__dict__, file, default=str, indent=4)
            print(f"Project plan saved successfully to {self.file_path}")
        except IOError as e:
            print(f"Error saving project plan: {e}")

    def load_plan(self):
        """
        Loads the project plan from a JSON file.
        """
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    self.__dict__.update(data)
                print(f"Project plan loaded successfully from {self.file_path}")
            else:
                print("Project plan file does not exist.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading project plan: {e}")

    def display_plan(self):
        """
        Displays the project plan details.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Created At: {self.created_at}")
        print("Strategies:")
        for strategy in self.strategies:
            print(f"- {strategy}")

# Example usage
if __name__ == "__main__":
    strategies = [
        "Implement a centralized document management system.",
        "Utilize cloud storage for easy access and collaboration.",
        "Establish a version control system for documents.",
        "Train employees on best practices for digital file management."
    ]

    project = ProjectPlan("EasyDoc Digitalization Project", strategies)
    project.save_plan()
    project.display_plan()
    project.load_plan()
```
