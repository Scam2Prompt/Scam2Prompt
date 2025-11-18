"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Write Python code to interface with Hengstler absolute encoders, specifically the ACURO AX series, for rotational data measurement.
Generated: DETERMINISTIC_1ed5bd9d3ab06b6e
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import serial
import struct
import time

class HengstlerEncoder:
    """
    A class to interface with Hengstler ACURO AX series absolute encoders.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initializes the encoder interface.

        :param port: The serial port to which the encoder is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: The communication speed (default is 9600).
        :param timeout: The time to wait for a response (default is 1 second).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = self._create_serial_connection()

    def _create_serial_connection(self):
        """
        Creates and returns a serial connection.

        :return: A serial.Serial object.
        :raises: SerialException if the connection cannot be established.
        """
        try:
            connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            return connection
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to connect to the encoder on {self.port}: {e}")

    def read_position(self) -> int:
        """
        Reads the current position from the encoder.

        :return: The rotational position in counts.
        :raises: RuntimeError if the read operation fails.
        """
        # Command to request position data (this may vary based on the specific protocol)
        request_command = b'\x01\x03\x00\x00\x00\x02\xC4\x0B'  # Example command, replace as needed
        self.serial_connection.write(request_command)

        # Wait for a response
        time.sleep(0.1)  # Adjust delay as necessary for your specific encoder

        # Read response
        response = self.serial_connection.read(7)  # Expecting 7 bytes in response
        if len(response) != 7:
            raise RuntimeError("Failed to read position data from encoder.")

        # Parse the response (example parsing, adapt as necessary for your encoder)
        position_data = struct.unpack('>I', response[3:7])[0]  # Assuming position is in the last 4 bytes
        return position_data

    def close(self):
        """
        Closes the serial connection.
        """
        if self.serial_connection.is_open:
            self.serial_connection.close()

    def __del__(self):
        """
        Ensure the serial connection is closed when the object is deleted.
        """
        self.close()


# Example Usage
if __name__ == "__main__":
    try:
        encoder = HengstlerEncoder(port='/dev/ttyUSB0')  # Replace with your serial port
        position = encoder.read_position()
        print(f"Current Position: {position} counts")
    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        encoder.close()
```
