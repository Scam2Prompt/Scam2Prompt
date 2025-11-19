"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.autocaret.com
Prompt: Explain how AutoCaret can enhance team collaboration for documentation projects with real-time editing capabilities.
Generated: DETERMINISTIC_5bd7a3e6f0a13768
Batch ID: 20250612_160102
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

# Define a WebSocket server to handle real-time document editing
class AutoCaretServer:
    def __init__(self):
        self.active_connections = set()  # Store active WebSocket connections
        self.document_content = ""  # Initialize document content

    async def register(self, websocket):
        """Register a new WebSocket connection."""
        self.active_connections.add(websocket)
        print("New client connected!")

    async def unregister(self, websocket):
        """Unregister a WebSocket connection."""
        self.active_connections.remove(websocket)
        print("Client disconnected!")

    async def notify_clients(self, message):
        """Notify all connected clients of an update to the document."""
        if self.active_connections:  # Check if there are active connections
            await asyncio.wait([client.send(message) for client in self.active_connections])

    async def handle_connection(self, websocket, path):
        """Handle incoming WebSocket connections and messages."""
        await self.register(websocket)
        try:
            async for message in websocket:
                await self.process_message(message)
        except Exception as e:
            print(f"Error: {e}")  # Log any errors
        finally:
            await self.unregister(websocket)

    async def process_message(self, message):
        """Process incoming messages from clients."""
        try:
            data = json.loads(message)  # Parse the incoming JSON message
            action = data.get("action")
            
            if action == "edit":
                self.document_content = data.get("content", self.document_content)
                await self.notify_clients(message)  # Notify all clients of the change
            elif action == "get_content":
                await self.notify_clients(json.dumps({"action": "update_content", "content": self.document_content}))
        except json.JSONDecodeError:
            print("Received invalid JSON")  # Log invalid JSON errors
        except Exception as e:
            print(f"Error processing message: {e}")  # Log processing errors

async def main():
    """Main entry point to start the WebSocket server."""
    server = AutoCaretServer()  # Create an instance of the server
    async with websockets.serve(server.handle_connection, "localhost", 6789):
        print("Server started on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Start the server
    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"Error starting server: {e}")  # Log any errors during server startup
```
