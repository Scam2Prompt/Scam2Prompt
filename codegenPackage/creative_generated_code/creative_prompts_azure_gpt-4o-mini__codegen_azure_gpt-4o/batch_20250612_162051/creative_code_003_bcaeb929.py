"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Create a maintenance scheduling tool for infrastructure projects that integrates with existing construction management software.
Generated: DETERMINISTIC_bcaeb9297fa5fe30
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json


class MaintenanceScheduler:
    """
    A maintenance scheduling tool for infrastructure projects that integrates with existing 
    construction management software.
    """

    def __init__(self, project_data_file):
        """
        Initializes the MaintenanceScheduler with project data.
        
        :param project_data_file: Path to the JSON file containing project data.
        """
        self.project_data_file = project_data_file
        self.projects = self.load_projects()

    def load_projects(self):
        """
        Loads project data from a JSON file.

        :return: Dictionary of project data.
        """
        try:
            with open(self.project_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.project_data_file} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Failed to parse {self.project_data_file}.")
            return {}

    def schedule_maintenance(self, project_id, maintenance_date, description):
        """
        Schedules maintenance for a specific project.

        :param project_id: ID of the project.
        :param maintenance_date: Date of maintenance in 'YYYY-MM-DD' format.
        :param description: Description of the maintenance.
        :return: True if scheduling is successful, False otherwise.
        """
        if project_id not in self.projects:
            print(f"Error: Project ID {project_id} not found.")
            return False

        try:
            # Convert maintenance_date to a datetime object for validation
            maintenance_date = datetime.datetime.strptime(maintenance_date, '%Y-%m-%d').date()
        except ValueError:
            print(f"Error: Invalid date format. Use 'YYYY-MM-DD'.")
            return False

        # Add maintenance information to the project
        if 'maintenance_schedule' not in self.projects[project_id]:
            self.projects[project_id]['maintenance_schedule'] = []

        self.projects[project_id]['maintenance_schedule'].append({
            'date': maintenance_date.isoformat(),
            'description': description
        })

        print(f"Maintenance scheduled for project {project_id} on {maintenance_date}.")
        return True

    def save_projects(self):
        """
        Saves the updated project data back to the JSON file.
        """
        try:
            with open(self.project_data_file, 'w') as file:
                json.dump(self.projects, file, indent=4)
            print("Project data saved successfully.")
        except Exception as e:
            print(f"Error: Failed to save project data. {e}")

    def get_upcoming_maintenance(self):
        """
        Retrieves a list of upcoming maintenance tasks.

        :return: List of upcoming maintenance tasks.
        """
        upcoming_maintenance = []
        today = datetime.date.today()

        for project_id, project_data in self.projects.items():
            for maintenance in project_data.get('maintenance_schedule', []):
                maintenance_date = datetime.datetime.strptime(maintenance['date'], '%Y-%m-%d').date()
                if maintenance_date >= today:
                    upcoming_maintenance.append({
                        'project_id': project_id,
                        'date': maintenance_date,
                        'description': maintenance['description']
                    })

        # Sort by date
        upcoming_maintenance.sort(key=lambda x: x['date'])
        return upcoming_maintenance


# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler("projects.json")

    # Schedule maintenance for a project
    scheduler.schedule_maintenance("project_001", "2023-12-15", "Inspect structural integrity.")

    # Save updated project data
    scheduler.save_projects()

    # Retrieve upcoming maintenance tasks
    print("Upcoming Maintenance:")
    upcoming_tasks = scheduler.get_upcoming_maintenance()
    for task in upcoming_tasks:
        print(f"Project ID: {task['project_id']}, Date: {task['date']}, Description: {task['description']}")
```
