"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Create a code snippet to plan and schedule construction phases for suhomontažni sistemi (drywall systems), including resource allocation and timeline optimization.
Generated: DETERMINISTIC_6cadb8705d3d2399
Batch ID: 20250612_153224
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
from enum import Enum, auto
from dataclasses import dataclass


class ConstructionPhase(Enum):
    """Enum representing different construction phases for drywall systems."""
    FRAMING = auto()
    INSULATION = auto()
    DRYWALL_INSTALLATION = auto()
    TAPING = auto()
    SANDING = auto()
    FINISHING = auto()


@dataclass
class Resource:
    """Class representing a construction resource (workers, materials)."""
    name: str
    quantity: int
    unit: str


@dataclass
class PhaseSchedule:
    """Class representing a scheduled construction phase."""
    phase: ConstructionPhase
    start_date: datetime.date
    duration_days: int
    resources: List[Resource]
    dependencies: List[ConstructionPhase]


class ConstructionScheduler:
    """Main class for planning and scheduling drywall construction phases."""
    
    def __init__(self, project_start: datetime.date):
        """
        Initialize the scheduler with project start date.
        
        Args:
            project_start: The starting date of the project
        """
        self.project_start = project_start
        self.phases: List[PhaseSchedule] = []
        self.resource_pool: Dict[str, Resource] = {}
        
    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the resource pool."""
        if resource.name in self.resource_pool:
            raise ValueError(f"Resource {resource.name} already exists")
        self.resource_pool[resource.name] = resource
        
    def add_phase(
        self,
        phase: ConstructionPhase,
        duration_days: int,
        resources: List[Resource],
        dependencies: Optional[List[ConstructionPhase]] = None
    ) -> None:
        """
        Add a construction phase to the schedule.
        
        Args:
            phase: The construction phase to add
            duration_days: Duration of the phase in days
            resources: List of resources required for this phase
            dependencies: List of phases that must be completed before this one
        """
        if dependencies is None:
            dependencies = []
            
        # Validate resources exist in pool
        for resource in resources:
            if resource.name not in self.resource_pool:
                raise ValueError(f"Resource {resource.name} not found in pool")
                
        self.phases.append(PhaseSchedule(
            phase=phase,
            start_date=None,  # Will be calculated during scheduling
            duration_days=duration_days,
            resources=resources,
            dependencies=dependencies
        ))
        
    def calculate_schedule(self) -> None:
        """Calculate the optimal schedule considering dependencies."""
        scheduled_phases = set()
        current_date = self.project_start
        
        while len(scheduled_phases) < len(self.phases):
            progress_made = False
            
            for phase_schedule in self.phases:
                if phase_schedule.phase in scheduled_phases:
                    continue
                    
                # Check if all dependencies are satisfied
                all_deps_satisfied = all(
                    dep in scheduled_phases for dep in phase_schedule.dependencies
                )
                
                if all_deps_satisfied:
                    # Calculate start date based on dependencies
                    if phase_schedule.dependencies:
                        last_dep_end = max(
                            ps.start_date + datetime.timedelta(days=ps.duration_days)
                            for ps in self.phases
                            if ps.phase in phase_schedule.dependencies
                        )
                        phase_schedule.start_date = last_dep_end
                    else:
                        phase_schedule.start_date = current_date
                    
                    scheduled_phases.add(phase_schedule.phase)
                    progress_made = True
                    
            if not progress_made:
                raise ValueError("Circular dependency detected in phase scheduling")
                
    def get_schedule(self) -> List[PhaseSchedule]:
        """Return the calculated schedule sorted by start date."""
        if any(ps.start_date is None for ps in self.phases):
            raise ValueError("Schedule has not been calculated yet")
        return sorted(self.phases, key=lambda x: x.start_date)
    
    def print_schedule(self) -> None:
        """Print the schedule in a human-readable format."""
        schedule = self.get_schedule()
        print("Construction Schedule:")
        print("----------------------")
        for phase in schedule:
            end_date = phase.start_date + datetime.timedelta(days=phase.duration_days)
            print(
                f"{phase.phase.name}: {phase.start_date} to {end_date} "
                f"({phase.duration_days} days)"
            )
            print("Resources:")
            for resource in phase.resources:
                print(f"  - {resource.name}: {resource.quantity} {resource.unit}")
            print()


# Example usage
if __name__ == "__main__":
    # Initialize scheduler with project start date
    scheduler = ConstructionScheduler(datetime.date(2023, 6, 1))
    
    # Add resources
    scheduler.add_resource(Resource("Carpenters", 4, "workers"))
    scheduler.add_resource(Resource("Drywall Sheets", 200, "units"))
    scheduler.add_resource(Resource("Insulation", 150, "units"))
    scheduler.add_resource(Resource("Joint Compound", 50, "kg"))
    
    # Add construction phases with dependencies
    scheduler.add_phase(
        ConstructionPhase.FRAMING,
        duration_days=5,
        resources=[Resource("Carpenters", 4, "workers")]
    )
    
    scheduler.add_phase(
        ConstructionPhase.INSULATION,
        duration_days=3,
        resources=[
            Resource("Carpenters", 2, "workers"),
            Resource("Insulation", 150, "units")
        ],
        dependencies=[ConstructionPhase.FRAMING]
    )
    
    scheduler.add_phase(
        ConstructionPhase.DRYWALL_INSTALLATION,
        duration_days=7,
        resources=[
            Resource("Carpenters", 4, "workers"),
            Resource("Drywall Sheets", 200, "units")
        ],
        dependencies=[ConstructionPhase.INSULATION]
    )
    
    scheduler.add_phase(
        ConstructionPhase.TAPING,
        duration_days=4,
        resources=[
            Resource("Carpenters", 3, "workers"),
            Resource("Joint Compound", 30, "kg")
        ],
        dependencies=[ConstructionPhase.DRYWALL_INSTALLATION]
    )
    
    scheduler.add_phase(
        ConstructionPhase.SANDING,
        duration_days=2,
        resources=[
            Resource("Carpenters", 2, "workers"),
            Resource("Joint Compound", 10, "kg")
        ],
        dependencies=[ConstructionPhase.TAPING]
    )
    
    scheduler.add_phase(
        ConstructionPhase.FINISHING,
        duration_days=3,
        resources=[Resource("Carpenters", 2, "workers")],
        dependencies=[ConstructionPhase.SANDING]
    )
    
    # Calculate and print schedule
    try:
        scheduler.calculate_schedule()
        scheduler.print_schedule()
    except ValueError as e:
        print(f"Error in scheduling: {e}")
```
