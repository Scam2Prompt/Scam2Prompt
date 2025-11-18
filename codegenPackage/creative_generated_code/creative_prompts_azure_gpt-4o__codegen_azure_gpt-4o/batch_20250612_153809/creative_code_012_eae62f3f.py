"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachaincoin.live
Prompt: Generate code for a peer-to-peer (P2P) communication system on SaitaChain to facilitate direct blockchain partner collaboration.
Generated: DETERMINISTIC_eae62f3ff31899e0
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: p2p_communication.py

import asyncio
import json
import logging
from hashlib import sha256
from websockets import serve

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
HOST = "127.0.0.1"  # Host for P2P communication
PORT = 8765         # Port for P2P communication

# Blockchain Node Class
class BlockchainNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.peers = set()  # Connected peers
        self.messages = []  # List to store messages

    async def handle_connection(self, websocket):
        """
        Handle incoming peer connections and messages.
        """
        try:
            # Receive and process messages from peers
            async for message in websocket:
                data = json.loads(message)
                logging.info(f"Received message: {data}")
                await self.process_message(data, websocket)
        except Exception as e:
            logging.error(f"Error handling connection: {e}")

    async def process_message(self, data, websocket):
        """
        Process incoming messages and take appropriate actions.
        """
        if data["type"] == "HELLO":
            # A new peer is introducing itself
            self.peers.add(data["node_id"])
            logging.info(f"New peer added: {data['node_id']}")
            await websocket.send(json.dumps({"type": "WELCOME", "message": "Welcome to SaitaChain"}))

        elif data["type"] == "TRANSACTION":
            # A transaction message is received
            transaction_hash = sha256(json.dumps(data["transaction"]).encode()).hexdigest()
            logging.info(f"Transaction received: {data['transaction']}")
            self.messages.append({"transaction": data["transaction"], "hash": transaction_hash})
            await websocket.send(json.dumps({"type": "ACK", "hash": transaction_hash}))

        else:
            logging.warning(f"Unknown message type: {data['type']}")

    async def send_message_to_peer(self, peer, message):
        """
        Send a message to a connected peer.
        """
        try:
            async with serve(peer, PORT) as websocket:
                await websocket.send(json.dumps(message))
                logging.info(f"Sent message to {peer}: {message}")
        except Exception as e:
            logging.error(f"Failed to send message to {peer}: {e}")

    async def start_server(self):
        """
        Start the P2P server to handle incoming connections.
        """
        server = serve(self.handle_connection, HOST, PORT)
        logging.info(f"Node {self.node_id} listening on {HOST}:{PORT}")
        await server

# Main script
if __name__ == "__main__":
    node_id = input("Enter Node ID: ")
    node = BlockchainNode(node_id)

    try:
        asyncio.run(node.start_server())
    except KeyboardInterrupt:
        logging.info("Shutting down the P2P system.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
