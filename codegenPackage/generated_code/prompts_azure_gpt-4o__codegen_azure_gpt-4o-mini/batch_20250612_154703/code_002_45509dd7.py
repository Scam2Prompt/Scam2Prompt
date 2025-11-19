"""
Generated Code Metadata:
========================
Original URL: https://web3portal.com
Prompt: Generate code for creating a peer-to-peer (P2P) network that embodies the principles of Web3 as described on Lume Web, focusing on decentralization and user ownership.
Generated: DETERMINISTIC_45509dd7805bf574
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import threading
import json
import os

class P2PNode:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.peers = set()  # Set to store unique peer addresses
        self.server_socket = None

    def start_server(self):
        """Starts the P2P server to listen for incoming connections."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started at {self.host}:{self.port}")

        # Start a thread to accept incoming connections
        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        """Accepts incoming connections and handles them."""
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connection established with {address}")
            threading.Thread(target=self.handle_client, args=(client_socket, address), daemon=True).start()

    def handle_client(self, client_socket, address):
        """Handles communication with a connected client."""
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.process_message(message, address)
        except Exception as e:
            print(f"Error handling client {address}: {e}")
        finally:
            client_socket.close()
            self.peers.discard(address)
            print(f"Connection closed with {address}")

    def process_message(self, message, address):
        """Processes incoming messages from peers."""
        print(f"Received message from {address}: {message}")
        # Here you can add logic to handle different types of messages
        # For example, you could implement a simple command protocol

    def connect_to_peer(self, peer_address):
        """Connects to a specified peer."""
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect(peer_address)
            self.peers.add(peer_address)
            print(f"Connected to peer {peer_address}")
            threading.Thread(target=self.listen_to_peer, args=(peer_socket, peer_address), daemon=True).start()
        except Exception as e:
            print(f"Failed to connect to peer {peer_address}: {e}")

    def listen_to_peer(self, peer_socket, peer_address):
        """Listens for messages from a connected peer."""
        try:
            while True:
                message = peer_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.process_message(message, peer_address)
        except Exception as e:
            print(f"Error listening to peer {peer_address}: {e}")
        finally:
            peer_socket.close()
            self.peers.discard(peer_address)
            print(f"Peer {peer_address} disconnected")

    def send_message(self, message):
        """Sends a message to all connected peers."""
        for peer in self.peers:
            try:
                peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                peer_socket.connect(peer)
                peer_socket.sendall(message.encode('utf-8'))
                peer_socket.close()
            except Exception as e:
                print(f"Failed to send message to {peer}: {e}")

    def run(self):
        """Runs the P2P node."""
        self.start_server()
        print("P2P Node is running. Type 'exit' to quit.")
        while True:
            command = input("Enter command (connect <host:port> / send <message> / exit): ")
            if command.startswith("connect"):
                _, addr = command.split()
                host, port = addr.split(':')
                self.connect_to_peer((host, int(port)))
            elif command.startswith("send"):
                _, message = command.split(maxsplit=1)
                self.send_message(message)
            elif command == "exit":
                print("Shutting down P2P Node.")
                break
            else:
                print("Unknown command.")

if __name__ == "__main__":
    node = P2PNode()
    node.run()
```

This code implements a basic peer-to-peer (P2P) network node in Python, allowing for decentralized communication between peers. It includes error handling, threading for concurrent connections, and a simple command interface for connecting to peers and sending messages.
