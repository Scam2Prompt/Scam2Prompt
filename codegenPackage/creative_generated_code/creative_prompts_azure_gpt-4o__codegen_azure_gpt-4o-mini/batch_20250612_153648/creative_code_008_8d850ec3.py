"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Write code to automate the scheduling and resource allocation for managing large-scale residential complexes, inspired by the project management capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_8d850ec3971d7a3d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any, Optional

class Resource:
    """Class representing a resource (e.g., worker, equipment) in the system."""
    
    def __init__(self, resource_id: str, resource_type: str):
        self.resource_id = resource_id
        self.resource_type = resource_type
    
    def __repr__(self):
        return f"Resource(id={self.resource_id}, type={self.resource_type})"


class Task:
    """Class representing a task that needs to be scheduled."""
    
    def __init__(self, task_id: str, description: str, duration: int):
        self.task_id = task_id
        self.description = description
        self.duration = duration  # duration in hours
        self.schedule: Optional[datetime.datetime] = None
        self.resources: List[Resource] = []
    
    def assign_resources(self, resources: List[Resource]):
        """Assign resources to the task."""
        self.resources.extend(resources)
    
    def schedule_task(self, start_time: datetime.datetime):
        """Schedule the task by setting its start time."""
        self.schedule = start_time + datetime.timedelta(hours=self.duration)
    
    def __repr__(self):
        return (f"Task(id={self.task_id}, description={self.description}, "
                f"duration={self.duration}, schedule={self.schedule}, "
                f"resources={self.resources})")


class Scheduler:
    """Class to manage the scheduling of tasks and resource allocation."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.resources: List[Resource] = []
    
    def add_task(self, task: Task):
        """Add a task to the scheduler."""
        self.tasks.append(task)
    
    def add_resource(self, resource: Resource):
        """Add a resource to the scheduler."""
        self.resources.append(resource)
    
    def schedule_tasks(self, start_time: datetime.datetime):
        """Schedule all tasks sequentially based on the start time."""
        current_time = start_time
        
        for task in self.tasks:
            try:
                task.schedule_task(current_time)
                print(f"Scheduled {task} starting at {current_time}")
                current_time = task.schedule  # Update time to end of current task
            except Exception as e:
                print(f"Error scheduling task {task.task_id}: {str(e)}")
    
    def allocate_resources(self):
        """Allocate resources to tasks based on availability."""
        for task in self.tasks:
            if not task.resources:
                try:
                    available_resources = self.resources[:2]  # Example logic, adjust as needed
                    task.assign_resources(available_resources)
                    print(f"Allocated resources {available_resources} to task {task.task_id}")
                except Exception as e:
                    print(f"Error allocating resources to task {task.task_id}: {str(e)}")


# Example usage of the Scheduler
if __name__ == "__main__":
    # Create a scheduler instance
    scheduler = Scheduler()

    # Create resources
    resource1 = Resource(resource_id="R1", resource_type="Worker")
    resource2 = Resource(resource_id="R2", resource_type="Equipment")
    
    # Add resources to the scheduler
    scheduler.add_resource(resource1)
    scheduler.add_resource(resource2)

    # Create tasks
    task1 = Task(task_id="T1", description="Site preparation", duration=5)
    task2 = Task(task_id="T2", description="Foundation laying", duration=8)

    # Add tasks to the scheduler
    scheduler.add_task(task1)
    scheduler.add_task(task2)

    # Schedule tasks starting from the current datetime
    start_time = datetime.datetime.now()
    scheduler.schedule_tasks(start_time)

    # Allocate resources to tasks
    scheduler.allocate_resources()
```
