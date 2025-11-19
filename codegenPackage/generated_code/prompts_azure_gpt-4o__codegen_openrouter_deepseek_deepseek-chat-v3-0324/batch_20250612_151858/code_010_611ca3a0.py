"""
Generated Code Metadata:
========================
Original URL: https://www.led-card.com
Prompt: Provide Python code to interface with the Novastar MX30 LED display controller for real-time video processing on LED screens.
Generated: DETERMINISTIC_611ca3a008953829
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import struct
import time
from typing import Tuple, Optional

class NovastarMX30:
    """
    A class to interface with the Novastar MX30 LED display controller.
    Handles communication, video processing, and control commands.
    """
    
    def __init__(self, ip_address: str, port: int = 5200, timeout: float = 5.0):
        """
        Initialize the Novastar MX30 controller connection.
        
        Args:
            ip_address: IP address of the MX30 controller
            port: Port number (default: 5200)
            timeout: Socket timeout in seconds (default: 5.0)
        """
        self.ip_address = ip_address
        self.port = port
        self.timeout = timeout
        self.socket = None
        self.connect()
    
    def connect(self) -> None:
        """Establish a TCP connection to the MX30 controller."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.ip_address, self.port))
        except socket.error as e:
            raise ConnectionError(f"Failed to connect to MX30 at {self.ip_address}:{self.port}: {e}")
    
    def disconnect(self) -> None:
        """Close the connection to the MX30 controller."""
        if self.socket:
            try:
                self.socket.close()
            except socket.error:
                pass
            finally:
                self.socket = None
    
    def _send_command(self, command: bytes, expect_response: bool = False) -> Optional[bytes]:
        """
        Send a command to the MX30 controller and optionally wait for response.
        
        Args:
            command: Command bytes to send
            expect_response: Whether to wait for a response
            
        Returns:
            Response bytes if expect_response is True, else None
            
        Raises:
            ConnectionError: If communication fails
        """
        if not self.socket:
            raise ConnectionError("Not connected to MX30 controller")
        
        try:
            self.socket.sendall(command)
            if expect_response:
                return self._receive_response()
            return None
        except socket.error as e:
            raise ConnectionError(f"Communication error with MX30: {e}")
    
    def _receive_response(self) -> bytes:
        """
        Receive response from the MX30 controller.
        
        Returns:
            Response bytes
            
        Raises:
            ConnectionError: If response is invalid or timeout occurs
        """
        try:
            header = self.socket.recv(4)
            if len(header) != 4:
                raise ConnectionError("Invalid response header length")
            
            payload_length = struct.unpack('>I', header)[0]
            payload = self.socket.recv(payload_length)
            
            if len(payload) != payload_length:
                raise ConnectionError("Incomplete response payload")
            
            return payload
        except socket.timeout:
            raise ConnectionError("Timeout waiting for response from MX30")
        except struct.error as e:
            raise ConnectionError(f"Invalid response format: {e}")
    
    def send_video_data(self, data: bytes, x: int = 0, y: int = 0, width: int = 1920, height: int = 1080) -> None:
        """
        Send video data to the LED screen.
        
        Args:
            data: Raw video data bytes (RGB format)
            x: X coordinate of the top-left corner
            y: Y coordinate of the top-left corner
            width: Width of the video area
            height: Height of the video area
            
        Raises:
            ValueError: If parameters are invalid
            ConnectionError: If communication fails
        """
        if not (0 <= x < 65535 and 0 <= y < 65535):
            raise ValueError("Invalid coordinates")
        if not (0 < width <= 65535 and 0 < height <= 65535):
            raise ValueError("Invalid dimensions")
        if len(data) != width * height * 3:
            raise ValueError("Data size doesn't match dimensions")
        
        # Create command packet
        header = struct.pack('>IIIIII', 0x12345678, x, y, width, height, len(data))
        command = header + data
        
        try:
            self._send_command(command)
        except ConnectionError as e:
            raise ConnectionError(f"Failed to send video data: {e}")
    
    def set_brightness(self, brightness: int) -> None:
        """
        Set the brightness of the LED screen.
        
        Args:
            brightness: Brightness level (0-100)
            
        Raises:
            ValueError: If brightness is out of range
            ConnectionError: If communication fails
        """
        if not 0 <= brightness <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        
        command = struct.pack('>BB', 0x01, brightness)
        try:
            self._send_command(command)
        except ConnectionError as e:
            raise ConnectionError(f"Failed to set brightness: {e}")
    
    def get_status(self) -> Tuple[int, int, int]:
        """
        Get the current status of the controller.
        
        Returns:
            Tuple of (temperature, humidity, fan_speed)
            
        Raises:
            ConnectionError: If communication fails
        """
        command = struct.pack('>B', 0x02)
        try:
            response = self._send_command(command, expect_response=True)
            if len(response) != 12:
                raise ConnectionError("Invalid status response length")
            
            temp, hum, fan = struct.unpack('>III', response)
            return temp, hum, fan
        except ConnectionError as e:
            raise ConnectionError(f"Failed to get status: {e}")
    
    def reboot(self) -> None:
        """Reboot the controller."""
        command = struct.pack('>B', 0x03)
        try:
            self._send_command(command)
            time.sleep(5)  # Wait for reboot
            self.connect()  # Reconnect after reboot
        except ConnectionError as e:
            raise ConnectionError(f"Failed to reboot controller: {e}")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()
```
