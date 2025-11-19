"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: Illustrate how to implement error handling in a program that communicates with the 200QJ equipment, ensuring robust operation as described in the site content.
Generated: DETERMINISTIC_0d4232bd0f775d52
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EquipmentCommunicationError(Exception):
    """Custom exception for equipment communication errors."""
    pass

class Equipment200QJ:
    """Class to handle communication with the 200QJ equipment."""
    
    def __init__(self, host: str, port: int):
        """Initialize the equipment communication with host and port."""
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        """Establish a connection to the equipment."""
        try:
            self.socket = socket.create_connection((self.host, self.port))
            logging.info("Successfully connected to the equipment.")
        except socket.error as e:
            logging.error(f"Connection error: {e}")
            raise EquipmentCommunicationError("Failed to connect to the equipment.")

    def send_command(self, command: str) -> str:
        """Send a command to the equipment and return the response."""
        if self.socket is None:
            raise EquipmentCommunicationError("Socket is not connected.")
        
        try:
            self.socket.sendall(command.encode('utf-8'))
            logging.info(f"Command sent: {command}")
            response = self.socket.recv(1024).decode('utf-8')
            logging.info(f"Response received: {response}")
            return response
        except socket.error as e:
            logging.error(f"Error sending command: {e}")
            raise EquipmentCommunicationError("Failed to send command to the equipment.")

    def disconnect(self):
        """Close the connection to the equipment."""
        if self.socket:
            try:
                self.socket.close()
                logging.info("Connection closed.")
            except socket.error as e:
                logging.error(f"Error closing connection: {e}")
                raise EquipmentCommunicationError("Failed to close the connection.")

def main():
    """Main function to demonstrate communication with the 200QJ equipment."""
    equipment = Equipment200QJ(host='192.168.1.100', port=5000)

    try:
        equipment.connect()
        response = equipment.send_command("GET_STATUS")
        print(f"Equipment response: {response}")
    except EquipmentCommunicationError as e:
        logging.error(f"Communication error: {e}")
    finally:
        equipment.disconnect()

if __name__ == "__main__":
    main()
```
