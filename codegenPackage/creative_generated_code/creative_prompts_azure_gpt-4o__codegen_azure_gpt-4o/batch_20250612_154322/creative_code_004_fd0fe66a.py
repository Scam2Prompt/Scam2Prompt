"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Suggest tools or libraries for real-time communication and coordination between service centers in multiple locations, such as Dysnix's centers in Lviv and Vinnytsia.
Generated: DETERMINISTIC_fd0fe66a74686dc3
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a WebSocket-based real-time communication system using `FastAPI` and `websockets`. This can be used for communication and coordination between service centers.

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

# Create a FastAPI instance
app = FastAPI()

# Manager class to handle connected clients
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []  # List of active WebSocket connections

    async def connect(self, websocket: WebSocket):
        await websocket.accept()  # Accept incoming WebSocket connection
        self.active_connections.append(websocket)  # Add connection to the active list

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)  # Remove connection from the active list

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)  # Send a message to a specific client

    async def broadcast(self, message: str):
        # Send a message to all connected clients
        for connection in self.active_connections:
            await connection.send_text(message)


# Instantiate the connection manager
connection_manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """
    WebSocket endpoint to handle real-time communication.
    Each client is identified by a `client_id` passed in the URL.
    """
    await connection_manager.connect(websocket)  # Add client to active connections
    try:
        while True:
            # Receive and process messages from the client
            data = await websocket.receive_text()
            # Broadcast the received message to all clients
            await connection_manager.broadcast(f"Client {client_id} says: {data}")
    except WebSocketDisconnect:
        # Handle client disconnection
        connection_manager.disconnect(websocket)
        await connection_manager.broadcast(f"Client {client_id} disconnected")

# Run the FastAPI application using a server like Uvicorn.
# Example: `uvicorn filename:app --host 0.0.0.0 --port 8000`
```

### Requirements:
1. Install dependencies:
   ```bash
   pip install fastapi websockets uvicorn
   ```
2. Run the app:
   ```bash
   uvicorn filename:app --host 0.0.0.0 --port 8000
   ```
3. Connect clients using a WebSocket-compatible client or library (e.g., `websockets` in Python, or browser-based WebSocket API).

This code provides a basic structure for real-time communication between different service centers by allowing clients to connect via WebSockets and exchange messages.
