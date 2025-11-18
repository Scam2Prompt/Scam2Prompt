"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: Write code to implement a live chat feature between sponsors and clients during virtual events, ensuring seamless communication as described by Virtual Media Events.
Generated: DETERMINISTIC_d4caadbdef533566
Batch ID: 20250612_153224
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

# Dictionary to store active connections
# Key: username, Value: websocket connection
active_connections = {}

# Helper function to broadcast a message to all connected clients
async def broadcast(message):
    for connection in active_connections.values():
        try:
            await connection.send(message)
        except websockets.exceptions.ConnectionClosed:
            pass

# Function to handle an individual client connection
async def handle_connection(websocket, path):
    # Receive the first message, which is expected to be the username
    try:
        username = await websocket.recv()
        if username in active_connections:
            await websocket.send("Username already taken. Please reconnect with a different username.")
            return

        # Add the username and websocket connection to active connections
        active_connections[username] = websocket
        await broadcast(f"{username} has joined the chat.")
        print(f"{username} connected.")  # Log connection for server admin

        # Main loop to handle messages from the client
        while True:
            try:
                message = await websocket.recv()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                broadcast_message = f"[{timestamp}] {username}: {message}"
                await broadcast(broadcast_message)
            except websockets.exceptions.ConnectionClosed:
                break

    except Exception as e:
        print(f"Error in connection: {str(e)}")  # Log error for server admin

    finally:
        # Remove the client from active connections on disconnect
        if username in active_connections:
            del active_connections[username]
            await broadcast(f"{username} has left the chat.")
            print(f"{username} disconnected.")  # Log disconnection for server admin

# Start the WebSocket server
async def start_server():
    print("Starting WebSocket chat server...")
    async with websockets.serve(handle_connection, "0.0.0.0", 6789):
        await asyncio.Future()  # Run forever

# Entry point of the application
if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("Server stopped manually.")
    except Exception as e:
        print(f"Server error: {str(e)}")
```

**Features of this code:**
1. Establishes a WebSocket server for live chat communication using asyncio and websockets.
2. Supports multiple clients connecting and chatting simultaneously.
3. Includes a mechanism to broadcast messages to all connected clients.
4. Handles errors like duplicate usernames and connection interruptions gracefully.
5. Logs activity for server administrators for monitoring purposes.
