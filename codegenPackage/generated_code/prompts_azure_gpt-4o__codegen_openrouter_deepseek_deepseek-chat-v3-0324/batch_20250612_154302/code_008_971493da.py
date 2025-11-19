"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate a Python program to model the operation of a pipe beveling machine, incorporating features of the FMOD 1500 clamping system described on the DBX Tools website.
Generated: DETERMINISTIC_971493da782bdaab
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from enum import Enum
from typing import Optional, Tuple, List

class ClampingStatus(Enum):
    """Enum representing the possible clamping statuses of the FMOD 1500 system."""
    UNCLAMPED = 0
    CLAMPING_IN_PROGRESS = 1
    CLAMPED = 2
    UNCLAMPING_IN_PROGRESS = 3
    ERROR = 4

class BevelingStatus(Enum):
    """Enum representing the possible beveling statuses."""
    IDLE = 0
    BEVELING_IN_PROGRESS = 1
    COMPLETED = 2
    ERROR = 3

class PipeBevelingMachine:
    """Model of a pipe beveling machine with FMOD 1500 clamping system."""
    
    def __init__(self):
        """Initialize the pipe beveling machine."""
        self.clamping_status = ClampingStatus.UNCLAMPED
        self.beveling_status = BevelingStatus.IDLE
        self.pipe_diameter = 0.0
        self.pipe_thickness = 0.0
        self.bevel_angle = 0.0
        self.clamping_pressure = 0.0
        self.max_clamping_pressure = 1500  # Maximum pressure in PSI for FMOD 1500
        self.safety_interlock = True
    
    def set_pipe_parameters(self, diameter: float, thickness: float) -> bool:
        """Set the pipe diameter and thickness.
        
        Args:
            diameter: Pipe diameter in mm
            thickness: Pipe wall thickness in mm
            
        Returns:
            bool: True if parameters are valid and set, False otherwise
        """
        if diameter <= 0 or thickness <= 0:
            print("Error: Pipe diameter and thickness must be positive values.")
            return False
        
        self.pipe_diameter = diameter
        self.pipe_thickness = thickness
        return True
    
    def set_bevel_angle(self, angle: float) -> bool:
        """Set the desired bevel angle.
        
        Args:
            angle: Bevel angle in degrees (0-45)
            
        Returns:
            bool: True if angle is valid and set, False otherwise
        """
        if angle < 0 or angle > 45:
            print("Error: Bevel angle must be between 0 and 45 degrees.")
            return False
        
        self.bevel_angle = angle
        return True
    
    def clamp_pipe(self, pressure: float) -> bool:
        """Simulate the clamping process of the FMOD 1500 system.
        
        Args:
            pressure: Desired clamping pressure in PSI
            
        Returns:
            bool: True if clamping initiated successfully, False otherwise
        """
        if not self.safety_interlock:
            print("Error: Safety interlock is not engaged.")
            return False
        
        if pressure <= 0 or pressure > self.max_clamping_pressure:
            print(f"Error: Clamping pressure must be between 0 and {self.max_clamping_pressure} PSI.")
            return False
        
        if self.clamping_status != ClampingStatus.UNCLAMPED:
            print("Error: Pipe is not in unclamped state.")
            return False
        
        self.clamping_status = ClampingStatus.CLAMPING_IN_PROGRESS
        self.clamping_pressure = pressure
        
        # Simulate clamping process
        time.sleep(2)  # Simulate time to clamp
        self.clamping_status = ClampingStatus.CLAMPED
        return True
    
    def unclamp_pipe(self) -> bool:
        """Simulate the unclamping process of the FMOD 1500 system.
        
        Returns:
            bool: True if unclamping initiated successfully, False otherwise
        """
        if self.clamping_status != ClampingStatus.CLAMPED:
            print("Error: Pipe is not in clamped state.")
            return False
        
        if self.beveling_status == BevelingStatus.BEVELING_IN_PROGRESS:
            print("Error: Cannot unclamp during beveling operation.")
            return False
        
        self.clamping_status = ClampingStatus.UNCLAMPING_IN_PROGRESS
        
        # Simulate unclamping process
        time.sleep(1)  # Simulate time to unclamp
        self.clamping_status = ClampingStatus.UNCLAMPED
        self.clamping_pressure = 0.0
        return True
    
    def start_beveling(self) -> bool:
        """Start the beveling process.
        
        Returns:
            bool: True if beveling started successfully, False otherwise
        """
        if self.clamping_status != ClampingStatus.CLAMPED:
            print("Error: Pipe must be clamped before beveling.")
            return False
        
        if self.bevel_angle <= 0:
            print("Error: Bevel angle must be set before beveling.")
            return False
        
        if self.beveling_status == BevelingStatus.BEVELING_IN_PROGRESS:
            print("Error: Beveling already in progress.")
            return False
        
        self.beveling_status = BevelingStatus.BEVELING_IN_PROGRESS
        
        # Simulate beveling process
        time.sleep(3)  # Simulate time to bevel
        self.beveling_status = BevelingStatus.COMPLETED
        return True
    
    def emergency_stop(self) -> None:
        """Simulate an emergency stop of the machine."""
        print("EMERGENCY STOP ACTIVATED!")
        if self.clamping_status == ClampingStatus.CLAMPING_IN_PROGRESS:
            self.clamping_status = ClampingStatus.UNCLAMPED
        elif self.clamping_status == ClampingStatus.CLAMPED:
            self.clamping_status = ClampingStatus.UNCLAMPING_IN_PROGRESS
            time.sleep(0.5)  # Simulate quick unclamping
            self.clamping_status = ClampingStatus.UNCLAMPED
        
        if self.beveling_status == BevelingStatus.BEVELING_IN_PROGRESS:
            self.beveling_status = BevelingStatus.ERROR
        
        self.clamping_pressure = 0.0
        self.safety_interlock = False
    
    def reset_machine(self) -> bool:
        """Reset the machine after an emergency stop or error.
        
        Returns:
            bool: True if reset successful, False otherwise
        """
        if self.clamping_status != ClampingStatus.UNCLAMPED:
            print("Error: Machine must be unclamped before reset.")
            return False
        
        if self.beveling_status == BevelingStatus.BEVELING_IN_PROGRESS:
            print("Error: Cannot reset during beveling operation.")
            return False
        
        self.beveling_status = BevelingStatus.IDLE
        self.safety_interlock = True
        return True
    
    def get_status(self) -> Tuple[ClampingStatus, BevelingStatus, float]:
        """Get current machine status.
        
        Returns:
            Tuple containing:
                - Current clamping status
                - Current beveling status
                - Current clamping pressure
        """
        return (self.clamping_status, self.beveling_status, self.clamping_pressure)

# Example usage
if __name__ == "__main__":
    machine = PipeBevelingMachine()
    
    # Set pipe parameters
    machine.set_pipe_parameters(100.0, 5.0)  # 100mm diameter, 5mm thickness
    machine.set_bevel_angle(30.0)  # 30 degree bevel
    
    # Clamp the pipe
    machine.clamp_pipe(1200.0)  # 1200 PSI clamping pressure
    
    # Start beveling
    machine.start_beveling()
    
    # Get status
    clamp_status, bevel_status, pressure = machine.get_status()
    print(f"Clamp Status: {clamp_status.name}, Bevel Status: {bevel_status.name}, Pressure: {pressure} PSI")
    
    # Unclamp when done
    machine.unclamp_pipe()
```
