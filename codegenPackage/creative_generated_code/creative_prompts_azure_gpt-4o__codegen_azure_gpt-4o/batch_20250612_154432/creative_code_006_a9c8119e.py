"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hengstler.imall.pro
Prompt: Create a Python program to read data from Hengstler multi-functional counters, such as the Tico or Colibri series, for production monitoring.
Generated: DETERMINISTIC_a9c8119e3671f559
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
import time


class CounterReader:
    """
    A class to interface with Hengstler multi-functional counters (e.g., Tico or Colibri series)
    for production monitoring.
    """
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the serial connection to the counter.

        Args:
            port (str): The serial port (e.g., 'COM1', '/dev/ttyUSB0').
            baudrate (int): Baud rate for the serial connection (default: 9600).
            timeout (float): Timeout for reading data (default: 1 second).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establishes a connection to the counter via the serial port.
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            print(f"Connected to counter on {self.port}")
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to connect to counter: {e}")

    def disconnect(self):
        """
        Closes the connection to the counter.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print(f"Disconnected from counter on {self.port}")

    def read_data(self):
        """
        Reads data from the counter.

        Returns:
            str: The data read from the counter.

        Raises:
            RuntimeError: If the serial connection is not established or an error occurs during reading.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise RuntimeError("Serial connection is not established")

        try:
            # Send command to request data from the counter (replace 'READ' with actual command for Hengstler)
            self.serial_connection.write(b'READ\n')
            time.sleep(0.1)  # Wait for the counter to respond

            # Read the response from the counter
            response = self.serial_connection.readline().decode('utf-8').strip()
            return response
        except serial.SerialException as e:
            raise RuntimeError(f"Error reading data from counter: {e}")


def main():
    """
    Main function to demonstrate reading data from the Hengstler counter.
    """
    # Replace 'COM1' with your actual serial port
    port_name = 'COM1'

    # Create an instance of CounterReader
    counter_reader = CounterReader(port=port_name)

    try:
        # Connect to the counter
        counter_reader.connect()

        # Read data from the counter
        data = counter_reader.read_data()
        print(f"Data from counter: {data}")
    except RuntimeError as e:
        print(e)
    finally:
        # Disconnect from the counter
        counter_reader.disconnect()


if __name__ == "__main__":
    main()
```

Make sure to replace `'READ'` and `'COM1'` with the appropriate command and serial port for your Hengstler counter setup. This code assumes the counter communicates over a serial interface and follows standard serial communication protocols.
