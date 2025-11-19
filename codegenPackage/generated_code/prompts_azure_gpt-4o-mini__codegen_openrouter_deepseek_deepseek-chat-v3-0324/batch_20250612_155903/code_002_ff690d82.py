"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Write a Python script to automate the operation of an Electric Tube Expansion Model Drive EDB-1, including safety checks based on the features listed on the DBX Tools website.
Generated: DETERMINISTIC_ff690d82c8ebbbde
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from enum import Enum, auto
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('EDB-1_Driver')

class DriveState(Enum):
    """Enum representing possible drive states."""
    IDLE = auto()
    RUNNING = auto()
    ERROR = auto()
    EMERGENCY_STOP = auto()

class ExpansionMode(Enum):
    """Enum representing expansion modes."""
    MANUAL = auto()
    AUTOMATIC = auto()
    SEMI_AUTOMATIC = auto()

class SafetyCheckError(Exception):
    """Custom exception for safety check failures."""
    pass

class EDB1Driver:
    """
    Class to control the Electric Tube Expansion Model Drive EDB-1.
    Implements safety checks and operational controls based on DBX Tools specifications.
    """
    
    def __init__(self):
        """Initialize the drive with default parameters."""
        self.state = DriveState.IDLE
        self.current_pressure = 0.0  # psi
        self.max_pressure = 150.0  # psi (from specifications)
        self.temperature = 25.0  # °C
        self.max_temperature = 80.0  # °C (from specifications)
        self.expansion_mode = ExpansionMode.MANUAL
        self.emergency_stop_engaged = False
        self.last_maintenance_time = time.time()
        
    def _check_safety_conditions(self) -> Tuple[bool, str]:
        """
        Perform all safety checks before any operation.
        
        Returns:
            Tuple[bool, str]: (True, "") if safe, (False, error_message) if unsafe
        """
        if self.emergency_stop_engaged:
            return (False, "Emergency stop is engaged")
        
        if self.current_pressure > self.max_pressure:
            return (False, f"Pressure {self.current_pressure} exceeds maximum {self.max_pressure} psi")
            
        if self.temperature > self.max_temperature:
            return (False, f"Temperature {self.temperature} exceeds maximum {self.max_temperature} °C")
            
        if time.time() - self.last_maintenance_time > 2592000:  # 30 days in seconds
            return (False, "Maintenance overdue (30 days)")
            
        return (True, "")
    
    def set_pressure(self, pressure: float) -> None:
        """
        Set the working pressure of the drive.
        
        Args:
            pressure: Desired pressure in psi
            
        Raises:
            SafetyCheckError: If safety checks fail
            ValueError: If pressure is negative
        """
        if pressure < 0:
            raise ValueError("Pressure cannot be negative")
            
        safe, msg = self._check_safety_conditions()
        if not safe:
            raise SafetyCheckError(f"Cannot set pressure: {msg}")
            
        self.current_pressure = pressure
        logger.info(f"Pressure set to {pressure} psi")
    
    def set_expansion_mode(self, mode: ExpansionMode) -> None:
        """
        Set the expansion mode of the drive.
        
        Args:
            mode: ExpansionMode enum value
            
        Raises:
            SafetyCheckError: If safety checks fail
        """
        safe, msg = self._check_safety_conditions()
        if not safe:
            raise SafetyCheckError(f"Cannot change mode: {msg}")
            
        self.expansion_mode = mode
        logger.info(f"Expansion mode set to {mode.name}")
    
    def start_expansion(self) -> None:
        """
        Start the tube expansion process.
        
        Raises:
            SafetyCheckError: If safety checks fail
            RuntimeError: If already running
        """
        if self.state == DriveState.RUNNING:
            raise RuntimeError("Drive is already running")
            
        safe, msg = self._check_safety_conditions()
        if not safe:
            raise SafetyCheckError(f"Cannot start expansion: {msg}")
            
        self.state = DriveState.RUNNING
        logger.info("Expansion process started")
    
    def stop_expansion(self) -> None:
        """
        Stop the tube expansion process.
        """
        if self.state == DriveState.RUNNING:
            self.state = DriveState.IDLE
            logger.info("Expansion process stopped")
    
    def emergency_stop(self) -> None:
        """
        Immediately stop all operations and engage emergency stop.
        """
        self.state = DriveState.EMERGENCY_STOP
        self.emergency_stop_engaged = True
        self.current_pressure = 0.0
        logger.warning("EMERGENCY STOP ENGAGED")
    
    def reset_emergency_stop(self) -> None:
        """
        Reset the emergency stop condition after resolving the issue.
        
        Raises:
            SafetyCheckError: If safety checks still fail
        """
        safe, msg = self._check_safety_conditions()
        if not safe and not self.emergency_stop_engaged:
            raise SafetyCheckError(f"Cannot reset emergency stop: {msg}")
            
        self.emergency_stop_engaged = False
        self.state = DriveState.IDLE
        logger.info("Emergency stop reset")
    
    def update_temperature(self, temp: float) -> None:
        """
        Update the current temperature reading.
        
        Args:
            temp: Current temperature in °C
        """
        self.temperature = temp
        logger.debug(f"Temperature updated to {temp} °C")
    
    def perform_maintenance(self) -> None:
        """Record that maintenance was performed."""
        self.last_maintenance_time = time.time()
        logger.info("Maintenance performed and recorded")
    
    def get_status(self) -> dict:
        """
        Get current status of the drive.
        
        Returns:
            dict: Dictionary containing all status parameters
        """
        return {
            'state': self.state.name,
            'current_pressure': self.current_pressure,
            'temperature': self.temperature,
            'expansion_mode': self.expansion_mode.name,
            'emergency_stop': self.emergency_stop_engaged,
            'days_since_maintenance': (time.time() - self.last_maintenance_time) / 86400
        }

# Example usage
if __name__ == "__main__":
    try:
        drive = EDB1Driver()
        
        # Example operational sequence
        drive.set_pressure(100.0)
        drive.set_expansion_mode(ExpansionMode.AUTOMATIC)
        drive.start_expansion()
        
        # Simulate operation
        time.sleep(2)
        drive.update_temperature(45.0)
        
        # Check status
        print("Current status:", drive.get_status())
        
        # Normal stop
        drive.stop_expansion()
        
        # Emergency scenario
        drive.set_pressure(160.0)  # This should raise SafetyCheckError
        
    except (SafetyCheckError, ValueError, RuntimeError) as e:
        logger.error(f"Operation failed: {str(e)}")
        drive.emergency_stop()
```
