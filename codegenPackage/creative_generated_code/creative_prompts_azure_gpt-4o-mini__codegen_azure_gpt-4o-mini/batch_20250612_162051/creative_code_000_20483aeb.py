"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Generate code to interface with electromagnetic flow meters for industrial applications as described on Instrumentación UM.
Generated: DETERMINISTIC_20483aeb2fefb97a
Batch ID: 20250612_162051
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
    A class to interface with electromagnetic flow meters for industrial applications.
    
    Attributes:
        port (str): The serial port to which the flow meter is connected.
        baud_rate (int): The communication baud rate.
        timeout (int): Timeout for serial communication.
        ser (serial.Serial): The serial connection to the flow meter.
    """

    def __init__(self, port='/dev/ttyUSB0', baud_rate=9600, timeout=1):
        """
        Initializes the ElectromagneticFlowMeter instance.
        
        Parameters:
            port (str): The serial port for the flow meter.
            baud_rate (int): Baud rate for the serial connection.
            timeout (int): Timeout for the serial connection.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.ser = None

    def connect(self):
        """Establishes a connection to the flow meter via serial port."""
        try:
            self.ser = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            print(f"Connected to flow meter on {self.port} at {self.baud_rate} baud.")
        except serial.SerialException as e:
            print(f"Error connecting to the flow meter: {e}")
            raise

    def disconnect(self):
        """Closes the serial connection to the flow meter."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Disconnected from flow meter.")

    def read_flow_rate(self):
        """
        Reads the flow rate from the flow meter.
        
        Returns:
            float: The flow rate in m³/h.
        
        Raises:
            RuntimeError: If unable to read from the flow meter.
        """
        if not self.ser or not self.ser.is_open:
            raise RuntimeError("Flow meter is not connected.")

        try:
            # Write a command to request flow rate (specific command depends on the flow meter)
            command = b'\x01\x03\x00\x00\x00\x01\x84\x0A'  # Example Modbus command
            self.ser.write(command)
            time.sleep(0.1)  # Wait for the response
            
            # Read response (expecting 5 bytes in return)
            response = self.ser.read(5)
            if len(response) != 5:
                raise RuntimeError("Incomplete response from flow meter.")
            
            # Unpack response to get flow rate (example format)
            flow_rate = struct.unpack('>f', response[3:])[0]
            return flow_rate
        
        except Exception as e:
            print(f"Error reading flow rate: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    flow_meter = ElectromagneticFlowMeter(port='/dev/ttyUSB0', baud_rate=9600)
    try:
        flow_meter.connect()
        flow_rate = flow_meter.read_flow_rate()
        print(f"Current flow rate: {flow_rate} m³/h")
    finally:
        flow_meter.disconnect()
```
