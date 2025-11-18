"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumaipce.com
Prompt: Write a Python script to demonstrate the integration of PLC programming for industrial automation, referencing Puma Ipce's expertise in system control and instrumentation calibration.
Generated: DETERMINISTIC_5fe8058f5c13309f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PLCConnectionError(Exception):
    """Custom exception for PLC connection errors."""
    pass

class PLCController:
    """
    A class to represent a PLC (Programmable Logic Controller) for industrial automation.
    This class provides methods to connect to the PLC, read data, and write control signals.
    """

    def __init__(self, ip_address, port):
        """
        Initializes the PLCController with the given IP address and port.
        
        :param ip_address: The IP address of the PLC.
        :param port: The port number to connect to the PLC.
        """
        self.ip_address = ip_address
        self.port = port
        self.connected = False

    def connect(self):
        """Establish a connection to the PLC."""
        try:
            # Simulate connection to PLC (this would be replaced with actual connection code)
            logging.info(f"Connecting to PLC at {self.ip_address}:{self.port}...")
            # Assume connection is established successfully
            self.connected = True
            logging.info("Connected to PLC successfully.")
        except Exception as e:
            logging.error(f"Failed to connect to PLC: {e}")
            raise PLCConnectionError("Could not connect to PLC.")

    def read_data(self):
        """
        Read data from the PLC.
        
        :return: Mock data from PLC (replace with actual read logic).
        """
        if not self.connected:
            raise PLCConnectionError("Not connected to PLC.")

        # Simulated data reading
        data = {"temperature": 75, "pressure": 30}
        logging.info(f"Read data from PLC: {data}")
        return data

    def write_control_signal(self, signal):
        """
        Write a control signal to the PLC.
        
        :param signal: The control signal to be sent to the PLC.
        """
        if not self.connected:
            raise PLCConnectionError("Not connected to PLC.")

        try:
            logging.info(f"Sending control signal to PLC: {signal}")
            # Simulate writing the signal (this would be replaced with actual write logic)
            logging.info("Control signal sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send control signal: {e}")

    def disconnect(self):
        """Disconnect from the PLC."""
        if self.connected:
            logging.info("Disconnecting from PLC...")
            # Simulate disconnection
            self.connected = False
            logging.info("Disconnected from PLC.")

def main():
    """Main function to demonstrate PLC controller functionality."""
    plc = PLCController("192.168.1.100", 502)

    try:
        plc.connect()
        data = plc.read_data()
        logging.info(f"Data received: {data}")

        # Example of writing a control signal
        plc.write_control_signal("START")
    except PLCConnectionError as e:
        logging.error(e)
    finally:
        plc.disconnect()

if __name__ == "__main__":
    main()
```
