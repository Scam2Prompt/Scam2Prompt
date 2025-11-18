"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Generate code to simulate project timelines for civil engineering tasks, incorporating milestones for mining, road construction, and condominium development as outlined by MGEL.
Generated: DETERMINISTIC_f05136dd70678ee5
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class CivilEngineeringProject:
    def __init__(self, name: str):
        """Initialize the project with a name and an empty list of tasks."""
        self.name = name
        self.tasks: List[Dict] = []

    def add_task(self, title: str, duration_days: int, start_date: datetime.date):
        """
        Add a task to the project.
        
        Parameters:
            title (str): The title of the task.
            duration_days (int): The duration of the task in days.
            start_date (datetime.date): The start date of the task.
        """
        end_date = start_date + datetime.timedelta(days=duration_days)
        task = {
            'title': title,
            'start_date': start_date,
            'end_date': end_date,
            'duration_days': duration_days
        }
        self.tasks.append(task)

    def simulate_timeline(self) -> List[Dict]:
        """
        Simulate the project timeline by returning a list of tasks with their start and end dates.

        Returns:
            List[Dict]: A list of dictionaries containing task details.
        """
        timeline = []
        for task in self.tasks:
            timeline.append({
                'Task': task['title'],
                'Start': task['start_date'].strftime('%Y-%m-%d'),
                'End': task['end_date'].strftime('%Y-%m-%d'),
                'Duration (days)': task['duration_days']
            })
        return timeline

def main():
    # Create a new civil engineering project
    project = CivilEngineeringProject("MGEL Civil Engineering Project")

    # Define tasks with their durations and start dates
    try:
        project.add_task("Mining", duration_days=60, start_date=datetime.date(2023, 11, 1))
        project.add_task("Road Construction", duration_days=120, start_date=datetime.date(2024, 1, 2))
        project.add_task("Condominium Development", duration_days=180, start_date=datetime.date(2024, 5, 1))
        
        # Simulate the timeline for the project
        timeline = project.simulate_timeline()

        # Display the project timeline
        for task in timeline:
            print(f"Task: {task['Task']}, Start: {task['Start']}, End: {task['End']}, Duration: {task['Duration (days)']} days")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
