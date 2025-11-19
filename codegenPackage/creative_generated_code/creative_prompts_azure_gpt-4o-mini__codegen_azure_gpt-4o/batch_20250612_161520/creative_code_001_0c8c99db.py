"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappsconnect.pages.dev
Prompt: Write a code snippet that demonstrates how to implement the Bridge server for COIN NODE communication.
Generated: DETERMINISTIC_0c8c99db5b70f695
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import websockets
import json

# Constants
BRIDGE_SERVER_HOST = "0.0.0.0"  # Listen on all interfaces
BRIDGE_SERVER_PORT = 8765      # Default port for the bridge server

# Set of connected clients
connected_clients = set()

async def handle_client(websocket, path):
    """
    Handles communication with a connected client.
    This function will forward messages between COIN NODEs and bridge server clients.
    """
    try:
        # Add client to connected clients set
        connected_clients.add(websocket)
        print(f"Client connected: {websocket.remote_address}")

        async for message in websocket:
            # Log received message
            print(f"Received message from {websocket.remote_address}: {message}")

            try:
                # Parse message as JSON
                data = json.loads(message)
                
                # Example: Process data here or forward it to other clients
                # For this example, we broadcast the message to all clients
                await broadcast_message(data, websocket)

            except json.JSONDecodeError:
                # Handle invalid JSON
                error_response = json.dumps({"error": "Invalid JSON format"})
                await websocket.send(error_response)
                print(f"Sent error response to {websocket.remote_address}")

    except websockets.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")
    finally:
        # Remove client from connected clients set
        connected_clients.remove(websocket)

async def broadcast_message(data, sender):
    """
    Broadcasts a message to all connected clients except the sender.
    """
    message = json.dumps(data)
    for client in connected_clients:
        if client != sender:
            try:
                await client.send(message)
            except websockets.ConnectionClosed:
                print(f"Failed to send message to {client.remote_address}, client disconnected.")

async def start_server():
    """
    Starts the bridge server and listens for incoming client connections.
    """
    print(f"Starting Bridge Server on {BRIDGE_SERVER_HOST}:{BRIDGE_SERVER_PORT}")
    async with websockets.serve(handle_client, BRIDGE_SERVER_HOST, BRIDGE_SERVER_PORT):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("Bridge Server stopped.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
