"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Provide code examples for implementing a 24-hour service scheduling system for water pipeline maintenance, inspired by Aktiv Rørteknikk AS's round-the-clock service model.
Generated: DETERMINISTIC_f72812eb8687f006
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(
    title="24-Hour Water Pipeline Maintenance Scheduler",
    description="API for managing round-the-clock water pipeline maintenance services",
    version="1.0.0"
)

class MaintenancePriority(Enum):
    EMERGENCY = "Emergency"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class MaintenanceStatus(Enum):
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class MaintenanceTeam(BaseModel):
    id: str
    name: str
    contact_number: str
    current_location: str
    is_available: bool = True

class MaintenanceTask(BaseModel):
    id: str
    description: str
    location: str
    priority: MaintenancePriority
    status: MaintenanceStatus = MaintenanceStatus.SCHEDULED
    scheduled_time: datetime.datetime
    estimated_duration: datetime.timedelta
    assigned_team: Optional[str] = None
    customer_name: str
    customer_contact: str

    @validator('scheduled_time')
    def validate_scheduled_time(cls, v):
        if v < datetime.datetime.now():
            raise ValueError("Scheduled time cannot be in the past")
        return v

# In-memory database for demonstration
teams_db: Dict[str, MaintenanceTeam] = {}
tasks_db: Dict[str, MaintenanceTask] = {}

def find_available_team() -> Optional[MaintenanceTeam]:
    for team in teams_db.values():
        if team.is_available:
            return team
    return None

@app.post("/teams/", response_model=MaintenanceTeam, status_code=status.HTTP_201_CREATED)
async def register_team(team: MaintenanceTeam):
    if team.id in teams_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Team with this ID already exists"
        )
    teams_db[team.id] = team
    return team

@app.get("/teams/", response_model=List[MaintenanceTeam])
async def list_teams(available: bool = None):
    if available is not None:
        return [team for team in teams_db.values() if team.is_available == available]
    return list(teams_db.values())

@app.post("/tasks/", response_model=MaintenanceTask, status_code=status.HTTP_201_CREATED)
async def create_task(task: MaintenanceTask):
    if task.id in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task with this ID already exists"
        )
    
    if task.priority == MaintenancePriority.EMERGENCY:
        available_team = find_available_team()
        if available_team:
            task.assigned_team = available_team.id
            available_team.is_available = False
    
    tasks_db[task.id] = task
    return task

@app.get("/tasks/", response_model=List[MaintenanceTask])
async def list_tasks(
    status: MaintenanceStatus = None,
    priority: MaintenancePriority = None
):
    tasks = tasks_db.values()
    if status:
        tasks = [t for t in tasks if t.status == status]
    if priority:
        tasks = [t for t in tasks if t.priority == priority]
    return list(tasks)

@app.put("/tasks/{task_id}/assign", response_model=MaintenanceTask)
async def assign_team(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    task = tasks_db[task_id]
    if task.assigned_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task already has an assigned team"
        )
    
    available_team = find_available_team()
    if not available_team:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="No available teams at the moment"
        )
    
    task.assigned_team = available_team.id
    available_team.is_available = False
    return task

@app.put("/tasks/{task_id}/status", response_model=MaintenanceTask)
async def update_task_status(task_id: str, new_status: MaintenanceStatus):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    task = tasks_db[task_id]
    task.status = new_status
    
    if new_status == MaintenanceStatus.COMPLETED or new_status == MaintenanceStatus.CANCELLED:
        if task.assigned_team and task.assigned_team in teams_db:
            teams_db[task.assigned_team].is_available = True
    
    return task

@app.get("/tasks/emergency", response_model=List[MaintenanceTask])
async def get_emergency_tasks():
    return [
        task for task in tasks_db.values()
        if task.priority == MaintenancePriority.EMERGENCY
        and task.status != MaintenanceStatus.COMPLETED
    ]

@app.get("/dashboard")
async def get_dashboard():
    return {
        "total_teams": len(teams_db),
        "available_teams": len([t for t in teams_db.values() if t.is_available]),
        "total_tasks": len(tasks_db),
        "emergency_tasks": len([
            t for t in tasks_db.values()
            if t.priority == MaintenancePriority.EMERGENCY
            and t.status != MaintenanceStatus.COMPLETED
        ]),
        "tasks_by_status": {
            status.value: len([t for t in tasks_db.values() if t.status == status])
            for status in MaintenanceStatus
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
