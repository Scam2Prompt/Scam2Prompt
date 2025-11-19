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
import serial
import time
from typing import Optional, Tuple

class ElectromagneticFlowMeter:
    """
    A class to interface with electromagnetic flow meters over serial communication.
    Supports common protocols like Modbus RTU for industrial applications.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the flow meter connection.
        
        Args:
            port: Serial port name (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate: Baud rate for serial communication (default: 9600)
            timeout: Read timeout in seconds (default: 1.0)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def connect(self) -> bool:
        """
        Establish connection to the flow meter.
        
        Returns:
            bool: True if connection was successful, False otherwise
        """
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=self.timeout
            )
            return self.serial_conn.is_open
        except serial.SerialException as e:
            print(f"Error connecting to flow meter: {e}")
            return False

    def disconnect(self) -> None:
        """Close the serial connection."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def read_flow_rate(self, slave_address: int = 1) -> Optional[float]:
        """
        Read the current flow rate from the flow meter.
        
        Args:
            slave_address: Modbus slave address (default: 1)
            
        Returns:
            float: Current flow rate in configured units, None if read failed
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            print("Error: Not connected to flow meter")
            return None

        # Modbus RTU request for holding register (function code 0x03)
        # Assuming flow rate is stored in register 0 (may vary by device)
        request = self._create_modbus_request(slave_address, 0x03, 0x0000, 0x0001)
        
        try:
            self.serial_conn.write(request)
            response = self.serial_conn.read(7)  # Expected response length
            
            if len(response) == 7 and self._verify_crc(response):
                # Extract flow rate from response (assuming 32-bit float in registers 0-1)
                value_bytes = response[3:7]
                flow_rate = self._bytes_to_float(value_bytes)
                return flow_rate
            else:
                print("Error: Invalid response from flow meter")
                return None
        except serial.SerialException as e:
            print(f"Error reading from flow meter: {e}")
            return None

    def _create_modbus_request(self, slave_address: int, function_code: int, 
                             register_address: int, register_count: int) -> bytes:
        """
        Create a Modbus RTU request frame with CRC.
        
        Args:
            slave_address: Modbus slave address
            function_code: Modbus function code
            register_address: Starting register address
            register_count: Number of registers to read
            
        Returns:
            bytes: Complete Modbus RTU request frame
        """
        request = bytearray([
            slave_address,
            function_code,
            (register_address >> 8) & 0xFF,
            register_address & 0xFF,
            (register_count >> 8) & 0xFF,
            register_count & 0xFF
        ])
        crc = self._calculate_crc(request)
        request.append(crc & 0xFF)
        request.append((crc >> 8) & 0xFF)
        return bytes(request)

    @staticmethod
    def _calculate_crc(data: bytearray) -> int:
        """
        Calculate Modbus RTU CRC for the given data.
        
        Args:
            data: Data to calculate CRC for
            
        Returns:
            int: 16-bit CRC value
        """
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc

    @staticmethod
    def _verify_crc(data: bytes) -> bool:
        """
        Verify the CRC of a Modbus RTU response.
        
        Args:
            data: Complete Modbus RTU response frame
            
        Returns:
            bool: True if CRC is valid, False otherwise
        """
        if len(data) < 2:
            return False
            
        received_crc = (data[-1] << 8) | data[-2]
        calculated_crc = ElectromagneticFlowMeter._calculate_crc(data[:-2])
        return received_crc == calculated_crc

    @staticmethod
    def _bytes_to_float(data: bytes) -> float:
        """
        Convert 4 bytes to a 32-bit float (IEEE 754).
        
        Args:
            data: 4 bytes representing the float value
            
        Returns:
            float: Converted float value
        """
        import struct
        return struct.unpack('>f', data)[0]

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    # Replace with actual serial port
    PORT = "/dev/ttyUSB0"
    
    with ElectromagneticFlowMeter(PORT) as flow_meter:
        if flow_meter.serial_conn and flow_meter.serial_conn.is_open:
            flow_rate = flow_meter.read_flow_rate()
            if flow_rate is not None:
                print(f"Current flow rate: {flow_rate:.2f} m³/h")
            else:
                print("Failed to read flow rate")
        else:
            print("Failed to connect to flow meter")
```
