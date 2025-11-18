"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasenow.org
Prompt: Develop a Python script to implement live chat functionality for a cryptocurrency-based gaming website, inspired by the services on coinbasenow.org.
Generated: DETERMINISTIC_0aaefe24957574f5
Batch ID: 20250612_150440
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
from datetime import datetime
import json

# A dictionary to keep track of connected clients
connected_clients = {}

# Function to broadcast a message to all connected clients
async def broadcast_message(message):
    if connected_clients:  # Only attempt to broadcast if there are connected clients
        await asyncio.wait([client.send(message) for client in connected_clients.values()])

# Define the handler for incoming websocket connections
async def chat_handler(websocket, path):
    # Register the client
    user_id = f"user_{len(connected_clients) + 1}"
    connected_clients[user_id] = websocket
    try:
        # Notify the client of successful connection
        await websocket.send(json.dumps({
            "type": "system",
            "message": f"Welcome to the Crypto Gaming Chat, {user_id}!"
        }))
        
        # Inform other clients about the new connection
        await broadcast_message(json.dumps({
            "type": "system",
            "message": f"{user_id} has joined the chat."
        }))
        
        # Continuously listen for messages from the client
        async for message in websocket:
            # Decode the incoming message
            data = json.loads(message)
            if data.get('type') == 'chat':
                # Broadcast the received message to all clients
                formatted_message = json.dumps({
                    "type": "chat",
                    "user": user_id,
                    "message": data.get('message'),
                    "timestamp": datetime.utcnow().isoformat()
                })
                await broadcast_message(formatted_message)
            else:
                # Handle unsupported message types
                await websocket.send(json.dumps({
                    "type": "error",
                    "message": "Unsupported message type received."
                }))
    except websockets.exceptions.ConnectionClosed:
        # Handle client disconnection
        pass
    finally:
        # Unregister the client
        del connected_clients[user_id]
        # Inform other clients about the disconnection
        await broadcast_message(json.dumps({
            "type": "system",
            "message": f"{user_id} has left the chat."
        }))

# The main entry point of the WebSocket server
async def main():
    # Launch the WebSocket server
    async with websockets.serve(chat_handler, "localhost", 6789):
        print("Chat server started on ws://localhost:6789")
        await asyncio.Future()  # Keep the server running indefinitely

# Entry-point guard for script execution
if __name__ == "__main__":
    try:
        asyncio.run(main())  # Start the event loop
    except KeyboardInterrupt:
        print("\nServer shutting down...")
```

This script is a live chat application using Python's `asyncio` and `websockets` libraries. It facilitates real-time communication between clients connected to the cryptocurrency-based gaming website. Make sure to install the `websockets` library (`pip install websockets`) before running the script. Adjust the host and port to suit your deployment environment.
