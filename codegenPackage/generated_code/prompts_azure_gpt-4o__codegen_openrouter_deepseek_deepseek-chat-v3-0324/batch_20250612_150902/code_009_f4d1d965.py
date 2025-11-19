"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Generate code for simulating the rotational movement of an electric turntable (电动转盘) used in conjunction with EVO视讯平车 systems.
Generated: DETERMINISTIC_f4d1d96544494c67
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading
from enum import Enum
from typing import Optional, Callable

class RotationDirection(Enum):
    """Enumeration for turntable rotation directions."""
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1
    STOPPED = 0

class TurntableSimulator:
    """
    Simulates the rotational movement of an electric turntable for EVO视讯平车 systems.
    
    Attributes:
        current_angle (float): Current angle of rotation in degrees (0-360)
        rotation_speed (float): Rotation speed in degrees per second
        is_running (bool): Flag indicating if turntable is rotating
        direction (RotationDirection): Current rotation direction
        on_rotation_change (Optional[Callable]): Callback for rotation updates
    """
    
    def __init__(self, rotation_speed: float = 30.0):
        """
        Initialize the turntable simulator.
        
        Args:
            rotation_speed: Rotation speed in degrees per second (default: 30)
        """
        self.current_angle = 0.0
        self.rotation_speed = rotation_speed
        self.is_running = False
        self.direction = RotationDirection.STOPPED
        self.on_rotation_change = None
        self._rotation_thread = None
        self._stop_event = threading.Event()
        
    def start_rotation(self, direction: RotationDirection) -> None:
        """
        Start rotating the turntable in specified direction.
        
        Args:
            direction: Rotation direction (CLOCKWISE/COUNTER_CLOCKWISE)
            
        Raises:
            ValueError: If invalid direction is provided
        """
        if not isinstance(direction, RotationDirection):
            raise ValueError("Invalid rotation direction")
            
        if direction == RotationDirection.STOPPED:
            self.stop_rotation()
            return
            
        if self.is_running and self.direction == direction:
            return  # Already rotating in requested direction
            
        self.stop_rotation()  # Stop any existing rotation
        self.direction = direction
        self.is_running = True
        self._stop_event.clear()
        self._rotation_thread = threading.Thread(target=self._rotate)
        self._rotation_thread.start()
        
    def stop_rotation(self) -> None:
        """Stop the turntable rotation."""
        if not self.is_running:
            return
            
        self._stop_event.set()
        if self._rotation_thread and self._rotation_thread.is_alive():
            self._rotation_thread.join()
            
        self.is_running = False
        self.direction = RotationDirection.STOPPED
        
    def _rotate(self) -> None:
        """Internal rotation thread function."""
        last_time = time.time()
        
        while not self._stop_event.is_set():
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time
            
            # Calculate angle change based on direction and speed
            angle_change = self.rotation_speed * delta_time * self.direction.value
            self.current_angle = (self.current_angle + angle_change) % 360
            
            # Notify listener if registered
            if callable(self.on_rotation_change):
                self.on_rotation_change(self.current_angle, self.direction)
                
            time.sleep(0.01)  # Prevent CPU overuse
            
    def get_current_angle(self) -> float:
        """Get current rotation angle in degrees."""
        return self.current_angle
        
    def get_rotation_status(self) -> dict:
        """Get current rotation status as a dictionary."""
        return {
            'angle': self.current_angle,
            'speed': self.rotation_speed,
            'is_running': self.is_running,
            'direction': self.direction.name
        }
        
    def __del__(self):
        """Destructor to ensure clean shutdown."""
        self.stop_rotation()


# Example usage
if __name__ == "__main__":
    def rotation_callback(angle: float, direction: RotationDirection):
        print(f"Turntable angle: {angle:.2f}°, Direction: {direction.name}")
    
    turntable = TurntableSimulator(rotation_speed=45.0)
    turntable.on_rotation_change = rotation_callback
    
    try:
        print("Starting clockwise rotation")
        turntable.start_rotation(RotationDirection.CLOCKWISE)
        time.sleep(2)
        
        print("Changing to counter-clockwise rotation")
        turntable.start_rotation(RotationDirection.COUNTER_CLOCKWISE)
        time.sleep(2)
        
        print("Stopping rotation")
        turntable.stop_rotation()
        
        print(f"Final angle: {turntable.get_current_angle():.2f}°")
        
    except KeyboardInterrupt:
        turntable.stop_rotation()
        print("Turntable stopped by user")
```
