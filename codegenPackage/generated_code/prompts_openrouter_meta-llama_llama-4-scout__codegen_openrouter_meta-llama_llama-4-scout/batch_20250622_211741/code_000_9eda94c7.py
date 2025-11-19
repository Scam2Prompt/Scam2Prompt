"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: "Write a Python code snippet to interface with Hengstler's ACURO absolute encoders (AC, AD, AR, AX series) using a serial communication protocol."
Generated: DETERMINISTIC_9eda94c736c75d2a
Batch ID: 20250622_211741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial
import struct

class HengstlerEncoder:
    """
    Interface with Hengstler's ACURO absolute encoders (AC, AD, AR, AX series) using serial communication protocol.

    Attributes:
        port (str): Serial port name (e.g., 'COM3', '/dev/ttyUSB0')
        baudrate (int): Baudrate for serial communication (default: 9600)
        timeout (int): Timeout for serial communication (default: 1 second)
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a serial connection to the encoder.

        Raises:
            serial.SerialException: If the serial connection cannot be established.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        except serial.SerialException as e:
            raise serial.SerialException(f"Failed to connect to {self.port}: {e}")

    def disconnect(self):
        """
        Close the serial connection to the encoder.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

    def read_position(self):
        """
        Read the absolute position from the encoder.

        Returns:
            int: Absolute position value.

        Raises:
            Exception: If the response is invalid or a communication error occurs.
        """
        if not self.serial_connection:
            raise Exception("Not connected to the encoder")

        # Send request to read position ( command: 'r' )
        self.serial_connection.write(b'r')

        # Read response ( 4 bytes: 2 bytes status, 2 bytes position high, 2 bytes position low )
        response = self.serial_connection.read(6)

        if len(response) != 6:
            raise Exception("Invalid response length")

        # Unpack response
        status = struct.unpack('>H', response[:2])[0]
        position_high = struct.unpack('>H', response[2:4])[0]
        position_low = struct.unpack('>H', response[4:6])[0]

        # Combine position high and low
        position = (position_high << 16) | position_low

        return position

    def read_parameters(self):
        """
        Read the encoder parameters.

        Returns:
            dict: Dictionary containing the encoder parameters.

        Raises:
            Exception: If the response is invalid or a communication error occurs.
        """
        if not self.serial_connection:
            raise Exception("Not connected to the encoder")

        # Send request to read parameters ( command: 'p' )
        self.serial_connection.write(b'p')

        # Read response ( 8 bytes: 2 bytes status, 2 bytes resolution, 2 bytes max speed, 2 bytes acceleration )
        response = self.serial_connection.read(8)

        if len(response) != 8:
            raise Exception("Invalid response length")

        # Unpack response
        status = struct.unpack('>H', response[:2])[0]
        resolution = struct.unpack('>H', response[2:4])[0]
        max_speed = struct.unpack('>H', response[4:6])[0]
        acceleration = struct.unpack('>H', response[6:8])[0]

        parameters = {
            'status': status,
            'resolution': resolution,
            'max_speed': max_speed,
            'acceleration': acceleration
        }

        return parameters


def main():
    if __name__ == "__main__":
        port = 'COM3'  # Replace with your serial port
        encoder = HengstlerEncoder(port)

        try:
            encoder.connect()
            position = encoder.read_position()
            print(f"Absolute Position: {position}")

            parameters = encoder.read_parameters()
            print("Encoder Parameters:")
            for key, value in parameters.items():
                print(f"{key.capitalize()}: {value}")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            encoder.disconnect()


if __name__ == "__main__":
    main()
```
