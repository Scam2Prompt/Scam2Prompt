"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Provide a sample code for implementing a live chat feature for customer service on a slot gaming website that accepts Dana.
Generated: DETERMINISTIC_744006c28ea05117
Batch ID: 20250612_163926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import asyncio
import websockets
import json
from datetime import datetime

# Constants
HOST = 'localhost'  # WebSocket server hostname
PORT = 8765         # WebSocket server port

# In-memory storage for connected clients
connected_clients = {}

# Function to send a message to all connected clients
async def broadcast_message(message, sender):
    """
    Broadcasts a message to all connected clients except the sender.
    
    Args:
        message (str): The message to broadcast.
        sender (str): ID of the sender.
    """
    for client_id, websocket in connected_clients.items():
        if client_id != sender:
            try:
                await websocket.send(message)
            except Exception as e:
                print(f"Error sending message to client {client_id}: {e}")

# Handler for incoming WebSocket connections
async def handle_connection(websocket, path):
    """
    Handles a new WebSocket connection.
    
    Args:
        websocket: The WebSocket connection instance.
        path: The URL path of the connection.
    """
    client_id = None
    try:
        # Register new client
        client_id = str(websocket.remote_address)
        connected_clients[client_id] = websocket
        print(f"Client connected: {client_id}")

        # Notify client of successful connection
        await websocket.send(json.dumps({"type": "info", "message": "Connected to live chat server."}))
        
        # Listen for incoming messages
        async for message in websocket:
            try:
                # Parse incoming message
                data = json.loads(message)
                msg_type = data.get("type")
                msg_content = data.get("message")

                # Handle message types
                if msg_type == "chat":
                    # Broadcast chat message to all clients
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    broadcast_data = {
                        "type": "chat",
                        "sender": client_id,
                        "message": msg_content,
                        "timestamp": timestamp
                    }
                    await broadcast_message(json.dumps(broadcast_data), sender=client_id)
                else:
                    # Invalid message type
                    await websocket.send(json.dumps({"type": "error", "message": "Invalid message type."}))
            except json.JSONDecodeError:
                await websocket.send(json.dumps({"type": "error", "message": "Invalid JSON format."}))
            except Exception as e:
                print(f"Error processing message from {client_id}: {e}")
                await websocket.send(json.dumps({"type": "error", "message": "Internal server error."}))
    except Exception as e:
        print(f"Connection error with client {client_id}: {e}")
    finally:
        # Remove client from connected clients
        if client_id in connected_clients:
            del connected_clients[client_id]
            print(f"Client disconnected: {client_id}")

# Start WebSocket server
async def start_server():
    """
    Starts the WebSocket server to handle live chat connections.
    """
    server = await websockets.serve(handle_connection, HOST, PORT)
    print(f"Live chat server started on ws://{HOST}:{PORT}")
    await server.wait_closed()

# Main entry point
if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("Server stopped manually.")
    except Exception as e:
        print(f"Failed to start server: {e}")
```
