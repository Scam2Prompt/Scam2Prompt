"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Write a Python script that automates the scheduling of tasks related to the installation of ball protection nets and fences in construction sites.
Generated: DETERMINISTIC_4e4772e18e557169
Batch ID: 20250612_135230
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
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TaskScheduler:
    def __init__(self, config_file: str):
        """
        Initializes the TaskScheduler with the provided configuration file.

        :param config_file: Path to the JSON configuration file containing task information.
        """
        self.tasks = self.load_tasks(config_file)

    def load_tasks(self, config_file: str) -> List[Dict[str, Any]]:
        """
        Loads tasks from a JSON configuration file.

        :param config_file: Path to the JSON configuration file.
        :return: List of tasks as dictionaries.
        """
        try:
            with open(config_file, 'r') as file:
                tasks = json.load(file)
                logging.info("Tasks successfully loaded from the configuration file.")
                return tasks
        except FileNotFoundError:
            logging.error(f"Configuration file {config_file} not found.")
            raise
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from the configuration file {config_file}.")
            raise

    def schedule_tasks(self) -> List[str]:
        """
        Schedules the tasks based on their start date and duration.

        :return: List of scheduled task strings.
        """
        scheduled_tasks = []
        for task in self.tasks:
            try:
                start_date = datetime.datetime.strptime(task['start_date'], '%Y-%m-%d')
                duration = task['duration']  # Duration in days
                end_date = start_date + datetime.timedelta(days=duration)

                task_schedule = f"Task: {task['name']}, Start: {start_date.date()}, End: {end_date.date()}"
                scheduled_tasks.append(task_schedule)
                logging.info(f"Scheduled: {task_schedule}")
            except KeyError as e:
                logging.error(f"Missing key in task: {e}")
            except ValueError as e:
                logging.error(f"Date format error for task {task['name']}: {e}")

        return scheduled_tasks

    def display_schedule(self):
        """
        Displays the scheduled tasks in a readable format.
        """
        scheduled_tasks = self.schedule_tasks()
        logging.info("Scheduled Tasks:")
        for task in scheduled_tasks:
            print(task)

if __name__ == "__main__":
    try:
        # Load the configuration file and schedule tasks
        scheduler = TaskScheduler('tasks_config.json')
        scheduler.display_schedule()
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```

Ensure to create a `tasks_config.json` file with the proper structure before running the script. The JSON should be formatted like this:

```json
[
    {
        "name": "Install Ball Protection Net",
        "start_date": "2023-10-01",
        "duration": 5
    },
    {
        "name": "Install Fences",
        "start_date": "2023-10-06",
        "duration": 3
    }
]
```
