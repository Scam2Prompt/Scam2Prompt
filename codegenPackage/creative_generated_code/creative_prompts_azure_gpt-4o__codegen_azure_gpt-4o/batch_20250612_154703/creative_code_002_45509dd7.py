"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal.com
Prompt: Generate code for creating a peer-to-peer (P2P) network that embodies the principles of Web3 as described on Lume Web, focusing on decentralization and user ownership.
Generated: DETERMINISTIC_45509dd7805bf574
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import json
import logging
import os
import websockets
from hashlib import sha256

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
PORT = 8765  # Default port to run the P2P node
PEERS = set()  # Set to store connected peers
DATA_STORE = {}  # Simulated decentralized data store

# Utility: Generate a unique identifier for peers
def generate_peer_id():
    return sha256(os.urandom(32)).hexdigest()

# Utility: Broadcast a message to all connected peers
async def broadcast(message):
    if PEERS:
        logging.info(f"Broadcasting message to {len(PEERS)} peers: {message}")
        await asyncio.wait([peer.send(message) for peer in PEERS])
    else:
        logging.warning("No peers to broadcast to.")

# Handler: Handle incoming messages
async def handle_message(peer, message):
    try:
        logging.info(f"Received message from peer: {message}")
        data = json.loads(message)

        if data['type'] == 'store':
            # Store data in decentralized storage
            key = data['key']
            value = data['value']
            DATA_STORE[key] = value
            logging.info(f"Data stored: {key} -> {value}")
            await broadcast(json.dumps({"type": "update", "key": key, "value": value}))
        
        elif data['type'] == 'get':
            # Retrieve data from decentralized storage
            key = data['key']
            value = DATA_STORE.get(key, None)
            response = {"type": "response", "key": key, "value": value}
            await peer.send(json.dumps(response))

        elif data['type'] == 'update':
            # Update peers with new data
            key = data['key']
            value = data['value']
            DATA_STORE[key] = value
            logging.info(f"Data updated from peer: {key} -> {value}")

    except json.JSONDecodeError:
        logging.error("Failed to parse incoming message. Ensure it is valid JSON.")
    except Exception as e:
        logging.error(f"Error handling message: {e}")

# Handler: Manage new peer connections
async def register_peer(websocket):
    peer_id = generate_peer_id()
    PEERS.add(websocket)
    logging.info(f"New peer connected: {peer_id}")
    await websocket.send(json.dumps({"type": "welcome", "peer_id": peer_id}))

# Handler: Manage peer disconnections
async def unregister_peer(websocket):
    PEERS.remove(websocket)
    logging.info("Peer disconnected.")

# Main WebSocket server handler
async def p2p_handler(websocket, path):
    await register_peer(websocket)
    try:
        async for message in websocket:
            await handle_message(websocket, message)
    except websockets.ConnectionClosed:
        logging.warning("Connection closed.")
    finally:
        await unregister_peer(websocket)

# Entry point: Start the WebSocket server
async def start_server():
    logging.info(f"Starting P2P Web3 server on port {PORT}...")
    server = await websockets.serve(p2p_handler, "localhost", PORT)
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        logging.info("Server stopped manually.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
