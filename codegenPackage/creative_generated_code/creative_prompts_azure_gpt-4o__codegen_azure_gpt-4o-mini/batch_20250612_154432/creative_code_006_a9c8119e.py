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
import json

class HengstlerCounterReader:
    """
    A class to read data from Hengstler multi-functional counters.
    
    Attributes:
        port (str): The serial port to which the counter is connected.
        baudrate (int): The baud rate for the serial communication.
        timeout (int): Timeout for reading from the serial port.
    """

    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the counter reader with the given parameters.

        Args:
            port (str): The serial port to connect to.
            baudrate (int): The baud rate for the connection (default is 9600).
            timeout (int): Timeout for the serial connection in seconds (default is 1).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """Establishes a serial connection to the counter."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to counter on {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Failed to connect to port {self.port}: {e}")
            raise

    def read_data(self):
        """Reads data from the counter and returns it as a dictionary.

        Returns:
            dict: The data read from the counter.

        Raises:
            Exception: If reading data fails.
        """
        try:
            if not self.serial_connection or not self.serial_connection.is_open:
                raise Exception("Serial connection is not established.")
            
            # Send a command to request data (adjust based on the counter's protocol)
            self.serial_connection.write(b'READ_DATA_COMMAND\n')
            time.sleep(0.5)  # Wait for a response

            # Read the response
            response = self.serial_connection.readline().decode('utf-8').strip()

            # Parse the response into a dictionary (assumes JSON format for this example)
            data = json.loads(response)
            return data
        except Exception as e:
            print(f"Error reading data: {e}")
            raise

    def close(self):
        """Closes the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Connection closed.")
        else:
            print("Connection is already closed or was not established.")

def main():
    # Example usage
    port = 'COM3'  # Adjust to the correct COM port for your system
    counter_reader = HengstlerCounterReader(port)

    try:
        counter_reader.connect()
        data = counter_reader.read_data()
        print("Data read from counter:", data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        counter_reader.close()

if __name__ == "__main__":
    main()
```
