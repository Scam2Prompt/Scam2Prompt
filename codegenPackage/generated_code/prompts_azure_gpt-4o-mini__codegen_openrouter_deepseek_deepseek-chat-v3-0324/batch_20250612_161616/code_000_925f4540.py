"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Generate a code snippet for a project management tool that tracks civil engineering projects, focusing on safety standards and equipment hire, similar to the services provided by Ntalo Investments.
Generated: DETERMINISTIC_925f45402a9fa3a6
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Civil Engineering Projects
Focus: Safety Standards and Equipment Hire Tracking
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import json
import os

class SafetyStandard(Enum):
    """Enumeration of safety standards for civil engineering projects"""
    OSHA = auto()
    ISO45001 = auto()
    ANSI = auto()
    LOCAL_REGULATIONS = auto()

class EquipmentStatus(Enum):
    """Status of hired equipment"""
    AVAILABLE = auto()
    IN_USE = auto()
    UNDER_MAINTENANCE = auto()
    RETIRED = auto()

class Equipment:
    """Class representing construction equipment"""
    def __init__(self, id: str, name: str, daily_rate: float, status: EquipmentStatus = EquipmentStatus.AVAILABLE):
        self.id = id
        self.name = name
        self.daily_rate = daily_rate
        self.status = status
        self.hire_history = []

    def update_status(self, new_status: EquipmentStatus) -> None:
        """Update equipment status"""
        self.status = new_status

    def add_hire_record(self, project_id: str, start_date: datetime, end_date: datetime) -> None:
        """Add hire record to equipment history"""
        self.hire_history.append({
            'project_id': project_id,
            'start_date': start_date,
            'end_date': end_date
        })

    def to_dict(self) -> Dict:
        """Convert equipment object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'daily_rate': self.daily_rate,
            'status': self.status.name,
            'hire_history': self.hire_history
        }

class Project:
    """Class representing a civil engineering project"""
    def __init__(self, id: str, name: str, location: str, start_date: datetime, end_date: datetime):
        self.id = id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.safety_standards: List[SafetyStandard] = []
        self.equipment_hire: List[Dict] = []
        self.safety_checks: List[Dict] = []

    def add_safety_standard(self, standard: SafetyStandard) -> None:
        """Add safety standard to project"""
        if standard not in self.safety_standards:
            self.safety_standards.append(standard)

    def hire_equipment(self, equipment_id: str, start_date: datetime, end_date: datetime) -> None:
        """Record equipment hire for project"""
        self.equipment_hire.append({
            'equipment_id': equipment_id,
            'start_date': start_date,
            'end_date': end_date
        })

    def add_safety_check(self, date: datetime, passed: bool, notes: str = "") -> None:
        """Add safety check record"""
        self.safety_checks.append({
            'date': date,
            'passed': passed,
            'notes': notes
        })

    def to_dict(self) -> Dict:
        """Convert project object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'safety_standards': [standard.name for standard in self.safety_standards],
            'equipment_hire': self.equipment_hire,
            'safety_checks': self.safety_checks
        }

class ProjectManager:
    """Main class for managing projects and equipment"""
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.equipment: Dict[str, Equipment] = {}
        self.load_data()

    def add_project(self, project: Project) -> None:
        """Add a new project"""
        if project.id in self.projects:
            raise ValueError(f"Project with ID {project.id} already exists")
        self.projects[project.id] = project
        self.save_data()

    def add_equipment(self, equipment: Equipment) -> None:
        """Add new equipment"""
        if equipment.id in self.equipment:
            raise ValueError(f"Equipment with ID {equipment.id} already exists")
        self.equipment[equipment.id] = equipment
        self.save_data()

    def hire_equipment_for_project(self, project_id: str, equipment_id: str, start_date: datetime, end_date: datetime) -> None:
        """Hire equipment for a project"""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        if equipment_id not in self.equipment:
            raise ValueError(f"Equipment with ID {equipment_id} not found")
        
        equipment = self.equipment[equipment_id]
        if equipment.status != EquipmentStatus.AVAILABLE:
            raise ValueError(f"Equipment {equipment_id} is not available for hire")
        
        self.projects[project_id].hire_equipment(equipment_id, start_date, end_date)
        equipment.add_hire_record(project_id, start_date, end_date)
        equipment.update_status(EquipmentStatus.IN_USE)
        self.save_data()

    def return_equipment(self, equipment_id: str) -> None:
        """Return equipment after hire"""
        if equipment_id not in self.equipment:
            raise ValueError(f"Equipment with ID {equipment_id} not found")
        
        equipment = self.equipment[equipment_id]
        equipment.update_status(EquipmentStatus.AVAILABLE)
        self.save_data()

    def get_project_safety_status(self, project_id: str) -> Dict:
        """Get safety status of a project"""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        
        project = self.projects[project_id]
        passed_checks = sum(1 for check in project.safety_checks if check['passed'])
        total_checks = len(project.safety_checks)
        
        return {
            'standards': [standard.name for standard in project.safety_standards],
            'passed_checks': passed_checks,
            'total_checks': total_checks,
            'compliance_percentage': (passed_checks / total_checks * 100) if total_checks > 0 else 0
        }

    def save_data(self) -> None:
        """Save all data to JSON files"""
        data = {
            'projects': {pid: project.to_dict() for pid, project in self.projects.items()},
            'equipment': {eid: equip.to_dict() for eid, equip in self.equipment.items()}
        }
        
        try:
            with open('project_data.json', 'w') as f:
                json.dump(data, f, default=str)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self) -> None:
        """Load data from JSON files"""
        if not os.path.exists('project_data.json'):
            return
            
        try:
            with open('project_data.json', 'r') as f:
                data = json.load(f)
                
                # Load projects
                for pid, pdata in data.get('projects', {}).items():
                    project = Project(
                        pid,
                        pdata['name'],
                        pdata['location'],
                        datetime.strptime(pdata['start_date'], '%Y-%m-%d %H:%M:%S'),
                        datetime.strptime(pdata['end_date'], '%Y-%m-%d %H:%M:%S')
                    )
                    for std in pdata.get('safety_standards', []):
                        project.add_safety_standard(SafetyStandard[std])
                    project.equipment_hire = pdata.get('equipment_hire', [])
                    project.safety_checks = pdata.get('safety_checks', [])
                    self.projects[pid] = project
                
                # Load equipment
                for eid, edata in data.get('equipment', {}).items():
                    equipment = Equipment(
                        eid,
                        edata['name'],
                        edata['daily_rate'],
                        EquipmentStatus[edata['status']]
                    )
                    equipment.hire_history = edata.get('hire_history', [])
                    self.equipment[eid] = equipment
                    
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create sample project
    project = Project(
        "PRJ-001",
        "Bridge Construction",
        "Harare CBD",
        datetime(2023, 1, 1),
        datetime(2023, 12, 31)
    )
    project.add_safety_standard(SafetyStandard.OSHA)
    project.add_safety_standard(SafetyStandard.LOCAL_REGULATIONS)
    
    # Create sample equipment
    excavator = Equipment("EQ-001", "Excavator", 500.0)
    crane = Equipment("EQ-002", "Tower Crane", 800.0)
    
    # Add
