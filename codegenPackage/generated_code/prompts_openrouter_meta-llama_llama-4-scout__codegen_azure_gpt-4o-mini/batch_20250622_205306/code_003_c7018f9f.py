"""
Generated Code Metadata:
========================
Original URL: https://layero.network
Prompt: Write a basic code snippet for a network application similar to what Layero might offer.
Generated: DETERMINISTIC_c7018f9f21c6d634
Batch ID: 20250622_205306
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

class NetworkApplication:
    def __init__(self, host='127.0.0.1', port=65432):
        """Initialize the network application with host and port."""
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []

    def start_server(self):
        """Start the server to listen for incoming connections."""
        try:
            # Create a TCP/IP socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen()
            print(f"Server started on {self.host}:{self.port}")

            while True:
                # Wait for a connection
                client_socket, client_address = self.server_socket.accept()
                print(f"Connection from {client_address} has been established.")
                self.clients.append(client_socket)

                # Start a new thread to handle the client
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.stop_server()

    def handle_client(self, client_socket):
        """Handle communication with a connected client."""
        try:
            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break  # No data means the client has disconnected

                print(f"Received data: {data.decode()}")
                # Echo the data back to the client
                client_socket.sendall(data)

        except Exception as e:
            print(f"An error occurred while handling client: {e}")
        finally:
            client_socket.close()
            print("Client connection closed.")

    def stop_server(self):
        """Stop the server and close all client connections."""
        if self.server_socket:
            self.server_socket.close()
            print("Server stopped.")

if __name__ == "__main__":
    app = NetworkApplication()
    app.start_server()
```
