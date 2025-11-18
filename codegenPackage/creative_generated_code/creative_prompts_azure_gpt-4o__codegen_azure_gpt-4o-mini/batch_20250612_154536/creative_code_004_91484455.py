"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain.netlify.app
Prompt: Create a script to simulate the "Heartbeat Protocol" in a peer-to-peer network, ensuring that nodes share their state, transaction data, and environmental metrics periodically.
Generated: DETERMINISTIC_9148445523b354ed
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import json
import time
import threading
import random

# Constants for the heartbeat protocol
HEARTBEAT_INTERVAL = 5  # seconds
HEARTBEAT_TIMEOUT = 15  # seconds
PORT = 5000              # Port to listen on

class Node:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.peers = []
        self.is_alive = True
        self.state = {}
        self.lock = threading.Lock()
        
        # Start the server thread
        threading.Thread(target=self.start_server, daemon=True).start()
        
        # Start the heartbeat thread
        threading.Thread(target=self.send_heartbeat, daemon=True).start()

    def start_server(self):
        """Start a UDP server to listen for heartbeat messages from peers."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((self.hostname, self.port))
            print(f"Node listening on {self.hostname}:{self.port}")
            while self.is_alive:
                try:
                    data, addr = server_socket.recvfrom(1024)
                    self.handle_heartbeat(data, addr)
                except Exception as e:
                    print(f"Error receiving heartbeat: {e}")

    def send_heartbeat(self):
        """Send the heartbeat message to all known peers periodically."""
        while self.is_alive:
            self.state = self.collect_state()
            heartbeat_message = self.create_heartbeat_message()
            for peer in self.peers:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
                        client_socket.sendto(heartbeat_message.encode(), peer)
                except Exception as e:
                    print(f"Error sending heartbeat to {peer}: {e}")
            time.sleep(HEARTBEAT_INTERVAL)

    def collect_state(self):
        """Collect and return the current state of the node."""
        return {
            "transactions": random.randint(1, 100),  # Simulated transaction count
            "environment": {
                "cpu_usage": random.uniform(0.1, 100.0),
                "memory_usage": random.uniform(0.1, 100.0)
            }
        }

    def create_heartbeat_message(self):
        """Create a JSON formatted heartbeat message."""
        return json.dumps({
            "source": f"{self.hostname}:{self.port}",
            "state": self.state
        })

    def handle_heartbeat(self, data, addr):
        """Handle incoming heartbeat messages from peers."""
        try:
            message = json.loads(data.decode())
            print(f"Heartbeat received from {message['source']}: {message['state']}")
            # Update known peers if not already in the list
            if addr not in self.peers:
                self.peers.append(addr)
        except json.JSONDecodeError:
            print(f"Invalid heartbeat message from {addr}")

    def shutdown(self):
        """Gracefully shutdown the node."""
        self.is_alive = False
        print("Shutting down the node...")

if __name__ == "__main__":
    # Example usage
    node = Node('127.0.0.1', PORT)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        node.shutdown()
```
