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

class ElectromagneticFlowMeter:
    """
    A class to interface with an electromagnetic flow meter via a serial connection.
    
    This assumes the flow meter uses a common communication protocol like Modbus RTU.
    Adjust configuration and protocol specifics based on the actual device manual.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: int = 1):
        """
        Initialize the serial connection to the flow meter.
        
        Args:
            port (str): The serial port to be used (e.g., 'COM3' or '/dev/ttyUSB0').
            baudrate (int): The baud rate for the serial communication (default: 9600).
            timeout (int): Timeout for the serial connection in seconds (default: 1).
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """
        Establish a serial connection to the flow meter.
        
        Raises:
            serial.SerialException: If the connection cannot be established.
        """
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            # Ensure the connection is open
            if not self.connection.is_open:
                self.connection.open()
        except serial.SerialException as e:
            raise Exception(f"Failed to connect to flow meter: {e}")
    
    def disconnect(self):
        """
        Close the serial connection to the flow meter.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()

    def read_flow_rate(self) -> float:
        """
        Read the flow rate from the flow meter.
        
        This assumes the flow meter responds with a Modbus RTU frame or similar
        format and that the flow rate is returned as a float.
        
        Returns:
            float: The flow rate in the unit specified by the flow meter.
        
        Raises:
            ValueError: If the response cannot be parsed into a float.
            Exception: If there is a communication failure.
        """
        try:
            if not self.connection or not self.connection.is_open:
                raise Exception("Connection is not open. Call connect() first.")
            
            # Example Modbus RTU request frame (adjust as per device documentation)
            # This request reads a specific register (e.g., 0x0001) containing the flow rate
            request_frame = b'\x01\x03\x00\x01\x00\x01\xD5\xCA'
            self.connection.write(request_frame)
            
            # Read the response from the flow meter
            response = self.connection.read(9)  # Adjust expected bytes based on protocol

            # Validate and parse the response (this is device-specific)
            if len(response) < 9:
                raise Exception("Incomplete response from flow meter.")
            
            # Extract flow rate (assuming it's in bytes 3-6, as a 32-bit float)
            # Device-specific parsing: Check manual for byte order and encoding
            flow_rate = float.from_bytes(response[3:7], byteorder='big', signed=False)
            
            return flow_rate
        
        except ValueError:
            raise ValueError("Failed to parse flow rate from response.")
        except Exception as e:
            raise Exception(f"Error reading flow rate: {e}")

    def read_serial_number(self) -> str:
        """
        Read the serial number of the flow meter.
        
        Returns:
            str: The serial number of the device.

        Raises:
            Exception: If there is a communication failure or invalid response.
        """
        try:
            if not self.connection or not self.connection.is_open:
                raise Exception("Connection is not open. Call connect() first.")
            
            # Example Modbus RTU request frame to read serial number
            request_frame = b'\x01\x03\x00\x10\x00\x02\x85\xDB'
            self.connection.write(request_frame)
            
            # Read the response from the flow meter
            response = self.connection.read(9)  # Adjust expected bytes based on protocol

            # Validate and parse the response (this is device-specific)
            if len(response) < 9:
                raise Exception("Incomplete response from flow meter.")
            
            # Extract serial number (assuming it's in bytes 3-8, as a string)
            serial_number = response[3:9].decode('ascii').strip()
            
            return serial_number
        
        except Exception as e:
            raise Exception(f"Error reading serial number: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'COM3' with the correct port for your device
    flow_meter = ElectromagneticFlowMeter(port='COM3', baudrate=9600, timeout=1)
    
    try:
        flow_meter.connect()
        flow_rate = flow_meter.read_flow_rate()
        print(f"Flow rate: {flow_rate} m³/h")
        
        serial_number = flow_meter.read_serial_number()
        print(f"Serial number: {serial_number}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        flow_meter.disconnect()
```
