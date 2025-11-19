"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: Write a Python script to manage and monitor a network installation project, inspired by the services provided by Ray-Z Entreprise.
Generated: DETERMINISTIC_aaf6d024af0e0e8a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
import os
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("network_project_manager.log"),
        logging.StreamHandler()
    ]
)

class NetworkInstallationProjectManager:
    """
    Class to manage and monitor a network installation project.
    Inspired by the services provided by Ray-Z Entreprise.
    """

    def __init__(self, project_file="project_data.json"):
        """
        Initialize the project manager instance.

        :param project_file: Path to the file where project data is stored.
        """
        self.project_file = project_file
        self.project_data = self.load_project_data()

    def load_project_data(self):
        """
        Load project data from a file.

        :return: Dictionary containing project data.
        """
        try:
            if os.path.exists(self.project_file):
                with open(self.project_file, "r") as file:
                    return json.load(file)
            else:
                logging.warning(
                    f"Project file '{self.project_file}' does not exist. Starting with empty data."
                )
                return {}
        except json.JSONDecodeError as e:
            logging.error(f"Failed to load project data: {e}")
            return {}

    def save_project_data(self):
        """
        Save current project data to a file.
        """
        try:
            with open(self.project_file, "w") as file:
                json.dump(self.project_data, file, indent=4)
                logging.info("Project data saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save project data: {e}")

    def add_project(self, project_name, description, deadline):
        """
        Add a new network installation project.

        :param project_name: Name of the project.
        :param description: Description of the project.
        :param deadline: Deadline for the project in 'YYYY-MM-DD' format.
        """
        if project_name in self.project_data:
            logging.warning(f"Project '{project_name}' already exists.")
            return

        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            self.project_data[project_name] = {
                "description": description,
                "deadline": deadline,
                "status": "Pending",
                "tasks": []
            }
            logging.info(f"Project '{project_name}' added successfully.")
            self.save_project_data()
        except ValueError as e:
            logging.error(f"Invalid deadline format: {e}")

    def update_project_status(self, project_name, status):
        """
        Update the status of an existing project.

        :param project_name: Name of the project.
        :param status: New status for the project (e.g., "In Progress", "Completed").
        """
        if project_name not in self.project_data:
            logging.warning(f"Project '{project_name}' does not exist.")
            return

        self.project_data[project_name]["status"] = status
        logging.info(f"Project '{project_name}' status updated to '{status}'.")
        self.save_project_data()

    def add_task_to_project(self, project_name, task_description):
        """
        Add a task to an existing project.

        :param project_name: Name of the project.
        :param task_description: Description of the task to be added.
        """
        if project_name not in self.project_data:
            logging.warning(f"Project '{project_name}' does not exist.")
            return

        self.project_data[project_name]["tasks"].append({
            "description": task_description,
            "status": "Pending"
        })
        logging.info(f"Task added to project '{project_name}'.")
        self.save_project_data()

    def update_task_status(self, project_name, task_index, status):
        """
        Update the status of a specific task in a project.

        :param project_name: Name of the project.
        :param task_index: Index of the task in the task list.
        :param status: New status for the task (e.g., "In Progress", "Completed").
        """
        if project_name not in self.project_data:
            logging.warning(f"Project '{project_name}' does not exist.")
            return

        try:
            self.project_data[project_name]["tasks"][task_index]["status"] = status
            logging.info(
                f"Task index {task_index} in project '{project_name}' updated to '{status}'."
            )
            self.save_project_data()
        except IndexError:
            logging.error(
                f"Invalid task index '{task_index}' for project '{project_name}'."
            )

    def generate_report(self):
        """
        Generate a summary report of all projects.

        :return: String containing the report.
        """
        report = "Network Installation Project Report:\n"
        report += "=" * 50 + "\n"

        for project_name, details in self.project_data.items():
            report += f"Project Name: {project_name}\n"
            report += f"Description: {details['description']}\n"
            report += f"Deadline: {details['deadline']}\n"
            report += f"Status: {details['status']}\n"
            report += "Tasks:\n"
            for idx, task in enumerate(details["tasks"]):
                report += f"  {idx + 1}. {task['description']} - {task['status']}\n"
            report += "-" * 50 + "\n"

        logging.info("Report generated successfully.")
        return report

# Main script functionality
if __name__ == "__main__":
    manager = NetworkInstallationProjectManager()

    # Example usage:
    manager.add_project("Office Network Setup", "Setup LAN and Wi-Fi for office.", "2023-12-01")
    manager.add_task_to_project("Office Network Setup", "Install routers.")
    manager.add_task_to_project("Office Network Setup", "Configure firewall.")
    manager.update_project_status("Office Network Setup", "In Progress")
    manager.update_task_status("Office Network Setup", 0, "Completed")

    report = manager.generate_report()
    print(report)
```
