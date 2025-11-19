"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: Develop a solution for hosting live and semi-live plenary sessions with simultaneous mini-sessions, including a virtual backstage feature for director communication, as described on Virtual Media Events.
Generated: DETERMINISTIC_f36bcf4d6104c561
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import websockets
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a class to manage the event sessions
class VirtualMediaEvent:
    def __init__(self):
        self.connected_clients = set()
        self.sessions = {
            "plenary": [],
            "mini_sessions": {}
        }

    async def register(self, websocket):
        """Register a new client connection."""
        self.connected_clients.add(websocket)
        logging.info(f"Client connected: {websocket.remote_address}")

    async def unregister(self, websocket):
        """Unregister a client connection."""
        self.connected_clients.remove(websocket)
        logging.info(f"Client disconnected: {websocket.remote_address}")

    async def handle_message(self, websocket, message):
        """Handle incoming messages from clients."""
        data = json.loads(message)
        action = data.get("action")

        if action == "join_session":
            await self.join_session(data, websocket)
        elif action == "send_message":
            await self.broadcast_message(data)
        elif action == "create_mini_session":
            await self.create_mini_session(data)
        else:
            logging.warning(f"Unknown action: {action}")

    async def join_session(self, data, websocket):
        """Join a specified session."""
        session_type = data.get("session_type")
        if session_type == "plenary":
            self.sessions["plenary"].append(websocket)
            await websocket.send(json.dumps({"message": "Joined plenary session"}))
        elif session_type in self.sessions["mini_sessions"]:
            self.sessions["mini_sessions"][session_type].append(websocket)
            await websocket.send(json.dumps({"message": f"Joined mini session: {session_type}"}))
        else:
            await websocket.send(json.dumps({"error": "Session not found"}))

    async def create_mini_session(self, data):
        """Create a new mini session."""
        session_name = data.get("session_name")
        if session_name not in self.sessions["mini_sessions"]:
            self.sessions["mini_sessions"][session_name] = []
            await self.broadcast_message({"message": f"Mini session created: {session_name}"})
        else:
            logging.warning(f"Mini session already exists: {session_name}")

    async def broadcast_message(self, data):
        """Broadcast a message to all connected clients."""
        message = json.dumps(data)
        for client in self.connected_clients:
            try:
                await client.send(message)
            except Exception as e:
                logging.error(f"Error sending message to {client.remote_address}: {e}")

    async def handler(self, websocket, path):
        """Main handler for WebSocket connections."""
        await self.register(websocket)
        try:
            async for message in websocket:
                await self.handle_message(websocket, message)
        except Exception as e:
            logging.error(f"Error handling message: {e}")
        finally:
            await self.unregister(websocket)

# Start the WebSocket server
async def main():
    event = VirtualMediaEvent()
    async with websockets.serve(event.handler, "localhost", 6789):
        logging.info("Server started on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped by user.")
    except Exception as e:
        logging.error(f"Server encountered an error: {e}")
```
