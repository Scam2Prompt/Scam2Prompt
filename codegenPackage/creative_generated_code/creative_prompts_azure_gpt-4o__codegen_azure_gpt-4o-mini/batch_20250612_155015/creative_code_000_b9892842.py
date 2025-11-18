"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superlbride.com
Prompt: Write Python code to simulate advanced networking infrastructure similar to the solutions described by SuperBridge, ensuring seamless connectivity across multiple nodes.
Generated: DETERMINISTIC_b9892842e51c4a68
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import threading
import json
import time
import random

class Node:
    """
    Represents a network node in a simulated advanced networking infrastructure.
    Responsible for sending and receiving messages to and from other nodes.
    """

    def __init__(self, host, port):
        """
        Initialize a new Node instance.

        :param host: Host address of the node.
        :param port: Port number for the node's communication.
        """
        self.host = host
        self.port = port
        self.running = True
        self.peers = {}  # Dictionary to store peer nodes

        # Create a socket for the node
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))

    def start(self):
        """
        Start the node to listen for incoming messages.
        """
        print(f"Node started at {self.host}:{self.port}")
        threading.Thread(target=self.listen_for_messages, daemon=True).start()

    def listen_for_messages(self):
        """
        Continuously listen for incoming messages from peers.
        """
        while self.running:
            try:
                message, addr = self.server_socket.recvfrom(1024)
                self.handle_message(message.decode('utf-8'), addr)
            except Exception as e:
                print(f"Error listening for messages: {e}")

    def handle_message(self, message, addr):
        """
        Handle incoming messages from peers.

        :param message: The message received from the peer.
        :param addr: The address of the sending peer.
        """
        print(f"Message received from {addr}: {message}")
        data = json.loads(message)

        # Add the sender to the known peers
        if addr not in self.peers:
            self.peers[addr] = data['node_id']

        # Echo the message back to all peers
        self.broadcast_message(message)

    def broadcast_message(self, message):
        """
        Broadcast a message to all known peers.

        :param message: The message to be sent to peers.
        """
        for peer in self.peers.keys():
            try:
                self.server_socket.sendto(message.encode('utf-8'), peer)
            except Exception as e:
                print(f"Error sending message to {peer}: {e}")

    def send_message(self, message):
        """
        Send a message to a specific peer.

        :param message: The message to be sent.
        :param peer: The address of the peer to send the message to.
        """
        for peer in self.peers.keys():
            try:
                self.server_socket.sendto(message.encode('utf-8'), peer)
            except Exception as e:
                print(f"Error sending message to {peer}: {e}")

    def stop(self):
        """
        Stop the node and close the socket.
        """
        self.running = False
        self.server_socket.close()
        print(f"Node at {self.host}:{self.port} stopped.")

# Example usage
def main():
    """
    Main function to start the network simulation.
    """
    node_id = random.randint(1, 1000)
    node = Node(host='127.0.0.1', port=5000)
    node.start()

    try:
        while True:
            # Example of sending a message to all peers every 5 seconds
            message = json.dumps({'node_id': node_id, 'content': 'Hello from node!'})
            node.broadcast_message(message)
            time.sleep(5)
    except KeyboardInterrupt:
        node.stop()

if __name__ == "__main__":
    main()
```
