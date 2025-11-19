"""
Generated Code Metadata:
========================
Original URL: https://fujimitsudynamic.com
Prompt: Generate a code snippet to interface with a Cam Splitter for industrial applications, as described by Fujimitsu Dynamic.
Generated: DETERMINISTIC_ab95127561e9f73b
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial  # For serial communication
import time    # For timing operations

class CamSplitterInterface:
    """
    A class to interface with the Fujimitsu Dynamic Cam Splitter for industrial applications.
    """

    def __init__(self, port: str, baud_rate: int = 9600, timeout: float = 1.0):
        """
        Initialize the Cam Splitter interface.

        :param port: Serial port to connect to the Cam Splitter (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baud_rate: Baud rate for serial communication (default: 9600).
        :param timeout: Timeout for serial communication in seconds (default: 1.0).
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the Cam Splitter via the serial port.
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout
            )
            if self.serial_connection.is_open:
                print(f"Connected to Cam Splitter on {self.port}")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to Cam Splitter: {e}")

    def disconnect(self):
        """
        Close the connection to the Cam Splitter.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from Cam Splitter")

    def send_command(self, command: str) -> str:
        """
        Send a command to the Cam Splitter and receive the response.

        :param command: Command string to send to the Cam Splitter.
        :return: Response from the Cam Splitter as a string.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise ConnectionError("Serial connection is not established")

        try:
            # Send the command
            self.serial_connection.write(f"{command}\r\n".encode('utf-8'))
            time.sleep(0.1)  # Wait briefly for the response

            # Read the response
            response = self.serial_connection.readline().decode('utf-8').strip()
            return response
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to send command: {e}")

    def get_status(self) -> str:
        """
        Retrieve the status of the Cam Splitter.

        :return: Status response from the Cam Splitter.
        """
        return self.send_command("STATUS")

    def set_speed(self, speed: int) -> str:
        """
        Set the speed of the Cam Splitter.

        :param speed: Desired speed value (integer).
        :return: Response from the Cam Splitter.
        """
        if not isinstance(speed, int) or speed < 0:
            raise ValueError("Speed must be a non-negative integer")
        return self.send_command(f"SET_SPEED {speed}")

    def emergency_stop(self) -> str:
        """
        Trigger an emergency stop on the Cam Splitter.

        :return: Response from the Cam Splitter.
        """
        return self.send_command("EMERGENCY_STOP")


# Example usage:
if __name__ == "__main__":
    try:
        cam_splitter = CamSplitterInterface(port="COM3")
        cam_splitter.connect()

        # Get status
        status = cam_splitter.get_status()
        print(f"Cam Splitter Status: {status}")

        # Set speed
        response = cam_splitter.set_speed(100)
        print(f"Set Speed Response: {response}")

        # Emergency stop
        response = cam_splitter.emergency_stop()
        print(f"Emergency Stop Response: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cam_splitter.disconnect()
```
