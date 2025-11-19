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
    Interface with Hengstler absolute encoders, specifically the ACURO AX series.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initialize the HengstlerEncoder object.

        Args:
            port (str): The serial port connected to the encoder (e.g., 'COM3', '/dev/ttyUSB0').
            baudrate (int, optional): The baudrate of the serial connection. Defaults to 9600.
            timeout (int, optional): The timeout for the serial connection in seconds. Defaults to 1.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the encoder via the serial port.
        """
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            self.serial_connection.bytesize = serial.EIGHTBITS
            self.serial_connection.parity = serial.PARITY_NONE
            self.serial_connection.stopbits = serial.STOPBITS_ONE
        except serial.SerialException as e:
            print(f"Failed to connect to the encoder: {e}")

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
            int: The current position of the encoder in ticks.
        """
        if not self.serial_connection:
            print("Not connected to the encoder.")
            return None

        try:
            # Send the command to read the position ( command: 0x01 )
            self.serial_connection.write(b'\x01')
            time.sleep(0.01)  # Wait for the response

            # Read the response ( 4 bytes for the position )
            response = self.serial_connection.read(4)
            if len(response) != 4:
                print("Invalid response from the encoder.")
                return None

            # Unpack the position value from the response
            position = struct.unpack('>I', response)[0]
            return position
        except serial.SerialException as e:
            print(f"Failed to read position from the encoder: {e}")
            return None

    def read_parameters(self):
        """
        Read the parameters from the encoder.

        Returns:
            dict: A dictionary containing the encoder's parameters.
        """
        if not self.serial_connection:
            print("Not connected to the encoder.")
            return None

        try:
            # Send the command to read the parameters ( command: 0x12 )
            self.serial_connection.write(b'\x12')
            time.sleep(0.01)  # Wait for the response

            # Read the response ( 7 bytes for the parameters )
            response = self.serial_connection.read(7)
            if len(response) != 7:
                print("Invalid response from the encoder.")
                return None

            # Unpack the parameters from the response
            params = {
                'resolution': struct.unpack('>H', response[:2])[0],
                'max_speed': struct.unpack('>H', response[2:4])[0],
                'acceleration': struct.unpack('>H', response[4:6])[0],
                'status': response[6]
            }
            return params
        except serial.SerialException as e:
            print(f"Failed to read parameters from the encoder: {e}")
            return None


def main():
    encoder = HengstlerEncoder('COM3')  # Replace 'COM3' with your actual serial port
    encoder.connect()

    position = encoder.read_position()
    if position is not None:
        print(f"Current position: {position} ticks")

    params = encoder.read_parameters()
    if params is not None:
        print("Encoder parameters:")
        print(f"  Resolution: {params['resolution']}")
        print(f"  Max speed: {params['max_speed']}")
        print(f"  Acceleration: {params['acceleration']}")
        print(f"  Status: {params['status']}")

    encoder.disconnect()


if __name__ == "__main__":
    main()
```
