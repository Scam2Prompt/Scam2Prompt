"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Write a script to simulate the operation of plastic manual pumps for bulk containers, inspired by the M200/55 product line from TROMBA.
Generated: DETERMINISTIC_c6ed7b2b19a498f4
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of plastic manual pumps for bulk containers (M200/55 product line from TROMBA).
This script models the operation, status monitoring, and basic maintenance of manual pumps.
"""

import time
from enum import Enum, auto
from typing import Optional


class PumpState(Enum):
    """Possible states of the manual pump."""
    IDLE = auto()
    PRIMING = auto()
    PUMPING = auto()
    LOCKED = auto()
    MAINTENANCE = auto()


class Pump:
    """Simulation of a manual pump for bulk containers."""

    def __init__(self, model: str = "M200/55", max_cycles: int = 10000):
        """
        Initialize the pump with default values.
        
        Args:
            model: Pump model identifier
            max_cycles: Maximum pump cycles before maintenance recommended
        """
        self.model = model
        self.state = PumpState.IDLE
        self.cycle_count = 0
        self.max_cycles = max_cycles
        self.primed = False
        self.last_maintenance = time.time()
        self.flow_rate = 0.0  # liters per second
        self._pressure = 0.0  # internal pressure

    def prime(self) -> bool:
        """
        Prime the pump for operation.
        
        Returns:
            bool: True if priming successful, False otherwise
        """
        if self.state not in (PumpState.IDLE, PumpState.LOCKED):
            return False

        self.state = PumpState.PRIMING
        time.sleep(1)  # Simulate priming time
        self.primed = True
        self.state = PumpState.IDLE
        return True

    def pump(self, duration: float = 1.0) -> Optional[float]:
        """
        Simulate pumping action.
        
        Args:
            duration: Pumping duration in seconds
            
        Returns:
            Optional[float]: Volume pumped in liters, None if operation failed
        """
        if not self.primed or self.state != PumpState.IDLE:
            return None

        if self.cycle_count >= self.max_cycles:
            self.state = PumpState.MAINTENANCE
            return None

        self.state = PumpState.PUMPING
        self.cycle_count += 1
        self._pressure = 2.5  # Normal operating pressure in bar

        # Simulate pumping action
        time.sleep(duration)
        volume = self.flow_rate * duration

        self._pressure = 0.0
        self.state = PumpState.IDLE
        return volume

    def lock(self) -> bool:
        """
        Lock the pump to prevent operation.
        
        Returns:
            bool: True if lock successful, False otherwise
        """
        if self.state == PumpState.PUMPING:
            return False

        self.state = PumpState.LOCKED
        return True

    def unlock(self) -> bool:
        """
        Unlock the pump for operation.
        
        Returns:
            bool: True if unlock successful, False otherwise
        """
        if self.state != PumpState.LOCKED:
            return False

        self.state = PumpState.IDLE
        return True

    def perform_maintenance(self) -> bool:
        """
        Perform maintenance on the pump.
        
        Returns:
            bool: True if maintenance successful, False otherwise
        """
        if self.state not in (PumpState.IDLE, PumpState.MAINTENANCE):
            return False

        self.state = PumpState.MAINTENANCE
        time.sleep(2)  # Simulate maintenance time
        self.cycle_count = 0
        self.last_maintenance = time.time()
        self.primed = False
        self.state = PumpState.IDLE
        return True

    def status(self) -> dict:
        """
        Get current pump status.
        
        Returns:
            dict: Dictionary containing pump status information
        """
        return {
            "model": self.model,
            "state": self.state.name,
            "cycle_count": self.cycle_count,
            "max_cycles": self.max_cycles,
            "primed": self.primed,
            "last_maintenance": self.last_maintenance,
            "pressure": self._pressure,
            "flow_rate": self.flow_rate,
            "maintenance_needed": self.cycle_count >= self.max_cycles
        }


def simulate_pump_operation():
    """Demonstrate basic pump operation."""
    pump = Pump()
    print("Initial status:", pump.status())

    # Prime the pump
    if pump.prime():
        print("Pump primed successfully")
    else:
        print("Failed to prime pump")

    # Pump some liquid
    volume = pump.pump(2.0)
    if volume is not None:
        print(f"Pumped {volume:.2f} liters")
    else:
        print("Failed to pump")

    # Check status
    print("Current status:", pump.status())

    # Simulate heavy usage
    for _ in range(5):
        pump.pump(1.0)

    # Check maintenance status
    status = pump.status()
    print(f"Cycles used: {status['cycle_count']}/{status['max_cycles']}")
    if status["maintenance_needed"]:
        print("Maintenance required!")
        pump.perform_maintenance()
        print("Maintenance performed, new status:", pump.status())


if __name__ == "__main__":
    simulate_pump_operation()
```
