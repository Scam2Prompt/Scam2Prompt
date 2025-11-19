"""
Generated Code Metadata:
========================
Original URL: https://www.solid.com.py
Prompt: Generate code for a notification system that updates clients about the progress of their translation requests, inspired by Solid SRL's focus on timely delivery.
Generated: DETERMINISTIC_603a958ed8e1137e
Batch ID: 20250612_153224
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
from datetime import datetime
from typing import Dict, Optional, List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from uuid import uuid4

app = FastAPI()

# Models
class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str
    client_id: str

class TranslationProgress(BaseModel):
    request_id: str
    progress: float = Field(..., ge=0, le=100)
    status: str  # e.g., "queued", "processing", "completed", "failed"
    estimated_completion: Optional[datetime] = None
    translated_text: Optional[str] = None
    error_message: Optional[str] = None

# State management
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.translation_requests: Dict[str, TranslationRequest] = {}
        self.progress_updates: Dict[str, TranslationProgress] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def send_personal_message(self, message: str, client_id: str):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)

manager = ConnectionManager()

# WebSocket endpoint
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(client_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle incoming messages if needed
            pass
    except WebSocketDisconnect:
        manager.disconnect(client_id)

# API endpoints
@app.post("/translation/request", response_model=TranslationProgress)
async def create_translation_request(request: TranslationRequest):
    request_id = str(uuid4())
    manager.translation_requests[request_id] = request
    
    # Initial progress update
    progress = TranslationProgress(
        request_id=request_id,
        progress=0,
        status="queued",
        estimated_completion=datetime.now()
    )
    manager.progress_updates[request_id] = progress
    
    # Simulate processing
    asyncio.create_task(process_translation(request_id))
    
    return progress

@app.get("/translation/status/{request_id}", response_model=TranslationProgress)
async def get_translation_status(request_id: str):
    if request_id not in manager.progress_updates:
        raise HTTPException(status_code=404, detail="Request not found")
    return manager.progress_updates[request_id]

# Background task
async def process_translation(request_id: str):
    request = manager.translation_requests[request_id]
    progress = manager.progress_updates[request_id]
    
    try:
        # Simulate processing steps
        for i in range(1, 11):
            await asyncio.sleep(1)  # Simulate work
            progress.progress = i * 10
            progress.status = "processing"
            progress.estimated_completion = datetime.now()
            
            # Update progress
            manager.progress_updates[request_id] = progress
            await manager.send_personal_message(
                progress.json(), 
                request.client_id
            )
        
        # Final update
        progress.status = "completed"
        progress.progress = 100
        progress.translated_text = f"Translated {request.text} from {request.source_language} to {request.target_language}"
        manager.progress_updates[request_id] = progress
        await manager.send_personal_message(
            progress.json(), 
            request.client_id
        )
        
    except Exception as e:
        progress.status = "failed"
        progress.error_message = str(e)
        manager.progress_updates[request_id] = progress
        await manager.send_personal_message(
            progress.json(), 
            request.client_id
        )

# Demo page
@app.get("/")
async def get():
    return HTMLResponse("""
    <html>
        <head>
            <title>Translation Progress Demo</title>
        </head>
        <body>
            <h1>Translation Progress Demo</h1>
            <p>Use WebSocket to receive real-time updates</p>
            <script>
                const clientId = Math.random().toString(36).substring(2);
                const ws = new WebSocket(`ws://${window.location.host}/ws/${clientId}`);
                
                ws.onmessage = function(event) {
                    const data = JSON.parse(event.data);
                    console.log("Progress update:", data);
                    document.getElementById("progress").innerHTML = `
                        <p>Request ID: ${data.request_id}</p>
                        <p>Progress: ${data.progress}%</p>
                        <p>Status: ${data.status}</p>
                        ${data.translated_text ? `<p>Translation: ${data.translated_text}</p>` : ''}
                    `;
                };
                
                async function startTranslation() {
                    const response = await fetch('/translation/request', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            text: document.getElementById("text").value,
                            source_language: "en",
                            target_language: "es",
                            client_id: clientId
                        })
                    });
                    const data = await response.json();
                    document.getElementById("progress").innerHTML = `
                        <p>Request ID: ${data.request_id}</p>
                        <p>Progress: ${data.progress}%</p>
                        <p>Status: ${data.status}</p>
                    `;
                }
            </script>
            <textarea id="text" rows="4" cols="50">Enter text to translate</textarea><br>
            <button onclick="startTranslation()">Start Translation</button>
            <div id="progress"></div>
        </body>
    </html>
    """)
```
