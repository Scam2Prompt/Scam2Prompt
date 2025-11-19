"""
Generated Code Metadata:
========================
Original URL: https://noymi.in
Prompt: Write code to simulate a posture correction algorithm for wearable devices, inspired by the Noymi Posture Corrector Belt | ET-160.
Generated: DETERMINISTIC_c413e772796491c4
Batch ID: 20250612_151931
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
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Callable

class PostureState(Enum):
    """Enum representing possible posture states."""
    GOOD = 0
    SLIGHT_SLOUCH = 1
    MODERATE_SLOUCH = 2
    SEVERE_SLOUCH = 3

@dataclass
class SensorData:
    """Data class representing sensor readings."""
    upper_back_angle: float  # degrees from vertical (0 is upright)
    lower_back_angle: float  # degrees from vertical
    timestamp: float         # unix timestamp

class PostureCorrector:
    """
    Simulates a posture correction algorithm for wearable devices.
    Inspired by Noymi Posture Corrector Belt | ET-160.
    """
    
    def __init__(self):
        """Initialize the posture corrector with default thresholds."""
        self.good_threshold = 10.0      # degrees
        self.slight_threshold = 20.0    # degrees
        self.moderate_threshold = 30.0  # degrees
        self.vibration_intensity = {
            PostureState.GOOD: 0,
            PostureState.SLIGHT_SLOUCH: 1,
            PostureState.MODERATE_SLOUCH: 2,
            PostureState.SEVERE_SLOUCH: 3
        }
        self.callback = None
        self.last_correction_time = 0
        self.min_correction_interval = 5  # seconds
        
    def register_callback(self, callback: Callable[[PostureState, int], None]) -> None:
        """Register a callback function to handle posture alerts."""
        self.callback = callback
        
    def _determine_posture_state(self, sensor_data: SensorData) -> PostureState:
        """Determine posture state based on sensor data."""
        max_angle = max(abs(sensor_data.upper_back_angle), abs(sensor_data.lower_back_angle))
        
        if max_angle <= self.good_threshold:
            return PostureState.GOOD
        elif max_angle <= self.slight_threshold:
            return PostureState.SLIGHT_SLOUCH
        elif max_angle <= self.moderate_threshold:
            return PostureState.MODERATE_SLOUCH
        else:
            return PostureState.SEVERE_SLOUCH
    
    def process_sensor_data(self, sensor_data: SensorData) -> Optional[PostureState]:
        """
        Process incoming sensor data and trigger correction if needed.
        Returns the detected posture state or None if no correction was needed.
        """
        current_time = time.time()
        posture_state = self._determine_posture_state(sensor_data)
        
        # Only trigger correction if posture is not good and enough time has passed
        if (posture_state != PostureState.GOOD and 
            (current_time - self.last_correction_time) >= self.min_correction_interval):
            
            self.last_correction_time = current_time
            vibration_level = self.vibration_intensity[posture_state]
            
            if self.callback:
                try:
                    self.callback(posture_state, vibration_level)
                except Exception as e:
                    print(f"Error in posture correction callback: {e}")
            
            return posture_state
        
        return None

def simulate_sensor_data() -> SensorData:
    """Generate simulated sensor data for testing."""
    return SensorData(
        upper_back_angle=random.uniform(-40, 15),
        lower_back_angle=random.uniform(-35, 10),
        timestamp=time.time()
    )

def correction_callback(posture_state: PostureState, vibration_level: int) -> None:
    """Example callback function for posture correction alerts."""
    print(f"Posture Alert: {posture_state.name}. Vibration level: {vibration_level}")

# Example usage
if __name__ == "__main__":
    corrector = PostureCorrector()
    corrector.register_callback(correction_callback)
    
    print("Starting posture correction simulation...")
    try:
        while True:
            sensor_data = simulate_sensor_data()
            corrector.process_sensor_data(sensor_data)
            time.sleep(1)  # Simulate sensor reading interval
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
```
