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
import logging
from typing import Dict, List

# Configure logger for debugging and error tracking
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("NetworkSimulator")


class Node:
    """
    A class representing a node in the networking infrastructure.
    Each node can send and receive data, simulating seamless connectivity.
    """
    def __init__(self, name: str, host: str, port: int):
        self.name = name
        self.host = host
        self.port = port
        self.connections: Dict[str, (str, int)] = {}  # Other nodes this node can connect to
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Start the server socket to listen for incoming connections from other nodes.
        """
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)  # Allow up to 5 simultaneous connections
            logger.info(f"{self.name} listening on {self.host}:{self.port}")
            threading.Thread(target=self._accept_connections, daemon=True).start()
        except socket.error as e:
            logger.error(f"Error starting server for {self.name}: {e}")
            self.server_socket.close()

    def connect_to_node(self, node_name: str, node_host: str, node_port: int):
        """
        Establish a connection to another node in the network.
        
        :param node_name: Name of the node to connect to
        :param node_host: Host of the node
        :param node_port: Port of the node
        """
        try:
            self.connections[node_name] = (node_host, node_port)
            logger.info(f"{self.name} successfully connected to {node_name} ({node_host}:{node_port})")
        except Exception as e:
            logger.error(f"Error connecting {self.name} to {node_name}: {e}")

    def send_message(self, node_name: str, message: str):
        """
        Send a message to a connected node.
        
        :param node_name: Name of the node to send the message to
        :param message: The message to send
        """
        try:
            if node_name not in self.connections:
                logger.warning(f"{self.name} is not connected to {node_name}. Message not sent.")
                return
            
            node_host, node_port = self.connections[node_name]
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((node_host, node_port))
                client_socket.sendall(json.dumps({"from": self.name, "message": message}).encode("utf-8"))
                logger.info(f"Message sent from {self.name} to {node_name}")
        except socket.error as e:
            logger.error(f"Error sending message from {self.name} to {node_name}: {e}")

    def _accept_connections(self):
        """
        Handle incoming connections and process received messages.
        """
        while True:
            try:
                client_socket, address = self.server_socket.accept()
                threading.Thread(
                    target=self._handle_client_connection, 
                    args=(client_socket, address),
                    daemon=True
                ).start()
            except socket.error as e:
                logger.error(f"Error accepting connection for {self.name}: {e}")
                break

    def _handle_client_connection(self, client_socket: socket.socket, address: tuple):
        """
        Handle the processing of incoming messages from connected nodes.
        
        :param client_socket: The socket object for the client connection
        :param address: The address of the connected client
        """
        try:
            data = client_socket.recv(1024)
            if not data:
                logger.warning(f"No data received from {address}")
                return
            
            message = json.loads(data.decode("utf-8"))
            logger.info(f"{self.name} received message: {message['message']} from {message['from']}")
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding message from {address}: {e}")
        except socket.error as e:
            logger.error(f"Error receiving data from {address}: {e}")
        finally:
            client_socket.close()

    def stop(self):
        """
        Stop the server and release resources.
        """
        self.server_socket.close()
        logger.info(f"{self.name} stopped.")


# Simulating networking infrastructure
if __name__ == "__main__":
    # Create and start nodes
    node1 = Node(name="Node1", host="127.0.0.1", port=5000)
    node2 = Node(name="Node2", host="127.0.0.1", port=5001)
    
    node1.start()
    node2.start()
    
    # Establish connections
    node1.connect_to_node("Node2", "127.0.0.1", 5001)
    node2.connect_to_node("Node1", "127.0.0.1", 5000)

    # Simulate message exchange
    threading.Timer(2, lambda: node1.send_message("Node2", "Hello from Node1")).start()
    threading.Timer(4, lambda: node2.send_message("Node1", "Hello from Node2")).start()
```
