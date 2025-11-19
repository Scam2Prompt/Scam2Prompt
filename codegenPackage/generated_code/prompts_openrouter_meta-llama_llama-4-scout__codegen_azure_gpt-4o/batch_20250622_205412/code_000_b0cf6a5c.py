"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a Python script to manage safety and health coordination for construction projects, including risk assessment and mitigation strategies, inspired by the AFCO's guidelines.
Generated: DETERMINISTIC_b0cf6a5cdaff53c0
Batch ID: 20250622_205412
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

class SafetyAndHealthManager:
    """
    A class to manage safety and health coordination for construction projects.
    Includes risk assessment and mitigation strategies inspired by AFCO's guidelines.
    """

    def __init__(self):
        """
        Initializes the SafetyAndHealthManager with an empty list of projects.
        """
        self.projects = []

    def add_project(self, name, start_date, end_date):
        """
        Adds a new construction project to the manager.

        Args:
            name (str): Name of the project.
            start_date (str): Start date of the project in YYYY-MM-DD format.
            end_date (str): End date of the project in YYYY-MM-DD format.
        """
        try:
            # Validate date format
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            if end_date <= start_date:
                raise ValueError("End date must be after start date.")

            project = {
                "name": name,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "risks": [],
                "mitigation_strategies": []
            }
            self.projects.append(project)
            print(f"Project '{name}' added successfully.")
        except ValueError as e:
            print(f"Error adding project: {e}")

    def add_risk(self, project_name, risk_description, severity):
        """
        Adds a risk to a specific project.

        Args:
            project_name (str): Name of the project.
            risk_description (str): Description of the risk.
            severity (str): Severity of the risk (e.g., 'Low', 'Medium', 'High').
        """
        project = self._find_project(project_name)
        if project:
            risk = {
                "description": risk_description,
                "severity": severity
            }
            project["risks"].append(risk)
            print(f"Risk added to project '{project_name}'.")
        else:
            print(f"Project '{project_name}' not found.")

    def add_mitigation_strategy(self, project_name, strategy_description):
        """
        Adds a mitigation strategy to a specific project.

        Args:
            project_name (str): Name of the project.
            strategy_description (str): Description of the mitigation strategy.
        """
        project = self._find_project(project_name)
        if project:
            project["mitigation_strategies"].append(strategy_description)
            print(f"Mitigation strategy added to project '{project_name}'.")
        else:
            print(f"Project '{project_name}' not found.")

    def view_project_details(self, project_name):
        """
        Displays the details of a specific project.

        Args:
            project_name (str): Name of the project.
        """
        project = self._find_project(project_name)
        if project:
            print(json.dumps(project, indent=4))
        else:
            print(f"Project '{project_name}' not found.")

    def _find_project(self, project_name):
        """
        Finds a project by name.

        Args:
            project_name (str): Name of the project.

        Returns:
            dict: The project details if found, None otherwise.
        """
        for project in self.projects:
            if project["name"] == project_name:
                return project
        return None

    def save_to_file(self, filename):
        """
        Saves all project data to a JSON file.

        Args:
            filename (str): Name of the file to save the data.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.projects, file, indent=4)
            print(f"Data saved to '{filename}'.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Loads project data from a JSON file.

        Args:
            filename (str): Name of the file to load the data from.
        """
        try:
            with open(filename, "r") as file:
                self.projects = json.load(file)
            print(f"Data loaded from '{filename}'.")
        except IOError as e:
            print(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


# Example usage
if __name__ == "__main__":
    manager = SafetyAndHealthManager()

    # Adding projects
    manager.add_project("Project Alpha", "2023-01-01", "2023-12-31")
    manager.add_project("Project Beta", "2023-06-01", "2023-11-30")

    # Adding risks and mitigation strategies
    manager.add_risk("Project Alpha", "Falling objects", "High")
    manager.add_mitigation_strategy("Project Alpha", "Provide helmets to all workers.")

    manager.add_risk("Project Beta", "Slippery surfaces", "Medium")
    manager.add_mitigation_strategy("Project Beta", "Install anti-slip mats.")

    # Viewing project details
    manager.view_project_details("Project Alpha")

    # Saving and loading data
    manager.save_to_file("projects.json")
    manager.load_from_file("projects.json")
```
