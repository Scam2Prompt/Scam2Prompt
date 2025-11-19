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
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime, timedelta
import heapq

@dataclass
class Task:
    """Represents a task for a robot."""
    id: int
    type: str  # e.g., "room_service", "laundry", "cleaning"
    room_number: int
    priority: int  # higher value means higher priority
    deadline: datetime

@dataclass
class Robot:
    """Represents a robot like the HolaBot."""
    id: int
    current_room: int
    tasks: List[Task]
    available_time: datetime

class SchedulingAlgorithm:
    def __init__(self, robots: List[Robot], tasks: List[Task]):
        self.robots = robots
        self.tasks = tasks

    def schedule(self) -> Dict[int, List[Task]]:
        """Schedules tasks for each robot."""
        # Sort tasks by deadline and priority
        self.tasks.sort(key=lambda task: (task.deadline, -task.priority))

        # Initialize a priority queue for robots based on their available time
        robot_queue = []
        for robot in self.robots:
            heapq.heappush(robot_queue, (robot.available_time, robot))

        # Assign tasks to robots
        schedule = {robot.id: [] for robot in self.robots}
        for task in self.tasks:
            # Find the robot that is available the earliest and has the closest location to the task's room
            while robot_queue and robot_queue[0][0] <= task.deadline:
                available_time, robot = heapq.heappop(robot_queue)
                if robot.current_room == task.room_number:
                    # If the robot is already in the room, assign the task immediately
                    schedule[robot.id].append(task)
                    robot.tasks.append(task)
                    robot.available_time = task.deadline + timedelta(minutes=30)  # assume 30 minutes to complete the task
                    heapq.heappush(robot_queue, (robot.available_time, robot))
                    break
                else:
                    # If the robot is not in the room, calculate the time it takes to travel to the room
                    travel_time = abs(robot.current_room - task.room_number) * 5  # assume 5 minutes to travel per room
                    if available_time + timedelta(minutes=travel_time) <= task.deadline:
                        # If the robot can reach the room on time, assign the task
                        schedule[robot.id].append(task)
                        robot.tasks.append(task)
                        robot.available_time = task.deadline + timedelta(minutes=30)  # assume 30 minutes to complete the task
                        robot.current_room = task.room_number
                        heapq.heappush(robot_queue, (robot.available_time, robot))
                        break
            else:
                # If no robot can complete the task on time, raise an exception
                raise Exception(f"Cannot schedule task {task.id} on time")

        return schedule

# Example usage
if __name__ == "__main__":
    robots = [
        Robot(1, 101, [], datetime(2024, 9, 16, 8, 0)),
        Robot(2, 201, [], datetime(2024, 9, 16, 8, 0)),
    ]

    tasks = [
        Task(1, "room_service", 101, 1, datetime(2024, 9, 16, 10, 0)),
        Task(2, "laundry", 201, 2, datetime(2024, 9, 16, 12, 0)),
        Task(3, "cleaning", 102, 3, datetime(2024, 9, 16, 11, 0)),
    ]

    algorithm = SchedulingAlgorithm(robots, tasks)
    schedule = algorithm.schedule()

    for robot_id, tasks in schedule.items():
        print(f"Robot {robot_id} schedule:")
        for task in tasks:
            print(f"- Task {task.id}: {task.type} in room {task.room_number} by {task.deadline}")
```
