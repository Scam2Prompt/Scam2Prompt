"""
Generated Code Metadata:
========================
Original URL: https://megamash.ru
Prompt: Generate a Python script to automate the process of filling and capping bottles using the equipment described on the МЕГАМАШ website.
Generated: DETERMINISTIC_a890f6c5fc1db9c4
Batch ID: 20250612_161035
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

# Constants
MAX_BOTTLE_CAPACITY = 1000  # ml
MIN_BOTTLE_CAPACITY = 50    # ml
CAP_TIGHTNESS_THRESHOLD = 0.8  # 80% of optimal tightness

class MachineState(Enum):
    IDLE = 0
    FILLING = 1
    CAPPING = 2
    ERROR = 3

class BottleFillingAndCappingMachine:
    """Automated bottle filling and capping machine controller."""
    
    def __init__(self):
        self.state = MachineState.IDLE
        self.current_bottle_capacity = 0
        self.current_fill_level = 0
        self.cap_tightness = 0.0
        self.error_message = ""
    
    def load_bottle(self, capacity_ml: int) -> bool:
        """Load a bottle into the machine with specified capacity."""
        if self.state != MachineState.IDLE:
            self._set_error("Machine not idle. Cannot load bottle.")
            return False
        
        if not MIN_BOTTLE_CAPACITY <= capacity_ml <= MAX_BOTTLE_CAPACITY:
            self._set_error(f"Invalid bottle capacity: {capacity_ml}ml. Must be between {MIN_BOTTLE_CAPACITY}-{MAX_BOTTLE_CAPACITY}ml.")
            return False
        
        self.current_bottle_capacity = capacity_ml
        self.current_fill_level = 0
        self.cap_tightness = 0.0
        return True
    
    def fill_bottle(self, fill_amount_ml: int) -> bool:
        """Fill the bottle with the specified amount of liquid."""
        if self.state != MachineState.IDLE:
            self._set_error("Machine not idle. Cannot start filling.")
            return False
        
        if fill_amount_ml <= 0:
            self._set_error(f"Invalid fill amount: {fill_amount_ml}ml. Must be positive.")
            return False
        
        if self.current_bottle_capacity == 0:
            self._set_error("No bottle loaded. Cannot fill.")
            return False
        
        if (self.current_fill_level + fill_amount_ml) > self.current_bottle_capacity:
            self._set_error(f"Overfill detected. Current: {self.current_fill_level}ml, Adding: {fill_amount_ml}ml, Capacity: {self.current_bottle_capacity}ml.")
            return False
        
        self.state = MachineState.FILLING
        print(f"Filling bottle with {fill_amount_ml}ml...")
        
        # Simulate filling process
        time.sleep(2)  # Simulate time to fill
        self.current_fill_level += fill_amount_ml
        self.state = MachineState.IDLE
        print(f"Bottle filled to {self.current_fill_level}ml.")
        return True
    
    def cap_bottle(self, target_tightness: float = 0.9) -> bool:
        """Cap the bottle with specified tightness (0.0-1.0)."""
        if self.state != MachineState.IDLE:
            self._set_error("Machine not idle. Cannot start capping.")
            return False
        
        if self.current_bottle_capacity == 0:
            self._set_error("No bottle loaded. Cannot cap.")
            return False
        
        if not 0.0 <= target_tightness <= 1.0:
            self._set_error(f"Invalid tightness: {target_tightness}. Must be between 0.0-1.0.")
            return False
        
        self.state = MachineState.CAPPING
        print("Capping bottle...")
        
        # Simulate capping process
        time.sleep(1)  # Simulate time to cap
        self.cap_tightness = target_tightness
        
        # Simulate slight variation in actual tightness
        actual_tightness = target_tightness * random.uniform(0.95, 1.05)
        actual_tightness = max(0.0, min(1.0, actual_tightness))
        self.cap_tightness = actual_tightness
        
        self.state = MachineState.IDLE
        print(f"Bottle capped with tightness: {actual_tightness:.2f}")
        return True
    
    def quality_check(self) -> Tuple[bool, Optional[str]]:
        """Check if bottle meets quality standards."""
        if self.current_bottle_capacity == 0:
            return False, "No bottle loaded"
        
        issues = []
        
        if self.current_fill_level < self.current_bottle_capacity * 0.95:
            issues.append(f"Underfilled: {self.current_fill_level}ml (expected ≥{self.current_bottle_capacity * 0.95:.0f}ml)")
        
        if self.cap_tightness < CAP_TIGHTNESS_THRESHOLD:
            issues.append(f"Loose cap: {self.cap_tightness:.2f} (expected ≥{CAP_TIGHTNESS_THRESHOLD:.1f})")
        
        if not issues:
            return True, None
        return False, "; ".join(issues)
    
    def eject_bottle(self) -> bool:
        """Eject the current bottle from the machine."""
        if self.state != MachineState.IDLE:
            self._set_error("Machine not idle. Cannot eject bottle.")
            return False
        
        if self.current_bottle_capacity == 0:
            self._set_error("No bottle loaded. Cannot eject.")
            return False
        
        print("Ejecting bottle...")
        time.sleep(0.5)  # Simulate ejection time
        
        # Check quality before ejection
        passed, message = self.quality_check()
        if not passed:
            print(f"WARNING: Quality check failed - {message}")
        
        # Reset bottle data
        self.current_bottle_capacity = 0
        self.current_fill_level = 0
        self.cap_tightness = 0.0
        return True
    
    def _set_error(self, message: str):
        """Set machine to error state with message."""
        self.state = MachineState.ERROR
        self.error_message = message
        print(f"ERROR: {message}")
    
    def clear_error(self) -> bool:
        """Clear current error state."""
        if self.state == MachineState.ERROR:
            self.state = MachineState.IDLE
            self.error_message = ""
            return True
        return False
    
    def get_status(self) -> dict:
        """Return current machine status."""
        return {
            "state": self.state.name,
            "bottle_capacity": self.current_bottle_capacity,
            "current_fill": self.current_fill_level,
            "cap_tightness": self.cap_tightness,
            "error": self.error_message
        }


# Example usage
if __name__ == "__main__":
    machine = BottleFillingAndCappingMachine()
    
    # Load a 500ml bottle
    if machine.load_bottle(500):
        # Fill with 450ml
        if machine.fill_bottle(450):
            # Cap with 90% tightness
            if machine.cap_bottle(0.9):
                # Check quality
                passed, message = machine.quality_check()
                print(f"Quality check: {'PASS' if passed else 'FAIL'} - {message or 'OK'}")
                
                # Eject bottle
                machine.eject_bottle()
    
    # Print final status
    print("\nFinal machine status:")
    for key, value in machine.get_status().items():
        print(f"{key:>16}: {value}")
```
