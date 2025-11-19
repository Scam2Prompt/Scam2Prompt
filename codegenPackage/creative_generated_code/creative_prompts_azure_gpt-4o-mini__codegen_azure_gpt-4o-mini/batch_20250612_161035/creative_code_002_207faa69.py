"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megamash.ru
Prompt: Write a code snippet that interfaces with Siemens industrial controllers for managing a beverage filling line as outlined by МЕГАМАШ.
Generated: DETERMINISTIC_207faa69205d1a9f
Batch ID: 20250612_161035
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SiemensController:
    def __init__(self, ip_address, port):
        """
        Initialize the SiemensController with the given IP address and port.

        :param ip_address: The IP address of the Siemens industrial controller.
        :param port: The port number to connect to the controller.
        """
        self.ip_address = ip_address
        self.port = port
        self.connection = None

    def connect(self):
        """Establish a connection to the Siemens controller."""
        try:
            self.connection = socket.create_connection((self.ip_address, self.port))
            logging.info(f"Connected to Siemens controller at {self.ip_address}:{self.port}")
        except Exception as e:
            logging.error(f"Failed to connect: {e}")
            raise

    def disconnect(self):
        """Close the connection to the Siemens controller."""
        if self.connection:
            self.connection.close()
            logging.info("Connection closed.")

    def send_command(self, command):
        """
        Send a command to the Siemens controller.

        :param command: The command to send to the controller.
        :return: Response from the controller.
        """
        if not self.connection:
            logging.error("Connection not established. Please connect first.")
            return None
        
        try:
            # Prepare and send the command (assuming command is a string)
            command_bytes = command.encode('utf-8')
            self.connection.sendall(command_bytes)
            logging.info(f"Command sent: {command}")

            # Receive response (example: expecting a fixed size response)
            response = self.connection.recv(1024)
            logging.info(f"Response received: {response.decode('utf-8')}")
            return response.decode('utf-8')

        except Exception as e:
            logging.error(f"Error while sending command: {e}")
            return None

    def manage_filling_line(self, action):
        """
        Manage the beverage filling line by sending appropriate commands.

        :param action: The action to perform on the filling line (e.g., "start", "stop", "status").
        """
        valid_actions = ["start", "stop", "status"]
        if action not in valid_actions:
            logging.error(f"Invalid action: {action}. Must be one of {valid_actions}.")
            return

        command = f"FILLING_LINE_{action.upper()}"
        return self.send_command(command)

if __name__ == '__main__':
    # Example usage of the SiemensController class
    controller = SiemensController(ip_address='192.168.1.100', port=102)

    try:
        controller.connect()
        response = controller.manage_filling_line('start')
        print(f"Filling line response: {response}")
    finally:
        controller.disconnect()
```
