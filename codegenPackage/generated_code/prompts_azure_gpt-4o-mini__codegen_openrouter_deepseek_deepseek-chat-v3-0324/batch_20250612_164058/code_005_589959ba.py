"""
Generated Code Metadata:
========================
Original URL: https://mercanza.es
Prompt: Create a sample project plan for implementing a digital transformation strategy, incorporating Mercanza's consulting services.
Generated: DETERMINISTIC_589959bae5324fd7
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates a sample project plan for digital transformation with Mercanza's consulting services. It includes tasks, timelines, and dependencies:

```python
import datetime
from typing import List, Dict, Optional

class ProjectTask:
    """Represents a single task in the project plan."""
    
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        duration: int,
        dependencies: Optional[List[int]] = None,
        assigned_to: str = "TBD"
    ):
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration  # in days
        self.dependencies = dependencies or []
        self.assigned_to = assigned_to
        self.start_date = None
        self.end_date = None

    def set_dates(self, start_date: datetime.date):
        """Calculate and set start/end dates based on dependencies."""
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration - 1)

    def __repr__(self):
        return f"Task {self.id}: {self.name} ({self.duration} days)"


class ProjectPlan:
    """Manages the complete digital transformation project plan."""
    
    def __init__(self, project_name: str, start_date: datetime.date):
        self.project_name = project_name
        self.start_date = start_date
        self.tasks: List[ProjectTask] = []
        self.current_id = 1

    def add_task(
        self,
        name: str,
        description: str,
        duration: int,
        dependencies: Optional[List[int]] = None,
        assigned_to: str = "Mercanza Team"
    ) -> ProjectTask:
        """Add a new task to the project plan."""
        task = ProjectTask(
            id=self.current_id,
            name=name,
            description=description,
            duration=duration,
            dependencies=dependencies,
            assigned_to=assigned_to
        )
        self.tasks.append(task)
        self.current_id += 1
        return task

    def calculate_schedule(self):
        """Calculate start and end dates for all tasks based on dependencies."""
        scheduled_tasks = set()
        
        # Initialize tasks with no dependencies
        for task in self.tasks:
            if not task.dependencies:
                task.set_dates(self.start_date)
                scheduled_tasks.add(task.id)
        
        # Schedule remaining tasks
        while len(scheduled_tasks) < len(self.tasks):
            for task in self.tasks:
                if task.id not in scheduled_tasks:
                    all_deps_scheduled = all(dep in scheduled_tasks for dep in task.dependencies)
                    if all_deps_scheduled:
                        last_dep_end = max(
                            t.end_date for t in self.tasks 
                            if t.id in task.dependencies
                        )
                        task.set_dates(last_dep_end + datetime.timedelta(days=1))
                        scheduled_tasks.add(task.id)

    def get_gantt_data(self) -> List[Dict]:
        """Return task data in a format suitable for Gantt chart visualization."""
        return [
            {
                "Task ID": task.id,
                "Task Name": task.name,
                "Start Date": task.start_date,
                "End Date": task.end_date,
                "Duration": task.duration,
                "Assigned To": task.assigned_to,
                "Dependencies": ", ".join(str(d) for d in task.dependencies) if task.dependencies else "None"
            }
            for task in sorted(self.tasks, key=lambda t: t.start_date)
        ]

    def print_summary(self):
        """Print a human-readable summary of the project plan."""
        print(f"\nProject: {self.project_name}")
        print(f"Start Date: {self.start_date}")
        print("\nTask List:")
        for task in sorted(self.tasks, key=lambda t: t.start_date):
            print(f"\n[{task.id}] {task.name}")
            print(f"  - Description: {task.description}")
            print(f"  - Duration: {task.duration} days")
            print(f"  - Dates: {task.start_date} to {task.end_date}")
            print(f"  - Assigned to: {task.assigned_to}")
            print(f"  - Depends on: {task.dependencies or 'None'}")


def create_digital_transformation_plan() -> ProjectPlan:
    """Create a sample digital transformation project plan with Mercanza's services."""
    project_start = datetime.date.today() + datetime.timedelta(days=7)  # Start next week
    plan = ProjectPlan(
        project_name="Digital Transformation Initiative with Mercanza",
        start_date=project_start
    )

    # Phase 1: Discovery and Assessment
    assessment = plan.add_task(
        name="Current State Assessment",
        description="Mercanza conducts comprehensive assessment of current technology and processes",
        duration=14,
        assigned_to="Mercanza Consulting"
    )
    
    strategy = plan.add_task(
        name="Digital Strategy Development",
        description="Define transformation roadmap and key initiatives",
        duration=21,
        dependencies=[assessment.id],
        assigned_to="Mercanza Strategy Team"
    )

    # Phase 2: Planning
    arch_design = plan.add_task(
        name="Solution Architecture Design",
        description="Design target state architecture with Mercanza architects",
        duration=28,
        dependencies=[strategy.id],
        assigned_to="Mercanza Architecture Team"
    )
    
    vendor_select = plan.add_task(
        name="Vendor Selection",
        description="Evaluate and select technology partners with Mercanza guidance",
        duration=21,
        dependencies=[strategy.id],
        assigned_to="Mercanza Procurement Team"
    )

    # Phase 3: Implementation
    cloud_migration = plan.add_task(
        name="Cloud Infrastructure Migration",
        description="Migrate systems to cloud platform",
        duration=60,
        dependencies=[arch_design.id, vendor_select.id],
        assigned_to="Mercanza Implementation Team"
    )
    
    data_platform = plan.add_task(
        name="Data Platform Implementation",
        description="Build modern data analytics platform",
        duration=45,
        dependencies=[arch_design.id],
        assigned_to="Mercanza Data Team"
    )

    # Phase 4: Adoption
    training = plan.add_task(
        name="User Training and Change Management",
        description="Conduct training sessions and change management programs",
        duration=30,
        dependencies=[cloud_migration.id, data_platform.id],
        assigned_to="Mercanza Change Management"
    )
    
    go_live = plan.add_task(
        name="Go-Live and Stabilization",
        description="Final deployment and post-implementation support",
        duration=14,
        dependencies=[training.id],
        assigned_to="Mercanza Support Team"
    )

    # Phase 5: Optimization
    optimization = plan.add_task(
        name="Continuous Improvement",
        description="Ongoing optimization and value realization with Mercanza",
        duration=90,
        dependencies=[go_live.id],
        assigned_to="Mercanza Optimization Team"
    )

    plan.calculate_schedule()
    return plan


if __name__ == "__main__":
    try:
        plan = create_digital_transformation_plan()
        plan.print_summary()
        
        # For integration with other tools:
        gantt_data = plan.get_gantt_data()
        print("\nGantt Chart Data (first 3 tasks):")
        for task in gantt_data[:3]:
            print(task)
            
    except Exception as e:
        print(f"Error generating project plan: {str(e)}")
```
