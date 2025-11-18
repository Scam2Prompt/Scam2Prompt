"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gsj-technology.com
Prompt: Write Python code to simulate the functionality of the PuduBot as described on the GSJ International Trade GmbH website, including its intelligent universal serving capabilities.
Generated: DETERMINISTIC_d256b7ab214cb568
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class PuduBot:
    """
    A class to simulate the functionality of the PuduBot, an intelligent universal serving robot.
    """

    def __init__(self, name="PuduBot"):
        """
        Initialize the PuduBot with default settings.

        :param name: Name of the robot (default is "PuduBot")
        """
        self.name = name
        self.tasks = []
        self.current_task = None
        self.is_operational = True

    def add_task(self, task):
        """
        Add a serving task to the robot's task queue.

        :param task: A dictionary containing task details (e.g., table number, dish name)
        """
        if not isinstance(task, dict) or not all(k in task for k in ["table", "dish"]):
            raise ValueError("Task must be a dictionary with 'table' and 'dish' keys.")
        self.tasks.append(task)
        print(f"Task added: {task}")

    def perform_tasks(self):
        """
        Perform all tasks in the task queue sequentially.
        """
        if not self.is_operational:
            print(f"{self.name} is not operational. Cannot perform tasks.")
            return

        while self.tasks:
            self.current_task = self.tasks.pop(0)
            print(f"Performing task: Delivering '{self.current_task['dish']}' to table {self.current_task['table']}.")
            time.sleep(2)  # Simulate task duration
            print(f"Task completed: '{self.current_task['dish']}' delivered to table {self.current_task['table']}.")
            self.current_task = None

        print("All tasks completed.")

    def stop_operation(self):
        """
        Stop the operation of the robot.
        """
        self.is_operational = False
        print(f"{self.name} stopped operation.")

    def resume_operation(self):
        """
        Resume the operation of the robot.
        """
        self.is_operational = True
        print(f"{self.name} resumed operation.")

    def status_report(self):
        """
        Print the current status of the robot.
        """
        operational_status = "Operational" if self.is_operational else "Not Operational"
        print(f"Robot Name: {self.name}")
        print(f"Status: {operational_status}")
        print(f"Current Task: {self.current_task if self.current_task else 'None'}")
        print(f"Tasks in Queue: {len(self.tasks)}")


# Example usage:

if __name__ == "__main__":
    pudu_bot = PuduBot(name="PuduBot-V1")

    # Add tasks
    pudu_bot.add_task({"table": 1, "dish": "Pasta"})
    pudu_bot.add_task({"table": 2, "dish": "Salad"})
    pudu_bot.add_task({"table": 3, "dish": "Soup"})

    # Check status
    pudu_bot.status_report()

    # Perform tasks
    pudu_bot.perform_tasks()

    # Stop operation
    pudu_bot.stop_operation()

    # Resume operation
    pudu_bot.resume_operation()

    # Check status
    pudu_bot.status_report()

    # Perform remaining tasks (if any)
    pudu_bot.perform_tasks()
```
