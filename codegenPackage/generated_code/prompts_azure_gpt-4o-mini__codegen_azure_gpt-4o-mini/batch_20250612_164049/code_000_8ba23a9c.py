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
import serial
import struct
import time

class HengstlerEncoder:
    """
    A class to interface with Hengstler's ACURO series absolute encoders.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the encoder interface.

        :param port: Serial port to which the encoder is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: Baud rate for the serial communication.
        :param timeout: Timeout for the serial communication.
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
            print(f"Connected to encoder on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error connecting to encoder: {e}")
            raise

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

        :return: The current position as an integer.
        :raises RuntimeError: If there is an error reading from the encoder.
        """
        try:
            # Command to request position (specific command may vary based on encoder model)
            command = b'\x01\x03\x00\x00\x00\x02\xC4\x0B'  # Example command
            self.serial_connection.write(command)

            # Read response (assuming 4 bytes for position)
            response = self.serial_connection.read(4)
            if len(response) != 4:
                raise RuntimeError("Incomplete response from encoder.")

            # Unpack the response to get the position
            position = struct.unpack('>I', response)[0]  # Big-endian unsigned int
            return position
        except Exception as e:
            print(f"Error reading position: {e}")
            raise

    def run(self):
        """
        Main loop to continuously read position from the encoder.
        """
        try:
            while True:
                position = self.read_position()
                print(f"Current Position: {position}")
                time.sleep(1)  # Adjust the sleep time as necessary
        except KeyboardInterrupt:
            print("Stopping data acquisition.")
        finally:
            self.disconnect()

if __name__ == "__main__":
    # Example usage
    encoder = HengstlerEncoder(port='/dev/ttyUSB0')  # Change to your port
    encoder.connect()
    encoder.run()
```
