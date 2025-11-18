"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beldex-claim.pages.dev
Prompt: Provide code to set up a decentralized VPN service using the BelNet protocol on the Beldex network.
Generated: DETERMINISTIC_822f8c22fe764585
Batch ID: 20250612_151931
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
import select
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BelNetVPNServer:
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = None

    def start_server(self):
        """Starts the BelNet VPN server."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  # Allow up to 5 queued connections
        logging.info(f"VPN server started on {self.host}:{self.port}")

        try:
            while True:
                # Wait for a client to connect
                client_socket, addr = self.server_socket.accept()
                logging.info(f"Connection from {addr}")
                self.clients.append(client_socket)
                # Handle client in a separate thread
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            self.shutdown()

    def handle_client(self, client_socket):
        """Handles communication with the connected client."""
        with client_socket:
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break  # Connection closed by client
                    logging.info(f"Received data: {data}")
                    self.broadcast(data, client_socket)
                except Exception as e:
                    logging.error(f"Error handling client: {e}")
                    break

    def broadcast(self, message, sender_socket):
        """Broadcasts a message to all connected clients except the sender."""
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except Exception as e:
                    logging.error(f"Error sending message to client: {e}")
                    self.clients.remove(client)

    def shutdown(self):
        """Shuts down the VPN server and closes all client connections."""
        logging.info("Shutting down the server...")
        for client in self.clients:
            client.close()
        if self.server_socket:
            self.server_socket.close()
        logging.info("Server shut down successfully.")

if __name__ == "__main__":
    vpn_server = BelNetVPNServer()
    vpn_server.start_server()
```

This Python code sets up a basic decentralized VPN service using a socket-based communication model. It manages multiple client connections and broadcasts messages received from any client to all other connected clients. Proper error handling and logging are included to ensure robustness and maintainability.
