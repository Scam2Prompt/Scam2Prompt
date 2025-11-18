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
import json
import hashlib
import socket
import threading
from datetime import datetime

# Constants for the network
HOST = "127.0.0.1"  # Localhost
PORT = 5000         # Port for the node
PEERS = []          # List to store connected peers

# Helper function to generate a unique ID for nodes
def generate_node_id():
    timestamp = str(datetime.utcnow())
    return hashlib.sha256(timestamp.encode()).hexdigest()

class Node:
    """
    Class representing a node in the decentralized network.
    """
    def __init__(self, name, host, port):
        self.node_id = generate_node_id()
        self.name = name
        self.host = host
        self.port = port
        self.peers = []  # List of connected peers

    def start_server(self):
        """
        Starts the node as a server to listen for incoming connections.
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"[{self.name}] Node server started at {self.host}:{self.port}")
            while True:
                conn, addr = server_socket.accept()
                threading.Thread(target=self.handle_peer, args=(conn, addr)).start()
        except Exception as e:
            print(f"[Error] Failed to start server: {e}")
        finally:
            server_socket.close()

    def handle_peer(self, conn, addr):
        """
        Handles communication with connected peers.
        """
        print(f"[{self.name}] Peer connected: {addr}")
        try:
            while True:
                data = conn.recv(1024).decode("utf-8")
                if not data:
                    break
                print(f"[{self.name}] Received message: {data}")
                conn.send(f"Echo: {data}".encode("utf-8"))
        except Exception as e:
            print(f"[Error] Communication error with peer {addr}: {e}")
        finally:
            conn.close()
            print(f"[{self.name}] Peer disconnected: {addr}")

    def connect_to_peer(self, peer_host, peer_port):
        """
        Connects to another peer in the network.
        """
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((peer_host, peer_port))
            self.peers.append((peer_host, peer_port))
            print(f"[{self.name}] Connected to peer {peer_host}:{peer_port}")
            threading.Thread(target=self.send_receive, args=(peer_socket,)).start()
        except Exception as e:
            print(f"[Error] Failed to connect to peer {peer_host}:{peer_port}: {e}")

    def send_receive(self, peer_socket):
        """
        Sends and receives messages with a connected peer.
        """
        try:
            while True:
                message = input(f"[{self.name}] Enter message to send: ")
                if message.lower() == "exit":
                    break
                peer_socket.send(message.encode("utf-8"))
                response = peer_socket.recv(1024).decode("utf-8")
                print(f"[{self.name}] Response from peer: {response}")
        except Exception as e:
            print(f"[Error] Communication error with peer: {e}")
        finally:
            peer_socket.close()

# Main function to start a node
def main():
    """
    Entry point for the script. Initializes and starts a node in the network.
    """
    node_name = input("Enter node name: ")
    node = Node(name=node_name, host=HOST, port=PORT)

    print(f"[{node.name}] Node ID: {node.node_id}")

    threading.Thread(target=node.start_server).start()

    while True:
        command = input("[Command] Enter 'connect' to link to a peer or 'exit' to quit: ")
        if command.lower() == "connect":
            try:
                peer_host = input("Enter peer host: ")
                peer_port = int(input("Enter peer port: "))
                node.connect_to_peer(peer_host, peer_port)
            except ValueError:
                print("[Error] Invalid port number.")
        elif command.lower() == "exit":
            print("[Info] Shutting down node.")
            break
        else:
            print("[Error] Unknown command.")

if __name__ == "__main__":
    main()
```
