"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Generate code using a project management library (e.g., `ProjectLibre` or similar) to simulate the planning phase of a construction project, incorporating milestones and dependencies as described by INARO S.A.S.
Generated: DETERMINISTIC_02febebaac4b6c32
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Planning Simulation using ProjectLibre-like functionality

This script simulates the planning phase of a construction project with milestones
and task dependencies, similar to what INARO S.A.S might use.
"""

import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Task:
    """Represents a construction project task with dependencies."""
    id: str
    name: str
    duration: int  # in days
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    dependencies: List[str] = None
    is_milestone: bool = False

class ConstructionProject:
    """Manages a construction project with tasks and dependencies."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}
        self.start_date: Optional[datetime.date] = None
        
    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        if task.id in self.tasks:
            raise ValueError(f"Task with ID {task.id} already exists")
        self.tasks[task.id] = task
        
    def set_project_start(self, start_date: datetime.date) -> None:
        """Set the project start date."""
        self.start_date = start_date
        
    def calculate_schedule(self) -> None:
        """Calculate the schedule for all tasks based on dependencies."""
        if not self.start_date:
            raise ValueError("Project start date must be set first")
            
        # Process tasks in dependency order
        processed = set()
        changed = True
        
        while changed:
            changed = False
            for task in self.tasks.values():
                if task.id in processed:
                    continue
                    
                # Check if all dependencies are processed
                all_deps_processed = True
                max_dep_end_date = self.start_date
                
                if task.dependencies:
                    for dep_id in task.dependencies:
                        if dep_id not in self.tasks:
                            raise ValueError(f"Dependency {dep_id} not found")
                        if dep_id not in processed:
                            all_deps_processed = False
                            break
                        dep = self.tasks[dep_id]
                        if dep.end_date and dep.end_date > max_dep_end_date:
                            max_dep_end_date = dep.end_date
                
                if all_deps_processed:
                    if task.is_milestone:
                        task.start_date = max_dep_end_date
                        task.end_date = max_dep_end_date
                    else:
                        task.start_date = max_dep_end_date
                        task.end_date = task.start_date + datetime.timedelta(days=task.duration)
                    processed.add(task.id)
                    changed = True
                    
        if len(processed) != len(self.tasks):
            unprocessed = set(self.tasks.keys()) - processed
            raise ValueError(f"Circular dependencies detected in tasks: {unprocessed}")
            
    def get_critical_path(self) -> List[Task]:
        """Identify the critical path of the project."""
        if not all(task.end_date for task in self.tasks.values()):
            self.calculate_schedule()
            
        # Find project end date
        end_date = max(task.end_date for task in self.tasks.values())
        
        # Work backwards to find critical path
        critical_path = []
        current_tasks = [task for task in self.tasks.values() if task.end_date == end_date]
        
        while current_tasks:
            current_task = current_tasks.pop()
            critical_path.append(current_task)
            
            if not current_task.dependencies:
                break
                
            # Find the latest finishing dependency
            latest_dep = None
            latest_end = datetime.date.min
            for dep_id in current_task.dependencies:
                dep = self.tasks[dep_id]
                if dep.end_date > latest_end:
                    latest_end = dep.end_date
                    latest_dep = dep
                    
            if latest_dep:
                current_tasks.append(latest_dep)
                
        return list(reversed(critical_path))
    
    def print_schedule(self) -> None:
        """Print the project schedule in a readable format."""
        if not all(task.end_date for task in self.tasks.values()):
            self.calculate_schedule()
            
        print(f"\nProject: {self.name}")
        print(f"Start Date: {self.start_date}\n")
        print("{:<10} {:<30} {:<15} {:<15} {:<15}".format(
            "Task ID", "Task Name", "Start Date", "End Date", "Duration"))
        print("-" * 85)
        
        for task in sorted(self.tasks.values(), key=lambda t: t.start_date):
            print("{:<10} {:<30} {:<15} {:<15} {:<15}".format(
                task.id,
                task.name,
                str(task.start_date),
                str(task.end_date),
                f"{task.duration} days" if not task.is_milestone else "Milestone"
            ))

# Example usage for INARO S.A.S construction project
if __name__ == "__main__":
    # Create project
    project = ConstructionProject("INARO Office Building Construction")
    
    # Set project start date
    project.set_project_start(datetime.date(2023, 1, 1))
    
    # Add tasks (with dependencies where applicable)
    project.add_task(Task("T1", "Site Preparation", 10, dependencies=[]))
    project.add_task(Task("T2", "Foundation Work", 15, dependencies=["T1"]))
    project.add_task(Task("T3", "Structural Steel", 20, dependencies=["T2"]))
    project.add_task(Task("T4", "Exterior Walls", 25, dependencies=["T3"]))
    project.add_task(Task("T5", "Roofing", 10, dependencies=["T3"]))
    project.add_task(Task("T6", "Interior Finishing", 30, dependencies=["T4", "T5"]))
    project.add_task(Task("T7", "Electrical Work", 15, dependencies=["T3"]))
    project.add_task(Task("T8", "Plumbing", 15, dependencies=["T3"]))
    project.add_task(Task("T9", "HVAC Installation", 20, dependencies=["T3"]))
    project.add_task(Task("T10", "Final Inspection", 0, dependencies=["T6", "T7", "T8", "T9"], is_milestone=True))
    
    # Calculate and print schedule
    project.calculate_schedule()
    project.print_schedule()
    
    # Print critical path
    print("\nCritical Path:")
    for task in project.get_critical_path():
        print(f"{task.id}: {task.name} ({task.start_date} to {task.end_date})")
```
