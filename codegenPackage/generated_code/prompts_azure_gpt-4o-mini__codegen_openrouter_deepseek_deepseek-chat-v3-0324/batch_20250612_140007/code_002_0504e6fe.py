"""
Generated Code Metadata:
========================
Original URL: https://kraken-ec.com
Prompt: Create a sample project plan for developing an e-commerce website, including phases like planning, design, and launch, based on the project management approach described by Kraken Digital.
Generated: DETERMINISTIC_0504e6feea9417d7
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Project Plan for E-commerce Website Development
Based on Kraken Digital's Project Management Approach
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum, auto

class PhaseStatus(Enum):
    """Enum for tracking phase status"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    BLOCKED = auto()

class ProjectPhase:
    """Class representing a project phase"""
    def __init__(self, name: str, description: str, duration_days: int, dependencies: List[str] = None):
        self.name = name
        self.description = description
        self.duration_days = duration_days
        self.dependencies = dependencies or []
        self.status = PhaseStatus.NOT_STARTED
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        
    def set_dates(self, start_date: datetime) -> None:
        """Calculate and set phase dates based on start date"""
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration_days)
        
    def __str__(self) -> str:
        return f"{self.name} ({self.status.name}): {self.start_date} - {self.end_date}"

class ProjectPlan:
    """Class representing the complete project plan"""
    def __init__(self, name: str, start_date: datetime):
        self.name = name
        self.start_date = start_date
        self.phases: Dict[str, ProjectPhase] = {}
        self.current_date = start_date
        
    def add_phase(self, phase: ProjectPhase) -> None:
        """Add a phase to the project plan"""
        self.phases[phase.name] = phase
        
    def generate_timeline(self) -> None:
        """Generate the project timeline by calculating phase dates"""
        # Process phases in order, respecting dependencies
        processed_phases = set()
        
        while len(processed_phases) < len(self.phases):
            for phase_name, phase in self.phases.items():
                if phase_name in processed_phases:
                    continue
                    
                # Check if all dependencies are processed
                all_deps_processed = all(
                    dep in processed_phases for dep in phase.dependencies
                )
                
                if all_deps_processed or not phase.dependencies:
                    # Set dates for this phase
                    if phase.dependencies:
                        # Start after last dependency ends
                        last_dep_end = max(
                            self.phases[dep].end_date for dep in phase.dependencies
                        )
                        phase.set_dates(last_dep_end)
                    else:
                        phase.set_dates(self.current_date)
                    
                    processed_phases.add(phase_name)
                    self.current_date = phase.end_date
        
    def print_plan(self) -> None:
        """Print the project plan in a readable format"""
        print(f"Project: {self.name}")
        print(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}")
        print("\nPhases:")
        for phase in self.phases.values():
            print(f"- {phase}")
            
    def get_gantt_data(self) -> List[Dict]:
        """Return data suitable for Gantt chart visualization"""
        return [
            {
                "phase": phase.name,
                "start": phase.start_date.strftime('%Y-%m-%d'),
                "end": phase.end_date.strftime('%Y-%m-%d'),
                "status": phase.status.name,
                "duration": phase.duration_days
            }
            for phase in self.phases.values()
        ]

def create_ecommerce_project_plan() -> ProjectPlan:
    """Create a sample e-commerce project plan"""
    project_start = datetime(2023, 1, 1)
    plan = ProjectPlan("E-commerce Website Development", project_start)
    
    # Define project phases
    phases = [
        ProjectPhase(
            "Discovery",
            "Requirements gathering and project planning",
            10
        ),
        ProjectPhase(
            "UX/UI Design",
            "Wireframing, prototyping, and visual design",
            15,
            ["Discovery"]
        ),
        ProjectPhase(
            "Frontend Development",
            "Implementing user interfaces and client-side functionality",
            30,
            ["UX/UI Design"]
        ),
        ProjectPhase(
            "Backend Development",
            "Server-side development, database design, and API creation",
            40,
            ["Discovery"]
        ),
        ProjectPhase(
            "Integration",
            "Connecting frontend and backend systems",
            10,
            ["Frontend Development", "Backend Development"]
        ),
        ProjectPhase(
            "Testing",
            "Quality assurance and user acceptance testing",
            15,
            ["Integration"]
        ),
        ProjectPhase(
            "Content Population",
            "Adding products, categories, and other content",
            10,
            ["Integration"]
        ),
        ProjectPhase(
            "Security Review",
            "Penetration testing and security audit",
            7,
            ["Testing"]
        ),
        ProjectPhase(
            "Performance Optimization",
            "Load testing and performance improvements",
            5,
            ["Testing"]
        ),
        ProjectPhase(
            "Launch Preparation",
            "Final deployment preparations and documentation",
            5,
            ["Security Review", "Performance Optimization", "Content Population"]
        ),
        ProjectPhase(
            "Soft Launch",
            "Limited release to a small user group",
            7,
            ["Launch Preparation"]
        ),
        ProjectPhase(
            "Full Launch",
            "Public release and marketing campaign",
            3,
            ["Soft Launch"]
        ),
        ProjectPhase(
            "Post-Launch Support",
            "Monitoring and initial bug fixes",
            30,
            ["Full Launch"]
        )
    ]
    
    # Add phases to plan
    for phase in phases:
        plan.add_phase(phase)
    
    # Generate timeline
    plan.generate_timeline()
    
    return plan

if __name__ == "__main__":
    # Create and display the project plan
    ecommerce_plan = create_ecommerce_project_plan()
    ecommerce_plan.print_plan()
    
    # Example of accessing Gantt data
    # gantt_data = ecommerce_plan.get_gantt_data()
    # print("\nGantt Data:")
    # print(gantt_data)
```
