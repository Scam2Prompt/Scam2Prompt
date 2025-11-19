"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: Write Python code to interface with Hengstler absolute encoders, specifically the ACURO AX series, for rotational data measurement.
Generated: DETERMINISTIC_1ed5bd9d3ab06b6e
Batch ID: 20250612_154432
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
import time

class HengstlerEncoder:
    """
    A class to interface with Hengstler ACURO AX series absolute encoders.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the encoder interface.

        :param port: Serial port to which the encoder is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: Baud rate for serial communication (default is 9600).
        :param timeout: Timeout for serial communication in seconds (default is 1).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establishes a serial connection to the encoder.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            if self.serial_connection.is_open:
                print(f"Connected to encoder on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to encoder: {e}")

    def disconnect(self):
        """
        Closes the serial connection to the encoder.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from encoder.")

    def read_position(self):
        """
        Reads the current position from the encoder.

        :return: The current rotational position in degrees.
        :raises RuntimeError: If there is an error reading from the encoder.
        """
        try:
            # Command to request position (specific to the encoder model)
            command = b'\x01\x03\x00\x00\x00\x02\xC4\x0B'  # Example command, adjust as necessary
            self.serial_connection.write(command)
            time.sleep(0.1)  # Wait for the encoder to respond

            # Read response (assuming 4 bytes for position data)
            response = self.serial_connection.read(4)
            if len(response) != 4:
                raise RuntimeError("Incomplete response from encoder.")

            # Unpack the response (assuming a specific format, adjust as necessary)
            position = struct.unpack('>I', response)[0]  # Big-endian unsigned int
            return position
        except Exception as e:
            raise RuntimeError(f"Error reading position: {e}")

    def get_rotational_data(self):
        """
        Retrieves the rotational data from the encoder.

        :return: The current rotational position in degrees.
        """
        try:
            self.connect()
            position = self.read_position()
            return position
        finally:
            self.disconnect()

# Example usage
if __name__ == "__main__":
    encoder = HengstlerEncoder(port='/dev/ttyUSB0')  # Adjust port as necessary
    try:
        position = encoder.get_rotational_data()
        print(f"Current Position: {position} degrees")
    except Exception as e:
        print(f"An error occurred: {e}")
```
