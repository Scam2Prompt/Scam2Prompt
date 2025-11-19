"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Illustrate how to implement a 24/7 support chat feature for a gaming website like BaxBet, ensuring users can get help with their queries at any time.
Generated: DETERMINISTIC_91d3641d13e3c5c0
Batch ID: 20250612_160045
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set the server port
PORT = 8765

# Store active clients
active_clients = set()

async def handle_client(websocket, path):
    """Handle incoming WebSocket connections from clients."""
    # Add the new client to the active clients set
    active_clients.add(websocket)
    logging.info(f"Client connected: {websocket.remote_address}")

    try:
        async for message in websocket:
            # Process incoming messages
            await process_message(websocket, message)
    except websockets.ConnectionClosed as e:
        logging.info(f"Client disconnected: {websocket.remote_address}, reason: {e.reason}")
    finally:
        # Remove client from the active clients set
        active_clients.remove(websocket)

async def process_message(websocket, message):
    """Process client messages and respond appropriately."""
    try:
        # Parse incoming JSON message
        data = json.loads(message)
        user_message = data.get("message", "")
        user_id = data.get("user_id", "")

        logging.info(f"Message from {user_id}: {user_message}")

        # Generate a response (this can be replaced with actual support logic)
        response = {
            "user_id": user_id,
            "response": f"Support message received: {user_message}"
        }

        # Send response back to the client
        await websocket.send(json.dumps(response))

    except json.JSONDecodeError:
        logging.error("Invalid JSON received")
        await websocket.send(json.dumps({"error": "Invalid JSON format"}))
    except Exception as e:
        logging.error(f"Error processing message: {e}")
        await websocket.send(json.dumps({"error": "Internal server error"}))

async def main():
    """Main function to start the WebSocket server."""
    async with websockets.serve(handle_client, "localhost", PORT):
        logging.info(f"Server started on ws://localhost:{PORT}")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        # Run the server
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped by user")
    except Exception as e:
        logging.error(f"Server error: {e}")
```

This code implements a simple WebSocket server for a 24/7 support chat feature, designed to handle connections from multiple clients and respond to their queries.
