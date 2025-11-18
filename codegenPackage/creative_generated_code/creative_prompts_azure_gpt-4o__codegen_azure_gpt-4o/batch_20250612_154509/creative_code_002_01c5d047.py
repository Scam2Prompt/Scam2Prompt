"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Generate Python code to set up remote support functionality for a retail IT system, inspired by Retail Tech Solutions' "Remote Support on Demand" feature.
Generated: DETERMINISTIC_01c5d047c58592af
Batch ID: 20250612_154509
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
import logging
import os

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("remote_support.log"),
        logging.StreamHandler()
    ]
)

class RemoteSupportServer:
    """
    A class to set up a remote support server for a retail IT system.
    This allows technicians to provide on-demand support to clients.
    """

    def __init__(self, host="0.0.0.0", port=9000):
        """
        Initialize the server with the given host and port.

        :param host: Host address to bind the server (default: 0.0.0.0 for all interfaces)
        :param port: Port to bind the server (default: 9000)
        """
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []  # List to manage connected clients

    def start_server(self):
        """
        Start the remote support server and listen for incoming connections.
        """
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logging.info(f"Server started and listening on {self.host}:{self.port}")
            self.accept_connections()
        except Exception as e:
            logging.error(f"Failed to start the server: {e}")
            self.shutdown_server()

    def accept_connections(self):
        """
        Accept incoming client connections in a separate thread.
        """
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                self.clients.append(client_socket)
                logging.info(f"Connection established with {client_address}")
                threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()
        except Exception as e:
            logging.error(f"Error accepting connections: {e}")
            self.shutdown_server()

    def handle_client(self, client_socket, client_address):
        """
        Handle communication with a connected client.

        :param client_socket: The socket object for the connected client
        :param client_address: The address of the connected client
        """
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    logging.info(f"Client {client_address} disconnected")
                    self.clients.remove(client_socket)
                    break
                logging.info(f"Received from {client_address}: {data.decode('utf-8')}")
                response = self.process_request(data.decode('utf-8'))
                client_socket.send(response.encode('utf-8'))
        except Exception as e:
            logging.error(f"Error handling client {client_address}: {e}")
        finally:
            client_socket.close()

    def process_request(self, request):
        """
        Process client requests and formulate a response.

        :param request: The client's request as a string
        :return: The response to send back to the client
        """
        try:
            if request.lower() == "help":
                return "How can we assist you today? Type 'exit' to disconnect."
            elif request.lower() == "exit":
                return "Goodbye!"
            else:
                return f"Unknown command: {request}"
        except Exception as e:
            logging.error(f"Error processing request: {e}")
            return "An error occurred while processing your request."

    def shutdown_server(self):
        """
        Shut down the server gracefully, closing all connections.
        """
        try:
            for client in self.clients:
                client.close()
            self.server_socket.close()
            logging.info("Server has been shut down.")
        except Exception as e:
            logging.error(f"Error shutting down the server: {e}")


if __name__ == "__main__":
    # Ensure proper environment setup
    try:
        host = os.getenv("REMOTE_SUPPORT_HOST", "0.0.0.0")  # Use environment variable or default to all interfaces
        port = int(os.getenv("REMOTE_SUPPORT_PORT", 9000))  # Use environment variable or default to port 9000

        # Start the server
        server = RemoteSupportServer(host=host, port=port)
        server.start_server()
    except KeyboardInterrupt:
        logging.info("Server interrupted by user. Shutting down...")
        server.shutdown_server()
    except Exception as e:
        logging.error(f"Fatal error: {e}")
```
