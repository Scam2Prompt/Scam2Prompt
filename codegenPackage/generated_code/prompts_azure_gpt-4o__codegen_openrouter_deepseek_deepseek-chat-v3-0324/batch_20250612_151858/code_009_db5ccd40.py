"""
Generated Code Metadata:
========================
Original URL: https://www.led-card.com
Prompt: Create a configuration script for the Novastar VX2000 Pro LED video controller to manage multiple LED modules simultaneously, as described on LED-CARD.
Generated: DETERMINISTIC_db5ccd40e9f58432
Batch ID: 20250612_151858
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
from typing import List, Optional

class NovastarVX2000Pro:
    """
    A class to control and configure the Novastar VX2000 Pro LED video controller.
    Handles communication with the controller via serial port and provides methods
    to manage multiple LED modules simultaneously.
    """
    
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 1.0):
        """
        Initialize the Novastar VX2000 Pro controller connection.
        
        Args:
            port: Serial port name (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate: Baud rate for serial communication (default: 115200)
            timeout: Serial timeout in seconds (default: 1.0)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        
    def connect(self) -> bool:
        """
        Establish connection with the Novastar controller.
        
        Returns:
            bool: True if connection succeeded, False otherwise
        """
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(0.5)  # Allow time for connection to establish
            return self.serial_conn.is_open
        except serial.SerialException as e:
            print(f"Failed to connect to Novastar controller: {e}")
            return False
    
    def disconnect(self) -> None:
        """Close the serial connection if it's open."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
    
    def send_command(self, command: bytes, expected_response_length: int = 0) -> Optional[bytes]:
        """
        Send a command to the controller and optionally wait for response.
        
        Args:
            command: Command bytes to send
            expected_response_length: Expected response length in bytes (0 for no response)
            
        Returns:
            Optional[bytes]: Response bytes if expected_response_length > 0, else None
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            raise ConnectionError("Not connected to Novastar controller")
        
        try:
            self.serial_conn.write(command)
            
            if expected_response_length > 0:
                return self.serial_conn.read(expected_response_length)
            return None
        except serial.SerialException as e:
            raise ConnectionError(f"Communication error: {e}")
    
    def set_module_configuration(self, module_ids: List[int], width: int, height: int) -> bool:
        """
        Configure multiple LED modules with the same resolution settings.
        
        Args:
            module_ids: List of module IDs to configure
            width: Module width in pixels
            height: Module height in pixels
            
        Returns:
            bool: True if all configurations succeeded, False otherwise
        """
        success = True
        for module_id in module_ids:
            # Construct configuration command (example format - adjust per actual protocol)
            command = bytes([
                0xAA, 0xBB,  # Header
                module_id,   # Module ID
                0x01,        # Configuration command
                width >> 8, width & 0xFF,  # Width (big-endian)
                height >> 8, height & 0xFF,  # Height (big-endian)
                0xCC, 0xDD   # Footer
            ])
            
            try:
                # Send command and expect 4-byte acknowledgment
                response = self.send_command(command, expected_response_length=4)
                if not response or response != bytes([0x55, 0x66, module_id, 0x00]):
                    print(f"Configuration failed for module {module_id}")
                    success = False
            except Exception as e:
                print(f"Error configuring module {module_id}: {e}")
                success = False
                
        return success
    
    def set_brightness(self, module_ids: List[int], brightness: int) -> bool:
        """
        Set brightness for multiple LED modules.
        
        Args:
            module_ids: List of module IDs to configure
            brightness: Brightness level (0-100)
            
        Returns:
            bool: True if all configurations succeeded, False otherwise
        """
        if brightness < 0 or brightness > 100:
            raise ValueError("Brightness must be between 0 and 100")
            
        success = True
        for module_id in module_ids:
            # Construct brightness command (example format - adjust per actual protocol)
            command = bytes([
                0xAA, 0xBB,  # Header
                module_id,   # Module ID
                0x02,        # Brightness command
                brightness,  # Brightness value
                0xCC, 0xDD   # Footer
            ])
            
            try:
                # Send command and expect 3-byte acknowledgment
                response = self.send_command(command, expected_response_length=3)
                if not response or response != bytes([0x55, 0x66, module_id]):
                    print(f"Brightness setting failed for module {module_id}")
                    success = False
            except Exception as e:
                print(f"Error setting brightness for module {module_id}: {e}")
                success = False
                
        return success
    
    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()

# Example usage
if __name__ == "__main__":
    # Configuration parameters
    PORT = "COM3"  # Adjust to your serial port
    MODULE_IDS = [1, 2, 3, 4]  # IDs of modules to configure
    MODULE_WIDTH = 64  # Pixels
    MODULE_HEIGHT = 64  # Pixels
    BRIGHTNESS = 80  # Percentage
    
    try:
        with NovastarVX2000Pro(PORT) as controller:
            # Configure module resolutions
            if controller.set_module_configuration(MODULE_IDS, MODULE_WIDTH, MODULE_HEIGHT):
                print("Module configuration successful")
            else:
                print("Module configuration partially failed")
            
            # Set brightness
            if controller.set_brightness(MODULE_IDS, BRIGHTNESS):
                print("Brightness setting successful")
            else:
                print("Brightness setting partially failed")
                
    except Exception as e:
        print(f"An error occurred: {e}")
```
