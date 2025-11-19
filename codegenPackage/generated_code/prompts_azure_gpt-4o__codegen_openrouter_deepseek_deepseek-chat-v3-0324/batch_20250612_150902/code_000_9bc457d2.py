"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Write Python code to simulate the operation of a KPX蓄电池供电平车, including battery power management and movement control on a factory floor.
Generated: DETERMINISTIC_9bc457d27d3b6302
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
import random
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, Tuple


class BatteryStatus(Enum):
    """Enum representing battery charge status."""
    CHARGING = auto()
    DISCHARGING = auto()
    FULL = auto()
    EMPTY = auto()


class MovementDirection(Enum):
    """Enum representing movement directions."""
    FORWARD = auto()
    BACKWARD = auto()
    LEFT = auto()
    RIGHT = auto()
    STOPPED = auto()


@dataclass
class Battery:
    """Class representing the battery system."""
    capacity: float  # in kWh
    current_charge: float  # in kWh
    charge_rate: float  # kWh per hour when charging
    discharge_rate: float  # kWh per hour when moving
    status: BatteryStatus

    def charge(self, hours: float) -> None:
        """Charge the battery for given hours."""
        if self.status == BatteryStatus.FULL:
            return

        self.status = BatteryStatus.CHARGING
        charge_amount = self.charge_rate * hours
        self.current_charge = min(self.capacity, self.current_charge + charge_amount)
        
        if self.current_charge >= self.capacity:
            self.status = BatteryStatus.FULL
            self.current_charge = self.capacity

    def discharge(self, hours: float) -> None:
        """Discharge the battery for given hours."""
        if self.status == BatteryStatus.EMPTY:
            return

        self.status = BatteryStatus.DISCHARGING
        discharge_amount = self.discharge_rate * hours
        self.current_charge = max(0, self.current_charge - discharge_amount)
        
        if self.current_charge <= 0:
            self.status = BatteryStatus.EMPTY
            self.current_charge = 0

    def get_charge_percentage(self) -> float:
        """Get current charge percentage."""
        return (self.current_charge / self.capacity) * 100


@dataclass
class Position:
    """Class representing the cart's position."""
    x: float
    y: float


class KPXCart:
    """Class representing the KPX battery-powered cart."""
    
    def __init__(
        self,
        battery_capacity: float = 10.0,
        charge_rate: float = 2.0,
        discharge_rate: float = 1.5,
        max_speed: float = 5.0  # in km/h
    ):
        """Initialize the cart with battery and movement parameters."""
        self.battery = Battery(
            capacity=battery_capacity,
            current_charge=battery_capacity,
            charge_rate=charge_rate,
            discharge_rate=discharge_rate,
            status=BatteryStatus.FULL
        )
        self.position = Position(0.0, 0.0)
        self.direction = MovementDirection.STOPPED
        self.max_speed = max_speed
        self.is_operational = True
        self.log = []

    def move(self, direction: MovementDirection, duration: float) -> bool:
        """
        Move the cart in specified direction for given duration.
        Returns True if movement was successful, False otherwise.
        """
        if not self.is_operational:
            self._log("Cannot move - cart is not operational")
            return False

        if self.battery.status == BatteryStatus.EMPTY:
            self._log("Cannot move - battery is empty")
            return False

        self.direction = direction
        self.battery.discharge(duration)
        
        distance = self.max_speed * duration
        
        if direction == MovementDirection.FORWARD:
            self.position.y += distance
        elif direction == MovementDirection.BACKWARD:
            self.position.y -= distance
        elif direction == MovementDirection.LEFT:
            self.position.x -= distance
        elif direction == MovementDirection.RIGHT:
            self.position.x += distance
        
        self._log(f"Moved {direction.name} for {duration} hours, new position: {self.position}")
        return True

    def charge_battery(self, hours: float) -> None:
        """Charge the battery for given hours."""
        if not self.is_operational:
            self._log("Cannot charge - cart is not operational")
            return

        self.battery.charge(hours)
        self._log(f"Charged for {hours} hours, battery at {self.battery.get_charge_percentage():.1f}%")

    def emergency_stop(self) -> None:
        """Immediately stop the cart."""
        self.direction = MovementDirection.STOPPED
        self._log("Emergency stop activated")

    def get_status(self) -> dict:
        """Return current status of the cart."""
        return {
            "position": (self.position.x, self.position.y),
            "direction": self.direction.name,
            "battery_percentage": self.battery.get_charge_percentage(),
            "battery_status": self.battery.status.name,
            "operational": self.is_operational
        }

    def _log(self, message: str) -> None:
        """Internal logging method."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.log.append(log_entry)
        print(log_entry)

    def simulate_random_operation(self, hours: float = 8.0) -> None:
        """Simulate random operation for given hours (factory shift)."""
        operations = [
            (self.move, random.choice(list(MovementDirection)[:-1]), random.uniform(0.1, 1.0)),
            (self.charge_battery, random.uniform(0.5, 2.0))
        ]
        
        elapsed = 0.0
        while elapsed < hours:
            if self.battery.get_charge_percentage() < 10:
                self.charge_battery(random.uniform(0.5, 2.0))
                continue
            
            operation = random.choice(operations)
            if len(operation) == 3:  # move operation
                func, direction, duration = operation
                func(direction, duration)
            else:  # charge operation
                func, duration = operation
                func(duration)
            
            elapsed += duration
            time.sleep(0.1)  # simulate time passing


if __name__ == "__main__":
    # Example usage
    cart = KPXCart()
    print("Initial status:", cart.get_status())
    
    # Simulate a factory shift
    cart.simulate_random_operation()
    
    print("\nFinal status:")
    for key, value in cart.get_status().items():
        print(f"{key}: {value}")
    
    print("\nOperation log:")
    for entry in cart.log[-5:]:  # print last 5 log entries
        print(entry)
```
