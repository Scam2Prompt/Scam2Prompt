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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectromagneticFlowMeter:
    """
    A class to interface with an electromagnetic flow meter via a serial connection.
    Compatible with industrial sensors as described on Instrumentación UM's website.
    """
    
    def __init__(self, port: str, baud_rate: int = 9600, timeout: float = 1.0):
        """
        Initializes the connection to the flow meter.

        :param port: Serial port to which the flow meter is connected (e.g., 'COM3', '/dev/ttyUSB0').
        :param baud_rate: Baud rate for the serial communication (default is 9600).
        :param timeout: Timeout for serial reads in seconds (default is 1.0).
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establishes a serial connection to the flow meter.
        Logs an error if the connection fails.
        """
        try:
            self.connection = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=self.timeout)
            logging.info(f"Connected to flow meter on port {self.port}.")
        except serial.SerialException as e:
            logging.error(f"Failed to connect to the flow meter: {e}")
            raise

    def disconnect(self):
        """
        Closes the serial connection to the flow meter if it is open.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            logging.info(f"Disconnected from flow meter on port {self.port}.")

    def read_flow_rate(self) -> float:
        """
        Reads the current flow rate from the flow meter.

        :return: Flow rate as a floating-point number.
        :raises: ValueError if the response is invalid or cannot be parsed.
        """
        if not self.connection or not self.connection.is_open:
            raise ConnectionError("Flow meter is not connected.")

        try:
            # Send a command to request the flow rate (this command depends on the specific flow meter protocol).
            # For demonstration purposes, we use a generic command 'READ_FLOW'.
            self.connection.write(b'READ_FLOW\n')

            # Read the response from the flow meter
            response = self.connection.readline().decode('utf-8').strip()
            
            # Parse the response and return the flow rate
            flow_rate = float(response)  # Assuming the response is a plain float value
            logging.info(f"Flow rate read successfully: {flow_rate} m³/s")
            return flow_rate
        except ValueError:
            logging.error(f"Invalid response received: {response}")
            raise
        except serial.SerialTimeoutException:
            logging.error("Timeout while reading flow rate from the flow meter.")
            raise

    def __enter__(self):
        """
        Context manager enter method. Automatically connects when used in a 'with' statement.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Context manager exit method. Automatically disconnects when exiting a 'with' statement.
        """
        self.disconnect()


# Example usage:
if __name__ == "__main__":
    try:
        # Replace 'COM3' with the correct port for your flow meter
        with ElectromagneticFlowMeter(port='COM3') as flow_meter:
            flow_rate = flow_meter.read_flow_rate()
            print(f"Flow Rate: {flow_rate} m³/s")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
