"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Write Python code to interface with an electromagnetic flow meter, ensuring compatibility with industrial sensors like those described on Instrumentación UM's website.
Generated: DETERMINISTIC_794120fc858d6e4c
Batch ID: 20250612_153224
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
import struct

class ElectromagneticFlowMeter:
    """
    A class to interface with an electromagnetic flow meter.
    This class handles the communication with the flow meter via
    a serial connection and provides methods to read flow data.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initializes the flow meter interface.

        Parameters:
        port (str): The COM port to which the flow meter is connected.
        baudrate (int): The baud rate for serial communication.
        timeout (float): Timeout for serial read operations.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        self.connect()

    def connect(self):
        """Establishes the serial connection to the flow meter."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(2)  # Wait for the connection to stabilize
            print(f"Connected to flow meter on {self.port}")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to the flow meter on {self.port}: {e}")

    def read_flow_data(self) -> float:
        """
        Reads flow data from the electromagnetic flow meter.

        Returns:
        float: The flow rate measured by the flow meter.

        Raises:
        ValueError: If the data received is invalid or cannot be parsed.
        ConnectionError: If there is an issue with the serial connection.
        """
        try:
            # Sending a command to request flow data
            self.serial_connection.write(b'READ_FLOW\r\n')
            time.sleep(0.1)  # Short delay to allow data to be sent back
            response = self.serial_connection.readline()

            if not response:
                raise ConnectionError("No response from the flow meter.")

            # Example response format: b'FLOW: 123.45\n'
            response_str = response.decode('utf-8').strip()
            if response_str.startswith('FLOW:'):
                flow_value = float(response_str.split(':')[1].strip())
                return flow_value
            else:
                raise ValueError(f"Invalid response format: {response_str}")

        except (ValueError, ConnectionError) as e:
            print(f"Error reading flow data: {e}")
            raise

    def close(self):
        """Closes the serial connection to the flow meter."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Connection to flow meter closed.")

if __name__ == "__main__":
    try:
        # Example usage
        flow_meter = ElectromagneticFlowMeter(port='/dev/ttyUSB0')  # Update with actual port
        flow_rate = flow_meter.read_flow_data()
        print(f"Current flow rate: {flow_rate} L/min")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        flow_meter.close()
```
