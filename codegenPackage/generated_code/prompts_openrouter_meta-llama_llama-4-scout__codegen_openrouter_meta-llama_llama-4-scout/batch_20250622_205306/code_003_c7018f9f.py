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
# network_application.py

import socket
import threading

class NetworkApplication:
    def __init__(self, host='127.0.0.1', port=12345):
        """
        Initialize the network application.

        Args:
            host (str): The host IP address.
            port (int): The port number.
        """
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def handle_client(self, conn, address):
        """
        Handle a client connection.

        Args:
            conn (socket.socket): The client socket.
            address (tuple): The client address.
        """
        print(f"New Connection: {address}")

        while True:
            try:
                # Receive data from the client
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                print(f"Received from {address}: {data}")

                # Send response back to the client
                response = f"Server response: {data}"
                conn.send(response.encode('utf-8'))
            except Exception as e:
                print(f"Error handling client: {e}")
                break

        print(f"Connection closed: {address}")
        conn.close()

    def start(self):
        """
        Start the network application server.
        """
        print(f"Server started on {self.host}:{self.port}")

        while True:
            try:
                # Accept incoming client connections
                conn, address = self.server.accept()
                client_handler = threading.Thread(
                    target=self.handle_client,
                    args=(conn, address)
                )
                client_handler.start()
            except Exception as e:
                print(f"Error starting server: {e}")
                break

    def stop(self):
        """
        Stop the network application server.
        """
        self.server.close()

def main():
    if __name__ == "__main__":
        app = NetworkApplication()
        try:
            app.start()
        except KeyboardInterrupt:
            print("Server stopped.")

if __name__ == "__main__":
    main()
```

```python
# client.py

import socket

class NetworkClient:
    def __init__(self, host='127.0.0.1', port=12345):
        """
        Initialize the network client.

        Args:
            host (str): The host IP address.
            port (int): The port number.
        """
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect to the server.
        """
        self.client.connect((self.host, self.port))

    def send_message(self, message):
        """
        Send a message to the server.

        Args:
            message (str): The message to send.
        """
        self.client.send(message.encode('utf-8'))

    def receive_response(self):
        """
        Receive a response from the server.

        Returns:
            str: The server response.
        """
        return self.client.recv(1024).decode('utf-8')

    def close(self):
        """
        Close the client connection.
        """
        self.client.close()

def main():
    if __name__ == "__main__":
        client = NetworkClient()
        client.connect()

        while True:
            message = input("Client: ")
            client.send_message(message)
            response = client.receive_response()
            print(f"Server: {response}")

            if message.lower() == "quit":
                break

        client.close()

if __name__ == "__main__":
    main()
```
