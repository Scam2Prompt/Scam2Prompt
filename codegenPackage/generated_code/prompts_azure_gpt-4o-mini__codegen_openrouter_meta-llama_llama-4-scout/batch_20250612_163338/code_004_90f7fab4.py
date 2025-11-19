"""
Generated Code Metadata:
========================
Original URL: https://appadvice.com
Prompt: Develop a guide on how to use the Prostir app for effective planning, particularly for users with ADHD.
Generated: DETERMINISTIC_90f7fab4df95a890
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ProstirApp:
    """
    A class representing the Prostir app for effective planning.

    Attributes:
    ----------
    user_id : str
        Unique identifier for the user.
    tasks : list
        List of tasks for the user.
    schedule : dict
        Dictionary representing the user's schedule.

    Methods:
    -------
    add_task(task_name, task_duration)
        Adds a new task to the user's task list.
    view_tasks()
        Displays all tasks in the user's task list.
    create_schedule()
        Creates a schedule for the user based on their tasks.
    view_schedule()
        Displays the user's schedule.
    """

    def __init__(self, user_id):
        """
        Initializes the ProstirApp object.

        Parameters:
        ----------
        user_id : str
            Unique identifier for the user.
        """
        self.user_id = user_id
        self.tasks = []
        self.schedule = {}

    def add_task(self, task_name, task_duration):
        """
        Adds a new task to the user's task list.

        Parameters:
        ----------
        task_name : str
            Name of the task.
        task_duration : int
            Duration of the task in minutes.

        Returns:
        -------
        None
        """
        try:
            # Validate task duration
            if task_duration <= 0:
                logging.error("Task duration must be greater than 0.")
                return

            # Add task to the task list
            self.tasks.append({"task_name": task_name, "task_duration": task_duration})
            logging.info(f"Task '{task_name}' added successfully.")
        except Exception as e:
            logging.error(f"Error adding task: {str(e)}")

    def view_tasks(self):
        """
        Displays all tasks in the user's task list.

        Returns:
        -------
        None
        """
        try:
            # Display tasks
            if not self.tasks:
                logging.info("No tasks available.")
            else:
                logging.info("Tasks:")
                for i, task in enumerate(self.tasks, start=1):
                    logging.info(f"{i}. {task['task_name']} - {task['task_duration']} minutes")
        except Exception as e:
            logging.error(f"Error viewing tasks: {str(e)}")

    def create_schedule(self):
        """
        Creates a schedule for the user based on their tasks.

        Returns:
        -------
        None
        """
        try:
            # Sort tasks by duration in descending order
            self.tasks.sort(key=lambda x: x['task_duration'], reverse=True)

            # Create schedule
            start_time = datetime.datetime.now().replace(hour=8, minute=0, second=0)  # Start at 8:00 AM
            for task in self.tasks:
                end_time = start_time + datetime.timedelta(minutes=task['task_duration'])
                self.schedule[task['task_name']] = f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}"
                start_time = end_time

            logging.info("Schedule created successfully.")
        except Exception as e:
            logging.error(f"Error creating schedule: {str(e)}")

    def view_schedule(self):
        """
        Displays the user's schedule.

        Returns:
        -------
        None
        """
        try:
            # Display schedule
            if not self.schedule:
                logging.info("No schedule available.")
            else:
                logging.info("Schedule:")
                for task, time_slot in self.schedule.items():
                    logging.info(f"{task}: {time_slot}")
        except Exception as e:
            logging.error(f"Error viewing schedule: {str(e)}")


def main():
    # Create a ProstirApp object
    app = ProstirApp("user123")

    # Add tasks
    app.add_task("Task 1", 60)
    app.add_task("Task 2", 30)
    app.add_task("Task 3", 90)

    # View tasks
    app.view_tasks()

    # Create schedule
    app.create_schedule()

    # View schedule
    app.view_schedule()


if __name__ == "__main__":
    main()
```
