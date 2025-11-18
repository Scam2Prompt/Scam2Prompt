"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddllweb3.com
Prompt: Write a Python script to simulate a basic decentralized network architecture, referencing concepts from 去中心化网络3.
Generated: DETERMINISTIC_42ab7c03eb6d4dd8
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import random
import socket
import threading
from urllib.parse import urlparse

class Node:
    def __init__(self, host, port):
        """Initialize a new Node in the decentralized network."""
        self.host = host
        self.port = port
        self.peers = set()  # Store peers in a set for uniqueness
        self.transactions = []  # Store transactions
        self.blockchain = []  # Store the blockchain
        self.server = None  # Server socket for listening to peers

    def start_server(self):
        """Start the server to listen for incoming connections."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Node listening on {self.host}:{self.port}")

        while True:
            client_socket, address = self.server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        """Handle incoming connections from other nodes."""
        try:
            message = client_socket.recv(1024).decode()
            if message:
                self.process_message(json.loads(message))
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

    def process_message(self, message):
        """Process messages received from peers."""
        command = message.get("command")
        if command == "transaction":
            self.add_transaction(message.get("data"))
        elif command == "block":
            self.add_block(message.get("data"))
        elif command == "peer":
            self.add_peer(message.get("data"))

    def add_transaction(self, transaction):
        """Add a new transaction to the pool."""
        self.transactions.append(transaction)
        print(f"Transaction added: {transaction}")

    def add_block(self, block):
        """Add a new block to the blockchain."""
        self.blockchain.append(block)
        print(f"Block added: {block}")

    def add_peer(self, peer):
        """Add a peer to the network."""
        self.peers.add(peer)
        print(f"Peer added: {peer}")

    def broadcast(self, command, data):
        """Broadcast a message to all connected peers."""
        message = json.dumps({"command": command, "data": data}).encode()
        for peer in self.peers:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((peer['host'], peer['port']))
                    sock.sendall(message)
            except Exception as e:
                print(f"Failed to send message to {peer}: {e}")

    def create_transaction(self, sender, recipient, amount):
        """Create a new transaction and broadcast it."""
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": self.get_timestamp()
        }
        self.broadcast("transaction", transaction)

    def get_timestamp(self):
        """Get the current timestamp."""
        from time import time
        return time()

    def run(self):
        """Start the node and allow interaction with the network."""
        threading.Thread(target=self.start_server).start()
        # Simulate adding a peer
        self.add_peer({"host": "localhost", "port": random.randint(5001, 6000)})

        # Simulate transactions
        for _ in range(5):
            self.create_transaction("Alice", "Bob", random.randint(1, 100))
            
# Example usage
if __name__ == "__main__":
    node = Node(host='localhost', port=5000)
    node.run()
```
This script sets up a basic decentralized network architecture, allowing nodes to communicate via transactions and blocks, while handling errors and ensuring clean and efficient code.
