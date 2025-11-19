"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: Write Python code to create a virtual classroom tool that incorporates features like video conferencing, file sharing, and real-time collaboration, as described in the "Enhancing Education: Virtual Classroom Tools" article on Elon Shiba.
Generated: DETERMINISTIC_bec81418b4f2e9a3
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
import logging
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import aiofiles
from starlette.websockets import WebSocketState

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Virtual Classroom Tool", version="1.0.0")

# Mount static files directory
os.makedirs("static/files", exist_ok=True)
os.makedirs("static/avatars", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Data models
class User(BaseModel):
    id: str
    name: str
    role: str  # "teacher" or "student"
    avatar: Optional[str] = None

class Message(BaseModel):
    sender: User
    content: str
    timestamp: str

class FileInfo(BaseModel):
    id: str
    name: str
    size: int
    uploader: User
    timestamp: str
    url: str

class ClassroomState(BaseModel):
    users: List[User]
    messages: List[Message]
    files: List[FileInfo]

# Connection manager for WebSockets
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.users: Dict[str, User] = {}
        self.messages: List[Message] = []
        self.files: List[FileInfo] = []

    async def connect(self, websocket: WebSocket, user: User):
        await websocket.accept()
        self.active_connections[user.id] = websocket
        self.users[user.id] = user
        await self.broadcast_user_list()

    async def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
        if user_id in self.users:
            del self.users[user_id]
        await self.broadcast_user_list()

    async def send_personal_message(self, message: str, websocket: WebSocket):
        if websocket.application_state == WebSocketState.CONNECTED:
            await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            if connection.application_state == WebSocketState.CONNECTED:
                await connection.send_text(message)

    async def broadcast_user_list(self):
        user_list = [user.dict() for user in self.users.values()]
        await self.broadcast_json({"type": "user_list", "data": user_list})

    async def broadcast_message(self, message: Message):
        self.messages.append(message)
        await self.broadcast_json({"type": "message", "data": message.dict()})

    async def broadcast_file(self, file_info: FileInfo):
        self.files.append(file_info)
        await self.broadcast_json({"type": "file", "data": file_info.dict()})

    async def broadcast_json(self, data: dict):
        for connection in self.active_connections.values():
            if connection.application_state == WebSocketState.CONNECTED:
                await connection.send_json(data)

    def get_classroom_state(self) -> ClassroomState:
        return ClassroomState(
            users=list(self.users.values()),
            messages=self.messages,
            files=self.files
        )

manager = ConnectionManager()

# API endpoints
@app.get("/", response_class=HTMLResponse)
async def get_homepage():
    return """
    <html>
        <head>
            <title>Virtual Classroom</title>
        </head>
        <body>
            <h1>Welcome to Virtual Classroom</h1>
            <p>Use WebSocket connections to interact with the classroom.</p>
        </body>
    </html>
    """

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    try:
        # Wait for initial user data
        data = await websocket.receive_json()
        user = User(**data)
        
        await manager.connect(websocket, user)
        await manager.send_personal_message(
            f"Welcome to the classroom, {user.name}!", websocket
        )
        
        # Send initial state
        state = manager.get_classroom_state()
        await websocket.send_json({"type": "init", "data": state.dict()})
        
        while True:
            data = await websocket.receive_json()
            
            if data["type"] == "message":
                message = Message(
                    sender=user,
                    content=data["content"],
                    timestamp=datetime.now().isoformat()
                )
                await manager.broadcast_message(message)
                
            elif data["type"] == "file_request":
                file_id = data["file_id"]
                file_info = next((f for f in manager.files if f.id == file_id), None)
                if file_info:
                    await websocket.send_json({
                        "type": "file_response",
                        "data": file_info.dict()
                    })
                
    except WebSocketDisconnect:
        await manager.disconnect(user_id)
        logger.info(f"User {user_id} disconnected")
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
        await manager.disconnect(user_id)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), user_id: str = None):
    if not user_id or user_id not in manager.users:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    user = manager.users[user_id]
    file_id = str(uuid.uuid4())
    file_path = f"static/files/{file_id}_{file.filename}"
    
    try:
        async with aiofiles.open(file_path, "wb") as buffer:
            content = await file.read()
            await buffer.write(content)
        
        file_info = FileInfo(
            id=file_id,
            name=file.filename,
            size=len(content),
            uploader=user,
            timestamp=datetime.now().isoformat(),
            url=f"/static/files/{file_id}_{file.filename}"
        )
        
        await manager.broadcast_file(file_info)
        return {"status": "success", "file_id": file_id}
    
    except Exception as e:
        logger.error(f"File upload error: {str(e)}")
        raise HTTPException(status_code=500, detail="File upload failed")

@app.get("/files/{file_id}")
async def download_file(file_id: str):
    file_info = next((f for f in manager.files if f.id == file_id), None)
    if not file_info:
        raise HTTPException(status_code=404, detail="File not found")
    
    file_path = file_info.url.replace("/static/", "static/")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on server")
    
    return FileResponse(
        file_path,
        filename=file_info.name,
        media_type="application/octet-stream"
    )

@app.get("/state/")
async def get_classroom_state():
    return manager.get_classroom_state()

# WebRTC signaling endpoints (simplified)
@app.post("/webrtc/offer/{user_id}")
async def handle_offer(user_id: str, offer: dict):
    if user_id not in manager.users:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    # In a real implementation, you would route this to the target user
    return {"status": "offer_received"}

@app.post("/webrtc/answer/{user_id}")
async def handle_answer(user_id: str, answer: dict):
    if user_id not in manager.users:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    # In a real implementation, you would route this to the target user
    return {"status": "answer_received"}

@app.post("/webrtc/ice-candidate/{user_id}")
async def handle_ice_candidate(user_id: str, candidate: dict):
    if user_id not in manager.users:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    # In a real implementation, you would route this to the target user
    return {"status": "ice_candidate_received"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
