"""
Generated Code Metadata:
========================
Original URL: https://nabberx.com
Prompt: Generate a project management tool prototype for construction firms using real-time collaboration features described in NabberX's IT solutions for the construction industry.
Generated: DETERMINISTIC_fac0f84b106f58f8
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Construction Firms with Real-time Collaboration

Features:
- Project creation and management
- Task assignment and tracking
- Real-time updates and notifications
- Document sharing and version control
- Team collaboration with chat functionality
"""

import os
import uuid
import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from enum import Enum
import motor.motor_asyncio
from bson import ObjectId

# Initialize FastAPI app
app = FastAPI(
    title="Construction Project Management Tool",
    description="Real-time collaboration platform for construction firms",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB configuration
MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.construction_projects

# Collections
projects_collection = db.projects
tasks_collection = db.tasks
documents_collection = db.documents
users_collection = db.users

# Models
class ProjectStatus(str, Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TaskStatus(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"

class UserRole(str, Enum):
    ADMIN = "admin"
    PROJECT_MANAGER = "project_manager"
    SITE_SUPERVISOR = "site_supervisor"
    WORKER = "worker"
    CLIENT = "client"

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    role: UserRole
    company: str

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    status: ProjectStatus = ProjectStatus.PLANNING
    start_date: datetime.date
    end_date: Optional[datetime.date] = None
    budget: Optional[float] = None
    manager_id: str  # User ID of the project manager
    team_members: List[str] = []  # List of user IDs
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    project_id: str
    title: str
    description: str
    status: TaskStatus = TaskStatus.NOT_STARTED
    assigned_to: str  # User ID
    due_date: datetime.date
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    project_id: str
    name: str
    file_path: str
    uploaded_by: str  # User ID
    version: int = 1
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    project_id: str
    sender_id: str  # User ID
    content: str
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now)

# WebSocket Manager for real-time updates
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, project_id: str, websocket: WebSocket):
        await websocket.accept()
        if project_id not in self.active_connections:
            self.active_connections[project_id] = []
        self.active_connections[project_id].append(websocket)

    def disconnect(self, project_id: str, websocket: WebSocket):
        if project_id in self.active_connections:
            self.active_connections[project_id].remove(websocket)

    async def broadcast(self, project_id: str, message: str):
        if project_id in self.active_connections:
            for connection in self.active_connections[project_id]:
                try:
                    await connection.send_text(message)
                except WebSocketDisconnect:
                    self.disconnect(project_id, connection)

manager = ConnectionManager()

# API Endpoints
@app.post("/users/", response_model=User)
async def create_user(user: User):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    user_dict = user.dict()
    await users_collection.insert_one(user_dict)
    return user

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await users_collection.find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/projects/", response_model=Project)
async def create_project(project: Project):
    # Verify manager exists
    manager = await users_collection.find_one({"id": project.manager_id})
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")
    
    project_dict = project.dict()
    await projects_collection.insert_one(project_dict)
    return project

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str):
    project = await projects_collection.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.post("/projects/{project_id}/tasks/", response_model=Task)
async def create_task(project_id: str, task: Task):
    # Verify project exists
    project = await projects_collection.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Verify assigned user exists
    user = await users_collection.find_one({"id": task.assigned_to})
    if not user:
        raise HTTPException(status_code=404, detail="Assigned user not found")
    
    task_dict = task.dict()
    await tasks_collection.insert_one(task_dict)
    
    # Notify team members
    await manager.broadcast(project_id, f"New task created: {task.title}")
    
    return task

@app.put("/tasks/{task_id}/status", response_model=Task)
async def update_task_status(task_id: str, status: TaskStatus):
    task = await tasks_collection.find_one({"id": task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    updates = {"status": status, "updated_at": datetime.datetime.now()}
    await tasks_collection.update_one({"id": task_id}, {"$set": updates})
    
    updated_task = await tasks_collection.find_one({"id": task_id})
    
    # Notify team members
    await manager.broadcast(task["project_id"], f"Task status updated: {task['title']} is now {status}")
    
    return updated_task

@app.post("/projects/{project_id}/documents/", response_model=Document)
async def upload_document(project_id: str, document: Document):
    # Verify project exists
    project = await projects_collection.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Verify uploader exists
    user = await users_collection.find_one({"id": document.uploaded_by})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    document_dict = document.dict()
    await documents_collection.insert_one(document_dict)
    
    # Notify team members
    await manager.broadcast(project_id, f"New document uploaded: {document.name}")
    
    return document

@app.websocket("/projects/{project_id}/ws")
async def websocket_endpoint(project_id: str, websocket: WebSocket):
    await manager.connect(project_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast message to all connected clients
            await manager.broadcast(project_id, f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(project_id, websocket)
        await manager.broadcast(project_id, f"Client left the chat")

# Utility functions
async def get_project_tasks(project
