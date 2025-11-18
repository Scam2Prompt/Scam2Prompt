"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gsj-technology.com
Prompt: Develop a scheduling algorithm for optimizing the tasks of robots like the HolaBot in a hotel environment, as described in the Maritim Hotel use case on the GSJ website.
Generated: DETERMINISTIC_053021d348d54364
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
from datetime import datetime, timedelta
from typing import List, Tuple, Dict

class Task:
    """Represents a task that a robot needs to perform."""
    
    def __init__(self, task_id: int, location: str, duration: int, priority: int, start_time: datetime = None):
        self.task_id = task_id
        self.location = location
        self.duration = duration  # in minutes
        self.priority = priority    # 1 is highest priority
        self.start_time = start_time or datetime.now()
    
    def __lt__(self, other):
        """Compares tasks based on priority and start time for scheduling."""
        if self.priority == other.priority:
            return self.start_time < other.start_time
        return self.priority < other.priority

class Scheduler:
    """Schedules tasks for robots in a hotel environment."""

    def __init__(self):
        self.tasks: List[Task] = []
        self.current_time = datetime.now()

    def add_task(self, task: Task):
        """Adds a new task to the scheduler."""
        heapq.heappush(self.tasks, task)

    def schedule_tasks(self) -> List[Tuple[int, datetime]]:
        """Schedules tasks based on priority and returns a list of (task_id, start_time)."""
        schedule = []
        
        while self.tasks:
            task = heapq.heappop(self.tasks)
            task_start_time = max(self.current_time, task.start_time)
            task_end_time = task_start_time + timedelta(minutes=task.duration)
            schedule.append((task.task_id, task_start_time))
            self.current_time = task_end_time  # Update current time to task's end time
        
        return schedule

def main():
    """Main function to demonstrate the scheduler."""
    scheduler = Scheduler()

    # Example tasks for the scheduler
    tasks_data = [
        (1, "Lobby", 30, 2),
        (2, "Room 101", 15, 1),
        (3, "Room 202", 45, 3),
        (4, "Conference Room", 60, 2),
    ]

    # Adding tasks to the scheduler
    for task_id, location, duration, priority in tasks_data:
        task = Task(task_id, location, duration, priority)
        scheduler.add_task(task)

    # Scheduling tasks
    scheduled_tasks = scheduler.schedule_tasks()

    # Output the scheduled tasks
    for task_id, start_time in scheduled_tasks:
        print(f"Task ID: {task_id}, Scheduled Start Time: {start_time}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Log the error in a production-ready way
        print(f"An error occurred: {e}")
```
