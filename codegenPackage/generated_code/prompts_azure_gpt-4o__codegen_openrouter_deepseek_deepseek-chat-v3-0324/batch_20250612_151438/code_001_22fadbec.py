"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Recommend a library or API to simulate the functionality of a "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m" in a home automation system, including motion detection and light control.
Generated: DETERMINISTIC_22fadbec7eddbc2f
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import Optional, Callable

class MotionSensorSimulator:
    """
    Simulates a motion sensor with light control functionality.
    Mimics the behavior of Qualitronix Qa26m presence sensor.
    """
    
    def __init__(self, motion_callback: Optional[Callable] = None, 
                 no_motion_callback: Optional[Callable] = None):
        """
        Initialize the motion sensor simulator.
        
        Args:
            motion_callback: Function to call when motion is detected
            no_motion_callback: Function to call when no motion is detected
        """
        self.motion_callback = motion_callback
        self.no_motion_callback = no_motion_callback
        self.motion_detected = False
        self.light_control_enabled = True
        
    def detect_motion(self) -> bool:
        """
        Simulate motion detection with random events.
        
        Returns:
            bool: True if motion is detected, False otherwise
        """
        # 30% chance of motion detection in each check
        self.motion_detected = random.random() < 0.3
        
        if self.motion_detected and self.motion_callback:
            self.motion_callback()
        elif not self.motion_detected and self.no_motion_callback:
            self.no_motion_callback()
            
        return self.motion_detected
    
    def control_light(self, turn_on: bool) -> None:
        """
        Simulate light control based on motion detection.
        
        Args:
            turn_on: Whether to turn the light on or off
        """
        if not self.light_control_enabled:
            return
            
        if turn_on:
            print("Light turned ON - Motion detected")
        else:
            print("Light turned OFF - No motion")
    
    def enable_light_control(self, enable: bool) -> None:
        """
        Enable or disable automatic light control.
        
        Args:
            enable: True to enable, False to disable
        """
        self.light_control_enabled = enable
        print(f"Light control {'enabled' if enable else 'disabled'}")


# Example usage
if __name__ == "__main__":
    def on_motion_detected():
        print("Motion detected!")
        sensor.control_light(True)
    
    def on_no_motion():
        print("No motion detected")
        sensor.control_light(False)
    
    sensor = MotionSensorSimulator(on_motion_detected, on_no_motion)
    
    try:
        while True:
            sensor.detect_motion()
            time.sleep(2)  # Check every 2 seconds
    except KeyboardInterrupt:
        print("\nSensor simulation stopped")
```
