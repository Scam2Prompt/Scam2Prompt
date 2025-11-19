"""
Generated Code Metadata:
========================
Original URL: https://www.led-card.com
Prompt: Write a code example for configuring an LED display screen using Linsn's EX901 multifunction board.
Generated: DETERMINISTIC_9cc17cbb5cacb6b0
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import serial
import time
from enum import Enum

class LEDCommand(Enum):
    """Enumeration of LED display commands"""
    SET_BRIGHTNESS = 0x10
    SET_DISPLAY_MODE = 0x11
    SET_COLOR_TEMP = 0x12
    SET_SCREEN_SIZE = 0x13
    SET_REFRESH_RATE = 0x14
    GET_STATUS = 0x20

class LEDDisplayController:
    """Controller for Linsn EX901 LED display board"""
    
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initialize the LED display controller
        
        Args:
            port (str): Serial port name (e.g., 'COM3' or '/dev/ttyUSB0')
            baudrate (int): Baud rate for communication (default: 115200)
            timeout (float): Serial timeout in seconds (default: 1)
        """
        self.serial_conn = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=timeout
        )
        
    def _send_command(self, command, data=None):
        """
        Send a command to the LED display board
        
        Args:
            command (LEDCommand): Command to send
            data (bytes, optional): Additional data for the command
            
        Returns:
            bytes: Response from the board
        """
        try:
            # Command packet structure: [STX, LEN, CMD, DATA..., ETX]
            packet = bytearray()
            packet.append(0x02)  # STX
            
            cmd_byte = command.value
            if data:
                packet.append(len(data) + 1)  # LEN
                packet.append(cmd_byte)       # CMD
                packet.extend(data)           # DATA
            else:
                packet.append(1)               # LEN
                packet.append(cmd_byte)        # CMD
            
            packet.append(0x03)  # ETX
            
            self.serial_conn.write(packet)
            time.sleep(0.1)  # Small delay for board processing
            
            # Read response
            response = self.serial_conn.read_all()
            return response
            
        except serial.SerialException as e:
            raise RuntimeError(f"Serial communication error: {str(e)}")
    
    def set_brightness(self, level):
        """
        Set display brightness level
        
        Args:
            level (int): Brightness level (0-100)
        """
        if not 0 <= level <= 100:
            raise ValueError("Brightness level must be between 0 and 100")
        
        self._send_command(LEDCommand.SET_BRIGHTNESS, bytes([level]))
    
    def set_display_mode(self, mode):
        """
        Set display mode
        
        Args:
            mode (int): Display mode (0-normal, 1-test, 2-standby)
        """
        if not 0 <= mode <= 2:
            raise ValueError("Display mode must be 0, 1, or 2")
        
        self._send_command(LEDCommand.SET_DISPLAY_MODE, bytes([mode]))
    
    def set_color_temperature(self, temp):
        """
        Set color temperature
        
        Args:
            temp (int): Color temperature (0-cold, 1-normal, 2-warm)
        """
        if not 0 <= temp <= 2:
            raise ValueError("Color temperature must be 0, 1, or 2")
        
        self._send_command(LEDCommand.SET_COLOR_TEMP, bytes([temp]))
    
    def set_screen_size(self, width, height):
        """
        Set screen resolution
        
        Args:
            width (int): Screen width in pixels
            height (int): Screen height in pixels
        """
        if width <= 0 or height <= 0:
            raise ValueError("Screen dimensions must be positive integers")
            
        data = bytes([
            (width >> 8) & 0xFF,
            width & 0xFF,
            (height >> 8) & 0xFF,
            height & 0xFF
        ])
        self._send_command(LEDCommand.SET_SCREEN_SIZE, data)
    
    def set_refresh_rate(self, rate):
        """
        Set refresh rate
        
        Args:
            rate (int): Refresh rate in Hz (60-240)
        """
        if not 60 <= rate <= 240:
            raise ValueError("Refresh rate must be between 60 and 240 Hz")
        
        self._send_command(LEDCommand.SET_REFRESH_RATE, bytes([rate]))
    
    def get_status(self):
        """
        Get current display status
        
        Returns:
            bytes: Status information from the board
        """
        return self._send_command(LEDCommand.GET_STATUS)
    
    def close(self):
        """Close the serial connection"""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize controller (replace with actual port)
        controller = LEDDisplayController(port="/dev/ttyUSB0")
        
        # Configure display settings
        controller.set_brightness(80)
        controller.set_display_mode(0)
        controller.set_color_temperature(1)
        controller.set_screen_size(1920, 1080)
        controller.set_refresh_rate(120)
        
        # Get status
        status = controller.get_status()
        print(f"Display status: {status.hex()}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        controller.close()
```
