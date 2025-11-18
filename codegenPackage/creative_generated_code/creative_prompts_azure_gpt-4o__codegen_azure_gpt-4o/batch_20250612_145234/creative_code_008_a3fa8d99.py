"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.prointegrationfuture.asia
Prompt: Write code for a networking application that connects AVL professionals and system integrators, inspired by the collaboration opportunities at Pro Integration Future Asia.
Generated: DETERMINISTIC_a3fa8d9915c60874
Batch ID: 20250612_145234
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

# Networking application to connect AVL professionals and system integrators
class NetworkingApp:
    def __init__(self, host='127.0.0.1', port=5000):
        """
        Initialize the server with the specified host and port.
        """
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}  # Dictionary to store connected clients

    def start_server(self):
        """
        Start the server to listen for incoming connections.
        """
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"Server started on {self.host}:{self.port}")
            self.accept_clients()
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            self.server_socket.close()

    def accept_clients(self):
        """
        Accept incoming client connections.
        """
        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"New connection from {client_address}")
                threading.Thread(
                    target=self.handle_client, args=(client_socket, client_address)
                ).start()
            except Exception as e:
                print(f"Error accepting client: {e}")
                break

    def handle_client(self, client_socket, client_address):
        """
        Handle communication with a connected client.
        """
        try:
            client_id = client_address[1]
            self.clients[client_id] = client_socket
            self.send_message(
                client_socket,
                {"message": "Welcome! You are connected to the networking app."},
            )

            while True:
                message = self.receive_message(client_socket)
                if message is None:
                    print(f"Client {client_address} disconnected.")
                    break
                print(f"Received from {client_address}: {message}")
                self.broadcast_message(client_id, message)

        except Exception as e:
            print(f"Error with client {client_address}: {e}")
        finally:
            client_socket.close()
            del self.clients[client_id]

    def send_message(self, client_socket, message):
        """
        Send a JSON-encoded message to a specific client.
        """
        try:
            client_socket.send(json.dumps(message).encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive_message(self, client_socket):
        """
        Receive and decode a JSON message from a client.
        """
        try:
            data = client_socket.recv(1024)
            if not data:
                return None
            return json.loads(data.decode('utf-8'))
        except Exception:
            return None

    def broadcast_message(self, sender_id, message):
        """
        Broadcast a message to all connected clients except the sender.
        """
        for client_id, client_socket in self.clients.items():
            if client_id != sender_id:
                self.send_message(client_socket, {"sender": sender_id, "message": message})


if __name__ == "__main__":
    # Start the networking server
    app = NetworkingApp()
    try:
        app.start_server()
    except KeyboardInterrupt:
        print("Server shutting down...")
```
