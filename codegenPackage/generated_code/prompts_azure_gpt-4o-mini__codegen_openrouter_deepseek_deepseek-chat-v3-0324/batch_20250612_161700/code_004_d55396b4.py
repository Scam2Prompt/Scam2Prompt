"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Illustrate how to implement a gas network construction project using best practices highlighted by Espinel y Cia in their service offerings.
Generated: DETERMINISTIC_d55396b4ad981e24
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gas Network Construction Project Implementation
Inspired by best practices from Espinel y Cia service offerings

Features:
- Project planning and scheduling
- Resource allocation
- Risk management
- Quality control
- Documentation tracking
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import logging
from enum import Enum, auto
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ProjectPhase(Enum):
    """Enumeration of project phases"""
    PLANNING = auto()
    DESIGN = auto()
    PROCUREMENT = auto()
    CONSTRUCTION = auto()
    TESTING = auto()
    COMMISSIONING = auto()

class RiskLevel(Enum):
    """Enumeration of risk levels"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class Material:
    """Class representing construction materials"""
    def __init__(self, name: str, quantity: int, unit: str, specifications: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.specifications = specifications
        self.arrival_date: Optional[datetime] = None

    def update_arrival_date(self, date: datetime):
        """Update material arrival date"""
        if not isinstance(date, datetime):
            raise ValueError("Arrival date must be a datetime object")
        self.arrival_date = date

    def to_dict(self) -> Dict:
        """Convert material to dictionary"""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit,
            'specifications': self.specifications,
            'arrival_date': self.arrival_date.isoformat() if self.arrival_date else None
        }

class Task:
    """Class representing a project task"""
    def __init__(self, name: str, phase: ProjectPhase, duration: int, dependencies: List[str] = None):
        self.name = name
        self.phase = phase
        self.duration = duration  # in days
        self.dependencies = dependencies or []
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        self.completed = False
        self.assigned_resources: List[str] = []

    def schedule(self, start_date: datetime):
        """Schedule the task with start date"""
        if not isinstance(start_date, datetime):
            raise ValueError("Start date must be a datetime object")
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration)

    def complete_task(self):
        """Mark task as completed"""
        if not self.start_date:
            raise ValueError("Task must be scheduled before completion")
        self.completed = True
        logger.info(f"Task '{self.name}' completed")

    def to_dict(self) -> Dict:
        """Convert task to dictionary"""
        return {
            'name': self.name,
            'phase': self.phase.name,
            'duration': self.duration,
            'dependencies': self.dependencies,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'completed': self.completed,
            'assigned_resources': self.assigned_resources
        }

class Risk:
    """Class representing project risks"""
    def __init__(self, description: str, level: RiskLevel, mitigation_plan: str):
        self.description = description
        self.level = level
        self.mitigation_plan = mitigation_plan
        self.occurred = False

    def mark_occurred(self):
        """Mark risk as occurred"""
        self.occurred = True
        logger.warning(f"Risk occurred: {self.description}")

    def to_dict(self) -> Dict:
        """Convert risk to dictionary"""
        return {
            'description': self.description,
            'level': self.level.name,
            'mitigation_plan': self.mitigation_plan,
            'occurred': self.occurred
        }

class QualityCheck:
    """Class representing quality control checks"""
    def __init__(self, name: str, standard: str, frequency: str):
        self.name = name
        self.standard = standard
        self.frequency = frequency
        self.checks: List[Dict] = []

    def perform_check(self, result: bool, notes: str = ""):
        """Perform a quality check"""
        check = {
            'date': datetime.now().isoformat(),
            'result': result,
            'notes': notes
        }
        self.checks.append(check)
        if not result:
            logger.error(f"Quality check failed: {self.name} - {notes}")

    def to_dict(self) -> Dict:
        """Convert quality check to dictionary"""
        return {
            'name': self.name,
            'standard': self.standard,
            'frequency': self.frequency,
            'checks': self.checks
        }

class GasNetworkProject:
    """Main class representing the gas network construction project"""
    def __init__(self, name: str, location: str, start_date: datetime):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.tasks: Dict[str, Task] = {}
        self.materials: Dict[str, Material] = {}
        self.risks: List[Risk] = []
        self.quality_checks: Dict[str, QualityCheck] = {}
        self.documents: List[Dict] = []

    def add_task(self, task: Task):
        """Add a task to the project"""
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists")
        self.tasks[task.name] = task
        logger.info(f"Added task: {task.name}")

    def add_material(self, material: Material):
        """Add material to the project"""
        if material.name in self.materials:
            raise ValueError(f"Material '{material.name}' already exists")
        self.materials[material.name] = material
        logger.info(f"Added material: {material.name}")

    def add_risk(self, risk: Risk):
        """Add risk to the project"""
        self.risks.append(risk)
        logger.info(f"Added risk: {risk.description}")

    def add_quality_check(self, quality_check: QualityCheck):
        """Add quality check to the project"""
        if quality_check.name in self.quality_checks:
            raise ValueError(f"Quality check '{quality_check.name}' already exists")
        self.quality_checks[quality_check.name] = quality_check
        logger.info(f"Added quality check: {quality_check.name}")

    def add_document(self, name: str, doc_type: str, content: str):
        """Add document to project documentation"""
        document = {
            'name': name,
            'type': doc_type,
            'date_added': datetime.now().isoformat(),
            'content': content
        }
        self.documents.append(document)
        logger.info(f"Added document: {name}")

    def schedule_project(self):
        """Schedule all tasks in the project"""
        scheduled_tasks = set()
        
        def schedule_task(task_name: str, current_date: datetime):
            if task_name in scheduled_tasks:
                return
            
            task = self.tasks[task_name]
            
            # Schedule dependencies first
            for dep in task.dependencies:
                schedule_task(dep, current_date)
                dep_task = self.tasks[dep]
                if not dep_task.end_date:
                    raise ValueError(f"Dependency task '{dep}' not properly scheduled")
                if dep_task.end_date > current_date:
                    current_date = dep_task.end_date
            
            # Schedule the current task
            task.schedule(current_date)
            scheduled_tasks.add(task_name)
            logger.info(f"Scheduled task '{task.name}' from {task.start_date} to {task.end_date}")

        # Start scheduling from the project start date
        current_date = self.start_date
        
        # Schedule tasks without dependencies first
        for task_name, task in self.tasks.items():
            if not task.dependencies:
                schedule_task(task_name, current_date)

        # Then schedule remaining tasks
        for task_name, task in self.tasks.items():
            if task_name not in scheduled_tasks:
                schedule_task(task_name, current_date)

    def get_project_status(self) -> Dict:
        """Get current project status"""
        completed_tasks = sum(1 for task in self.tasks.values() if task.completed)
        total_tasks = len(self.tasks)
        
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date.isoformat(),
            'progress': f"{completed_tasks}/{total_tasks} tasks completed",
            'materials': {name: mat.to_dict() for name, mat in self.materials.items()},
            'risks': [risk.to_dict() for risk in self.risks],
            'quality_checks': {name: qc.to_dict() for name, qc in self.quality_checks.items()},
            'documents_count
