"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeauthapp.pages.dev
Prompt: Write a code snippet that demonstrates how to implement the Bridge server for COIN NODE communication.
Generated: DETERMINISTIC_0c8c99db5b70f695
Batch ID: 20250612_162616
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
import threading

class BridgeServer:
    def __init__(self, host='localhost', port=5000):
        """Initialize the BridgeServer with host and port."""
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []

    def start_server(self):
        """Start the bridge server to listen for incoming connections."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)  # Allow up to 5 pending connections
            print(f"Bridge server started on {self.host}:{self.port}")

            while True:
                client_socket, address = self.server_socket.accept()
                print(f"Connection accepted from {address}")
                self.clients.append(client_socket)
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()

        except Exception as e:
            print(f"Error starting server: {e}")
        finally:
            self.stop_server()

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break  # Connection closed by the client
                
                # Process the incoming data
                message = json.loads(data.decode('utf-8'))
                print(f"Received message: {message}")

                # Example of responding to the client
                response = {'status': 'received', 'data': message}
                client_socket.send(json.dumps(response).encode('utf-8'))

        except json.JSONDecodeError:
            print("Received invalid JSON data.")
            client_socket.send(json.dumps({'error': 'Invalid JSON format'}).encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()
            self.clients.remove(client_socket)
            print("Client disconnected.")

    def stop_server(self):
        """Stop the server and close all active connections."""
        if self.server_socket:
            self.server_socket.close()
            print("Server stopped.")

if __name__ == "__main__":
    bridge_server = BridgeServer()
    bridge_server.start_server()
```
