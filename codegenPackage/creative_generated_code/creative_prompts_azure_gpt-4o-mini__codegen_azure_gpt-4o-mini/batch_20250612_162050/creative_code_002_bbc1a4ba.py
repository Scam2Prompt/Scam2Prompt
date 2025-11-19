"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simice-tec-elevators.cz
Prompt: Create a code snippet that interfaces with the Beta Control open protocol for modernizing elevator controls, as outlined by SIMICE-TEC-ELEVATORS.
Generated: DETERMINISTIC_bbc1a4bad338fbab
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import json
import logging
from typing import Any, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElevatorControlInterface:
    """A class to interface with the Beta Control open protocol for modernizing elevator controls."""

    def __init__(self, server_ip: str, server_port: int):
        """Initialize the ElevatorControlInterface with server IP and port.
        
        Args:
            server_ip (str): The IP address of the control server.
            server_port (int): The port number of the control server.
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.socket = None

    def connect(self) -> None:
        """Establish a connection to the elevator control server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_ip, self.server_port))
            logging.info("Connected to elevator control server at %s:%d", self.server_ip, self.server_port)
        except socket.error as e:
            logging.error("Failed to connect to server: %s", e)
            raise

    def send_command(self, command: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Send a command to the elevator control server and receive a response.
        
        Args:
            command (str): The command to send (e.g., 'MOVE', 'STOP').
            parameters (Dict[str, Any]): A dictionary of parameters for the command.
        
        Returns:
            Dict[str, Any]: The server's response parsed as a JSON object.
        """
        if not self.socket:
            logging.error("Socket is not connected. Please connect first.")
            raise ConnectionError("Not connected to the elevator control server.")

        # Prepare the command message
        message = json.dumps({"command": command, "parameters": parameters}).encode('utf-8')

        try:
            # Send command
            self.socket.sendall(message)
            logging.info("Sent command: %s with parameters: %s", command, parameters)

            # Receive response
            response = self.socket.recv(4096)
            response_data = json.loads(response.decode('utf-8'))
            logging.info("Received response: %s", response_data)
            return response_data
        except (socket.error, json.JSONDecodeError) as e:
            logging.error("Error sending command or receiving response: %s", e)
            raise

    def close(self) -> None:
        """Close the connection to the elevator control server."""
        if self.socket:
            self.socket.close()
            logging.info("Connection closed.")
        else:
            logging.warning("No connection to close.")

# Example usage
if __name__ == "__main__":
    elevator_controller = ElevatorControlInterface(server_ip="192.168.1.100", server_port=5000)
    try:
        elevator_controller.connect()
        response = elevator_controller.send_command("MOVE", {"floor": 5})
        print("Elevator response:", response)
    except Exception as e:
        logging.error("An error occurred: %s", e)
    finally:
        elevator_controller.close()
```
