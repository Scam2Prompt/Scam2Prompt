"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: Write a Python script to manage and monitor a network installation project, inspired by the services provided by Ray-Z Entreprise.
Generated: DETERMINISTIC_aaf6d024af0e0e8a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import datetime
import json
import os

# Configure logging
LOG_FILE = "network_installation.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
PROJECT_DATA_FILE = "project_data.json"

# Classes
class NetworkInstallationProject:
    """
    Class to manage and monitor a network installation project.
    """

    def __init__(self, project_name, client_name, deadline):
        """
        Initialize the project with basic details.
        :param project_name: Name of the project
        :param client_name: Name of the client
        :param deadline: Deadline for the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        self.tasks = []
        self.status = "Not Started"
        logging.info(f"Project '{self.project_name}' initialized for client '{self.client_name}'.")

    def add_task(self, task_name, assigned_to, due_date):
        """
        Add a task to the project.
        :param task_name: Name of the task
        :param assigned_to: Name of the person assigned to the task
        :param due_date: Due date for the task (YYYY-MM-DD)
        """
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            task = {
                "task_name": task_name,
                "assigned_to": assigned_to,
                "due_date": due_date_obj,
                "status": "Pending"
            }
            self.tasks.append(task)
            logging.info(f"Task '{task_name}' added to project '{self.project_name}'.")
        except ValueError as e:
            logging.error(f"Error adding task: {e}")
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def update_task_status(self, task_name, status):
        """
        Update the status of a specific task.
        :param task_name: Name of the task
        :param status: New status of the task (e.g., 'Completed', 'In Progress')
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["status"] = status
                logging.info(f"Task '{task_name}' status updated to '{status}'.")
                return
        logging.warning(f"Task '{task_name}' not found in project '{self.project_name}'.")

    def save_project_data(self):
        """
        Save project data to a JSON file.
        """
        try:
            project_data = {
                "project_name": self.project_name,
                "client_name": self.client_name,
                "deadline": self.deadline.strftime("%Y-%m-%d"),
                "tasks": self.tasks,
                "status": self.status
            }
            with open(PROJECT_DATA_FILE, "w") as file:
                json.dump(project_data, file, indent=4)
            logging.info(f"Project data for '{self.project_name}' saved to '{PROJECT_DATA_FILE}'.")
        except Exception as e:
            logging.error(f"Error saving project data: {e}")
            raise

    def load_project_data(self):
        """
        Load project data from a JSON file.
        """
        try:
            if os.path.exists(PROJECT_DATA_FILE):
                with open(PROJECT_DATA_FILE, "r") as file:
                    project_data = json.load(file)
                self.project_name = project_data["project_name"]
                self.client_name = project_data["client_name"]
                self.deadline = datetime.datetime.strptime(project_data["deadline"], "%Y-%m-%d")
                self.tasks = project_data["tasks"]
                self.status = project_data["status"]
                logging.info(f"Project data for '{self.project_name}' loaded from '{PROJECT_DATA_FILE}'.")
            else:
                logging.warning(f"Project data file '{PROJECT_DATA_FILE}' does not exist.")
        except Exception as e:
            logging.error(f"Error loading project data: {e}")
            raise

    def monitor_progress(self):
        """
        Monitor the progress of the project.
        """
        completed_tasks = sum(1 for task in self.tasks if task["status"] == "Completed")
        total_tasks = len(self.tasks)
        progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        logging.info(f"Project '{self.project_name}' progress: {progress:.2f}% completed.")
        return progress

# Main script
if __name__ == "__main__":
    try:
        # Example usage
        project = NetworkInstallationProject("Office Network Setup", "Ray-Z Entreprise", "2023-12-31")
        project.add_task("Install Routers", "Alice", "2023-11-15")
        project.add_task("Configure Switches", "Bob", "2023-11-20")
        project.update_task_status("Install Routers", "Completed")
        project.save_project_data()
        project.load_project_data()
        progress = project.monitor_progress()
        print(f"Project progress: {progress:.2f}%")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
```
