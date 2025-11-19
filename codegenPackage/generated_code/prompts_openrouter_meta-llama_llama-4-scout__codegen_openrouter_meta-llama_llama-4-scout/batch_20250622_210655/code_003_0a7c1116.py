"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: "Generate a sample construction project plan using ILMAM Construction's services, including site preparation, foundation laying, and finishing work, and provide a Gantt chart to visualize the project timeline."
Generated: DETERMINISTIC_0a7c11168c07e140
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

class ConstructionProject:
    def __init__(self, project_name):
        """
        Initialize a construction project.

        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task_name, start_date, end_date):
        """
        Add a task to the project.

        Args:
            task_name (str): The name of the task.
            start_date (datetime): The start date of the task.
            end_date (datetime): The end date of the task.
        """
        self.tasks.append({
            'task_name': task_name,
            'start_date': start_date,
            'end_date': end_date
        })

    def visualize_project_timeline(self):
        """
        Visualize the project timeline using a Gantt chart.
        """
        fig, ax = plt.subplots()

        for i, task in enumerate(self.tasks):
            ax.plot([task['start_date'], task['end_date']], [i, i], 'b', linewidth=10)
            ax.plot([task['start_date'], task['start_date']], [i-0.2, i+0.2], 'r', linewidth=2)
            ax.plot([task['end_date'], task['end_date']], [i-0.2, i+0.2], 'g', linewidth=2)
            ax.text(task['start_date'], i, task['task_name'], ha='left', va='center')

        ax.set_yticks([])
        ax.set_xlim([min(task['start_date'] for task in self.tasks) - timedelta(days=1), 
                     max(task['end_date'] for task in self.tasks) + timedelta(days=1)])
        ax.set_ylim([-1, len(self.tasks)])
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        fig.autofmt_xdate()

        plt.title(self.project_name + ' Project Timeline')
        plt.show()


def main():
    try:
        project = ConstructionProject('ILMAM Construction Project')

        # Site preparation
        site_preparation_start = datetime(2024, 9, 1)
        site_preparation_end = datetime(2024, 9, 15)
        project.add_task('Site Preparation', site_preparation_start, site_preparation_end)

        # Foundation laying
        foundation_laying_start = datetime(2024, 9, 16)
        foundation_laying_end = datetime(2024, 10, 15)
        project.add_task('Foundation Laying', foundation_laying_start, foundation_laying_end)

        # Finishing work
        finishing_work_start = datetime(2024, 10, 16)
        finishing_work_end = datetime(2024, 11, 30)
        project.add_task('Finishing Work', finishing_work_start, finishing_work_end)

        project.visualize_project_timeline()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
