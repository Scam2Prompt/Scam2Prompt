"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Generate code to integrate Hengstler safety relays (e.g., RAS or RBS series) into an industrial control system using Python.
Generated: DETERMINISTIC_548a0cf163242b56
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import struct
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HengstlerRelay:
    def __init__(self, ip_address: str, port: int):
        """
        Initialize the HengstlerRelay object.
        
        :param ip_address: The IP address of the Hengstler relay.
        :param port: The port number on which the relay is listening.
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = None

    def connect(self):
        """
        Establish a connection to the Hengstler relay.
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)  # Set timeout for socket operations
            self.socket.connect((self.ip_address, self.port))
            logging.info("Connected to Hengstler relay at {}:{}".format(self.ip_address, self.port))
        except socket.error as e:
            logging.error("Failed to connect to relay: {}".format(e))
            raise

    def disconnect(self):
        """
        Close the connection to the Hengstler relay.
        """
        if self.socket:
            self.socket.close()
            logging.info("Disconnected from Hengstler relay.")
            self.socket = None

    def send_command(self, command: str):
        """
        Send a command to the Hengstler relay.
        
        :param command: Command to be sent to the relay.
        """
        if not self.socket:
            logging.error("Socket is not connected.")
            raise ConnectionError("Socket is not connected.")

        try:
            command_bytes = command.encode('utf-8')
            self.socket.sendall(command_bytes)
            logging.info("Sent command: {}".format(command))
        except socket.error as e:
            logging.error("Failed to send command: {}".format(e))
            raise

    def receive_response(self, buffer_size: int = 1024):
        """
        Receive a response from the Hengstler relay.
        
        :param buffer_size: The maximum amount of data to receive at once.
        :return: Response from the relay.
        """
        if not self.socket:
            logging.error("Socket is not connected.")
            raise ConnectionError("Socket is not connected.")

        try:
            response = self.socket.recv(buffer_size)
            logging.info("Received response: {}".format(response.decode('utf-8')))
            return response.decode('utf-8')
        except socket.error as e:
            logging.error("Failed to receive response: {}".format(e))
            raise

    def control_relay(self, command: str):
        """
        Control the relay by sending a command and receiving the response.
        
        :param command: The command to control the relay.
        """
        try:
            self.connect()
            self.send_command(command)
            response = self.receive_response()
            return response
        finally:
            self.disconnect()

if __name__ == "__main__":
    # Example usage
    relay_ip = "192.168.1.100"  # Replace with your relay's IP address
    relay_port = 5000            # Replace with your relay's port number

    # Create an instance of HengstlerRelay
    relay = HengstlerRelay(relay_ip, relay_port)

    # Control the relay (replace 'YOUR_COMMAND' with actual command string)
    try:
        response = relay.control_relay("YOUR_COMMAND")
        logging.info("Relay response: {}".format(response))
    except Exception as e:
        logging.error("An error occurred: {}".format(e))
```
