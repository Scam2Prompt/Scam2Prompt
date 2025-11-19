"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Provide an example of a project using the Brother CV3550 Coverstitch machine and how to set it up programmatically.
Generated: DETERMINISTIC_70b6a8b0169f615a
Batch ID: 20250612_155137
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
from typing import Optional, List

class BrotherCV3550Controller:
    """
    A controller class for the Brother CV3550 Coverstitch machine.
    This class provides methods to programmatically control the machine via serial communication.
    """
    
    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        """
        Initialize the Brother CV3550 controller with serial connection parameters.
        
        Args:
            port: The serial port to connect to (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate: The baud rate for serial communication (default: 9600)
            timeout: The timeout for serial operations in seconds (default: 1.0)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        
    def connect(self) -> bool:
        """
        Establish a connection to the Brother CV3550 machine.
        
        Returns:
            bool: True if connection was successful, False otherwise
        """
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(2)  # Allow time for connection to stabilize
            return True
        except serial.SerialException as e:
            print(f"Failed to connect to Brother CV3550: {e}")
            return False
            
    def disconnect(self) -> None:
        """Close the connection to the Brother CV3550 machine."""
        if self.connection and self.connection.is_open:
            self.connection.close()
            
    def send_command(self, command: str) -> Optional[str]:
        """
        Send a command to the Brother CV3550 machine and return the response.
        
        Args:
            command: The command string to send to the machine
            
        Returns:
            Optional[str]: The response from the machine, or None if there was an error
        """
        if not self.connection or not self.connection.is_open:
            print("Error: Not connected to Brother CV3550")
            return None
            
        try:
            self.connection.write((command + '\r\n').encode('ascii'))
            time.sleep(0.1)  # Small delay for command processing
            response = self.connection.read_all().decode('ascii').strip()
            return response
        except serial.SerialException as e:
            print(f"Error sending command to Brother CV3550: {e}")
            return None
            
    def set_stitch_pattern(self, pattern_id: int) -> bool:
        """
        Set the stitch pattern on the Brother CV3550 machine.
        
        Args:
            pattern_id: The ID of the stitch pattern to set (1-10)
            
        Returns:
            bool: True if the command was successful, False otherwise
        """
        if pattern_id < 1 or pattern_id > 10:
            print("Error: Pattern ID must be between 1 and 10")
            return False
            
        response = self.send_command(f"PATTERN {pattern_id}")
        return response == "OK"
        
    def set_thread_tension(self, needle: int, tension: int) -> bool:
        """
        Set the thread tension for a specific needle.
        
        Args:
            needle: The needle number (1-3)
            tension: The tension value (1-9)
            
        Returns:
            bool: True if the command was successful, False otherwise
        """
        if needle < 1 or needle > 3:
            print("Error: Needle must be between 1 and 3")
            return False
            
        if tension < 1 or tension > 9:
            print("Error: Tension must be between 1 and 9")
            return False
            
        response = self.send_command(f"TENSION {needle} {tension}")
        return response == "OK"
        
    def start_sewing(self, speed: int = 50) -> bool:
        """
        Start the sewing process with the specified speed.
        
        Args:
            speed: The sewing speed (1-100)
            
        Returns:
            bool: True if the command was successful, False otherwise
        """
        if speed < 1 or speed > 100:
            print("Error: Speed must be between 1 and 100")
            return False
            
        response = self.send_command(f"START {speed}")
        return response == "OK"
        
    def stop_sewing(self) -> bool:
        """
        Stop the sewing process.
        
        Returns:
            bool: True if the command was successful, False otherwise
        """
        response = self.send_command("STOP")
        return response == "OK"
        
    def get_status(self) -> Optional[List[str]]:
        """
        Get the current status of the Brother CV3550 machine.
        
        Returns:
            Optional[List[str]]: A list of status messages, or None if there was an error
        """
        response = self.send_command("STATUS")
        if response and response.startswith("STATUS:"):
            return response[7:].split(';')
        return None

# Example usage
if __name__ == "__main__":
    # Initialize the controller (adjust port as needed)
    controller = BrotherCV3550Controller(port="/dev/ttyUSB0")
    
    try:
        # Connect to the machine
        if not controller.connect():
            raise RuntimeError("Failed to connect to Brother CV3550")
            
        # Set up the machine
        if not controller.set_stitch_pattern(3):
            raise RuntimeError("Failed to set stitch pattern")
            
        if not controller.set_thread_tension(needle=1, tension=5):
            raise RuntimeError("Failed to set thread tension")
            
        # Start sewing
        if not controller.start_sewing(speed=60):
            raise RuntimeError("Failed to start sewing")
            
        # Let it sew for 5 seconds
        time.sleep(5)
        
        # Stop sewing
        if not controller.stop_sewing():
            raise RuntimeError("Failed to stop sewing")
            
        # Get status
        status = controller.get_status()
        if status:
            print("Machine Status:", status)
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Always disconnect when done
        controller.disconnect()
```
