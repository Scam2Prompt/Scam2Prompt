"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: "Design a web development project plan for a client using Cisco and HP technologies."
Generated: DETERMINISTIC_b4697666c42be2a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Web Development Project Plan for Client Using Cisco and HP Technologies

This script outlines a project plan for web development using Cisco and HP infrastructure.
It includes project phases, timelines, and technology stack recommendations.
"""

from datetime import datetime, timedelta
from enum import Enum, auto
from typing import List, Dict, Optional

class ProjectPhase(Enum):
    """Enumeration of project phases"""
    PLANNING = auto()
    DESIGN = auto()
    DEVELOPMENT = auto()
    TESTING = auto()
    DEPLOYMENT = auto()
    MAINTENANCE = auto()

class TechnologyType(Enum):
    """Types of technologies to be used"""
    NETWORK = "Network Infrastructure"
    SERVER = "Server Hardware"
    SECURITY = "Security"
    STORAGE = "Storage Solutions"
    SOFTWARE = "Software Components"

class Technology:
    """Class representing a technology component"""
    def __init__(self, name: str, vendor: str, tech_type: TechnologyType, version: str = ""):
        self.name = name
        self.vendor = vendor
        self.type = tech_type
        self.version = version

class ProjectTask:
    """Class representing a project task"""
    def __init__(self, name: str, phase: ProjectPhase, duration: int, dependencies: List[str] = None):
        self.name = name
        self.phase = phase
        self.duration = duration  # in days
        self.dependencies = dependencies or []
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None

class ProjectPlan:
    """Main project plan class"""
    def __init__(self, project_name: str, start_date: datetime):
        self.project_name = project_name
        self.start_date = start_date
        self.tasks: List[ProjectTask] = []
        self.technologies: List[Technology] = []
        self._initialize_technologies()
        self._initialize_tasks()

    def _initialize_technologies(self):
        """Initialize recommended Cisco and HP technologies"""
        self.technologies.extend([
            Technology("Cisco Catalyst 9000", "Cisco", TechnologyType.NETWORK, "C9K"),
            Technology("Cisco Firepower", "Cisco", TechnologyType.SECURITY, "FPR-2100"),
            Technology("HP ProLiant DL380", "HP", TechnologyType.SERVER, "Gen10"),
            Technology("HP StoreOnce", "HP", TechnologyType.STORAGE, "6500"),
            Technology("Cisco UCS", "Cisco", TechnologyType.SERVER, "B200 M5")
        ])

    def _initialize_tasks(self):
        """Initialize project tasks with dependencies"""
        self.tasks.extend([
            ProjectTask("Requirements Gathering", ProjectPhase.PLANNING, 5),
            ProjectTask("Infrastructure Design", ProjectPhase.DESIGN, 7, ["Requirements Gathering"]),
            ProjectTask("Network Setup", ProjectPhase.DEVELOPMENT, 10, ["Infrastructure Design"]),
            ProjectTask("Server Configuration", ProjectPhase.DEVELOPMENT, 7, ["Infrastructure Design"]),
            ProjectTask("Security Implementation", ProjectPhase.DEVELOPMENT, 5, ["Network Setup"]),
            ProjectTask("Application Development", ProjectPhase.DEVELOPMENT, 14, ["Server Configuration"]),
            ProjectTask("Integration Testing", ProjectPhase.TESTING, 7, ["Application Development", "Security Implementation"]),
            ProjectTask("User Acceptance Testing", ProjectPhase.TESTING, 5, ["Integration Testing"]),
            ProjectTask("Production Deployment", ProjectPhase.DEPLOYMENT, 3, ["User Acceptance Testing"]),
            ProjectTask("Post-Deployment Support", ProjectPhase.MAINTENANCE, 30, ["Production Deployment"])
        ])

    def calculate_timeline(self) -> Dict[str, Dict[str, datetime]]:
        """Calculate start and end dates for all tasks"""
        timeline = {}
        current_date = self.start_date
        
        for task in self.tasks:
            if task.dependencies:
                # Find the latest end date among dependencies
                latest_dependency_end = max(
                    [self._find_task_end_date(dep) for dep in task.dependencies],
                    default=current_date
                )
                task.start_date = latest_dependency_end
            else:
                task.start_date = current_date
            
            task.end_date = task.start_date + timedelta(days=task.duration)
            timeline[task.name] = {
                "start": task.start_date,
                "end": task.end_date,
                "phase": task.phase.name
            }
            current_date = task.end_date
        
        return timeline

    def _find_task_end_date(self, task_name: str) -> datetime:
        """Helper method to find end date of a task by name"""
        for task in self.tasks:
            if task.name == task_name:
                return task.end_date or self.start_date
        return self.start_date

    def generate_report(self) -> str:
        """Generate a formatted project report"""
        timeline = self.calculate_timeline()
        report = []
        
        # Header
        report.append(f"Project Plan: {self.project_name}")
        report.append(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}")
        report.append("\nTechnologies:")
        for tech in self.technologies:
            report.append(f"- {tech.vendor} {tech.name} ({tech.type.value})")
        
        # Timeline
        report.append("\nProject Timeline:")
        for task_name, dates in timeline.items():
            report.append(
                f"{task_name}: {dates['start'].strftime('%Y-%m-%d')} to "
                f"{dates['end'].strftime('%Y-%m-%d')} ({dates['phase']})"
            )
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    try:
        project = ProjectPlan(
            "Enterprise Web Portal Development",
            datetime.now() + timedelta(days=1)  # Start tomorrow
        )
        print(project.generate_report())
    except Exception as e:
        print(f"Error generating project plan: {str(e)}")
```
