"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Write a Python script that automates the scheduling of construction tasks based on the project management principles used by Construye RK.
Generated: DETERMINISTIC_2176c2a47ea47ed3
Batch ID: 20250612_163218
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
import os

class ConstructionScheduler:
    """
    A class to automate the scheduling of construction tasks using project management principles.
    """

    def __init__(self):
        """
        Initializes the construction scheduler with an empty list of tasks.
        """
        self.tasks = []

    def load_tasks_from_file(self, file_path):
        """
        Loads tasks from a JSON file.

        :param file_path: Path to the JSON file containing task data
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        try:
            with open(file_path, 'r') as file:
                self.tasks = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def save_schedule_to_file(self, file_path):
        """
        Saves the generated schedule to a JSON file.

        :param file_path: Path to the JSON file where schedule will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except Exception as e:
            raise Exception(f"An unexpected error occurred while saving the schedule: {e}")

    def add_task(self, name, duration_days, dependencies=None, start_date=None):
        """
        Adds a construction task to the scheduler.

        :param name: Name of the task
        :param duration_days: Duration of the task in days
        :param dependencies: List of task names this task depends on
        :param start_date: Optional start date for the task (ISO format yyyy-mm-dd)
        """
        task = {
            "name": name,
            "duration_days": duration_days,
            "dependencies": dependencies if dependencies else [],
            "start_date": start_date,
            "end_date": None
        }
        self.tasks.append(task)

    def schedule_tasks(self):
        """
        Schedules all tasks by calculating their start and end dates.
        """
        # Map to store task completion dates for dependency resolution
        task_completion_dates = {}

        for task in self.tasks:
            # Resolve dependencies
            if task["dependencies"]:
                latest_dependency_date = max(
                    task_completion_dates.get(dep, datetime.date.today())
                    for dep in task["dependencies"]
                )
                start_date = latest_dependency_date
            else:
                # Default start date if no dependencies
                start_date = datetime.date.today()

            if task["start_date"]:
                start_date = max(start_date, datetime.date.fromisoformat(task["start_date"]))

            # Calculate end date
            end_date = start_date + datetime.timedelta(days=task["duration_days"])

            # Update task details
            task["start_date"] = start_date.isoformat()
            task["end_date"] = end_date.isoformat()

            # Record completion date
            task_completion_dates[task["name"]] = end_date

    def display_schedule(self):
        """
        Displays the scheduled tasks in a human-readable format.
        """
        print("Scheduled Tasks:")
        for task in self.tasks:
            print(f"Task: {task['name']}")
            print(f"  Start Date: {task['start_date']}")
            print(f"  End Date: {task['end_date']}")
            print(f"  Duration (days): {task['duration_days']}")
            print(f"  Dependencies: {', '.join(task['dependencies']) if task['dependencies'] else 'None'}")
            print("-" * 40)


if __name__ == "__main__":
    # Example usage of the ConstructionScheduler class
    try:
        scheduler = ConstructionScheduler()

        # Adding example tasks
        scheduler.add_task(name="Foundation", duration_days=10)
        scheduler.add_task(name="Framing", duration_days=5, dependencies=["Foundation"])
        scheduler.add_task(name="Roofing", duration_days=7, dependencies=["Framing"], start_date="2023-11-01")

        # Schedule tasks
        scheduler.schedule_tasks()

        # Display scheduled tasks
        scheduler.display_schedule()

        # Save schedule to file
        scheduler.save_schedule_to_file("construction_schedule.json")

        print("\nSchedule saved to 'construction_schedule.json'.")
    except Exception as e:
        print(f"Error: {e}")
```
