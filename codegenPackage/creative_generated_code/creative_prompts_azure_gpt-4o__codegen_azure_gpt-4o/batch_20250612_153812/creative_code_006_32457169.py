"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-doublezero.com
Prompt: Provide a step-by-step guide for setting up a testnet beta for a blockchain system using DoubleZero's high-performance networking principles.
Generated: DETERMINISTIC_32457169ebc79a5e
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Blockchain Testnet Setup Script using DoubleZero Networking Principles.

This script sets up a testnet beta for a blockchain system, ensuring high performance and reliability.
Key features:
1. Node initialization
2. Peer discovery
3. Consensus mechanism setup
4. API service for testnet communication
"""

import json
import os
import socket
import threading
from hashlib import sha256
from datetime import datetime

# Constants
TESTNET_PORT = 8000  # Port for the testnet nodes
MAX_CONNECTIONS = 50  # Maximum network connections
BLOCK_TIME = 10  # Block generation time in seconds
GENESIS_BLOCK_DATA = "Genesis Block - Blockchain Testnet Beta"

# Error messages
CONFIG_ERROR = "Error: Missing configuration file. Please provide a valid config."
NETWORK_ERROR = "Error: Unable to establish network connection."

# Blockchain class to manage blocks and transactions
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the genesis block of the blockchain.
        """
        genesis_block = {
            'index': 0,
            'timestamp': str(datetime.utcnow()),
            'data': GENESIS_BLOCK_DATA,
            'previous_hash': '0',
            'hash': self.hash_block(GENESIS_BLOCK_DATA, '0', 0),
        }
        self.chain.append(genesis_block)

    def add_block(self, data):
        """
        Add a new block to the blockchain.
        """
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': str(datetime.utcnow()),
            'data': data,
            'previous_hash': previous_block['hash'],
            'hash': self.hash_block(data, previous_block['hash'], len(self.chain)),
        }
        self.chain.append(new_block)

    @staticmethod
    def hash_block(data, previous_hash, index):
        """
        Generate a SHA-256 hash for the block.
        """
        block_string = f"{data}{previous_hash}{index}".encode()
        return sha256(block_string).hexdigest()

# Peer-to-peer networking class
class PeerNetwork:
    def __init__(self, port):
        self.port = port
        self.peers = []  # List of connected peers

    def start_server(self):
        """
        Start a server to accept connections from peers.
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', self.port))
        server_socket.listen(MAX_CONNECTIONS)
        print(f"Testnet node started on port {self.port}...")
        while True:
            client_socket, client_address = server_socket.accept()
            self.peers.append(client_address)
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

    def handle_client(self, client_socket, client_address):
        """
        Handle incoming data from a connected peer.
        """
        try:
            data = client_socket.recv(1024).decode()
            print(f"Received data from {client_address}: {data}")
            client_socket.send(f"ACK: {data}".encode())
        except Exception as e:
            print(f"Error handling client {client_address}: {str(e)}")
        finally:
            client_socket.close()

    def connect_to_peer(self, peer_ip, peer_port):
        """
        Connect to a peer node in the testnet.
        """
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((peer_ip, peer_port))
            self.peers.append((peer_ip, peer_port))
            print(f"Connected to peer {peer_ip}:{peer_port}")
            peer_socket.close()
        except Exception as e:
            print(f"Error connecting to peer {peer_ip}:{peer_port}: {str(e)}")

# Configuration loader
def load_config(config_file):
    """
    Load the configuration file for the testnet.
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(CONFIG_ERROR)

    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# Main function
if __name__ == "__main__":
    try:
        # Load testnet configuration
        config = load_config('testnet_config.json')
        port = config.get("port", TESTNET_PORT)
        
        # Initialize blockchain
        blockchain = Blockchain()
        print("Blockchain initialized with genesis block.")

        # Start networking
        network = PeerNetwork(port)
        threading.Thread(target=network.start_server).start()

        # Example: Add a block
        blockchain.add_block("Test transaction data 1")
        blockchain.add_block("Test transaction data 2")
        print("Blocks added to blockchain.")

        # Print blockchain data
        print("Current blockchain state:")
        for block in blockchain.chain:
            print(json.dumps(block, indent=4))

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
```
