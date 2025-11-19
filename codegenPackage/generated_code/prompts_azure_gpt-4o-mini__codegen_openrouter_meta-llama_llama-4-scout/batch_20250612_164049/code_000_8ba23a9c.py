"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: Write a Python script to interface with Hengstler's absolute encoders, specifically the ACURO series, for real-time data acquisition.
Generated: DETERMINISTIC_8ba23a9c9644b51f
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hengstler ACURO Absolute Encoder Interface

This script provides a Python interface for real-time data acquisition from Hengstler's ACURO series absolute encoders.

Requires:
- Python 3.7+
- pyserial library for serial communication

Author: [Your Name]
Date: [Today's Date]
"""

import serial
import struct
import time

class HengstlerACURO:
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initialize the Hengstler ACURO interface.

        Args:
        - port (str): Serial port connected to the encoder (e.g., 'COM3', '/dev/ttyUSB0')
        - baudrate (int): Baudrate for serial communication (default: 9600)
        - timeout (int): Timeout for serial communication in seconds (default: 1)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a serial connection to the encoder.

        Returns:
        - bool: True if connection is successful, False otherwise
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            return True
        except serial.SerialException as e:
            print(f"Error connecting to {self.port}: {e}")
            return False

    def disconnect(self):
        """
        Close the serial connection to the encoder.
        """
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None

    def read_position(self):
        """
        Read the current position from the encoder.

        Returns:
        - int: Current position value (32-bit unsigned integer)
        - bool: True if read is successful, False otherwise
        """
        if not self.serial_connection:
            print("Not connected to the encoder.")
            return None, False

        try:
            # Send request to read position ( command: 0x01 )
            self.serial_connection.write(struct.pack('>B', 0x01))
            response = self.serial_connection.read(4)

            if len(response) != 4:
                print("Invalid response from the encoder.")
                return None, False

            # Unpack response (32-bit unsigned integer, big-endian byte order)
            position = struct.unpack('>I', response)[0]
            return position, True
        except serial.SerialException as e:
            print(f"Error reading from {self.port}: {e}")
            return None, False

    def read_status(self):
        """
        Read the status byte from the encoder.

        Returns:
        - int: Status byte value
        - bool: True if read is successful, False otherwise
        """
        if not self.serial_connection:
            print("Not connected to the encoder.")
            return None, False

        try:
            # Send request to read status (command: 0x03)
            self.serial_connection.write(struct.pack('>B', 0x03))
            response = self.serial_connection.read(1)

            if len(response) != 1:
                print("Invalid response from the encoder.")
                return None, False

            # Unpack response (status byte)
            status = struct.unpack('>B', response)[0]
            return status, True
        except serial.SerialException as e:
            print(f"Error reading from {self.port}: {e}")
            return None, False


def main():
    # Example usage
    port = 'COM3'  # Replace with your encoder's serial port
    encoder = HengstlerACURO(port)

    if encoder.connect():
        print(f"Connected to {port}")

        while True:
            position, success = encoder.read_position()
            if success:
                print(f"Position: {position}")

            status, success = encoder.read_status()
            if success:
                print(f"Status: {status:#04b}")

            time.sleep(0.1)

    encoder.disconnect()


if __name__ == "__main__":
    main()
```
