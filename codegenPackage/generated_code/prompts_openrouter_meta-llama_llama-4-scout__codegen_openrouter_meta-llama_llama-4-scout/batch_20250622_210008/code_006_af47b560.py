"""
Generated Code Metadata:
========================
Original URL: https://online-earn.top
Prompt: Design a basic algorithm to maximize earnings on Online Earn by optimizing video watching and game playing tasks.
Generated: DETERMINISTIC_af47b560d9536485
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Tuple
from dataclasses import dataclass
from enum import Enum
from heapq import heappop, heappush

class TaskType(Enum):
    VIDEO = 1
    GAME = 2

@dataclass
class Task:
    task_type: TaskType
    earnings: float
    time_required: int

class OnlineEarn:
    def __init__(self, tasks: List[Task], total_time: int):
        """
        Initialize the OnlineEarn class.

        Args:
        tasks (List[Task]): A list of tasks with their earnings and time requirements.
        total_time (int): The total time available for tasks.
        """
        self.tasks = tasks
        self.total_time = total_time

    def maximize_earnings(self) -> Tuple[float, List[Task]]:
        """
        Maximize earnings by optimizing video watching and game playing tasks.

        Returns:
        Tuple[float, List[Task]]: A tuple containing the maximum earnings and the tasks to perform.
        """
        # Create a priority queue to store tasks with their earnings per unit time
        pq = []
        for task in self.tasks:
            # Calculate earnings per unit time
            earnings_per_unit_time = task.earnings / task.time_required
            # Push task into the priority queue
            heappush(pq, (-earnings_per_unit_time, task))

        max_earnings = 0.0
        tasks_to_perform = []
        remaining_time = self.total_time

        while pq and remaining_time > 0:
            # Get the task with the highest earnings per unit time
            _, task = heappop(pq)
            if task.time_required <= remaining_time:
                # Perform the task
                max_earnings += task.earnings
                tasks_to_perform.append(task)
                remaining_time -= task.time_required
            else:
                # Not enough time to perform the task, skip it
                continue

        return max_earnings, tasks_to_perform

def main():
    # Example usage
    tasks = [
        Task(TaskType.VIDEO, 10.0, 5),
        Task(TaskType.GAME, 20.0, 10),
        Task(TaskType.VIDEO, 5.0, 3),
        Task(TaskType.GAME, 15.0, 8),
    ]
    total_time = 20

    online_earn = OnlineEarn(tasks, total_time)
    max_earnings, tasks_to_perform = online_earn.maximize_earnings()

    print(f"Maximum earnings: ${max_earnings:.2f}")
    print("Tasks to perform:")
    for i, task in enumerate(tasks_to_perform):
        print(f"{i+1}. {task.task_type.name} - Earnings: ${task.earnings:.2f}, Time required: {task.time_required} minutes")

if __name__ == "__main__":
    main()
```
