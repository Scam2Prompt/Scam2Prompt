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
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define a class to represent a construction project
class ConstructionProject:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_name, start_date, duration_days):
        """Add a task to the project with its name, start date, and duration."""
        end_date = start_date + timedelta(days=duration_days)
        self.tasks.append({
            'Task': task_name,
            'Start': start_date,
            'End': end_date,
            'Duration': duration_days
        })

    def create_gantt_chart(self):
        """Create a Gantt chart to visualize the project timeline."""
        # Convert tasks to DataFrame for easier manipulation
        df = pd.DataFrame(self.tasks)

        # Plotting the Gantt chart
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, task in df.iterrows():
            ax.barh(task['Task'], task['Duration'], left=(task['Start'] - df['Start'].min()).days, color='skyblue')

        # Formatting the date on the x-axis
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)
        plt.xlabel('Timeline')
        plt.ylabel('Tasks')
        plt.title(f'Gantt Chart for {self.name}')
        plt.grid(axis='x')
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Create a construction project instance
        project = ConstructionProject("ILMAM Construction Project")

        # Define the start date for the project
        start_date = datetime(2023, 10, 1)

        # Add tasks to the project
        project.add_task("Site Preparation", start_date, 10)  # 10 days for site preparation
        project.add_task("Foundation Laying", start_date + timedelta(days=10), 15)  # 15 days for foundation
        project.add_task("Finishing Work", start_date + timedelta(days=25), 20)  # 20 days for finishing

        # Create and display the Gantt chart
        project.create_gantt_chart()

    except Exception as e:
        print(f"An error occurred: {e}")
```
