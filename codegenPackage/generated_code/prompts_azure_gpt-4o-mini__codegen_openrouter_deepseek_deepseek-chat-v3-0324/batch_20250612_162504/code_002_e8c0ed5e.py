"""
Generated Code Metadata:
========================
Original URL: https://www.metis-labs.com
Prompt: Create a project plan for implementing a bespoke cloud solution that evolves with business growth, based on the collaborative approach of Metis Labs.
Generated: DETERMINISTIC_e8c0ed5e9b32ff0e
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Plan for Bespoke Cloud Solution Implementation

This script outlines a project plan for implementing a scalable cloud solution
using a collaborative approach inspired by Metis Labs. It includes phases,
milestones, and key deliverables.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json

class ProjectPhase:
    """Represents a phase in the project plan with its attributes."""
    
    def __init__(self, name: str, description: str, duration: timedelta, 
                 dependencies: Optional[List[str]] = None):
        """
        Initialize a project phase.
        
        Args:
            name: Name of the phase
            description: Description of what the phase entails
            duration: Estimated time to complete the phase
            dependencies: List of phase names this phase depends on
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.dependencies = dependencies or []
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
    
    def to_dict(self) -> Dict:
        """Convert phase to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "duration_days": self.duration.days,
            "dependencies": self.dependencies,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None
        }

class ProjectPlan:
    """Manages the complete project plan with all phases."""
    
    def __init__(self, name: str, start_date: datetime):
        """
        Initialize the project plan.
        
        Args:
            name: Name of the project
            start_date: Planned start date of the project
        """
        self.name = name
        self.start_date = start_date
        self.phases: Dict[str, ProjectPhase] = {}
    
    def add_phase(self, phase: ProjectPhase) -> None:
        """Add a phase to the project plan."""
        if phase.name in self.phases:
            raise ValueError(f"Phase '{phase.name}' already exists in the project plan")
        self.phases[phase.name] = phase
    
    def calculate_schedule(self) -> None:
        """Calculate start and end dates for all phases based on dependencies."""
        scheduled_phases = set()
        
        def schedule_phase(phase_name: str) -> datetime:
            """Recursively schedule a phase and its dependencies."""
            if phase_name in scheduled_phases:
                return self.phases[phase_name].end_date
            
            phase = self.phases[phase_name]
            
            # Schedule dependencies first
            dependency_end_dates = []
            for dep in phase.dependencies:
                if dep not in self.phases:
                    raise ValueError(f"Dependency '{dep}' not found for phase '{phase_name}'")
                dep_end_date = schedule_phase(dep)
                dependency_end_dates.append(dep_end_date)
            
            # Phase starts after last dependency ends
            if dependency_end_dates:
                phase.start_date = max(dependency_end_dates)
            else:
                phase.start_date = self.start_date
            
            phase.end_date = phase.start_date + phase.duration
            scheduled_phases.add(phase_name)
            return phase.end_date
        
        # Schedule all phases
        for phase_name in self.phases:
            if phase_name not in scheduled_phases:
                schedule_phase(phase_name)
    
    def to_json(self) -> str:
        """Serialize the project plan to JSON."""
        plan_dict = {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "phases": [phase.to_dict() for phase in self.phases.values()]
        }
        return json.dumps(plan_dict, indent=2)
    
    def print_gantt_chart(self) -> None:
        """Print a simple text-based Gantt chart of the project plan."""
        print(f"Project: {self.name}")
        print(f"Start Date: {self.start_date.date()}\n")
        
        print("Phases:")
        for phase in sorted(self.phases.values(), key=lambda p: p.start_date):
            print(f"{phase.name}:")
            print(f"  Description: {phase.description}")
            print(f"  Start: {phase.start_date.date()}")
            print(f"  End: {phase.end_date.date()}")
            print(f"  Duration: {phase.duration.days} days")
            if phase.dependencies:
                print(f"  Depends on: {', '.join(phase.dependencies)}")
            print()

def create_metis_cloud_plan() -> ProjectPlan:
    """Create a project plan for the bespoke cloud solution implementation."""
    plan = ProjectPlan(
        name="Bespoke Cloud Solution Implementation",
        start_date=datetime.now()
    )
    
    # Define project phases
    phases = [
        ProjectPhase(
            name="Discovery & Assessment",
            description="Collaborative workshops to understand business needs and current infrastructure",
            duration=timedelta(days=14)
        ),
        ProjectPhase(
            name="Architecture Design",
            description="Design scalable cloud architecture with growth in mind",
            duration=timedelta(days=21),
            dependencies=["Discovery & Assessment"]
        ),
        ProjectPhase(
            name="Proof of Concept",
            description="Implement a small-scale proof of concept to validate design",
            duration=timedelta(days=28),
            dependencies=["Architecture Design"]
        ),
        ProjectPhase(
            name="Core Implementation",
            description="Implement the core cloud infrastructure and services",
            duration=timedelta(days=60),
            dependencies=["Proof of Concept"]
        ),
        ProjectPhase(
            name="Integration & Migration",
            description="Integrate with existing systems and migrate data",
            duration=timedelta(days=45),
            dependencies=["Core Implementation"]
        ),
        ProjectPhase(
            name="Testing & Optimization",
            description="Comprehensive testing and performance optimization",
            duration=timedelta(days=30),
            dependencies=["Integration & Migration"]
        ),
        ProjectPhase(
            name="Deployment & Go-Live",
            description="Deploy solution to production environment",
            duration=timedelta(days=7),
            dependencies=["Testing & Optimization"]
        ),
        ProjectPhase(
            name="Monitoring & Evolution",
            description="Ongoing monitoring and iterative improvements",
            duration=timedelta(days=90),
            dependencies=["Deployment & Go-Live"]
        )
    ]
    
    # Add phases to plan
    for phase in phases:
        plan.add_phase(phase)
    
    # Calculate schedule
    plan.calculate_schedule()
    
    return plan

if __name__ == "__main__":
    try:
        # Create and display the project plan
        project_plan = create_metis_cloud_plan()
        project_plan.print_gantt_chart()
        
        # Optionally save to JSON
        with open("cloud_solution_plan.json", "w") as f:
            f.write(project_plan.to_json())
            
    except Exception as e:
        print(f"Error generating project plan: {str(e)}")
```
