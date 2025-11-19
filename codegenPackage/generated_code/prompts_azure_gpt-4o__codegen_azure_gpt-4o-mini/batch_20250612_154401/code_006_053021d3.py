"""
Generated Code Metadata:
========================
Original URL: https://gsj-technology.com
Prompt: Develop a scheduling algorithm for optimizing the tasks of robots like the HolaBot in a hotel environment, as described in the Maritim Hotel use case on the GSJ website.
Generated: DETERMINISTIC_053021d348d54364
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from datetime import datetime, timedelta
from typing import List, Tuple, Dict

class Task:
    """Represents a task for the robot to perform."""
    
    def __init__(self, task_id: int, location: str, duration: int, priority: int):
        self.task_id = task_id
        self.location = location
        self.duration = duration  # Duration in minutes
        self.priority = priority  # Lower number means higher priority

    def __lt__(self, other):
        """Compare tasks based on priority and duration."""
        return (self.priority, self.duration) < (other.priority, other.duration)

class RobotScheduler:
    """Schedules tasks for robots in a hotel environment."""
    
    def __init__(self):
        self.task_queue: List[Task] = []
        self.current_time: datetime = datetime.now()

    def add_task(self, task: Task):
        """Adds a task to the scheduling queue."""
        heapq.heappush(self.task_queue, task)

    def schedule_tasks(self) -> List[Tuple[int, datetime]]:
        """Schedules tasks based on priority and returns a list of scheduled tasks with their start times."""
        scheduled_tasks: List[Tuple[int, datetime]] = []
        
        while self.task_queue:
            task = heapq.heappop(self.task_queue)
            start_time = self.current_time
            end_time = start_time + timedelta(minutes=task.duration)
            scheduled_tasks.append((task.task_id, start_time))
            self.current_time = end_time  # Update current time to the end of the last task
            
        return scheduled_tasks

    def reset_schedule(self):
        """Resets the scheduler to the current time."""
        self.current_time = datetime.now()

def main():
    """Main function to demonstrate the scheduling algorithm."""
    scheduler = RobotScheduler()
    
    # Example tasks (task_id, location, duration in minutes, priority)
    tasks = [
        Task(1, "Lobby", 15, 1),
        Task(2, "Room 101", 30, 2),
        Task(3, "Room 202", 20, 1),
        Task(4, "Conference Room", 45, 3),
        Task(5, "Pool Area", 10, 1)
    ]
    
    # Add tasks to the scheduler
    for task in tasks:
        scheduler.add_task(task)

    # Schedule tasks and print the results
    scheduled_tasks = scheduler.schedule_tasks()
    for task_id, start_time in scheduled_tasks:
        print(f"Task {task_id} scheduled at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
