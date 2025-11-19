"""
Generated Code Metadata:
========================
Original URL: https://webbcode.com
Prompt: Write Python code to automate a workflow for a business using the agile process steps (Concept, Design, Development, Testing & Feedback, Release) as described by WebbCode Ltd.
Generated: DETERMINISTIC_7e714fc1d002bf45
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AgilePhase(Enum):
    """Enum representing the agile process phases."""
    CONCEPT = "Concept"
    DESIGN = "Design"
    DEVELOPMENT = "Development"
    TESTING_FEEDBACK = "Testing & Feedback"
    RELEASE = "Release"

@dataclass
class Task:
    """Represents a task in the agile workflow."""
    name: str
    description: str
    phase: AgilePhase
    assigned_to: str
    due_date: datetime
    is_completed: bool = False
    dependencies: List[str] = field(default_factory=list)

@dataclass
class Project:
    """Represents a project with agile workflow."""
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    tasks: Dict[str, Task] = field(default_factory=dict)
    current_phase: AgilePhase = AgilePhase.CONCEPT

    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists in project.")
        self.tasks[task.name] = task
        logger.info(f"Added task '{task.name}' to project '{self.name}'")

    def complete_task(self, task_name: str) -> None:
        """Mark a task as completed."""
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' not found in project.")
        self.tasks[task_name].is_completed = True
        logger.info(f"Completed task '{task_name}' in project '{self.name}'")

    def move_to_next_phase(self) -> None:
        """Move the project to the next agile phase."""
        current_phase_index = list(AgilePhase).index(self.current_phase)
        if current_phase_index >= len(AgilePhase) - 1:
            raise ValueError("Project is already in the final phase.")
        
        # Check if all tasks in current phase are completed
        current_phase_tasks = [
            t for t in self.tasks.values() 
            if t.phase == self.current_phase and not t.is_completed
        ]
        if current_phase_tasks:
            raise ValueError(
                f"Cannot move to next phase. {len(current_phase_tasks)} tasks "
                f"in {self.current_phase.value} phase are incomplete."
            )
        
        self.current_phase = list(AgilePhase)[current_phase_index + 1]
        logger.info(
            f"Project '{self.name}' moved to {self.current_phase.value} phase"
        )

    def get_project_status(self) -> Dict:
        """Get the current status of the project."""
        return {
            "project_name": self.name,
            "current_phase": self.current_phase.value,
            "total_tasks": len(self.tasks),
            "completed_tasks": sum(t.is_completed for t in self.tasks.values()),
            "phases": {
                phase.value: {
                    "total_tasks": sum(
                        1 for t in self.tasks.values() if t.phase == phase
                    ),
                    "completed_tasks": sum(
                        t.is_completed for t in self.tasks.values() 
                        if t.phase == phase
                    )
                }
                for phase in AgilePhase
            }
        }

class AgileWorkflowAutomation:
    """Main class to automate the agile workflow process."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
    
    def create_project(
        self,
        name: str,
        description: str,
        start_date: datetime,
        end_date: datetime
    ) -> Project:
        """Create a new project."""
        if name in self.projects:
            raise ValueError(f"Project '{name}' already exists.")
        
        project = Project(name, description, start_date, end_date)
        self.projects[name] = project
        logger.info(f"Created new project '{name}'")
        return project
    
    def get_project(self, name: str) -> Optional[Project]:
        """Get a project by name."""
        return self.projects.get(name)
    
    def save_to_file(self, filename: str) -> None:
        """Save projects to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {
                        name: {
                            "name": project.name,
                            "description": project.description,
                            "start_date": project.start_date.isoformat(),
                            "end_date": project.end_date.isoformat(),
                            "current_phase": project.current_phase.value,
                            "tasks": {
                                task_name: {
                                    "name": task.name,
                                    "description": task.description,
                                    "phase": task.phase.value,
                                    "assigned_to": task.assigned_to,
                                    "due_date": task.due_date.isoformat(),
                                    "is_completed": task.is_completed,
                                    "dependencies": task.dependencies
                                }
                                for task_name, task in project.tasks.items()
                            }
                        }
                        for name, project in self.projects.items()
                    },
                    f,
                    indent=2
                )
            logger.info(f"Saved projects to file '{filename}'")
        except Exception as e:
            logger.error(f"Error saving to file: {str(e)}")
            raise
    
    def load_from_file(self, filename: str) -> None:
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.projects.clear()
                
                for project_name, project_data in data.items():
                    project = Project(
                        name=project_data["name"],
                        description=project_data["description"],
                        start_date=datetime.fromisoformat(
                            project_data["start_date"]
                        ),
                        end_date=datetime.fromisoformat(
                            project_data["end_date"]
                        )
                    )
                    project.current_phase = AgilePhase(
                        project_data["current_phase"]
                    )
                    
                    for task_name, task_data in project_data["tasks"].items():
                        task = Task(
                            name=task_data["name"],
                            description=task_data["description"],
                            phase=AgilePhase(task_data["phase"]),
                            assigned_to=task_data["assigned_to"],
                            due_date=datetime.fromisoformat(
                                task_data["due_date"]
                            ),
                            is_completed=task_data["is_completed"],
                            dependencies=task_data["dependencies"]
                        )
                        project.tasks[task_name] = task
                    
                    self.projects[project_name] = project
            logger.info(f"Loaded projects from file '{filename}'")
        except Exception as e:
            logger.error(f"Error loading from file: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    workflow = AgileWorkflowAutomation()
    
    try:
        # Create a project
        project = workflow.create_project(
            name="Website Redesign",
            description="Redesign company website with modern UI/UX",
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=90)
        )
        
        # Add tasks for Concept phase
        project.add_task(Task(
            name="Market Research",
            description="Research current web design trends",
            phase=AgilePhase.CONCEPT,
            assigned_to="Product Manager",
            due_date=datetime.now() + timedelta(days=7)
        ))
        
        project.add_task(Task(
            name="Define Requirements",
            description="Document business and technical requirements",
            phase=AgilePhase.CONCEPT,
            assigned_to="Business Analyst",
            due_date=datetime.now() + timedelta(days=14),
            dependencies=["Market Research"]
        ))
        
        # Complete tasks and move to next phase
        project.complete_task("Market Research")
        project.complete_task("Define Requirements")
        project.move_to_next_phase()
        
        # Save to file
        workflow.save_to_file("projects.json")
        
        # Print project status
        print(json.dumps(project.get_project_status(), indent=2))
        
    except Exception as e:
        logger.error(f"Error in workflow automation: {str(e)}")
```
