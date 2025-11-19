"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Write a script to model logistics and installation planning for air treatment systems in modern facilities, inspired by BerlinerLuft's new headquarters in Alvorada/Rio Grande do Sul.
Generated: DETERMINISTIC_dab4a959a846ad2d
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Air Treatment System Logistics and Installation Planner

This script models the logistics and installation planning for air treatment systems
in modern facilities, inspired by BerlinerLuft's new headquarters in Alvorada/RS.

Features:
- Facility layout modeling
- Equipment requirements calculation
- Installation scheduling
- Resource allocation
- Cost estimation
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum, auto
import math


class SystemType(Enum):
    """Types of air treatment systems"""
    VENTILATION = auto()
    AIR_CONDITIONING = auto()
    PURIFICATION = auto()
    HUMIDIFICATION = auto()
    DEHUMIDIFICATION = auto()


class InstallationPhase(Enum):
    """Phases of installation process"""
    PLANNING = auto()
    SITE_PREP = auto()
    EQUIPMENT_DELIVERY = auto()
    INSTALLATION = auto()
    TESTING = auto()
    COMMISSIONING = auto()


@dataclass
class Facility:
    """Represents a facility where systems will be installed"""
    name: str
    location: str
    total_area: float  # in square meters
    floor_count: int
    rooms: List[Dict] = field(default_factory=list)
    existing_systems: List[str] = field(default_factory=list)


@dataclass
class AirTreatmentSystem:
    """Represents an air treatment system to be installed"""
    system_id: str
    system_type: SystemType
    coverage_area: float  # in square meters
    power_requirements: float  # in kW
    installation_time: float  # in hours
    unit_cost: float  # in local currency


@dataclass
class InstallationTask:
    """Represents a task in the installation process"""
    task_id: str
    phase: InstallationPhase
    description: str
    duration: timedelta
    dependencies: List[str] = field(default_factory=list)
    assigned_team: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    completed: bool = False


class InstallationPlanner:
    """Main class for planning air treatment system installations"""
    
    def __init__(self, facility: Facility):
        self.facility = facility
        self.systems: List[AirTreatmentSystem] = []
        self.tasks: List[InstallationTask] = []
        self.teams: Dict[str, List[str]] = {}  # team_name: [members]
        self.resources: Dict[str, int] = {}  # resource_type: quantity
        
    def add_system(self, system: AirTreatmentSystem) -> None:
        """Add an air treatment system to the plan"""
        self.systems.append(system)
        
    def calculate_system_requirements(self) -> Dict:
        """Calculate the number of units needed for each system type"""
        requirements = {}
        total_area = self.facility.total_area
        
        for system in self.systems:
            units_needed = math.ceil(total_area / system.coverage_area)
            requirements[system.system_type.name] = {
                'units': units_needed,
                'total_power': units_needed * system.power_requirements,
                'total_cost': units_needed * system.unit_cost
            }
            
        return requirements
    
    def create_installation_plan(self, start_date: datetime) -> List[InstallationTask]:
        """Create a timeline of installation tasks"""
        # Base tasks for any installation
        base_tasks = [
            InstallationTask(
                task_id="T001",
                phase=InstallationPhase.PLANNING,
                description="Initial site assessment and planning",
                duration=timedelta(days=3)
            ),
            InstallationTask(
                task_id="T002",
                phase=InstallationPhase.SITE_PREP,
                description="Site preparation and infrastructure setup",
                duration=timedelta(days=5),
                dependencies=["T001"]
            ),
            InstallationTask(
                task_id="T003",
                phase=InstallationPhase.EQUIPMENT_DELIVERY,
                description="Equipment delivery and inventory",
                duration=timedelta(days=2),
                dependencies=["T002"]
            )
        ]
        
        # System-specific installation tasks
        system_tasks = []
        for i, system in enumerate(self.systems, start=1):
            system_tasks.append(
                InstallationTask(
                    task_id=f"T1{i:02d}",
                    phase=InstallationPhase.INSTALLATION,
                    description=f"Install {system.system_type.name} system",
                    duration=timedelta(hours=system.installation_time),
                    dependencies=["T003"]
                )
            )
        
        # Final tasks
        final_tasks = [
            InstallationTask(
                task_id="T100",
                phase=InstallationPhase.TESTING,
                description="System testing and calibration",
                duration=timedelta(days=2),
                dependencies=[f"T1{i:02d}" for i in range(1, len(self.systems)+1)]
            ),
            InstallationTask(
                task_id="T101",
                phase=InstallationPhase.COMMISSIONING,
                description="System commissioning and handover",
                duration=timedelta(days=1),
                dependencies=["T100"]
            )
        ]
        
        all_tasks = base_tasks + system_tasks + final_tasks
        self._schedule_tasks(all_tasks, start_date)
        self.tasks = all_tasks
        return all_tasks
    
    def _schedule_tasks(self, tasks: List[InstallationTask], start_date: datetime) -> None:
        """Schedule tasks based on dependencies"""
        task_map = {task.task_id: task for task in tasks}
        
        for task in tasks:
            if not task.dependencies:
                task.start_date = start_date
                task.end_date = start_date + task.duration
            else:
                latest_end = start_date
                for dep_id in task.dependencies:
                    dep_task = task_map[dep_id]
                    if dep_task.end_date and dep_task.end_date > latest_end:
                        latest_end = dep_task.end_date
                task.start_date = latest_end
                task.end_date = latest_end + task.duration
    
    def assign_resources(self, team_assignments: Dict[str, List[str]]) -> None:
        """Assign teams to tasks"""
        for task_id, team_name in team_assignments.items():
            task = next((t for t in self.tasks if t.task_id == task_id), None)
            if task:
                task.assigned_team = team_name
    
    def calculate_total_cost(self) -> float:
        """Calculate total estimated cost of installation"""
        requirements = self.calculate_system_requirements()
        system_costs = sum(req['total_cost'] for req in requirements.values())
        
        # Estimate labor costs (simplified)
        labor_days = sum((task.end_date - task.start_date).days for task in self.tasks)
        labor_cost = labor_days * 800  # Assuming 800 currency units per day
        
        return system_costs + labor_cost
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive installation report"""
        requirements = self.calculate_system_requirements()
        total_cost = self.calculate_total_cost()
        
        return {
            "facility": {
                "name": self.facility.name,
                "location": self.facility.location,
                "total_area": self.facility.total_area
            },
            "system_requirements": requirements,
            "installation_timeline": [
                {
                    "task_id": task.task_id,
                    "description": task.description,
                    "phase": task.phase.name,
                    "start_date": task.start_date.isoformat() if task.start_date else None,
                    "end_date": task.end_date.isoformat() if task.end_date else None,
                    "assigned_team": task.assigned_team
                }
                for task in self.tasks
            ],
            "total_estimated_cost": total_cost,
            "estimated_completion_date": max(
                task.end_date for task in self.tasks if task.end_date
            ).isoformat() if self.tasks else None
        }
    
    def save_plan(self, filename: str) -> None:
        """Save the installation plan to a JSON file"""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)


# Example usage
if __name__ == "__main__":
    # Create a facility (inspired by BerlinerLuft's HQ)
    facility = Facility(
        name="BerlinerLuft Headquarters",
        location="Alvorada, Rio Grande do Sul",
        total_area=2500,
        floor_count=3,
        rooms=[
            {"name": "Reception", "area": 120},
            {"name": "Open Office", "area": 800},
            {"name": "Meeting Rooms", "area": 300},
            {"name": "Laboratory", "area": 200}
        ],
        existing_systems=["Basic ventilation"]
    )
    
    # Create systems to be installed
    systems = [
        AirTreatmentSystem(
            system
