"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yoway.com
Prompt: Illustrate how to implement a live chat feature for customer support on an online gaming platform similar to Gempa777.
Generated: DETERMINISTIC_79a7dedc57dea3fd
Batch ID: 20250612_164132
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
from datetime import datetime

# Define constants
HOST = "localhost"
PORT = 6789

# Active connections dictionary to track connected users
active_connections = {}

# Function to broadcast a message to all connected users
async def broadcast_message(message, sender):
    """
    Broadcast a message to all connected users except the sender.
    
    :param message: The message to be broadcasted.
    :param sender: The WebSocket connection of the sender.
    """
    for connection in active_connections.values():
        if connection != sender:
            try:
                await connection.send(message)
            except websockets.exceptions.ConnectionClosedError:
                # Handle the case where a connection was closed unexpectedly
                pass

# Function to handle incoming client connections
async def handle_client(websocket, path):
    """
    Handle communication with a connected client.
    
    :param websocket: The WebSocket connection for the client.
    :param path: The WebSocket connection path.
    """
    try:
        # Register the new connection
        client_id = f"User_{len(active_connections) + 1}"
        active_connections[client_id] = websocket
        print(f"{client_id} connected.")

        # Notify all users of the new participant
        await broadcast_message(f"{client_id} has joined the chat!", websocket)

        # Event loop to receive and process messages from the client
        async for message in websocket:
            formatted_message = f"{client_id} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}): {message}"
            print(f"Received: {formatted_message}")
            await broadcast_message(formatted_message, websocket)

    except websockets.exceptions.ConnectionClosedError:
        print(f"{client_id} disconnected.")
    finally:
        # Clean up disconnected clients
        if client_id in active_connections:
            del active_connections[client_id]
            await broadcast_message(f"{client_id} has left the chat.", websocket)

# Main function to start the WebSocket server
async def main():
    """
    Start the WebSocket server for live chat.
    """
    print(f"Starting live chat server on {HOST}:{PORT}")
    async with websockets.serve(handle_client, HOST, PORT):
        await asyncio.Future()  # Run forever

# Entry point for the script
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Live chat server stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code implements a basic live chat feature using Python's `asyncio` and `websockets` libraries. It provides real-time communication between users, with proper error handling and clean, production-ready code.
