"""
Generated Code Metadata:
========================
Original URL: https://digitaldhara.com
Prompt: "Generate a Mobile & Web Development project plan using Digital Dhara's 10+ years of experience in frontend web development and mobile app development."
Generated: DETERMINISTIC_b1a5ee4fb7532f9e
Batch ID: 20250622_211550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Dhara Project Plan Generator
This script generates a comprehensive project plan for Mobile & Web Development projects
based on Digital Dhara's 10+ years of experience in frontend web and mobile development.
"""

from datetime import datetime, timedelta
from enum import Enum
import json
from typing import List, Dict, Optional

class ProjectType(Enum):
    WEB = "Web Development"
    MOBILE = "Mobile App Development"
    HYBRID = "Hybrid (Web + Mobile)"

class ProjectPhase(Enum):
    DISCOVERY = "Discovery"
    DESIGN = "Design"
    DEVELOPMENT = "Development"
    TESTING = "Testing"
    DEPLOYMENT = "Deployment"
    MAINTENANCE = "Maintenance"

class TechnologyStack(Enum):
    FRONTEND = ["React", "Angular", "Vue.js", "HTML5/CSS3/JS"]
    MOBILE = ["React Native", "Flutter", "Swift (iOS)", "Kotlin (Android)"]
    BACKEND = ["Node.js", "Django", "Spring Boot", "Laravel"]
    DATABASE = ["PostgreSQL", "MySQL", "MongoDB", "Firebase"]

class ProjectPlan:
    def __init__(self, project_name: str, project_type: ProjectType, duration_weeks: int):
        """
        Initialize a new project plan
        :param project_name: Name of the project
        :param project_type: Type of project (WEB, MOBILE, HYBRID)
        :param duration_weeks: Estimated duration in weeks
        """
        self.project_name = project_name
        self.project_type = project_type
        self.duration_weeks = duration_weeks
        self.start_date = datetime.now().date()
        self.phases: List[Dict] = []
        self.technology_stack: List[str] = []
        self.team: List[str] = []
        self.risks: List[str] = []
        self.assumptions: List[str] = []

    def add_phase(self, phase: ProjectPhase, duration_days: int, description: str) -> None:
        """Add a phase to the project plan"""
        self.phases.append({
            "phase": phase.value,
            "duration_days": duration_days,
            "description": description,
            "tasks": []
        })

    def add_task_to_phase(self, phase_name: str, task: str, owner: str) -> None:
        """Add a task to a specific phase"""
        for phase in self.phases:
            if phase["phase"] == phase_name:
                phase["tasks"].append({"task": task, "owner": owner})
                return
        raise ValueError(f"Phase '{phase_name}' not found")

    def set_technology_stack(self, stack: List[str]) -> None:
        """Set the technology stack for the project"""
        self.technology_stack = stack

    def add_team_member(self, role: str, name: str) -> None:
        """Add a team member to the project"""
        self.team.append({"role": role, "name": name})

    def add_risk(self, risk: str, mitigation: str) -> None:
        """Add a risk with mitigation strategy"""
        self.risks.append({"risk": risk, "mitigation": mitigation})

    def add_assumption(self, assumption: str) -> None:
        """Add an assumption to the project"""
        self.assumptions.append(assumption)

    def generate_timeline(self) -> List[Dict]:
        """Generate project timeline with dates"""
        timeline = []
        current_date = self.start_date
        
        for phase in self.phases:
            end_date = current_date + timedelta(days=phase["duration_days"])
            timeline.append({
                "phase": phase["phase"],
                "start_date": current_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "duration_days": phase["duration_days"]
            })
            current_date = end_date + timedelta(days=1)  # Start next phase the day after
            
        return timeline

    def to_json(self) -> str:
        """Convert project plan to JSON format"""
        plan = {
            "project_name": self.project_name,
            "project_type": self.project_type.value,
            "duration_weeks": self.duration_weeks,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "phases": self.phases,
            "technology_stack": self.technology_stack,
            "team": self.team,
            "risks": self.risks,
            "assumptions": self.assumptions,
            "timeline": self.generate_timeline()
        }
        return json.dumps(plan, indent=2)

def create_sample_web_project() -> ProjectPlan:
    """Create a sample web development project plan"""
    project = ProjectPlan(
        project_name="E-commerce Platform",
        project_type=ProjectType.WEB,
        duration_weeks=16
    )
    
    # Add phases
    project.add_phase(ProjectPhase.DISCOVERY.value, 10, "Requirements gathering and analysis")
    project.add_phase(ProjectPhase.DESIGN.value, 14, "UI/UX design and prototyping")
    project.add_phase(ProjectPhase.DEVELOPMENT.value, 40, "Frontend and backend development")
    project.add_phase(ProjectPhase.TESTING.value, 14, "Quality assurance and user testing")
    project.add_phase(ProjectPhase.DEPLOYMENT.value, 7, "Production deployment")
    project.add_phase(ProjectPhase.MAINTENANCE.value, 30, "Post-launch support and maintenance")

    # Add tasks to phases
    project.add_task_to_phase("Discovery", "Conduct stakeholder interviews", "PM")
    project.add_task_to_phase("Discovery", "Define user personas", "UX Designer")
    project.add_task_to_phase("Design", "Create wireframes", "UX Designer")
    project.add_task_to_phase("Design", "Develop UI components", "UI Designer")
    project.add_task_to_phase("Development", "Implement frontend", "Frontend Dev")
    project.add_task_to_phase("Development", "Build API endpoints", "Backend Dev")
    project.add_task_to_phase("Testing", "Perform integration testing", "QA Engineer")
    project.add_task_to_phase("Deployment", "Configure production environment", "DevOps")

    # Set technology stack
    project.set_technology_stack([
        TechnologyStack.FRONTEND.value[0],  # React
        TechnologyStack.BACKEND.value[0],   # Node.js
        TechnologyStack.DATABASE.value[0]   # PostgreSQL
    ])

    # Add team members
    project.add_team_member("Project Manager", "John Doe")
    project.add_team_member("UX Designer", "Jane Smith")
    project.add_team_member("Frontend Developer", "Mike Johnson")
    project.add_team_member("Backend Developer", "Sarah Williams")
    project.add_team_member("QA Engineer", "David Brown")

    # Add risks
    project.add_risk("Scope creep", "Implement change control process")
    project.add_risk("Third-party API delays", "Identify fallback options early")

    # Add assumptions
    project.add_assumption("Client will provide content by design phase completion")
    project.add_assumption("Stakeholders will be available for weekly check-ins")

    return project

if __name__ == "__main__":
    try:
        # Generate a sample project plan
        project = create_sample_web_project()
        
        # Output the project plan as JSON
        print(project.to_json())
        
        # Optionally save to file
        with open("project_plan.json", "w") as f:
            f.write(project.to_json())
            
    except Exception as e:
        print(f"Error generating project plan: {str(e)}")
```
