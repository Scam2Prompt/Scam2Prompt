"""
Generated Code Metadata:
========================
Original URL: https://hengstler.imall.pro
Prompt: Generate code to integrate Hengstler safety relays (e.g., RAS or RBS series) into an industrial control system using Python.
Generated: DETERMINISTIC_548a0cf163242b56
Batch ID: 20250612_154432
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
from enum import Enum
from typing import Optional, Tuple

class SafetyRelayError(Exception):
    """Base exception for safety relay communication errors."""
    pass

class RelayStatus(Enum):
    """Enum representing possible relay statuses."""
    SAFE = 0
    ACTIVE = 1
    FAULT = 2
    UNKNOWN = 3

class HengstlerSafetyRelay:
    """
    Class for communicating with Hengstler safety relays (RAS/RBS series) via serial interface.
    
    Args:
        port (str): Serial port name (e.g., 'COM3' or '/dev/ttyUSB0')
        baudrate (int): Baud rate for communication (default 9600)
        timeout (float): Serial timeout in seconds (default 1.0)
    """
    
    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        
    def connect(self) -> None:
        """Establish serial connection to the safety relay."""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
            # Allow time for connection to establish
            time.sleep(0.1)
        except serial.SerialException as e:
            raise SafetyRelayError(f"Failed to connect to relay: {str(e)}")
    
    def disconnect(self) -> None:
        """Close the serial connection."""
        if self.serial_conn and self.serial_conn.is_open:
            try:
                self.serial_conn.close()
            except serial.SerialException as e:
                raise SafetyRelayError(f"Error disconnecting: {str(e)}")
    
    def send_command(self, command: str) -> str:
        """
        Send a command to the relay and return the response.
        
        Args:
            command (str): Command string to send
            
        Returns:
            str: Response from the relay
            
        Raises:
            SafetyRelayError: If communication fails or invalid response
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            raise SafetyRelayError("Not connected to relay")
        
        try:
            # Clear buffers
            self.serial_conn.reset_input_buffer()
            self.serial_conn.reset_output_buffer()
            
            # Send command with termination
            self.serial_conn.write((command + '\r').encode('ascii'))
            
            # Read response (assuming relay responds within timeout)
            response = self.serial_conn.read_until(b'\r').decode('ascii').strip()
            
            if not response:
                raise SafetyRelayError("No response from relay")
                
            return response
        except serial.SerialException as e:
            raise SafetyRelayError(f"Communication error: {str(e)}")
    
    def get_status(self) -> Tuple[RelayStatus, Optional[str]]:
        """
        Get the current status of the safety relay.
        
        Returns:
            Tuple[RelayStatus, Optional[str]]: (status, additional_info)
            
        Raises:
            SafetyRelayError: If status cannot be determined
        """
        try:
            response = self.send_command("STATUS")
            
            # Parse response (example format: "STATUS:1,OK")
            parts = response.split(':')
            if len(parts) != 2:
                raise SafetyRelayError(f"Invalid status response: {response}")
                
            status_parts = parts[1].split(',')
            status_code = int(status_parts[0])
            info = status_parts[1] if len(status_parts) > 1 else None
            
            try:
                return (RelayStatus(status_code), info)
            except ValueError:
                return (RelayStatus.UNKNOWN, info)
                
        except (ValueError, IndexError) as e:
            raise SafetyRelayError(f"Failed to parse status: {str(e)}")
    
    def reset(self) -> bool:
        """
        Attempt to reset the safety relay.
        
        Returns:
            bool: True if reset was successful, False otherwise
        """
        try:
            response = self.send_command("RESET")
            return response.upper() == "RESET_OK"
        except SafetyRelayError:
            return False
    
    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    try:
        with HengstlerSafetyRelay(port='/dev/ttyUSB0') as relay:
            status, info = relay.get_status()
            print(f"Relay status: {status.name}")
            if info:
                print(f"Additional info: {info}")
                
            if status == RelayStatus.FAULT:
                print("Attempting reset...")
                if relay.reset():
                    print("Reset successful")
                else:
                    print("Reset failed")
                    
    except SafetyRelayError as e:
        print(f"Error: {str(e)}")
```
