"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Write a Python script that simulates a Scrum process, including roles like Product Owner and Scrum Master, inspired by the training offered at CrestAgile.
Generated: DETERMINISTIC_e0a92a241832bd1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class ScrumRole:
    """
    Represents a role in the Scrum process.
    """
    def __init__(self, name):
        self.name = name

    def perform_role(self):
        """
        Placeholder for role-specific actions. To be overridden by subclasses.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

class ProductOwner(ScrumRole):
    def __init__(self):
        super().__init__("Product Owner")

    def define_backlog(self):
        """
        Define the product backlog with tasks.
        """
        backlog = [
            "Create login page",
            "Develop API for user authentication",
            "Design database schema",
            "Build frontend dashboard",
            "Implement unit tests"
        ]
        print("Product Owner defines the backlog:")
        for idx, task in enumerate(backlog, start=1):
            print(f"{idx}. {task}")
        return backlog

class ScrumMaster(ScrumRole):
    def __init__(self):
        super().__init__("Scrum Master")

    def facilitate_meeting(self, meeting_type):
        """
        Facilitate a Scrum meeting.
        """
        print(f"Scrum Master facilitates a {meeting_type} meeting.")

class Developer(ScrumRole):
    def __init__(self, name):
        super().__init__("Developer")
        self.dev_name = name

    def work_on_task(self, task):
        """
        Simulate working on a task.
        """
        print(f"{self.dev_name} is working on: {task}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate task duration
        print(f"{self.dev_name} has completed: {task}")

class ScrumSimulation:
    """
    Simulates the Scrum process.
    """
    def __init__(self):
        self.product_owner = ProductOwner()
        self.scrum_master = ScrumMaster()
        self.developers = [Developer("Alice"), Developer("Bob"), Developer("Charlie")]

    def run_sprint(self):
        """
        Run a Scrum sprint simulation.
        """
        try:
            print("Starting a new sprint...\n")

            # Sprint Planning
            self.scrum_master.facilitate_meeting("Sprint Planning")
            backlog = self.product_owner.define_backlog()

            # Daily Scrum
            print("\nDay 1: Daily Scrum")
            self.scrum_master.facilitate_meeting("Daily Scrum")

            # Developers work on tasks
            for task in backlog:
                developer = random.choice(self.developers)
                developer.work_on_task(task)

            # Sprint Review
            print("\nSprint Review:")
            self.scrum_master.facilitate_meeting("Sprint Review")
            print("Demonstrating completed tasks.")

            # Sprint Retrospective
            print("\nSprint Retrospective:")
            self.scrum_master.facilitate_meeting("Sprint Retrospective")
            print("Discussing improvements for the next sprint.")

            print("\nSprint completed successfully!")

        except Exception as e:
            print(f"An error occurred during the sprint: {e}")

if __name__ == "__main__":
    # Entry point for the Scrum simulation
    simulation = ScrumSimulation()
    simulation.run_sprint()
```
