"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Generate code to integrate the EasyOn glue gun with a temperature control system using the Nordson temperature controller.
Generated: DETERMINISTIC_a1d7fbf0e91c9a03
Batch ID: 20250612_164316
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
from typing import Optional

class NordsonTemperatureController:
    """
    A class to interface with the Nordson temperature controller for EasyOn glue gun.
    Handles communication, temperature control, and error handling.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the Nordson temperature controller.

        Args:
            port (str): Serial port name (e.g., 'COM3' or '/dev/ttyUSB0').
            baudrate (int, optional): Baud rate for serial communication. Defaults to 9600.
            timeout (float, optional): Serial timeout in seconds. Defaults to 1.0.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn: Optional[serial.Serial] = None

    def connect(self) -> bool:
        """
        Establish a connection to the Nordson temperature controller.

        Returns:
            bool: True if connection is successful, False otherwise.
        """
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            return self.serial_conn.is_open
        except serial.SerialException as e:
            print(f"Failed to connect to Nordson controller: {e}")
            return False

    def disconnect(self) -> None:
        """Close the serial connection if it is open."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def send_command(self, command: str) -> Optional[str]:
        """
        Send a command to the Nordson controller and read the response.

        Args:
            command (str): Command string to send.

        Returns:
            Optional[str]: Response from the controller, or None if error occurs.
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            print("Error: Not connected to Nordson controller.")
            return None

        try:
            self.serial_conn.write(f"{command}\r\n".encode())
            time.sleep(0.1)  # Allow time for response
            response = self.serial_conn.readline().decode().strip()
            return response
        except serial.SerialException as e:
            print(f"Error communicating with Nordson controller: {e}")
            return None

    def set_temperature(self, temperature: float) -> bool:
        """
        Set the target temperature for the EasyOn glue gun.

        Args:
            temperature (float): Desired temperature in Celsius.

        Returns:
            bool: True if command was successful, False otherwise.
        """
        if temperature < 0 or temperature > 300:  # Example range, adjust as needed
            print("Error: Temperature out of range.")
            return False

        response = self.send_command(f"SET_TEMP {temperature}")
        return response == "OK" if response else False

    def get_current_temperature(self) -> Optional[float]:
        """
        Get the current temperature reading from the glue gun.

        Returns:
            Optional[float]: Current temperature in Celsius, or None if error occurs.
        """
        response = self.send_command("GET_TEMP")
        try:
            return float(response) if response else None
        except (ValueError, TypeError):
            print("Error: Invalid temperature response from controller.")
            return None

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    with NordsonTemperatureController(port="COM3") as controller:
        # Set temperature to 150°C
        if controller.set_temperature(150):
            print("Temperature set successfully.")
        
        # Read current temperature
        current_temp = controller.get_current_temperature()
        if current_temp is not None:
            print(f"Current temperature: {current_temp}°C")
```
