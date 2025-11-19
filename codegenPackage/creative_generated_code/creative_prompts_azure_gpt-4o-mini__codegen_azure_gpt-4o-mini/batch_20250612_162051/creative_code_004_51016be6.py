"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Suggest a library for visualizing project timelines and resource management in civil engineering, akin to the detailed planning mentioned by C&M Pinnacle.
Generated: DETERMINISTIC_51016be6a11035b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for project visualization
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

class ProjectTimelineVisualizer:
    """
    A class to visualize project timelines and resource management for civil engineering projects.
    """

    def __init__(self, project_name):
        """
        Initializes the ProjectTimelineVisualizer with a project name.

        Args:
            project_name (str): The name of the project to visualize.
        """
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task_name, start_date, duration_days):
        """
        Adds a task to the project timeline.

        Args:
            task_name (str): The name of the task.
            start_date (str): Start date of the task in 'YYYY-MM-DD' format.
            duration_days (int): Duration of the task in days.
        """
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = start_date + timedelta(days=duration_days)
            self.tasks.append({
                'Task': task_name,
                'Start': start_date,
                'End': end_date
            })
        except ValueError as e:
            print(f"Error adding task '{task_name}': {e}")

    def visualize_timeline(self):
        """
        Visualizes the project timeline using a Gantt chart.
        """
        if not self.tasks:
            print("No tasks to visualize.")
            return
        
        # Prepare data for visualization
        df = pd.DataFrame(self.tasks)
        df['Duration'] = df['End'] - df['Start']

        # Create the Gantt chart
        plt.figure(figsize=(10, len(df) * 0.5))
        plt.barh(df['Task'], df['Duration'].dt.days, left=(df['Start'] - df['Start'].min()).dt.days)
        plt.xlabel('Days')
        plt.ylabel('Tasks')
        plt.title(f'Project Timeline for {self.project_name}')
        plt.grid(axis='x')

        # Show plot
        plt.show()


# Example usage:
if __name__ == '__main__':
    # Initialize the visualizer for a sample project
    visualizer = ProjectTimelineVisualizer("Civil Engineering Project")

    # Add tasks to the project
    visualizer.add_task("Site Preparation", "2023-10-01", 15)
    visualizer.add_task("Foundation Work", "2023-10-16", 30)
    visualizer.add_task("Structural Framing", "2023-11-15", 40)
    visualizer.add_task("Roof Installation", "2023-12-25", 20)

    # Visualize the project timeline
    visualizer.visualize_timeline()
```
