"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: Provide code examples for interfacing with frequency converters like Vacon or Variodyn for elevator systems, as highlighted on Simice-TEC-Elevators.
Generated: DETERMINISTIC_d505c47167a7288f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Frequency Converter Interface for Elevator Systems
# Supports Vacon and Variodyn converters

import serial
import time
from enum import Enum
from typing import Optional, Union

class ConverterType(Enum):
    VACON = 1
    VARIODYN = 2

class FrequencyConverterError(Exception):
    """Base exception for frequency converter errors"""
    pass

class CommunicationError(FrequencyConverterError):
    """Raised when communication with converter fails"""
    pass

class InvalidParameterError(FrequencyConverterError):
    """Raised when an invalid parameter is provided"""
    pass

class FrequencyConverter:
    def __init__(self, port: str, baudrate: int = 9600, converter_type: ConverterType = ConverterType.VACON):
        """
        Initialize frequency converter interface
        
        Args:
            port: Serial port name (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate: Communication baud rate (default: 9600)
            converter_type: Type of frequency converter (VACON or VARIODYN)
        """
        self.port = port
        self.baudrate = baudrate
        self.converter_type = converter_type
        self.serial_conn = None
        
    def connect(self) -> None:
        """Establish connection with the frequency converter"""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1
            )
            time.sleep(0.1)  # Allow time for connection to establish
        except serial.SerialException as e:
            raise CommunicationError(f"Failed to connect to converter: {str(e)}")
    
    def disconnect(self) -> None:
        """Close the connection with the frequency converter"""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
    
    def send_command(self, command: str) -> str:
        """
        Send a command to the frequency converter and return the response
        
        Args:
            command: Command string to send to the converter
            
        Returns:
            Response from the converter
            
        Raises:
            CommunicationError: If communication fails
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            raise CommunicationError("Not connected to converter")
        
        try:
            self.serial_conn.write((command + '\r').encode())
            time.sleep(0.1)  # Wait for response
            response = self.serial_conn.read_all().decode().strip()
            return response
        except serial.SerialException as e:
            raise CommunicationError(f"Communication error: {str(e)}")
    
    def set_frequency(self, frequency: float) -> None:
        """
        Set the output frequency of the converter
        
        Args:
            frequency: Desired frequency in Hz
            
        Raises:
            InvalidParameterError: If frequency is out of range
            CommunicationError: If command fails
        """
        if frequency < 0 or frequency > 50:  # Typical elevator motor range
            raise InvalidParameterError("Frequency must be between 0 and 50 Hz")
            
        if self.converter_type == ConverterType.VACON:
            response = self.send_command(f"FREQ {frequency:.2f}")
            if "OK" not in response:
                raise CommunicationError(f"Failed to set frequency: {response}")
        elif self.converter_type == ConverterType.VARIODYN:
            response = self.send_command(f"SETF {frequency:.2f}")
            if not response.startswith("ACK"):
                raise CommunicationError(f"Failed to set frequency: {response}")
    
    def get_frequency(self) -> float:
        """
        Get the current output frequency of the converter
        
        Returns:
            Current frequency in Hz
            
        Raises:
            CommunicationError: If command fails
        """
        if self.converter_type == ConverterType.VACON:
            response = self.send_command("GETF")
            try:
                return float(response.split('=')[1].strip())
            except (IndexError, ValueError) as e:
                raise CommunicationError(f"Failed to parse frequency: {response}")
        elif self.converter_type == ConverterType.VARIODYN:
            response = self.send_command("READF")
            try:
                return float(response.split(':')[1].strip())
            except (IndexError, ValueError) as e:
                raise CommunicationError(f"Failed to parse frequency: {response}")
    
    def start_motor(self) -> None:
        """Start the motor"""
        if self.converter_type == ConverterType.VACON:
            response = self.send_command("START")
            if "OK" not in response:
                raise CommunicationError(f"Failed to start motor: {response}")
        elif self.converter_type == ConverterType.VARIODYN:
            response = self.send_command("RUN")
            if not response.startswith("ACK"):
                raise CommunicationError(f"Failed to start motor: {response}")
    
    def stop_motor(self) -> None:
        """Stop the motor"""
        if self.converter_type == ConverterType.VACON:
            response = self.send_command("STOP")
            if "OK" not in response:
                raise CommunicationError(f"Failed to stop motor: {response}")
        elif self.converter_type == ConverterType.VARIODYN:
            response = self.send_command("HALT")
            if not response.startswith("ACK"):
                raise CommunicationError(f"Failed to stop motor: {response}")
    
    def get_status(self) -> dict:
        """
        Get the current status of the converter
        
        Returns:
            Dictionary containing status information
            
        Raises:
            CommunicationError: If command fails
        """
        status = {}
        
        if self.converter_type == ConverterType.VACON:
            response = self.send_command("STATUS")
            try:
                parts = response.split(',')
                status['running'] = parts[0].strip() == "RUN"
                status['frequency'] = float(parts[1].split('=')[1].strip())
                status['current'] = float(parts[2].split('=')[1].strip())
                status['voltage'] = float(parts[3].split('=')[1].strip())
            except (IndexError, ValueError) as e:
                raise CommunicationError(f"Failed to parse status: {response}")
                
        elif self.converter_type == ConverterType.VARIODYN:
            response = self.send_command("STAT")
            try:
                parts = response.split('|')
                status['running'] = parts[0].strip() == "1"
                status['frequency'] = float(parts[1].strip())
                status['current'] = float(parts[2].strip())
                status['voltage'] = float(parts[3].strip())
            except (IndexError, ValueError) as e:
                raise CommunicationError(f"Failed to parse status: {response}")
        
        return status

# Example usage
if __name__ == "__main__":
    try:
        # Example for Vacon converter
        with FrequencyConverter(port='/dev/ttyUSB0', converter_type=ConverterType.VACON) as converter:
            converter.set_frequency(30.0)
            print(f"Current frequency: {converter.get_frequency()} Hz")
            converter.start_motor()
            print("Motor started")
            print("Status:", converter.get_status())
            time.sleep(2)
            converter.stop_motor()
            print("Motor stopped")
            
        # Example for Variodyn converter
        with FrequencyConverter(port='COM3', converter_type=ConverterType.VARIODYN) as converter:
            converter.set_frequency(25.0)
            print(f"Current frequency: {converter.get_frequency()} Hz")
            converter.start_motor()
            print("Motor started")
            print("Status:", converter.get_status())
            time.sleep(2)
            converter.stop_motor()
            print("Motor stopped")
            
    except FrequencyConverterError as e:
        print(f"Error: {str(e)}")
```
