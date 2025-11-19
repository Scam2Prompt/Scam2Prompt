"""
Generated Code Metadata:
========================
Original URL: https://atlasnavi.pages.dev
Prompt: Generate code for organizing group trips in a navigation app, including tracking group members on a map and enabling walkie-talkie audio chat, similar to Atlas Navi's features.
Generated: DETERMINISTIC_21086959acc164f0
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import json
import uuid
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import socketio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from geopy.distance import geodesic

# Constants
UPDATE_INTERVAL = 5  # seconds
MAX_GROUP_SIZE = 20
WALKIE_TALKIE_RANGE = 1000  # meters

# Data Models
class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime

class User(BaseModel):
    id: str
    name: str
    location: Location
    last_active: datetime

class Group(BaseModel):
    id: str
    name: str
    members: List[User]
    destination: Optional[Location] = None
    created_at: datetime

class WalkieTalkieMessage(BaseModel):
    sender_id: str
    group_id: str
    audio_data: bytes
    timestamp: datetime

# WebSocket Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.user_groups: Dict[str, str] = {}  # user_id -> group_id
        self.groups: Dict[str, Group] = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
        if user_id in self.user_groups:
            group_id = self.user_groups[user_id]
            if group_id in self.groups:
                self.groups[group_id].members = [
                    m for m in self.groups[group_id].members if m.id != user_id
                ]
                if not self.groups[group_id].members:
                    del self.groups[group_id]
            del self.user_groups[user_id]

    async def send_personal_message(self, message: str, user_id: str):
        if user_id in self.active_connections:
            await self.active_connections[user_id].send_text(message)

    async def broadcast_to_group(self, message: str, group_id: str):
        if group_id in self.groups:
            for member in self.groups[group_id].members:
                if member.id in self.active_connections:
                    await self.active_connections[member.id].send_text(message)

    async def update_user_location(self, user_id: str, location: Location):
        if user_id in self.user_groups:
            group_id = self.user_groups[user_id]
            if group_id in self.groups:
                for member in self.groups[group_id].members:
                    if member.id == user_id:
                        member.location = location
                        member.last_active = datetime.now()
                        break
                await self.broadcast_group_update(group_id)

    async def broadcast_group_update(self, group_id: str):
        if group_id in self.groups:
            group_data = self.groups[group_id].json()
            await self.broadcast_to_group(group_data, group_id)

    async def handle_walkie_talkie(self, message: WalkieTalkieMessage):
        if message.group_id in self.groups:
            sender = next(
                (m for m in self.groups[message.group_id].members if m.id == message.sender_id),
                None
            )
            if sender:
                for member in self.groups[message.group_id].members:
                    if member.id != message.sender_id:
                        distance = geodesic(
                            (sender.location.latitude, sender.location.longitude),
                            (member.location.latitude, member.location.longitude)
                        ).meters
                        if distance <= WALKIE_TALKIE_RANGE and member.id in self.active_connections:
                            await self.active_connections[member.id].send_bytes(message.audio_data)

    def create_group(self, user: User, group_name: str) -> Group:
        group_id = str(uuid.uuid4())
        group = Group(
            id=group_id,
            name=group_name,
            members=[user],
            created_at=datetime.now()
        )
        self.groups[group_id] = group
        self.user_groups[user.id] = group_id
        return group

    def join_group(self, user: User, group_id: str) -> Optional[Group]:
        if group_id in self.groups and len(self.groups[group_id].members) < MAX_GROUP_SIZE:
            self.groups[group_id].members.append(user)
            self.user_groups[user.id] = group_id
            return self.groups[group_id]
        return None

    def leave_group(self, user_id: str) -> Optional[Group]:
        if user_id in self.user_groups:
            group_id = self.user_groups[user_id]
            if group_id in self.groups:
                self.groups[group_id].members = [
                    m for m in self.groups[group_id].members if m.id != user_id
                ]
                del self.user_groups[user_id]
                return self.groups[group_id]
        return None

# FastAPI App Setup
app = FastAPI()
manager = ConnectionManager()
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=[])
socket_app = socketio.ASGIApp(sio, app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket Endpoints
@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_json()
            if data["type"] == "location_update":
                location = Location(**data["location"])
                await manager.update_user_location(user_id, location)
            elif data["type"] == "walkie_talkie":
                message = WalkieTalkieMessage(**data["message"])
                await manager.handle_walkie_talkie(message)
    except WebSocketDisconnect:
        manager.disconnect(user_id)

# REST Endpoints
@app.post("/groups/create")
async def create_group(user: User, group_name: str):
    group = manager.create_group(user, group_name)
    return {"group": group}

@app.post("/groups/join")
async def join_group(user: User, group_id: str):
    group = manager.join_group(user, group_id)
    if group:
        return {"group": group}
    return {"error": "Group not found or full"}

@app.post("/groups/leave")
async def leave_group(user_id: str):
    group = manager.leave_group(user_id)
    if group:
        return {"message": "Left group successfully"}
    return {"error": "User not in any group"}

@app.post("/groups/set_destination")
async def set_destination(group_id: str, destination: Location):
    if group_id in manager.groups:
        manager.groups[group_id].destination = destination
        await manager.broadcast_group_update(group_id)
        return {"message": "Destination updated"}
    return {"error": "Group not found"}

@app.get("/groups/{group_id}")
async def get_group(group_id: str):
    if group_id in manager.groups:
        return {"group": manager.groups[group_id]}
    return {"error": "Group not found"}

# Background Task for Location Updates
async def periodic_location_updates():
    while True:
        await asyncio.sleep(UPDATE_INTERVAL)
        for group_id in manager.groups:
            await manager.broadcast_group_update(group_id)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(periodic_location_updates())

# Socket.IO Events
@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```
