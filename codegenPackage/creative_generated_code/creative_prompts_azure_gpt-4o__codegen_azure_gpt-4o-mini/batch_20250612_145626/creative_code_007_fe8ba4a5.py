"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mary.finance
Prompt: Generate a web service using Mary AI's platform that demonstrates the synergy between human creativity and AI computational power. Include real-time collaboration features.
Generated: DETERMINISTIC_fe8ba4a5d96d4f2c
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Allow CORS for frontend applications
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store connected clients
clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time collaboration.
    It allows clients to connect, send messages, and receive updates.
    """
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            # Wait for a message from the client
            data = await websocket.receive_text()
            # Broadcast the message to all connected clients
            await broadcast(data)
    except WebSocketDisconnect:
        # Remove client on disconnect
        clients.remove(websocket)

async def broadcast(message: str):
    """
    Broadcast the received message to all connected clients.
    
    Args:
        message (str): The message to be sent to clients.
    """
    for client in clients:
        await client.send_text(message)

@app.get("/")
async def get():
    """
    Root endpoint that serves a simple confirmation message.
    
    Returns:
        dict: A message indicating the service is running.
    """
    return {"message": "Web service is running. Connect via WebSocket."}

# Error handling middleware
@app.middleware("http")
async def error_handling_middleware(request, call_next):
    """
    Middleware to handle errors and provide JSON response on exceptions.
    """
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    # Running the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
