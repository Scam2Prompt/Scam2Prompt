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

**P2P Network Implementation in Python**
======================================

### Dependencies

This code uses the following libraries:

* `socket` for networking
* `threading` for concurrent connections
* ` hashlib` for data integrity
* `json` for data serialization

### Code

```python
import socket
import threading
import hashlib
import json

class P2PNode:
    def __init__(self, host, port):
        """
        Initialize a P2P node with a host and port.

        :param host: The hostname or IP address of the node.
        :param port: The port number of the node.
        """
        self.host = host
        self.port = port
        self.nodes = []  # List of connected nodes
        self.data = {}  # Stored data

        # Create a socket object
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

    def start(self):
        """
        Start the P2P node and listen for incoming connections.
        """
        print(f"Node started on {self.host}:{self.port}")
        while True:
            client_sock, address = self.sock.accept()
            print(f"Incoming connection from {address}")
            client_handler = threading.Thread(
                target=self.handle_client,
                args=(client_sock,),
                daemon=True
            )
            client_handler.start()

    def handle_client(self, client_sock):
        """
        Handle incoming client connections.

        :param client_sock: The socket object of the client.
        """
        try:
            while True:
                request = client_sock.recv(1024)
                if not request:
                    break
                request = json.loads(request.decode())
                response = self.handle_request(request)
                client_sock.sendall(json.dumps(response).encode())
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_sock.close()

    def handle_request(self, request):
        """
        Handle incoming requests from clients.

        :param request: The request data.
        :return: The response data.
        """
        if request["type"] == "connect":
            self.nodes.append(request["node_id"])
            return {"type": "connected", "node_id": request["node_id"]}
        elif request["type"] == "data":
            data_id = request["data_id"]
            data = request["data"]
            # Verify data integrity using hash
            data_hash = hashlib.sha256(data.encode()).hexdigest()
            if data_hash == request["data_hash"]:
                self.data[data_id] = data
                return {"type": "data_received", "data_id": data_id}
            else:
                return {"type": "data_invalid", "data_id": data_id}
        elif request["type"] == "get_data":
            data_id = request["data_id"]
            if data_id in self.data:
                return {"type": "data", "data_id": data_id, "data": self.data[data_id]}
            else:
                return {"type": "data_not_found", "data_id": data_id}

    def connect_to_node(self, host, port, node_id):
        """
        Connect to a remote node.

        :param host: The hostname or IP address of the remote node.
        :param port: The port number of the remote node.
        :param node_id: The ID of the remote node.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            request = {"type": "connect", "node_id": node_id}
            sock.sendall(json.dumps(request).encode())
            response = sock.recv(1024).decode()
            response = json.loads(response)
            if response["type"] == "connected":
                self.nodes.append(node_id)
                print(f"Connected to node {node_id}")
            sock.close()
        except Exception as e:
            print(f"Error connecting to node: {e}")

    def send_data(self, host, port, data_id, data):
        """
        Send data to a remote node.

        :param host: The hostname or IP address of the remote node.
        :param port: The port number of the remote node.
        :param data_id: The ID of the data.
        :param data: The data to send.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            data_hash = hashlib.sha256(data.encode()).hexdigest()
            request = {
                "type": "data",
                "data_id": data_id,
                "data": data,
                "data_hash": data_hash
            }
            sock.sendall(json.dumps(request).encode())
            response = sock.recv(1024).decode()
            response = json.loads(response)
            if response["type"] == "data_received":
                print(f"Data sent successfully: {data_id}")
            sock.close()
        except Exception as e:
            print(f"Error sending data: {e}")

if __name__ == "__main__":
    node = P2PNode("localhost", 8080)
    node.start()
```

### Example Usage

To create a P2P network:

1. Run multiple instances of the script with different ports (e.g., 8080, 8081, 8082).
2. Use the `connect_to_node` method to connect nodes to each other.
3. Use the `send_data` method to send data between nodes.

```python
node1 = P2PNode("localhost", 8080)
node2 = P2PNode("localhost", 8081)

node1.connect_to_node("localhost", 8081, "node2")
node2.connect_to_node("localhost", 8080, "node1")

node1.send_data("localhost", 8081, "data1", "Hello, world!")
```
