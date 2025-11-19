"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Write a Python script to control a quadcopter drone for aerial photography, considering the independent variation of rotor speeds for thrust and control.
Generated: DETERMINISTIC_bf923cf7fac90248
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import math
from typing import Tuple, Optional
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class DroneState:
    """Represents the current state of the drone."""
    altitude: float = 0.0
    pitch: float = 0.0
    roll: float = 0.0
    yaw: float = 0.0
    battery_level: float = 100.0
    is_armed: bool = False

class QuadcopterController:
    """Main controller class for quadcopter drone operations."""
    
    def __init__(self):
        """Initialize the quadcopter controller."""
        self.state = DroneState()
        self.rotor_speeds = [0.0, 0.0, 0.0, 0.0]  # FrontLeft, FrontRight, RearLeft, RearRight
        self.max_thrust = 100.0  # Maximum rotor speed percentage
        self.min_thrust = 0.0    # Minimum rotor speed percentage
        self.camera_angle = 0.0  # Camera tilt angle in degrees
        
    def arm(self) -> bool:
        """Arm the drone motors."""
        if self.state.is_armed:
            logger.warning("Drone is already armed")
            return False
        
        if self.state.battery_level < 20.0:
            logger.error("Battery level too low to arm")
            return False
            
        logger.info("Arming drone motors")
        self.state.is_armed = True
        return True
    
    def disarm(self) -> bool:
        """Disarm the drone motors."""
        if not self.state.is_armed:
            logger.warning("Drone is already disarmed")
            return False
            
        logger.info("Disarming drone motors")
        self.state.is_armed = False
        self._set_all_rotor_speeds(0.0)
        return True
    
    def takeoff(self, target_altitude: float) -> bool:
        """Execute takeoff procedure to reach target altitude."""
        if not self.state.is_armed:
            logger.error("Cannot takeoff - drone is not armed")
            return False
            
        if target_altitude <= 0:
            logger.error("Invalid target altitude")
            return False
            
        logger.info(f"Taking off to {target_altitude} meters")
        
        try:
            climb_rate = 0.5  # meters per second
            steps = int(target_altitude / climb_rate)
            
            for _ in range(steps):
                if not self._increase_altitude(climb_rate):
                    logger.error("Takeoff failed")
                    return False
                time.sleep(1)
                
            logger.info("Takeoff complete")
            return True
            
        except Exception as e:
            logger.error(f"Takeoff failed: {str(e)}")
            return False
    
    def land(self) -> bool:
        """Execute landing procedure."""
        if not self.state.is_armed:
            logger.error("Cannot land - drone is not armed")
            return False
            
        logger.info("Initiating landing sequence")
        
        try:
            while self.state.altitude > 0.1:
                if not self._decrease_altitude(0.2):
                    logger.error("Landing failed")
                    return False
                time.sleep(1)
                
            self.disarm()
            logger.info("Landing complete")
            return True
            
        except Exception as e:
            logger.error(f"Landing failed: {str(e)}")
            return False
    
    def move(self, pitch: float, roll: float, yaw: float, thrust: float) -> bool:
        """Control drone movement by adjusting rotor speeds."""
        if not self.state.is_armed:
            logger.error("Cannot move - drone is not armed")
            return False
            
        try:
            # Validate inputs
            if not (-30 <= pitch <= 30):
                raise ValueError("Pitch out of range (-30 to 30 degrees)")
            if not (-30 <= roll <= 30):
                raise ValueError("Roll out of range (-30 to 30 degrees)")
            if not (-180 <= yaw <= 180):
                raise ValueError("Yaw out of range (-180 to 180 degrees)")
            if not (0 <= thrust <= self.max_thrust):
                raise ValueError(f"Thrust out of range (0 to {self.max_thrust})")
            
            # Calculate rotor speeds for movement
            front_left = thrust + roll - pitch + yaw
            front_right = thrust - roll - pitch - yaw
            rear_left = thrust + roll + pitch + yaw
            rear_right = thrust - roll + pitch - yaw
            
            # Constrain rotor speeds
            self.rotor_speeds = [
                max(self.min_thrust, min(self.max_thrust, front_left)),
                max(self.min_thrust, min(self.max_thrust, front_right)),
                max(self.min_thrust, min(self.max_thrust, rear_left)),
                max(self.min_thrust, min(self.max_thrust, rear_right))
            ]
            
            # Update drone state
            self.state.pitch = pitch
            self.state.roll = roll
            self.state.yaw = yaw
            
            logger.debug(f"Movement command executed - Rotor speeds: {self.rotor_speeds}")
            return True
            
        except ValueError as ve:
            logger.error(f"Invalid movement parameters: {str(ve)}")
            return False
        except Exception as e:
            logger.error(f"Movement failed: {str(e)}")
            return False
    
    def capture_photo(self) -> bool:
        """Capture a photo using the drone's camera."""
        if not self.state.is_armed:
            logger.error("Cannot capture photo - drone is not armed")
            return False
            
        logger.info("Capturing photo")
        # Simulate photo capture
        time.sleep(1)
        logger.info("Photo captured")
        return True
    
    def set_camera_angle(self, angle: float) -> bool:
        """Set the camera tilt angle."""
        if not -90 <= angle <= 90:
            logger.error("Camera angle must be between -90 and 90 degrees")
            return False
            
        self.camera_angle = angle
        logger.info(f"Camera angle set to {angle} degrees")
        return True
    
    def _set_all_rotor_speeds(self, speed: float) -> None:
        """Set all rotors to the same speed."""
        self.rotor_speeds = [speed] * 4
    
    def _increase_altitude(self, amount: float) -> bool:
        """Increase altitude by specified amount."""
        if amount <= 0:
            return False
            
        # Apply equal thrust to all rotors
        self._set_all_rotor_speeds(50.0)  # Moderate thrust for ascent
        self.state.altitude += amount
        
        # Simulate battery drain
        self.state.battery_level = max(0, self.state.battery_level - 0.1)
        
        logger.debug(f"Altitude increased to {self.state.altitude:.1f}m")
        return True
    
    def _decrease_altitude(self, amount: float) -> bool:
        """Decrease altitude by specified amount."""
        if amount <= 0:
            return False
            
        # Reduce thrust to descend
        self._set_all_rotor_speeds(30.0)  # Low thrust for descent
        self.state.altitude = max(0, self.state.altitude - amount)
        
        # Simulate battery drain
        self.state.battery_level = max(0, self.state.battery_level - 0.05)
        
        logger.debug(f"Altitude decreased to {self.state.altitude:.1f}m")
        return True
    
    def get_state(self) -> DroneState:
        """Return the current drone state."""
        return self.state
    
    def emergency_stop(self) -> None:
        """Immediately stop all motors."""
        logger.warning("EMERGENCY STOP ACTIVATED")
        self._set_all_rotor_speeds(0.0)
        self.state.is_armed = False


# Example usage
if __name__ == "__main__":
    drone = QuadcopterController()
    
    try:
        # Arm the drone
        if not drone.arm():
            raise RuntimeError("Failed to arm drone")
        
        # Takeoff to 5 meters
        if not drone.takeoff(5.0):
            raise RuntimeError("Takeoff failed")
        
        # Move forward (positive pitch)
        if not drone.move(pitch=10.0, roll=0.0, yaw=0.0, thrust=60.0):
            raise RuntimeError("Movement failed")
        time.sleep(3)
        
        # Capture a photo
        if not drone.capture_photo():
            raise RuntimeError("Failed to capture photo")
        
        # Adjust camera angle
        if not drone.set_camera_angle(45.0):
            raise RuntimeError("Failed to set camera angle")
        
        # Land the drone
        if not drone.land():
