"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namebudget.net
Prompt: Write code to implement a live chat feature for domain registration support, mimicking the functionality provided by NameBudget.net's customer success team.
Generated: DETERMINISTIC_dca0acfae1d1f502
Batch ID: 20250612_152441
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
import datetime

# Constants for the server
HOST = 'localhost'
PORT = 8765

# Dictionary to store connected clients
connected_clients = {}

async def broadcast_message(message, sender):
    """
    Broadcast a message to all connected clients except the sender.
    """
    for client, username in connected_clients.items():
        if client != sender:
            try:
                await client.send(message)
            except Exception as e:
                print(f"Error sending message to {username}: {e}")

async def handle_messages(websocket, path):
    """
    Handle incoming messages from a client and manage chat functionality.
    """
    try:
        # Ask for the client's username
        await websocket.send("Welcome to Domain Registration Support Live Chat!\nPlease enter your username:")
        username = await websocket.recv()
        connected_clients[websocket] = username

        # Notify others that a user has joined
        welcome_message = f"{username} has joined the chat!"
        print(welcome_message)
        await broadcast_message(welcome_message, websocket)

        # Continuous message handling
        while True:
            message = await websocket.recv()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_message = f"[{timestamp}] {username}: {message}"
            print(formatted_message)  # Log the message on the server
            await broadcast_message(formatted_message, websocket)

    except websockets.exceptions.ConnectionClosed:
        # Handle client disconnection
        if websocket in connected_clients:
            disconnected_user = connected_clients.pop(websocket)
            disconnect_message = f"{disconnected_user} has left the chat."
            print(disconnect_message)
            await broadcast_message(disconnect_message, None)

    except Exception as e:
        print(f"Error handling messages: {e}")

async def start_server():
    """
    Start the WebSocket server for handling chat.
    """
    print(f"Starting chat server on ws://{HOST}:{PORT}")
    async with websockets.serve(handle_messages, HOST, PORT):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("\nChat server stopped manually.")
    except Exception as e:
        print(f"Error starting server: {e}")
```
