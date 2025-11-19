"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: Generate a script to implement live chat features between sponsors and clients during a virtual event using VME's web portal.
Generated: DETERMINISTIC_c1e04a14f21956ee
Batch ID: 20250612_162051
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

# Define constants for server configuration
HOST = 'localhost'
PORT = 8765

# Dictionary to store active connections
connections = {}

async def register_connection(websocket, user_role, user_id):
    """Register a new connection to the server."""
    connections[user_id] = {
        'role': user_role,
        'websocket': websocket
    }
    print(f"{user_role.capitalize()} {user_id} has connected.")

async def unregister_connection(user_id):
    """Unregister a connection from the server."""
    if user_id in connections:
        del connections[user_id]
        print(f"User {user_id} has disconnected.")

async def handle_message(websocket, message, sender_id):
    """Handle incoming messages and route them appropriately."""
    try:
        data = json.loads(message)
        recipient_id = data.get('recipient_id')
        content = data.get('content')

        if recipient_id in connections:
            recipient_ws = connections[recipient_id]['websocket']
            # Forward the message to the recipient
            await recipient_ws.send(json.dumps({
                'sender_id': sender_id,
                'content': content
            }))
        else:
            # Error: Recipient not found
            await websocket.send(json.dumps({
                'error': 'Recipient not found or is offline.'
            }))
    except json.JSONDecodeError:
        # Error: Invalid JSON
        await websocket.send(json.dumps({
            'error': 'Invalid message format.'
        }))

async def handle_connection(websocket, path):
    """Handle new websocket connections."""
    try:
        # Receive initial user data (role and ID) from the client
        initial_data = await websocket.recv()
        data = json.loads(initial_data)
        user_role = data.get('role')
        user_id = data.get('user_id')

        if not user_role or not user_id:
            await websocket.send(json.dumps({
                'error': 'Invalid connection data.'
            }))
            return

        # Register the connection
        await register_connection(websocket, user_role, user_id)

        # Listen for incoming messages
        async for message in websocket:
            await handle_message(websocket, message, sender_id=user_id)
    except websockets.exceptions.ConnectionClosed:
        # Handle disconnection
        print(f"Connection closed for User {user_id}.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Unregister connection on exit
        await unregister_connection(user_id)

# Start the websocket server
async def main():
    print(f"Starting WebSocket server on ws://{HOST}:{PORT}")
    async with websockets.serve(handle_connection, HOST, PORT):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server shut down gracefully.")

```
