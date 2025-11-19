"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Generate code to automate the scheduling of construction tasks, such as concrete pole installation and anti-ball net fence construction, using Python and relevant project management libraries.
Generated: DETERMINISTIC_da1672bc3b5b4444
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
import pandas as pd
from pandas import DataFrame
from enum import Enum, auto
import logging
from logging.handlers import RotatingFileHandler
from typing import Tuple
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('construction_scheduler.log', maxBytes=5*1024*1024, backupCount=2),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TaskType(Enum):
    CONCRETE_POLE_INSTALLATION = auto()
    ANTI_BALL_NET_FENCE = auto()
    SITE_PREPARATION = auto()
    MATERIAL_DELIVERY = auto()

@dataclass
class Task:
    task_id: str
    task_type: TaskType
    duration: int  # in days
    dependencies: List[str]  # list of task_ids this task depends on
    required_resources: List[str]
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None

@dataclass
class Resource:
    resource_id: str
    resource_type: str
    quantity: int
    available_from: datetime.date

class ConstructionScheduler:
    def __init__(self, tasks: List[Task], resources: List[Resource]):
        self.tasks = {task.task_id: task for task in tasks}
        self.resources = resources
        self.schedule = {}
        self.resource_allocations = defaultdict(list)
    
    def validate_dependencies(self) -> bool:
        """Check if all task dependencies exist."""
        for task in self.tasks.values():
            for dep in task.dependencies:
                if dep not in self.tasks:
                    logger.error(f"Dependency {dep} not found for task {task.task_id}")
                    return False
        return True
    
    def calculate_critical_path(self) -> List[str]:
        """Calculate critical path using forward and backward pass."""
        # Forward pass to calculate earliest start and finish
        for task_id in self.topological_sort():
            task = self.tasks[task_id]
            if not task.dependencies:
                task.start_date = datetime.date.today()
                task.end_date = task.start_date + datetime.timedelta(days=task.duration)
            else:
                max_end_date = max(
                    self.tasks[dep].end_date for dep in task.dependencies
                )
                task.start_date = max_end_date
                task.end_date = task.start_date + datetime.timedelta(days=task.duration)
        
        # Backward pass to calculate latest start and finish
        last_task = max(self.tasks.values(), key=lambda t: t.end_date)
        last_task.end_date = last_task.end_date  # Project completion date
        
        for task_id in reversed(self.topological_sort()):
            task = self.tasks[task_id]
            if task_id == last_task.task_id:
                task.end_date = last_task.end_date
                task.start_date = task.end_date - datetime.timedelta(days=task.duration)
            else:
                dependent_tasks = [
                    t for t in self.tasks.values() if task_id in t.dependencies
                ]
                if dependent_tasks:
                    min_start_date = min(t.start_date for t in dependent_tasks)
                    task.end_date = min_start_date
                    task.start_date = task.end_date - datetime.timedelta(days=task.duration)
                else:
                    task.end_date = last_task.end_date
                    task.start_date = task.end_date - datetime.timedelta(days=task.duration)
        
        # Identify critical path
        critical_path = []
        for task_id in self.topological_sort():
            task = self.tasks[task_id]
            if task.start_date == task.end_date - datetime.timedelta(days=task.duration):
                critical_path.append(task_id)
        
        return critical_path
    
    def topological_sort(self) -> List[str]:
        """Perform topological sort of tasks based on dependencies."""
        visited = set()
        order = []
        
        def dfs(task_id):
            if task_id not in visited:
                visited.add(task_id)
                for dep in self.tasks[task_id].dependencies:
                    dfs(dep)
                order.append(task_id)
        
        for task_id in self.tasks:
            dfs(task_id)
        
        return order
    
    def allocate_resources(self) -> bool:
        """Allocate resources to tasks based on availability."""
        resource_pool = {
            res.resource_id: res for res in self.resources
        }
        
        for task_id in self.topological_sort():
            task = self.tasks[task_id]
            
            # Check resource availability
            for resource_id in task.required_resources:
                resource = resource_pool.get(resource_id)
                if not resource:
                    logger.error(f"Resource {resource_id} not found for task {task_id}")
                    return False
                
                if resource.available_from > task.start_date:
                    logger.warning(
                        f"Resource {resource_id} not available until {resource.available_from} "
                        f"but needed for task {task_id} starting {task.start_date}"
                    )
                    return False
                
                # Check if resource is already allocated during this time
                for allocation in self.resource_allocations[resource_id]:
                    if not (task.end_date < allocation[0] or task.start_date > allocation[1]):
                        logger.warning(
                            f"Resource {resource_id} already allocated from {allocation[0]} to {allocation[1]} "
                            f"which conflicts with task {task_id} ({task.start_date} to {task.end_date})"
                        )
                        return False
            
            # Allocate resources
            for resource_id in task.required_resources:
                self.resource_allocations[resource_id].append(
                    (task.start_date, task.end_date)
                )
        
        return True
    
    def generate_schedule(self) -> Dict[str, Dict[str, str]]:
        """Generate the final schedule with task details."""
        if not self.validate_dependencies():
            raise ValueError("Invalid task dependencies")
        
        self.calculate_critical_path()
        
        if not self.allocate_resources():
            raise ValueError("Resource allocation failed")
        
        schedule = {}
        for task_id, task in self.tasks.items():
            schedule[task_id] = {
                "task_type": task.task_type.name,
                "start_date": task.start_date.strftime("%Y-%m-%d"),
                "end_date": task.end_date.strftime("%Y-%m-%d"),
                "duration": f"{task.duration} days",
                "resources": ", ".join(task.required_resources)
            }
        
        return schedule
    
    def export_to_csv(self, filename: str = "construction_schedule.csv") -> None:
        """Export schedule to CSV file."""
        schedule = self.generate_schedule()
        df = DataFrame.from_dict(schedule, orient='index')
        df.to_csv(filename, index_label="task_id")
        logger.info(f"Schedule exported to {filename}")

def sample_implementation():
    """Sample implementation with test data."""
    # Define resources
    resources = [
        Resource("crew1", "installation_crew", 5, datetime.date.today()),
        Resource("crew2", "fence_crew", 3, datetime.date.today()),
        Resource("crane1", "heavy_equipment", 1, datetime.date.today()),
        Resource("truck1", "transport", 2, datetime.date.today())
    ]
    
    # Define tasks
    tasks = [
        Task(
            task_id="t1",
            task_type=TaskType.SITE_PREPARATION,
            duration=2,
            dependencies=[],
            required_resources=["crew1", "truck1"]
        ),
        Task(
            task_id="t2",
            task_type=TaskType.MATERIAL_DELIVERY,
            duration=1,
            dependencies=[],
            required_resources=["truck1"]
        ),
        Task(
            task_id="t3",
            task_type=TaskType.CONCRETE_POLE_INSTALLATION,
            duration=5,
            dependencies=["t1", "t2"],
            required_resources=["crew1", "crane1"]
        ),
        Task(
            task_id="t4",
            task_type=TaskType.ANTI_BALL_NET_FENCE,
            duration=4,
            dependencies=["t3"],
            required_resources=["crew2"]
        )
    ]
    
    # Create and run scheduler
    scheduler = ConstructionScheduler(tasks, resources)
    try:
        schedule = scheduler.generate_schedule()
        print("Construction Schedule:")
        for task_id, details in schedule.items():
            print(f"{task_id}: {details}")
        
        scheduler.export_to_csv()
    except Exception as e:
        logger.error(f"Error generating schedule: {e}")

if __name__ == "__main__":
    sample_implementation()
```
