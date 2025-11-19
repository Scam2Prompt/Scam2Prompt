"""
Generated Code Metadata:
========================
Original URL: https://biamtechintl.com
Prompt: Write code to simulate the suction and irrigation process in laparoscopic surgeries, ensuring clear operative fields as described in BIAM Tech International’s suction irrigation product details.
Generated: DETERMINISTIC_4779711e76611445
Batch ID: 20250612_152410
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
from typing import Optional, Tuple

class SuctionIrrigationState(Enum):
    """Enum representing the possible states of the suction/irrigation system."""
    IDLE = 0
    SUCTION = 1
    IRRIGATION = 2
    PAUSED = 3

class PressureLevel(Enum):
    """Enum representing pressure levels for suction/irrigation."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class SuctionIrrigationSystem:
    """
    Simulates a laparoscopic suction and irrigation system for maintaining clear operative fields.
    
    Attributes:
        current_state (SuctionIrrigationState): Current operating state
        pressure_level (PressureLevel): Current pressure level
        fluid_level (float): Current irrigation fluid level (0-100%)
        debris_level (float): Current debris level in field (0-100%)
        is_operational (bool): System operational status
    """
    
    def __init__(self):
        """Initialize the system with default values."""
        self.current_state = SuctionIrrigationState.IDLE
        self.pressure_level = PressureLevel.MEDIUM
        self.fluid_level = 100.0  # Percentage
        self.debris_level = 0.0   # Percentage
        self.is_operational = True
        
    def start_suction(self, pressure: PressureLevel = PressureLevel.MEDIUM) -> Tuple[bool, str]:
        """
        Start the suction process.
        
        Args:
            pressure: Desired pressure level
            
        Returns:
            Tuple of (success, message)
        """
        if not self.is_operational:
            return False, "System is not operational"
            
        if self.current_state != SuctionIrrigationState.IDLE:
            return False, "System is already active"
            
        self.current_state = SuctionIrrigationState.SUCTION
        self.pressure_level = pressure
        return True, f"Suction started at {pressure.name} pressure"
        
    def start_irrigation(self, pressure: PressureLevel = PressureLevel.MEDIUM) -> Tuple[bool, str]:
        """
        Start the irrigation process.
        
        Args:
            pressure: Desired pressure level
            
        Returns:
            Tuple of (success, message)
        """
        if not self.is_operational:
            return False, "System is not operational"
            
        if self.current_state != SuctionIrrigationState.IDLE:
            return False, "System is already active"
            
        if self.fluid_level <= 5.0:
            return False, "Insufficient irrigation fluid"
            
        self.current_state = SuctionIrrigationState.IRRIGATION
        self.pressure_level = pressure
        return True, f"Irrigation started at {pressure.name} pressure"
        
    def stop(self) -> Tuple[bool, str]:
        """
        Stop any active process and return to idle.
        
        Returns:
            Tuple of (success, message)
        """
        if not self.is_operational:
            return False, "System is not operational"
            
        if self.current_state == SuctionIrrigationState.IDLE:
            return False, "System is already idle"
            
        prev_state = self.current_state
        self.current_state = SuctionIrrigationState.IDLE
        return True, f"Stopped {prev_state.name} process"
        
    def pause(self) -> Tuple[bool, str]:
        """
        Pause the current process.
        
        Returns:
            Tuple of (success, message)
        """
        if not self.is_operational:
            return False, "System is not operational"
            
        if self.current_state == SuctionIrrigationState.IDLE:
            return False, "System is idle - nothing to pause"
            
        if self.current_state == SuctionIrrigationState.PAUSED:
            return False, "System is already paused"
            
        self.current_state = SuctionIrrigationState.PAUSED
        return True, "System paused"
        
    def resume(self) -> Tuple[bool, str]:
        """
        Resume a paused process.
        
        Returns:
            Tuple of (success, message)
        """
        if not self.is_operational:
            return False, "System is not operational"
            
        if self.current_state != SuctionIrrigationState.PAUSED:
            return False, "System is not paused"
            
        # Determine previous state (assuming it was either SUCTION or IRRIGATION)
        if self.debris_level > 50.0:
            self.current_state = SuctionIrrigationState.SUCTION
            return True, "Resumed suction (high debris detected)"
        else:
            self.current_state = SuctionIrrigationState.IRRIGATION
            return True, "Resumed irrigation"
            
    def refill_fluid(self, amount: float = 100.0) -> Tuple[bool, str]:
        """
        Refill the irrigation fluid.
        
        Args:
            amount: Percentage amount to refill (0-100)
            
        Returns:
            Tuple of (success, message)
        """
        if not self.is_operational:
            return False, "System is not operational"
            
        if amount <= 0 or amount > 100:
            return False, "Invalid refill amount"
            
        self.fluid_level = min(100.0, self.fluid_level + amount)
        return True, f"Fluid refilled to {self.fluid_level}%"
        
    def update_system_state(self):
        """
        Update system state based on current operation.
        Should be called periodically to simulate real-time operation.
        """
        if not self.is_operational or self.current_state == SuctionIrrigationState.IDLE:
            return
            
        if self.current_state == SuctionIrrigationState.SUCTION:
            # Suction reduces debris but also some fluid
            debris_reduction = self.pressure_level.value * 0.5
            self.debris_level = max(0.0, self.debris_level - debris_reduction)
            self.fluid_level = max(0.0, self.fluid_level - 0.1)
            
            # If debris is cleared, auto-stop
            if self.debris_level <= 1.0:
                self.stop()
                
        elif self.current_state == SuctionIrrigationState.IRRIGATION:
            # Irrigation adds fluid but may stir up some debris
            fluid_added = self.pressure_level.value * 0.3
            self.fluid_level = min(100.0, self.fluid_level + fluid_added)
            self.debris_level = min(100.0, self.debris_level + 0.05)
            
            # If fluid is full, auto-stop
            if self.fluid_level >= 99.0:
                self.stop()
                
    def simulate_surgical_environment(self):
        """
        Simulate changes in the surgical environment (debris accumulation).
        """
        # Random debris accumulation (0-2%)
        self.debris_level = min(100.0, self.debris_level + random.uniform(0.0, 2.0))
        
        # If debris reaches critical level, auto-start suction if idle
        if (self.debris_level > 30.0 and 
            self.current_state == SuctionIrrigationState.IDLE and 
            self.is_operational):
            self.start_suction()
            
    def get_status(self) -> dict:
        """
        Get current system status.
        
        Returns:
            Dictionary containing system status
        """
        return {
            "state": self.current_state.name,
            "pressure": self.pressure_level.name,
            "fluid_level": round(self.fluid_level, 1),
            "debris_level": round(self.debris_level, 1),
            "is_operational": self.is_operational
        }
        
    def emergency_stop(self):
        """Immediately stop all operations and disable system."""
        self.current_state = SuctionIrrigationState.IDLE
        self.is_operational = False
        
    def reset_system(self):
        """Reset the system to initial state."""
        self.__init__()

# Example usage
if __name__ == "__main__":
    system = SuctionIrrigationSystem()
    
    # Simulate surgical procedure
    for i in range(20):
        print(f"\n--- Cycle {i+1} ---")
        system.simulate_surgical_environment()
        system.update_system_state()
        
        # Randomly choose actions
        action = random.choice(["suction", "irrigation", "pause", "resume", "refill", "none"])
        
        if action == "suction":
            pressure = random.choice(list(PressureLevel))
            success, msg = system.start_suction(pressure)
            print(f"Action: Start suction ({pressure.name}) - {msg}")
        elif action == "irrigation":
            pressure = random.choice(list(PressureLevel))
            success, msg = system.start_irrigation(pressure)
            print(f"Action: Start irrigation ({pressure.name}) - {msg}")
        elif action == "pause":
            success, msg = system.pause()
            print(f"Action: Pause - {msg}")
        elif action == "resume":
            success, msg = system.resume()
            print(f"Action: Resume - {msg}")
        elif action == "ref
