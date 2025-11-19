"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: Create a code snippet that interfaces with the Beta Control open protocol for modernizing elevator controls, as outlined by SIMICE-TEC-ELEVATORS.
Generated: DETERMINISTIC_bbc1a4bad338fbab
Batch ID: 20250612_162050
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
from typing import Optional, Dict, Any

class BetaControlProtocol:
    """
    A class to interface with the Beta Control open protocol for elevator controls.
    Handles communication, command sending, and response parsing.
    """

    def __init__(self, host: str, port: int, timeout: float = 5.0):
        """
        Initialize the BetaControlProtocol with connection parameters.
        
        Args:
            host: The hostname or IP address of the Beta Control server.
            port: The port number for the Beta Control protocol.
            timeout: Connection and operation timeout in seconds.
        """
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None

    def connect(self) -> bool:
        """
        Establish a connection to the Beta Control server.
        
        Returns:
            bool: True if connection was successful, False otherwise.
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.host, self.port))
            return True
        except (socket.error, socket.timeout) as e:
            print(f"Connection error: {e}")
            return False

    def disconnect(self) -> None:
        """Close the connection to the Beta Control server."""
        if self.socket:
            try:
                self.socket.close()
            except socket.error as e:
                print(f"Error while disconnecting: {e}")
            finally:
                self.socket = None

    def send_command(self, command: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Send a command to the Beta Control server and receive the response.
        
        Args:
            command: A dictionary containing the command and parameters.
            
        Returns:
            Optional[Dict[str, Any]]: The response from the server, or None if there was an error.
        """
        if not self.socket:
            if not self.connect():
                return None

        try:
            # Serialize command to JSON and send
            command_str = json.dumps(command) + "\n"
            self.socket.sendall(command_str.encode('utf-8'))

            # Receive response
            response_data = self.socket.recv(4096)
            if not response_data:
                return None

            # Parse JSON response
            response = json.loads(response_data.decode('utf-8'))
            return response

        except (socket.error, json.JSONDecodeError, ValueError) as e:
            print(f"Error during command execution: {e}")
            return None

    def get_elevator_status(self, elevator_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the current status of an elevator.
        
        Args:
            elevator_id: The unique identifier of the elevator.
            
        Returns:
            Optional[Dict[str, Any]]: The elevator status, or None if there was an error.
        """
        command = {
            "command": "get_status",
            "elevator_id": elevator_id
        }
        return self.send_command(command)

    def call_elevator(self, elevator_id: str, floor: int) -> Optional[Dict[str, Any]]:
        """
        Call an elevator to a specific floor.
        
        Args:
            elevator_id: The unique identifier of the elevator.
            floor: The floor number to call the elevator to.
            
        Returns:
            Optional[Dict[str, Any]]: The response from the server, or None if there was an error.
        """
        command = {
            "command": "call",
            "elevator_id": elevator_id,
            "floor": floor
        }
        return self.send_command(command)

    def set_elevator_mode(self, elevator_id: str, mode: str) -> Optional[Dict[str, Any]]:
        """
        Set the operating mode of an elevator (e.g., "normal", "maintenance").
        
        Args:
            elevator_id: The unique identifier of the elevator.
            mode: The desired operating mode.
            
        Returns:
            Optional[Dict[str, Any]]: The response from the server, or None if there was an error.
        """
        command = {
            "command": "set_mode",
            "elevator_id": elevator_id,
            "mode": mode
        }
        return self.send_command(command)

    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    # Initialize with your Beta Control server details
    with BetaControlProtocol(host="127.0.0.1", port=8080) as protocol:
        # Get elevator status
        status = protocol.get_elevator_status("elevator_1")
        print(f"Elevator status: {status}")

        # Call elevator to floor 5
        response = protocol.call_elevator("elevator_1", 5)
        print(f"Call response: {response}")

        # Set elevator to maintenance mode
        response = protocol.set_elevator_mode("elevator_1", "maintenance")
        print(f"Mode set response: {response}")
```
