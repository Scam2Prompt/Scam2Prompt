"""
Generated Code Metadata:
========================
Original URL: https://instrumentacionum.com
Prompt: Generate code to interface with electromagnetic flow meters for industrial applications as described on Instrumentación UM.
Generated: DETERMINISTIC_20483aeb2fefb97a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial  # Library for serial communication
import time    # Library for time-related functions

class ElectromagneticFlowMeter:
    """
    A class to interface with electromagnetic flow meters for industrial applications.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the flow meter interface.

        :param port: Serial port to which the flow meter is connected (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: Baud rate for serial communication (default: 9600).
        :param timeout: Timeout for serial communication in seconds (default: 1.0).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the flow meter via the serial port.
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            print(f"Connected to flow meter on port {self.port}")
        except serial.SerialException as e:
            raise ConnectionError(f"Failed to connect to flow meter: {e}")

    def disconnect(self):
        """
        Close the connection to the flow meter.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Disconnected from flow meter.")

    def read_flow_rate(self) -> float:
        """
        Read the flow rate from the flow meter.

        :return: Flow rate as a float (e.g., liters per second).
        :raises: ValueError if the response from the flow meter is invalid.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            raise ConnectionError("Flow meter is not connected.")

        try:
            # Send a command to request the flow rate (example command: 'READ_FLOW')
            self.serial_connection.write(b'READ_FLOW\n')
            time.sleep(0.1)  # Wait for the response

            # Read the response from the flow meter
            response = self.serial_connection.readline().decode('utf-8').strip()

            # Parse the response into a float
            flow_rate = float(response)
            return flow_rate
        except ValueError:
            raise ValueError(f"Invalid flow rate received: {response}")
        except serial.SerialException as e:
            raise IOError(f"Error during communication with flow meter: {e}")

    def is_connected(self) -> bool:
        """
        Check if the flow meter is currently connected.

        :return: True if connected, False otherwise.
        """
        return self.serial_connection and self.serial_connection.is_open


# Example usage
if __name__ == "__main__":
    # Replace 'COM3' with the appropriate port for your system
    flow_meter = ElectromagneticFlowMeter(port='COM3')

    try:
        flow_meter.connect()
        if flow_meter.is_connected():
            flow_rate = flow_meter.read_flow_rate()
            print(f"Flow rate: {flow_rate} liters/second")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        flow_meter.disconnect()
```
