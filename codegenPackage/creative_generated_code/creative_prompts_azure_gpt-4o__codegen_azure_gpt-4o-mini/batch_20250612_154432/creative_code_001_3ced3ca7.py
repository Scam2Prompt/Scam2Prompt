"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Recommend libraries or APIs to work with Hengstler incremental encoders, such as ICURO RI or RX series, for real-time position tracking.
Generated: DETERMINISTIC_3ced3ca7112507ef
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import serial

class HengstlerEncoder:
    """
    A class to interface with Hengstler incremental encoders.
    This class handles communication over a serial interface
    to read position data in real-time.
    """

    def __init__(self, port: str, baudrate: int = 9600):
        """
        Initializes the encoder communication.

        :param port: The serial port to which the encoder is connected.
        :param baudrate: The baud rate for communication (default: 9600).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None
        self.connect()

    def connect(self):
        """Establishes serial connection to the encoder."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to encoder on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            raise

    def read_position(self):
        """
        Reads the current position from the encoder.

        :return: The current position as an integer.
        :raises ValueError: If the response from the encoder is invalid.
        """
        try:
            # Send command to request position
            self.serial_connection.write(b'P')  # Example command for position
            response = self.serial_connection.readline().strip()

            # Convert response to integer
            position = int(response)
            return position
        except ValueError:
            print("Error: Invalid response received from encoder.")
            raise
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")
            raise

    def close(self):
        """Closes the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Serial connection closed.")

if __name__ == "__main__":
    try:
        # Example usage of the HengstlerEncoder class
        encoder = HengstlerEncoder(port='/dev/ttyUSB0')  # Replace with the appropriate port

        # Continuous position tracking loop
        while True:
            position = encoder.read_position()
            print(f"Current Position: {position}")
            time.sleep(1)  # Read position every second

    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")
    finally:
        encoder.close()  # Ensure the serial connection is closed
```
