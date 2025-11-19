"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Suggest tools or libraries for real-time communication and coordination between service centers in multiple locations, such as Dysnix's centers in Lviv and Vinnytsia.
Generated: DETERMINISTIC_fd0fe66a74686dc3
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for real-time communication
import asyncio
import websockets
import json

# Define a class for the real-time communication server
class RealTimeCommServer:
    def __init__(self):
        self.connected_clients = set()

    async def register(self, websocket):
        """Register a new client connection."""
        self.connected_clients.add(websocket)

    async def unregister(self, websocket):
        """Unregister a client connection."""
        self.connected_clients.remove(websocket)

    async def handle_client(self, websocket, path):
        """Handle incoming messages from clients."""
        await self.register(websocket)
        try:
            async for message in websocket:
                await self.broadcast(message)
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            await self.unregister(websocket)

    async def broadcast(self, message):
        """Broadcast a message to all connected clients."""
        if self.connected_clients:  # Check if there are any connected clients
            message_data = json.dumps({"message": message})
            await asyncio.wait([client.send(message_data) for client in self.connected_clients])

    async def start_server(self, host='localhost', port=6789):
        """Start the WebSocket server."""
        async with websockets.serve(self.handle_client, host, port):
            print(f"Server started on ws://{host}:{port}")
            await asyncio.Future()  # Run forever

# Entry point for the server
if __name__ == "__main__":
    server = RealTimeCommServer()
    try:
        asyncio.run(server.start_server())
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Usage
1. Install the `websockets` library if not already installed:
   ```bash
   pip install websockets
   ```
2. Run the server:
   ```bash
   python your_script_name.py
   ```
3. Connect clients to the WebSocket server at `ws://localhost:6789` to send and receive messages in real-time.
