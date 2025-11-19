"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Write a Python code snippet to control a digital torque controller, such as the DTW-15 model, for tube expansion operations.
Generated: DETERMINISTIC_34ab6e0a87723bad
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial
import time
from typing import Optional, Tuple

class DigitalTorqueController:
    """
    A class to control a digital torque controller (e.g., DTW-15) for tube expansion operations.
    Handles communication via serial port and provides methods for torque control.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the torque controller with serial connection parameters.

        Args:
            port (str): Serial port name (e.g., 'COM3' or '/dev/ttyUSB0').
            baudrate (int, optional): Baud rate for serial communication. Defaults to 9600.
            timeout (float, optional): Serial read timeout in seconds. Defaults to 1.0.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def connect(self) -> bool:
        """
        Establish a connection to the torque controller.

        Returns:
            bool: True if connection is successful, False otherwise.
        """
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)  # Allow time for connection to stabilize
            return True
        except serial.SerialException as e:
            print(f"Failed to connect to torque controller: {e}")
            return False

    def disconnect(self) -> None:
        """Close the serial connection if it is open."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def send_command(self, command: str) -> Optional[str]:
        """
        Send a command to the torque controller and read the response.

        Args:
            command (str): Command string to send.

        Returns:
            Optional[str]: Response from the controller, or None if error occurs.
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            print("Error: Not connected to torque controller.")
            return None

        try:
            self.serial_conn.write((command + '\r').encode())
            response = self.serial_conn.readline().decode().strip()
            return response
        except serial.SerialException as e:
            print(f"Error sending command: {e}")
            return None

    def set_torque(self, torque_value: float) -> bool:
        """
        Set the target torque value.

        Args:
            torque_value (float): Desired torque value in Nm.

        Returns:
            bool: True if command was successful, False otherwise.
        """
        command = f"SET TORQUE {torque_value}"
        response = self.send_command(command)
        return response == "OK"

    def get_torque(self) -> Optional[float]:
        """
        Get the current torque reading.

        Returns:
            Optional[float]: Current torque value in Nm, or None if error occurs.
        """
        response = self.send_command("GET TORQUE")
        if response and response.startswith("TORQUE"):
            try:
                return float(response.split()[1])
            except (IndexError, ValueError):
                print("Error parsing torque value.")
        return None

    def start_expansion(self) -> bool:
        """
        Start the tube expansion operation.

        Returns:
            bool: True if command was successful, False otherwise.
        """
        response = self.send_command("START")
        return response == "OK"

    def stop_expansion(self) -> bool:
        """
        Stop the tube expansion operation.

        Returns:
            bool: True if command was successful, False otherwise.
        """
        response = self.send_command("STOP")
        return response == "OK"

    def get_status(self) -> Optional[str]:
        """
        Get the current status of the torque controller.

        Returns:
            Optional[str]: Status message, or None if error occurs.
        """
        return self.send_command("STATUS")

# Example usage
if __name__ == "__main__":
    # Initialize controller (replace port with actual port)
    controller = DigitalTorqueController(port="/dev/ttyUSB0")

    try:
        if controller.connect():
            print("Connected to torque controller.")

            # Set torque and start expansion
            if controller.set_torque(15.5):
                print("Torque set to 15.5 Nm.")
                if controller.start_expansion():
                    print("Expansion started.")

                    # Monitor torque (example: monitor for 5 seconds)
                    start_time = time.time()
                    while time.time() - start_time < 5:
                        torque = controller.get_torque()
                        if torque is not None:
                            print(f"Current torque: {torque} Nm")
                        time.sleep(0.5)

                    # Stop expansion
                    if controller.stop_expansion():
                        print("Expansion stopped.")
    finally:
        controller.disconnect()
        print("Disconnected from torque controller.")
```
