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

class DedicatedIPConnection:
    """
    A class to set up a dedicated IP connection for high-speed internet.
    This example demonstrates connecting to MARUF ONLINE BD's service.
    """

    def __init__(self, server_ip, server_port):
        """
        Initialize the connection parameters.

        :param server_ip: The IP address of the MARUF ONLINE BD server.
        :param server_port: The port number for the dedicated connection.
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.connection = None

    def connect(self):
        """
        Establish a dedicated IP connection to the server.
        """
        try:
            # Create a socket object
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set socket options for better performance
            self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Connect to the server
            self.connection.connect((self.server_ip, self.server_port))
            print(f"Successfully connected to {self.server_ip}:{self.server_port}")
        except socket.error as e:
            print(f"Error establishing connection: {e}")
            self.connection = None

    def send_data(self, data):
        """
        Send data over the dedicated connection.

        :param data: The data to send (string).
        """
        if self.connection:
            try:
                # Send data to the server
                self.connection.sendall(data.encode('utf-8'))
                print("Data sent successfully.")
            except socket.error as e:
                print(f"Error sending data: {e}")
        else:
            print("No active connection. Please connect first.")

    def receive_data(self):
        """
        Receive data from the server.

        :return: The received data (string).
        """
        if self.connection:
            try:
                # Receive data from the server
                response = self.connection.recv(1024)  # Buffer size of 1024 bytes
                return response.decode('utf-8')
            except socket.error as e:
                print(f"Error receiving data: {e}")
                return None
        else:
            print("No active connection. Please connect first.")
            return None

    def close_connection(self):
        """
        Close the dedicated IP connection.
        """
        if self.connection:
            try:
                self.connection.close()
                print("Connection closed successfully.")
            except socket.error as e:
                print(f"Error closing connection: {e}")
        else:
            print("No active connection to close.")


# Example usage
if __name__ == "__main__":
    # Replace with actual server IP and port provided by MARUF ONLINE BD
    SERVER_IP = "192.168.1.1"
    SERVER_PORT = 8080

    # Create a DedicatedIPConnection instance
    connection = DedicatedIPConnection(SERVER_IP, SERVER_PORT)

    # Establish connection
    connection.connect()

    # Send data
    connection.send_data("Hello, MARUF ONLINE BD!")

    # Receive response
    response = connection.receive_data()
    if response:
        print(f"Received response: {response}")

    # Close connection
    connection.close_connection()
```
