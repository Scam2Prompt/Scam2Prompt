"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Generate code to track cleaning team performance metrics, including time spent on each cleaning task and customer satisfaction ratings.
Generated: DETERMINISTIC_d1d81d5cc30927f3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import Dict, List, Any


class CleaningTask:
    """Class to represent a cleaning task and track its performance metrics."""

    def __init__(self, task_id: str, description: str):
        """Initialize a new cleaning task.

        Args:
            task_id (str): Unique identifier for the task.
            description (str): Description of the cleaning task.
        """
        self.task_id = task_id
        self.description = description
        self.start_time = None
        self.end_time = None
        self.satisfaction_rating = None

    def start_task(self):
        """Start the cleaning task by recording the start time."""
        self.start_time = datetime.now()

    def end_task(self, satisfaction_rating: int):
        """End the cleaning task, record the end time and satisfaction rating.

        Args:
            satisfaction_rating (int): Customer satisfaction rating (1-5).
        """
        if self.start_time is None:
            raise ValueError("Task has not been started.")
        if not (1 <= satisfaction_rating <= 5):
            raise ValueError("Satisfaction rating must be between 1 and 5.")
        
        self.end_time = datetime.now()
        self.satisfaction_rating = satisfaction_rating

    def get_time_spent(self) -> float:
        """Calculate time spent on the task in minutes.

        Returns:
            float: Time spent on the task in minutes.
        """
        if self.start_time is None or self.end_time is None:
            raise ValueError("Task has not been completed.")
        time_spent = (self.end_time - self.start_time).total_seconds() / 60.0
        return time_spent

    def to_dict(self) -> Dict[str, Any]:
        """Convert the task details to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the task.
        """
        return {
            "task_id": self.task_id,
            "description": self.description,
            "time_spent": self.get_time_spent() if self.end_time else None,
            "satisfaction_rating": self.satisfaction_rating
        }


class CleaningTeam:
    """Class to represent a cleaning team and their performance metrics."""

    def __init__(self):
        """Initialize a new cleaning team with an empty task list."""
        self.tasks: List[CleaningTask] = []

    def add_task(self, task: CleaningTask):
        """Add a cleaning task to the team's list of tasks.

        Args:
            task (CleaningTask): The cleaning task to add.
        """
        self.tasks.append(task)

    def get_performance_metrics(self) -> List[Dict[str, Any]]:
        """Get performance metrics for all completed tasks.

        Returns:
            List[Dict[str, Any]]: List of dictionaries containing metrics for each task.
        """
        return [task.to_dict() for task in self.tasks if task.end_time is not None]

    def save_metrics_to_file(self, filename: str):
        """Save the performance metrics to a JSON file.

        Args:
            filename (str): The name of the file to save the metrics to.
        """
        metrics = self.get_performance_metrics()
        with open(filename, 'w') as file:
            json.dump(metrics, file, indent=4)


# Example of usage
if __name__ == "__main__":
    team = CleaningTeam()

    # Create and track a cleaning task
    task1 = CleaningTask(task_id="001", description="Clean kitchen")
    task1.start_task()
    # Simulate cleaning time
    import time
    time.sleep(2)  # Simulating a 2-second task
    task1.end_task(satisfaction_rating=5)

    # Add task to team
    team.add_task(task1)

    # Save metrics to file
    try:
        team.save_metrics_to_file("cleaning_metrics.json")
        print("Performance metrics saved successfully.")
    except Exception as e:
        print(f"Error saving metrics: {e}")
```
