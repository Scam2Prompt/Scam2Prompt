"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Generate a comprehensive plan for setting up an office from scratch, including design and execution of civil works, furniture, HVAC, electrical works, and fire protection systems."
Generated: DETERMINISTIC_4f47bf94cc7872b0
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
Office Setup Planner - Comprehensive Plan Generator
This script generates a detailed plan for setting up an office from scratch,
covering civil works, furniture, HVAC, electrical works, and fire protection systems.
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional

class TaskCategory(Enum):
    CIVIL_WORKS = "Civil Works"
    FURNITURE = "Furniture"
    HVAC = "HVAC System"
    ELECTRICAL = "Electrical Works"
    FIRE_PROTECTION = "Fire Protection"
    PLANNING = "Planning"
    PERMITS = "Permits and Approvals"

class Task:
    def __init__(self, name: str, category: TaskCategory, 
                 duration: int, dependencies: List[str] = None,
                 description: str = "", responsible_party: str = ""):
        self.name = name
        self.category = category
        self.duration = duration  # in days
        self.dependencies = dependencies or []
        self.description = description
        self.responsible_party = responsible_party
        self.start_date = None
        self.end_date = None

    def __str__(self):
        return f"{self.name} ({self.category.value}) - {self.duration} days"

class OfficeSetupPlan:
    def __init__(self, office_size: float, location: str, start_date: datetime.date):
        self.office_size = office_size  # in square meters
        self.location = location
        self.start_date = start_date
        self.tasks: List[Task] = []
        self.phases: Dict[str, List[Task]] = {}
        self._initialize_tasks()
        self._calculate_schedule()

    def _initialize_tasks(self):
        """Initialize all tasks required for office setup"""
        # Planning and Permits Phase
        self._add_task("Site Survey", TaskCategory.PLANNING, 3)
        self._add_task("Design Approval", TaskCategory.PLANNING, 5, ["Site Survey"])
        self._add_task("Obtain Building Permits", TaskCategory.PERMITS, 10, ["Design Approval"])
        
        # Civil Works Phase
        self._add_task("Demolition (if needed)", TaskCategory.CIVIL_WORKS, 5, ["Obtain Building Permits"])
        self._add_task("Structural Work", TaskCategory.CIVIL_WORKS, 15, ["Demolition (if needed)"])
        self._add_task("Partition Walls", TaskCategory.CIVIL_WORKS, 10, ["Structural Work"])
        self._add_task("Flooring Installation", TaskCategory.CIVIL_WORKS, 7, ["Partition Walls"])
        self._add_task("Ceiling Installation", TaskCategory.CIVIL_WORKS, 5, ["Partition Walls"])
        self._add_task("Painting", TaskCategory.CIVIL_WORKS, 5, ["Ceiling Installation", "Flooring Installation"])
        
        # Electrical Works Phase
        self._add_task("Main Electrical Wiring", TaskCategory.ELECTRICAL, 7, ["Partition Walls"])
        self._add_task("Lighting Installation", TaskCategory.ELECTRICAL, 5, ["Main Electrical Wiring", "Ceiling Installation"])
        self._add_task("Power Outlets Installation", TaskCategory.ELECTRICAL, 3, ["Main Electrical Wiring"])
        self._add_task("Data Cabling", TaskCategory.ELECTRICAL, 4, ["Main Electrical Wiring"])
        self._add_task("Electrical Testing", TaskCategory.ELECTRICAL, 2, ["Lighting Installation", "Power Outlets Installation", "Data Cabling"])
        
        # HVAC Phase
        self._add_task("HVAC Ductwork", TaskCategory.HVAC, 7, ["Ceiling Installation"])
        self._add_task("HVAC Unit Installation", TaskCategory.HVAC, 3, ["HVAC Ductwork"])
        self._add_task("HVAC Testing", TaskCategory.HVAC, 2, ["HVAC Unit Installation"])
        
        # Fire Protection Phase
        self._add_task("Fire Alarm System Installation", TaskCategory.FIRE_PROTECTION, 3, ["Ceiling Installation"])
        self._add_task("Sprinkler System Installation", TaskCategory.FIRE_PROTECTION, 4, ["Ceiling Installation"])
        self._add_task("Fire Extinguishers Installation", TaskCategory.FIRE_PROTECTION, 1)
        self._add_task("Fire Protection Testing", TaskCategory.FIRE_PROTECTION, 2, 
                      ["Fire Alarm System Installation", "Sprinkler System Installation"])
        
        # Furniture Phase
        self._add_task("Workstations Installation", TaskCategory.FURNITURE, 5, ["Flooring Installation", "Painting"])
        self._add_task("Meeting Room Furniture", TaskCategory.FURNITURE, 2, ["Flooring Installation", "Painting"])
        self._add_task("Reception Area Setup", TaskCategory.FURNITURE, 2, ["Flooring Installation", "Painting"])
        self._add_task("Break Room Setup", TaskCategory.FURNITURE, 2, ["Flooring Installation", "Painting"])
        
        # Final Phase
        self._add_task("Final Inspection", TaskCategory.PLANNING, 2, 
                      ["Electrical Testing", "HVAC Testing", "Fire Protection Testing", "Workstations Installation"])
        self._add_task("Office Setup Completion", TaskCategory.PLANNING, 1, ["Final Inspection"])

    def _add_task(self, name: str, category: TaskCategory, duration: int, 
                 dependencies: List[str] = None, description: str = "", 
                 responsible_party: str = ""):
        """Helper method to add a task to the plan"""
        task = Task(
            name=name,
            category=category,
            duration=duration,
            dependencies=dependencies,
            description=description,
            responsible_party=responsible_party
        )
        self.tasks.append(task)
        
        # Add to phases
        phase = category.value
        if phase not in self.phases:
            self.phases[phase] = []
        self.phases[phase].append(task)

    def _calculate_schedule(self):
        """Calculate start and end dates for all tasks based on dependencies"""
        completed_tasks = set()
        
        # Initialize all tasks with no dependencies
        for task in self.tasks:
            if not task.dependencies:
                task.start_date = self.start_date
                task.end_date = task.start_date + datetime.timedelta(days=task.duration)
                completed_tasks.add(task.name)
        
        # Process remaining tasks
        changed = True
        while changed:
            changed = False
            for task in self.tasks:
                if task.name not in completed_tasks:
                    all_deps_completed = all(dep in completed_tasks for dep in task.dependencies)
                    if all_deps_completed:
                        # Find the latest end date among dependencies
                        latest_end_date = self.start_date
                        for dep in task.dependencies:
                            dep_task = next(t for t in self.tasks if t.name == dep)
                            if dep_task.end_date > latest_end_date:
                                latest_end_date = dep_task.end_date
                        
                        task.start_date = latest_end_date + datetime.timedelta(days=1)
                        task.end_date = task.start_date + datetime.timedelta(days=task.duration)
                        completed_tasks.add(task.name)
                        changed = True

    def get_gantt_data(self) -> List[Dict]:
        """Prepare data for Gantt chart visualization"""
        gantt_data = []
        for task in self.tasks:
            gantt_data.append({
                "Task": task.name,
                "Category": task.category.value,
                "Start": task.start_date.strftime("%Y-%m-%d"),
                "End": task.end_date.strftime("%Y-%m-%d"),
                "Duration": task.duration,
                "Dependencies": ", ".join(task.dependencies) if task.dependencies else "None"
            })
        return gantt_data

    def get_phase_summary(self) -> Dict[str, Dict]:
        """Get summary information for each phase"""
        summary = {}
        for phase, tasks in self.phases.items():
            start_dates = [t.start_date for t in tasks]
            end_dates = [t.end_date for t in tasks]
            summary[phase] = {
                "task_count": len(tasks),
                "start_date": min(start_dates).strftime("%Y-%m-%d"),
                "end_date": max(end_dates).strftime("%Y-%m-%d"),
                "duration_days": (max(end_dates) - min(start_dates)).days + 1
            }
        return summary

    def get_total_duration(self) -> int:
        """Get total duration of the project in days"""
        end_dates = [task.end_date for task in self.tasks]
        return (max(end_dates) - self.start_date).days + 1

    def generate_report(self) -> str:
        """Generate a comprehensive report of the office setup plan"""
        report = []
        report.append(f"Office Setup Plan for {self.office_size} sqm at {self.location}")
        report.append(f"Project Start Date
