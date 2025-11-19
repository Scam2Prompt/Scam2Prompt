"""
Generated Code Metadata:
========================
Original URL: https://socket.exchange
Prompt: Design a simple SDK for interacting with Socket Exchange, focusing on its core features and use cases.
Generated: DETERMINISTIC_07a98341b042e077
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocketExchangeSDK:
    """
    A simple SDK for interacting with a Socket Exchange.
    
    This SDK provides methods to connect to a socket server, send messages,
    and receive messages. It handles basic error checking and logging.
    """

    def __init__(self, host: str, port: int):
        """
        Initializes the SDK with the server's host and port.

        :param host: The hostname or IP address of the socket server.
        :param port: The port number of the socket server.
        """
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        """Establishes a connection to the socket server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            logging.info(f"Connected to socket server at {self.host}:{self.port}")
        except socket.error as e:
            logging.error(f"Failed to connect to socket server: {e}")
            raise

    def send_message(self, message: dict):
        """
        Sends a JSON-encoded message to the socket server.

        :param message: A dictionary representing the message to send.
        """
        if self.socket is None:
            logging.error("Socket is not connected. Please connect first.")
            raise ConnectionError("Socket is not connected.")

        try:
            json_message = json.dumps(message).encode('utf-8')
            self.socket.sendall(json_message)
            logging.info(f"Sent message: {message}")
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
            raise

    def receive_message(self) -> dict:
        """
        Receives a message from the socket server.

        :return: A dictionary representing the received message.
        """
        if self.socket is None:
            logging.error("Socket is not connected. Please connect first.")
            raise ConnectionError("Socket is not connected.")

        try:
            response = self.socket.recv(4096)  # Buffer size of 4096 bytes
            message = json.loads(response.decode('utf-8'))
            logging.info(f"Received message: {message}")
            return message
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON message: {e}")
            raise
        except Exception as e:
            logging.error(f"Failed to receive message: {e}")
            raise

    def close(self):
        """Closes the connection to the socket server."""
        if self.socket:
            self.socket.close()
            logging.info("Socket connection closed.")
            self.socket = None

# Example usage:
if __name__ == "__main__":
    try:
        sdk = SocketExchangeSDK('localhost', 12345)
        sdk.connect()
        sdk.send_message({'action': 'ping'})
        response = sdk.receive_message()
        print("Response from server:", response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        sdk.close()
```
