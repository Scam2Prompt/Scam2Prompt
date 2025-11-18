"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal.com
Prompt: Suggest APIs or libraries for building a decentralized chat system reminiscent of Web1-era IRC, as described in the historical context on Lume Web.
Generated: DETERMINISTIC_ece9c91c7bb35362
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a decentralized chat system
import asyncio
import websockets
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define constants for the server
HOST = 'localhost'
PORT = 6789

# Simple user storage for connected clients
clients = {}

async def register_client(websocket):
    """Register a new client connection."""
    clients[websocket] = websocket
    logging.info(f"A new client has connected: {websocket.remote_address}")

async def unregister_client(websocket):
    """Unregister a client connection when it disconnects."""
    if websocket in clients:
        del clients[websocket]
        logging.info(f"A client has disconnected: {websocket.remote_address}")

async def handle_messages(websocket, path):
    """Handle incoming messages from clients and broadcast them."""
    await register_client(websocket)
    
    try:
        async for message in websocket:
            # Parse incoming message
            data = json.loads(message)
            logging.info(f"Message received: {data}")

            # Broadcast message to all connected clients
            await broadcast_message(data)
    except Exception as e:
        logging.error(f"Error handling message: {e}")
    finally:
        await unregister_client(websocket)

async def broadcast_message(message):
    """Broadcast a message to all connected clients."""
    for client in clients:
        try:
            await client.send(json.dumps(message))
        except Exception as e:
            logging.error(f"Error sending message to {client.remote_address}: {e}")

# Start the WebSocket server
async def start_server():
    """Start the WebSocket server."""
    async with websockets.serve(handle_messages, HOST, PORT):
        logging.info(f"Server started on ws://{HOST}:{PORT}")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        logging.info("Server stopped by user.")
    except Exception as e:
        logging.error(f"Server encountered an error: {e}")
```

### Usage:
To run this code, ensure you have the `websockets` library installed. You can install it using:
```bash
pip install websockets
```

Then execute the script. This will start a WebSocket server that can handle multiple client connections, relay messages between them, and log actions.
