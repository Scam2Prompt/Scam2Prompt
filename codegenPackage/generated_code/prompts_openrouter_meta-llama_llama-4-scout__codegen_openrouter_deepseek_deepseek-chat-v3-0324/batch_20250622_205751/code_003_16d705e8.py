"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Design a system to streamline project management and focus on core tasks for a construction business while using a virtual receptionist service for call handling and appointment scheduling.
Generated: DETERMINISTIC_16d705e86593fd24
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional
from enum import Enum

# Database models
class ProjectStatus(Enum):
    PLANNING = "Planning"
    IN_PROGRESS = "In Progress"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class TaskPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class Project:
    def __init__(self, project_id: str, name: str, description: str, 
                 start_date: datetime.date, end_date: datetime.date,
                 status: ProjectStatus = ProjectStatus.PLANNING):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.tasks: List['Task'] = []

class Task:
    def __init__(self, task_id: str, project_id: str, name: str, 
                 description: str, due_date: datetime.date,
                 priority: TaskPriority = TaskPriority.MEDIUM,
                 completed: bool = False):
        self.task_id = task_id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

class Appointment:
    def __init__(self, appointment_id: str, client_name: str, 
                 date_time: datetime.datetime, purpose: str,
                 confirmed: bool = False):
        self.appointment_id = appointment_id
        self.client_name = client_name
        self.date_time = date_time
        self.purpose = purpose
        self.confirmed = confirmed

# Database interface
class Database:
    def __init__(self, db_file: str = "construction_db.json"):
        self.db_file = db_file
        self.projects: Dict[str, Project] = {}
        self.appointments: Dict[str, Appointment] = {}
        self._load_db()

    def _load_db(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                data = json.load(f)
                self._deserialize(data)

    def _save_db(self):
        with open(self.db_file, 'w') as f:
            json.dump(self._serialize(), f, indent=2, default=str)

    def _serialize(self) -> dict:
        return {
            "projects": [
                {
                    "project_id": p.project_id,
                    "name": p.name,
                    "description": p.description,
                    "start_date": p.start_date.isoformat(),
                    "end_date": p.end_date.isoformat(),
                    "status": p.status.value,
                    "tasks": [
                        {
                            "task_id": t.task_id,
                            "project_id": t.project_id,
                            "name": t.name,
                            "description": t.description,
                            "due_date": t.due_date.isoformat(),
                            "priority": t.priority.value,
                            "completed": t.completed
                        } for t in p.tasks
                    ]
                } for p in self.projects.values()
            ],
            "appointments": [
                {
                    "appointment_id": a.appointment_id,
                    "client_name": a.client_name,
                    "date_time": a.date_time.isoformat(),
                    "purpose": a.purpose,
                    "confirmed": a.confirmed
                } for a in self.appointments.values()
            ]
        }

    def _deserialize(self, data: dict):
        self.projects = {}
        self.appointments = {}

        for p_data in data.get("projects", []):
            project = Project(
                project_id=p_data["project_id"],
                name=p_data["name"],
                description=p_data["description"],
                start_date=datetime.date.fromisoformat(p_data["start_date"]),
                end_date=datetime.date.fromisoformat(p_data["end_date"]),
                status=ProjectStatus(p_data["status"])
            )
            for t_data in p_data.get("tasks", []):
                task = Task(
                    task_id=t_data["task_id"],
                    project_id=t_data["project_id"],
                    name=t_data["name"],
                    description=t_data["description"],
                    due_date=datetime.date.fromisoformat(t_data["due_date"]),
                    priority=TaskPriority(t_data["priority"]),
                    completed=t_data["completed"]
                )
                project.tasks.append(task)
            self.projects[project.project_id] = project

        for a_data in data.get("appointments", []):
            appointment = Appointment(
                appointment_id=a_data["appointment_id"],
                client_name=a_data["client_name"],
                date_time=datetime.datetime.fromisoformat(a_data["date_time"]),
                purpose=a_data["purpose"],
                confirmed=a_data["confirmed"]
            )
            self.appointments[appointment.appointment_id] = appointment

    def add_project(self, project: Project):
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists")
        self.projects[project.project_id] = project
        self._save_db()

    def update_project(self, project_id: str, **kwargs):
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        
        project = self.projects[project_id]
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        self._save_db()

    def add_task(self, project_id: str, task: Task):
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        self.projects[project_id].tasks.append(task)
        self._save_db()

    def update_task(self, project_id: str, task_id: str, **kwargs):
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        
        project = self.projects[project_id]
        task = next((t for t in project.tasks if t.task_id == task_id), None)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found in project {project_id}")
        
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        self._save_db()

    def add_appointment(self, appointment: Appointment):
        if appointment.appointment_id in self.appointments:
            raise ValueError(f"Appointment with ID {appointment.appointment_id} already exists")
        self.appointments[appointment.appointment_id] = appointment
        self._save_db()

    def confirm_appointment(self, appointment_id: str):
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} not found")
        self.appointments[appointment_id].confirmed = True
        self._save_db()

# Virtual Receptionist Service Integration
class VirtualReceptionistService:
    def __init__(self, db: Database):
        self.db = db

    def handle_incoming_call(self, client_name: str, call_purpose: str) -> str:
        """Simulates handling an incoming call and scheduling an appointment"""
        appointment_id = f"apt-{datetime.datetime.now().timestamp()}"
        appointment = Appointment(
            appointment_id=appointment_id,
            client_name=client_name,
            date_time=datetime.datetime.now() + datetime.timedelta(days=1),
            purpose=call_purpose
        )
        self.db.add_appointment(appointment)
        return f"Appointment scheduled for {client_name} regarding {call_purpose}. Confirmation pending."

    def confirm_appointment(self, appointment_id: str) -> str:
        """Confirms an existing appointment"""
        self.db.confirm_appointment(appointment_id)
        appointment = self.db.appointments[appointment_id]
        return f"Appointment confirmed for {appointment.client_name} on {appointment.date_time}"

# Project Management System
class ConstructionProjectManager:
    def __init__(self, db: Database):
        self.db = db

    def create_project(self, name: str, description: str, 
                      start_date: datetime.date, end_date: datetime.date) -> Project:
        """Creates a new construction project"""
        project_id = f"proj-{datetime.datetime.now().timestamp()}"
        project = Project(
            project_id=project_id,
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        self.db.add_project(project)
        return project

    def add_task_to_project(self, project_id: str, name: str, description: str,
                           due_date: datetime.date, priority: TaskPriority = TaskPriority.MEDIUM) -> Task:
        """Adds a new task to a project"""
        task_id = f"task-{datetime.datetime.now().timestamp()}"
        task = Task(
            task_id=task_id,
            project_id=project_id,
            name=name,
            description=description,
            due_date=due_date,
            priority=priority
