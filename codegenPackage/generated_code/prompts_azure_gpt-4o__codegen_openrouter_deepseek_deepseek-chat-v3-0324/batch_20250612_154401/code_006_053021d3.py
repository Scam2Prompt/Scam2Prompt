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
from typing import List, Dict, Tuple, Optional

class Task:
    """Represents a task to be performed by a robot."""
    
    def __init__(self, task_id: str, task_type: str, priority: int, 
                 estimated_duration: timedelta, location: str, 
                 deadline: Optional[datetime] = None):
        """
        Initialize a Task.
        
        Args:
            task_id: Unique identifier for the task.
            task_type: Type of task (e.g., 'cleaning', 'delivery').
            priority: Priority level (lower number = higher priority).
            estimated_duration: Estimated time to complete the task.
            location: Where the task needs to be performed.
            deadline: Optional deadline for the task.
        """
        self.task_id = task_id
        self.task_type = task_type
        self.priority = priority
        self.estimated_duration = estimated_duration
        self.location = location
        self.deadline = deadline
        self.start_time = None
        self.end_time = None
    
    def __lt__(self, other: 'Task') -> bool:
        """Compare tasks based on priority and deadline for heapq."""
        if self.priority != other.priority:
            return self.priority < other.priority
        if self.deadline and other.deadline:
            return self.deadline < other.deadline
        return self.estimated_duration < other.estimated_duration

class Robot:
    """Represents a robot with its current state and schedule."""
    
    def __init__(self, robot_id: str, initial_location: str):
        """
        Initialize a Robot.
        
        Args:
            robot_id: Unique identifier for the robot.
            initial_location: Starting location of the robot.
        """
        self.robot_id = robot_id
        self.current_location = initial_location
        self.schedule = []
        self.available_at = datetime.now()
    
    def assign_task(self, task: Task, current_time: datetime) -> bool:
        """
        Assign a task to the robot if feasible.
        
        Args:
            task: Task to be assigned.
            current_time: Current simulation time.
            
        Returns:
            bool: True if task was successfully assigned, False otherwise.
        """
        if self.available_at > current_time:
            available_from = self.available_at
        else:
            available_from = current_time
        
        # Calculate travel time (simplified as fixed time per location change)
        travel_time = timedelta(minutes=5) if self.current_location != task.location else timedelta(0)
        
        task_start = available_from + travel_time
        task_end = task_start + task.estimated_duration
        
        # Check if task has deadline and can be completed before it
        if task.deadline and task_end > task.deadline:
            return False
        
        # Update robot's schedule
        task.start_time = task_start
        task.end_time = task_end
        self.schedule.append(task)
        self.available_at = task_end
        self.current_location = task.location
        return True

class Scheduler:
    """Manages task scheduling for multiple robots."""
    
    def __init__(self, robots: List[Robot]):
        """
        Initialize the Scheduler.
        
        Args:
            robots: List of available robots.
        """
        self.robots = robots
        self.task_queue = []
    
    def add_task(self, task: Task) -> None:
        """Add a task to the scheduling queue."""
        heapq.heappush(self.task_queue, task)
    
    def schedule_tasks(self, current_time: datetime) -> Dict[str, List[Task]]:
        """
        Schedule all tasks in the queue to available robots.
        
        Args:
            current_time: Current simulation time.
            
        Returns:
            Dict[str, List[Task]]: Mapping of robot IDs to their assigned tasks.
        """
        assignments = {robot.robot_id: [] for robot in self.robots}
        
        while self.task_queue:
            task = heapq.heappop(self.task_queue)
            assigned = False
            
            # Try to assign to the robot that will be available soonest
            best_robot = None
            earliest_available = None
            
            for robot in self.robots:
                if robot.assign_task(task, current_time):
                    if not best_robot or robot.available_at < earliest_available:
                        best_robot = robot
                        earliest_available = robot.available_at
            
            if best_robot:
                assignments[best_robot.robot_id].append(task)
            else:
                # No robot could take the task - log or handle accordingly
                print(f"Warning: Could not assign task {task.task_id}")
        
        return assignments

# Example Usage
if __name__ == "__main__":
    # Create robots
    robots = [
        Robot("HolaBot-1", "Lobby"),
        Robot("HolaBot-2", "Kitchen")
    ]
    
    scheduler = Scheduler(robots)
    
    # Add some tasks
    now = datetime.now()
    scheduler.add_task(Task("T1", "delivery", 1, timedelta(minutes=15), "Room 101", now + timedelta(minutes=30)))
    scheduler.add_task(Task("T2", "cleaning", 2, timedelta(minutes=20), "Room 201"))
    scheduler.add_task(Task("T3", "delivery", 1, timedelta(minutes=10), "Room 102", now + timedelta(minutes=45)))
    
    # Schedule tasks
    assignments = scheduler.schedule_tasks(now)
    
    # Print assignments
    for robot_id, tasks in assignments.items():
        print(f"Robot {robot_id} has {len(tasks)} tasks:")
        for task in tasks:
            print(f"  - {task.task_id}: {task.task_type} at {task.location} from {task.start_time} to {task.end_time}")
```
