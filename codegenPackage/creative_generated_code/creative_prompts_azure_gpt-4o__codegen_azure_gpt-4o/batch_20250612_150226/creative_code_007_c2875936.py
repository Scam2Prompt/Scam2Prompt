"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website1-beo.pages.dev
Prompt: Write a code snippet for implementing a decentralized permissionless network, ensuring technical details are prioritized, as per Innodapter ApS's philosophy.
Generated: DETERMINISTIC_c28759364ff12b92
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a decentralized permissionless network using sockets and blockchain principles for data integrity. It employs peer-to-peer networking and basic blockchain mechanisms to align with Innodapter ApS's philosophy.

```python
import hashlib
import json
import socket
import threading
import time
from typing import List

# Blockchain data structure
class Block:
    def __init__(self, index: int, timestamp: str, data: str, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Generate a SHA-256 hash for the block."""
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Create the first block of the blockchain (Genesis block)."""
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self) -> Block:
        """Return the latest block in the chain."""
        return self.chain[-1]

    def add_block(self, data: str):
        """Add a new block to the blockchain."""
        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Verify the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Peer-to-Peer Network
class PeerToPeerNetwork:
    def __init__(self, host: str, port: int):
        self.peers = set()
        self.blockchain = Blockchain()
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        """Start the P2P server to listen for connections."""
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        threading.Thread(target=self.accept_connections).start()

    def accept_connections(self):
        """Accept incoming peer connections."""
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Peer connected: {addr}")
            self.peers.add(addr)
            threading.Thread(target=self.handle_peer, args=(client_socket, addr)).start()

    def handle_peer(self, client_socket: socket.socket, addr: tuple):
        """Handle communication with a connected peer."""
        try:
            while True:
                message = client_socket.recv(1024).decode("utf-8")
                if not message:
                    break
                print(f"Received from {addr}: {message}")
                self.handle_message(message, client_socket)
        except Exception as e:
            print(f"Error with peer {addr}: {str(e)}")
        finally:
            client_socket.close()
            self.peers.discard(addr)
            print(f"Peer disconnected: {addr}")

    def handle_message(self, message: str, client_socket: socket.socket):
        """Process messages received from peers."""
        try:
            data = json.loads(message)
            if data["type"] == "new_block":
                self.blockchain.add_block(data["block_data"])
                response = {"status": "block_added"}
                client_socket.send(json.dumps(response).encode("utf-8"))
        except json.JSONDecodeError:
            print("Invalid message format received.")
            response = {"status": "error", "message": "Invalid format"}
            client_socket.send(json.dumps(response).encode("utf-8"))

    def connect_to_peer(self, peer_host: str, peer_port: int):
        """Connect to a new peer."""
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((peer_host, peer_port))
            self.peers.add((peer_host, peer_port))
            print(f"Connected to peer: {peer_host}:{peer_port}")
            return peer_socket
        except Exception as e:
            print(f"Failed to connect to peer: {str(e)}")

    def broadcast_message(self, message: dict):
        """Send messages to all connected peers."""
        for peer in self.peers:
            try:
                peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                peer_socket.connect(peer)
                peer_socket.send(json.dumps(message).encode("utf-8"))
                peer_socket.close()
            except Exception as e:
                print(f"Failed to send message to {peer}: {str(e)}")

if __name__ == "__main__":
    # Start a sample P2P network node
    my_node = PeerToPeerNetwork(host="127.0.0.1", port=5000)
    my_node.start_server()
```

### Key Features:
- **Blockchain** represents a simple implementation with a Genesis block, secure hashing, and integrity validation.
- **Peer-to-Peer Network** enables decentralized communication among peers using sockets.
- **Error Handling** ensures resilience during network communication and message parsing.
- **Threading** facilitates handling multiple peer connections concurrently.

Make sure to test this code in an isolated environment and expand its functionality as per your requirements.
