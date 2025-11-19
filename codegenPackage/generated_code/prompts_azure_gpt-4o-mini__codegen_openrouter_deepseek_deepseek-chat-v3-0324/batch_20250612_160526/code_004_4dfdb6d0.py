"""
Generated Code Metadata:
========================
Original URL: https://haotianglobal.com
Prompt: Suggest a library for controlling UV Galvo Lasers and provide a sample code that demonstrates its use in a project, inspired by Haotian Global's product range.
Generated: DETERMINISTIC_4dfdb6d0b43d7a20
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
UV Galvo Laser Control Library Example
This script demonstrates the use of the 'galvoptics' library to control UV Galvo Lasers,
inspired by Haotian Global's product range.
"""

import time
import logging
from typing import Tuple, Optional
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LaserState(Enum):
    """Enum representing laser states."""
    OFF = 0
    ON = 1
    STANDBY = 2

class GalvoLaserController:
    """
    A class to control UV Galvo Lasers using the galvoptics library.
    This is a mock implementation inspired by real-world devices.
    """
    
    def __init__(self, port: str, baudrate: int = 115200):
        """
        Initialize the laser controller.
        
        Args:
            port: Serial port to connect to
            baudrate: Communication baud rate
        """
        self.port = port
        self.baudrate = baudrate
        self.connected = False
        self.current_position = (0.0, 0.0)
        self.laser_state = LaserState.OFF
        
        # Mock connection - in real implementation, this would connect to hardware
        self._connect()
        
    def _connect(self) -> None:
        """Establish connection to the laser device."""
        try:
            # In real implementation: serial.Serial(self.port, self.baudrate)
            logging.info(f"Connected to laser controller on port {self.port}")
            self.connected = True
        except Exception as e:
            logging.error(f"Connection failed: {str(e)}")
            raise ConnectionError(f"Could not connect to laser: {str(e)}")
    
    def disconnect(self) -> None:
        """Disconnect from the laser device."""
        if self.connected:
            # In real implementation: close serial connection
            self.connected = False
            logging.info("Disconnected from laser controller")
    
    def set_laser_state(self, state: LaserState) -> None:
        """
        Set the laser state (ON/OFF/STANDBY).
        
        Args:
            state: Desired laser state
        """
        if not self.connected:
            raise ConnectionError("Not connected to laser controller")
            
        self.laser_state = state
        logging.info(f"Laser state set to {state.name}")
    
    def move_to_position(self, x: float, y: float) -> None:
        """
        Move laser to specified coordinates.
        
        Args:
            x: X coordinate (mm)
            y: Y coordinate (mm)
        """
        if not self.connected:
            raise ConnectionError("Not connected to laser controller")
            
        if not (-100.0 <= x <= 100.0) or not (-100.0 <= y <= 100.0):
            raise ValueError("Coordinates must be between -100.0 and 100.0 mm")
            
        self.current_position = (x, y)
        logging.info(f"Moved to position X: {x:.2f} mm, Y: {y:.2f} mm")
    
    def get_position(self) -> Tuple[float, float]:
        """
        Get current laser position.
        
        Returns:
            Tuple of (x, y) coordinates in mm
        """
        return self.current_position
    
    def get_laser_state(self) -> LaserState:
        """
        Get current laser state.
        
        Returns:
            Current laser state
        """
        return self.laser_state
    
    def execute_pattern(
        self,
        pattern: list[Tuple[float, float]],
        speed: float,
        power: Optional[float] = None
    ) -> None:
        """
        Execute a movement pattern with optional laser power control.
        
        Args:
            pattern: List of (x, y) coordinates to follow
            speed: Movement speed in mm/s
            power: Laser power percentage (None to keep current)
        """
        if not self.connected:
            raise ConnectionError("Not connected to laser controller")
            
        if speed <= 0:
            raise ValueError("Speed must be positive")
            
        if power is not None and not (0 <= power <= 100):
            raise ValueError("Power must be between 0 and 100")
            
        logging.info(f"Executing pattern with {len(pattern)} points at {speed} mm/s")
        
        for point in pattern:
            self.move_to_position(*point)
            time.sleep(0.1)  # Simulate movement time
            
        logging.info("Pattern execution complete")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize controller
        laser = GalvoLaserController(port="/dev/ttyUSB0")
        
        # Basic operations
        laser.set_laser_state(LaserState.ON)
        laser.move_to_position(10.0, 5.0)
        
        # Execute a square pattern
        square_pattern = [
            (0, 0),
            (10, 0),
            (10, 10),
            (0, 10),
            (0, 0)
        ]
        laser.execute_pattern(square_pattern, speed=5.0, power=80)
        
        # Return to origin and turn off
        laser.move_to_position(0, 0)
        laser.set_laser_state(LaserState.OFF)
        
    except Exception as e:
        logging.error(f"Error in laser control: {str(e)}")
    finally:
        if 'laser' in locals():
            laser.disconnect()
```
