"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://funmiscellintricat.pages.dev
Prompt: How can I implement a secure connection between wallets and Dapps using the DappsConnector protocol?
Generated: DETERMINISTIC_2016f077cdb5b93c
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import ssl
import socket

class DappsConnector:
    """
    A class to implement a secure connection between wallets and Dapps
    using the DappsConnector protocol.
    """

    def __init__(self, host: str, port: int):
        """
        Initialize the DappsConnector with the given host and port.
        
        :param host: The hostname or IP address of the Dapp server.
        :param port: The port number on which the Dapp server is listening.
        """
        self.host = host
        self.port = port
        self.sock = None

    def create_secure_socket(self):
        """
        Creates a secure socket using SSL.
        """
        context = ssl.create_default_context()
        self.sock = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=self.host)

    def connect(self):
        """
        Connects to the Dapp server.
        Raises an exception if the connection fails.
        """
        try:
            self.create_secure_socket()
            self.sock.connect((self.host, self.port))
            print(f"Connected to {self.host}:{self.port}")
        except (socket.error, ssl.SSLError) as e:
            raise ConnectionError(f"Failed to connect to {self.host}:{self.port}. Error: {e}")

    def send_data(self, data: dict):
        """
        Sends data to the Dapp server.
        
        :param data: A dictionary containing data to be sent.
        Raises an exception if the send operation fails.
        """
        try:
            json_data = json.dumps(data).encode('utf-8')
            self.sock.sendall(json_data)
            print("Data sent successfully.")
        except (socket.error, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to send data. Error: {e}")

    def receive_data(self) -> dict:
        """
        Receives data from the Dapp server.
        
        :return: A dictionary containing the received data.
        Raises an exception if the receive operation fails.
        """
        try:
            response = self.sock.recv(4096)  # buffer size
            if not response:
                raise RuntimeError("No response received.")

            data = json.loads(response.decode('utf-8'))
            return data
        except (socket.error, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to receive data. Error: {e}")

    def close(self):
        """
        Closes the socket connection.
        """
        if self.sock:
            self.sock.close()
            print("Connection closed.")

# Example usage
if __name__ == "__main__":
    try:
        connector = DappsConnector("dapp.example.com", 443)
        connector.connect()
        
        # Example data to send
        wallet_data = {
            "action": "connect",
            "wallet_id": "your-wallet-id",
            "nonce": 123456
        }

        connector.send_data(wallet_data)
        response = connector.receive_data()
        print("Received response:", response)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        connector.close()
```
