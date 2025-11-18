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
"""
Code to interface with Hengstler incremental encoders (e.g., ICURO RI or RX series) for real-time position tracking.
This script uses the PySerial library to communicate with the encoder through a serial interface.
"""

import serial  # Library for serial communication
import time    # Library for timing operations

class IncrementalEncoder:
    """
    A class to interact with Hengstler incremental encoders via a serial interface.
    """
    
    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the encoder interface.

        Args:
            port (str): The serial port to which the encoder is connected (e.g., 'COM3' or '/dev/ttyUSB0').
            baudrate (int): Communication speed (default: 9600).
            timeout (float): Timeout for serial communication in seconds (default: 1.0).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def connect(self):
        """
        Establish connection to the encoder via the serial port.
        """
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            print(f"Successfully connected to encoder on {self.port}")
        except serial.SerialException as e:
            print(f"Error connecting to encoder: {e}")
            raise

    def disconnect(self):
        """
        Close the connection to the encoder.
        """
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            print("Connection to encoder closed.")

    def read_position(self):
        """
        Read the current position from the encoder.

        Returns:
            str: The position data from the encoder.

        Raises:
            RuntimeError: If the connection is not open or reading fails.
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            raise RuntimeError("Encoder connection is not established.")

        try:
            # Send a command to request position data (specific to the encoder protocol)
            self.serial_conn.write(b'POSITION?\n')

            # Wait and read the response from the encoder
            response = self.serial_conn.readline()
            return response.decode('utf-8').strip()  # Decode and clean up the response
        except Exception as e:
            print(f"Error reading position from encoder: {e}")
            raise

    def reset_encoder(self):
        """
        Reset the encoder position to zero.

        This is useful for calibration or re-initialization during use.
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            raise RuntimeError("Encoder connection is not established.")

        try:
            # Send a reset command (specific to the encoder protocol)
            self.serial_conn.write(b'RESET\n')
            print("Encoder reset successfully.")
        except Exception as e:
            print(f"Error resetting encoder: {e}")
            raise


if __name__ == "__main__":
    """
    Main function to demonstrate the usage of IncrementalEncoder class.
    """
    try:
        # Replace 'COM3' with the appropriate port for your setup.
        encoder = IncrementalEncoder(port='COM3')
        encoder.connect()

        # Read the current position
        position = encoder.read_position()
        print(f"Current encoder position: {position}")

        # Reset the encoder
        encoder.reset_encoder()

        # Disconnect when done
        encoder.disconnect()

    except Exception as e:
        print(f"An error occurred: {e}")
```

### Required Dependencies:
- Install the PySerial library with `pip install pyserial`.

### Notes:
- Replace `'COM3'` in `IncrementalEncoder(port='COM3')` with the appropriate serial port for your setup.
- Ensure that the encoder's documentation is consulted to determine the exact commands (`POSITION?` and `RESET` in this example) for communication.
