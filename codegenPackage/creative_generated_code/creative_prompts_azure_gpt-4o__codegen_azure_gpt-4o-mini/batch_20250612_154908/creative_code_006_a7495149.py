"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: Write code to enable real-time updates for funding round statuses using WebSockets or a similar technology, as might be required for Gitcoin's Round Manager.
Generated: DETERMINISTIC_a7495149e1f00ad9
Batch ID: 20250612_154908
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a class to manage funding round statuses
class FundingRoundManager:
    def __init__(self):
        # Initialize a dictionary to hold funding round statuses
        self.round_statuses = {}

    async def update_status(self, round_id, status):
        """Update the funding round status and notify clients."""
        self.round_statuses[round_id] = status
        # Notify all connected clients about the status update
        await self.notify_clients(round_id, status)

    async def notify_clients(self, round_id, status):
        """Notify all clients about the funding round status change."""
        message = json.dumps({"round_id": round_id, "status": status})
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    async def register(self, websocket):
        """Register a new client connection."""
        if not hasattr(self, 'clients'):
            self.clients = set()  # Initialize the set of clients
        self.clients.add(websocket)
        try:
            # Keep the connection open
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)

# Create an instance of the FundingRoundManager
manager = FundingRoundManager()

async def handle_connection(websocket, path):
    """Handle incoming WebSocket connections."""
    await manager.register(websocket)

async def main():
    """Main entry point for the WebSocket server."""
    server = await websockets.serve(handle_connection, "localhost", 6789)
    logging.info("WebSocket server started on ws://localhost:6789")
    try:
        await server.wait_closed()  # Keep the server running
    except Exception as e:
        logging.error(f"Server error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped manually.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```

This code creates a WebSocket server that listens for incoming connections and allows real-time updates of funding round statuses. Each time a status is updated, all connected clients receive a notification. Proper error handling and logging have been implemented to ensure the server runs smoothly in a production environment.
