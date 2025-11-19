"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Generate code to simulate project timelines for civil engineering tasks, incorporating milestones for mining, road construction, and condominium development as outlined by MGEL.
Generated: DETERMINISTIC_f05136dd70678ee5
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class ProjectTimeline:
    def __init__(self, project_name):
        """
        Initialize a project timeline.

        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task_name, start_date, duration):
        """
        Add a task to the project timeline.

        Args:
            task_name (str): The name of the task.
            start_date (datetime): The start date of the task.
            duration (int): The duration of the task in days.
        """
        end_date = start_date + timedelta(days=duration)
        self.tasks.append({
            'task_name': task_name,
            'start_date': start_date,
            'end_date': end_date
        })

    def add_milestone(self, milestone_name, date):
        """
        Add a milestone to the project timeline.

        Args:
            milestone_name (str): The name of the milestone.
            date (datetime): The date of the milestone.
        """
        self.tasks.append({
            'task_name': milestone_name,
            'start_date': date,
            'end_date': date
        })

    def print_timeline(self):
        """
        Print the project timeline.
        """
        print(f"Project Timeline for {self.project_name}:")
        for task in sorted(self.tasks, key=lambda x: x['start_date']):
            if task['start_date'] == task['end_date']:
                print(f"- {task['task_name']}: {task['start_date'].strftime('%Y-%m-%d')} (Milestone)")
            else:
                print(f"- {task['task_name']}: {task['start_date'].strftime('%Y-%m-%d')} - {task['end_date'].strftime('%Y-%m-%d')}")


class MGELProjectTimeline(ProjectTimeline):
    def __init__(self, project_name):
        """
        Initialize an MGEL project timeline.

        Args:
            project_name (str): The name of the project.
        """
        super().__init__(project_name)

    def add_mining_milestone(self, date):
        """
        Add a mining milestone to the project timeline.

        Args:
            date (datetime): The date of the milestone.
        """
        self.add_milestone("Mining Milestone", date)

    def add_road_construction_task(self, start_date, duration):
        """
        Add a road construction task to the project timeline.

        Args:
            start_date (datetime): The start date of the task.
            duration (int): The duration of the task in days.
        """
        self.add_task("Road Construction", start_date, duration)

    def add_condominium_development_task(self, start_date, duration):
        """
        Add a condominium development task to the project timeline.

        Args:
            start_date (datetime): The start date of the task.
            duration (int): The duration of the task in days.
        """
        self.add_task("Condominium Development", start_date, duration)


def main():
    try:
        project_name = "MGEL Civil Engineering Project"
        project_timeline = MGELProjectTimeline(project_name)

        mining_milestone_date = datetime(2024, 3, 15)
        project_timeline.add_mining_milestone(mining_milestone_date)

        road_construction_start_date = datetime(2024, 1, 1)
        road_construction_duration = 120
        project_timeline.add_road_construction_task(road_construction_start_date, road_construction_duration)

        condominium_development_start_date = datetime(2024, 6, 1)
        condominium_development_duration = 180
        project_timeline.add_condominium_development_task(condominium_development_start_date, condominium_development_duration)

        project_timeline.print_timeline()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
