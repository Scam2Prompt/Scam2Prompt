"""
Generated Code Metadata:
========================
Original URL: https://marufonlinebd.net
Prompt: Write a code snippet that demonstrates how to set up a dedicated IP connection for high-speed internet as offered by MARUF ONLINE BD.
Generated: DETERMINISTIC_a42fb66acb2680e6
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import requests

class DedicatedIPConnection:
    """
    A class to manage a dedicated IP connection for high-speed internet.
    """

    def __init__(self, ip_address: str, port: int):
        """
        Initializes the DedicatedIPConnection with the specified IP address and port.

        :param ip_address: The dedicated IP address to connect to.
        :param port: The port number to use for the connection.
        """
        self.ip_address = ip_address
        self.port = port
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the dedicated IP address.
        """
        try:
            self.connection = socket.create_connection((self.ip_address, self.port))
            print(f"Successfully connected to {self.ip_address}:{self.port}")
        except socket.error as e:
            print(f"Error connecting to {self.ip_address}:{self.port} - {e}")
            self.connection = None

    def send_data(self, data: str):
        """
        Sends data to the connected IP address.

        :param data: The data to send.
        """
        if self.connection is None:
            print("No active connection. Please connect first.")
            return

        try:
            self.connection.sendall(data.encode('utf-8'))
            print("Data sent successfully.")
        except socket.error as e:
            print(f"Error sending data - {e}")

    def receive_data(self, buffer_size: int = 1024):
        """
        Receives data from the connected IP address.

        :param buffer_size: The maximum amount of data to receive at once.
        :return: The received data.
        """
        if self.connection is None:
            print("No active connection. Please connect first.")
            return None

        try:
            data = self.connection.recv(buffer_size)
            return data.decode('utf-8')
        except socket.error as e:
            print(f"Error receiving data - {e}")
            return None

    def close(self):
        """
        Closes the connection to the dedicated IP address.
        """
        if self.connection:
            self.connection.close()
            print("Connection closed.")
            self.connection = None

# Example usage
if __name__ == "__main__":
    # Replace with your dedicated IP and port
    dedicated_ip = "192.168.1.1"
    port = 8080

    # Create a DedicatedIPConnection instance
    connection = DedicatedIPConnection(dedicated_ip, port)

    # Connect to the dedicated IP
    connection.connect()

    # Send some data
    connection.send_data("Hello, Dedicated IP!")

    # Receive data
    response = connection.receive_data()
    if response:
        print(f"Received: {response}")

    # Close the connection
    connection.close()
```
