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

class RobotTaskScheduler:
    """
    Scheduler for optimizing tasks for robots in a hotel environment.
    """

    def __init__(self, robots, tasks):
        """
        Initialize the scheduler with available robots and tasks.

        :param robots: List of robot IDs (e.g., ["Robot1", "Robot2"])
        :param tasks: List of tasks. Each task is a dictionary with:
                      - 'id': Task ID (string)
                      - 'priority': Priority (integer, higher is more urgent)
                      - 'duration': Estimated duration in minutes (integer)
                      - 'time_window': Tuple of start and end times (datetime objects)
        """
        self.robots = robots  # List of available robots
        self.tasks = tasks  # List of tasks to be scheduled
        self.schedule = {robot: [] for robot in robots}  # Initialize schedule per robot

    def optimize_schedule(self):
        """
        Optimize the scheduling of tasks using a priority queue (heap).

        This algorithm distributes tasks based on priority, availability, and time window.
        """
        # Sort tasks by priority and time window start time
        sorted_tasks = sorted(self.tasks, key=lambda t: (-t['priority'], t['time_window'][0]))
        
        # Priority queue for assigning tasks to robots (min heap based on availability time)
        robot_availability = [(datetime.min, robot) for robot in self.robots]

        for task in sorted_tasks:
            task_id = task['id']
            task_duration = task['duration']
            task_start, task_end = task['time_window']

            # Find the earliest available robot within the task's time window
            heapq.heapify(robot_availability)
            for i, (available_time, robot) in enumerate(robot_availability):
                if available_time <= task_start:
                    # Assign task to this robot
                    self.schedule[robot].append({
                        "task_id": task_id,
                        "start_time": task_start,
                        "end_time": task_start + timedelta(minutes=task_duration)
                    })

                    # Update robot's next available time
                    robot_availability[i] = (task_start + timedelta(minutes=task_duration), robot)
                    break

    def get_schedule(self):
        """
        Get the optimized schedule for all robots.

        :return: Dictionary of schedules for each robot.
        """
        return self.schedule


# Example usage
if __name__ == "__main__":
    # Define robots
    robots = ["Robot1", "Robot2", "Robot3"]

    # Define tasks
    tasks = [
        {
            "id": "Task1",
            "priority": 5,
            "duration": 30,
            "time_window": (datetime(2023, 10, 1, 10, 0), datetime(2023, 10, 1, 12, 0))
        },
        {
            "id": "Task2",
            "priority": 3,
            "duration": 45,
            "time_window": (datetime(2023, 10, 1, 9, 0), datetime(2023, 10, 1, 11, 0))
        },
        {
            "id": "Task3",
            "priority": 4,
            "duration": 20,
            "time_window": (datetime(2023, 10, 1, 10, 30), datetime(2023, 10, 1, 12, 30))
        }
    ]

    # Initialize scheduler
    scheduler = RobotTaskScheduler(robots, tasks)

    # Optimize schedule
    scheduler.optimize_schedule()

    # Print the schedule
    for robot, schedule in scheduler.get_schedule().items():
        print(f"Schedule for {robot}:")
        for task in schedule:
            print(f"  Task {task['task_id']} from {task['start_time']} to {task['end_time']}")
```
