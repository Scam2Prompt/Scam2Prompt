"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Write code to control the operation of JECO's fire crash truck, simulating its water bowser and hydraulic systems.
Generated: DETERMINISTIC_94559fdf6bad9849
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from enum import Enum, auto
from typing import Optional

class SystemStatus(Enum):
    """Enum representing the possible statuses of a system."""
    OFF = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()
    ERROR = auto()

class WaterBowser:
    """Class representing the water bowser system of the fire crash truck."""
    
    def __init__(self, capacity_liters: float):
        """
        Initialize the water bowser system.
        
        Args:
            capacity_liters: Total capacity of the water bowser in liters.
        """
        self.capacity = capacity_liters
        self.current_volume = 0.0
        self.status = SystemStatus.OFF
        self.pressure = 0.0  # in psi
        
    def start(self) -> bool:
        """Start the water bowser system."""
        if self.status != SystemStatus.OFF:
            print("Water bowser is not in OFF state. Current state:", self.status)
            return False
        
        self.status = SystemStatus.STARTING
        print("Starting water bowser...")
        
        # Simulate startup sequence
        time.sleep(2)
        self.status = SystemStatus.RUNNING
        self.pressure = 50.0  # Default operating pressure
        print("Water bowser started successfully.")
        return True
    
    def stop(self) -> bool:
        """Stop the water bowser system."""
        if self.status != SystemStatus.RUNNING:
            print("Water bowser is not running. Current state:", self.status)
            return False
        
        self.status = SystemStatus.STOPPING
        print("Stopping water bowser...")
        
        # Simulate shutdown sequence
        time.sleep(1)
        self.status = SystemStatus.OFF
        self.pressure = 0.0
        print("Water bowser stopped successfully.")
        return True
    
    def fill(self, amount_liters: float) -> bool:
        """
        Fill the water bowser with specified amount of water.
        
        Args:
            amount_liters: Amount of water to add in liters.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if self.status != SystemStatus.RUNNING:
            print("Cannot fill - water bowser is not running.")
            return False
            
        if self.current_volume + amount_liters > self.capacity:
            print(f"Cannot fill {amount_liters}L - would exceed capacity of {self.capacity}L.")
            return False
            
        self.current_volume += amount_liters
        print(f"Added {amount_liters}L of water. Current volume: {self.current_volume}/{self.capacity}L")
        return True
    
    def spray(self, flow_rate_lps: float, duration_sec: float) -> Optional[float]:
        """
        Spray water at specified flow rate for specified duration.
        
        Args:
            flow_rate_lps: Flow rate in liters per second.
            duration_sec: Duration in seconds to spray.
            
        Returns:
            Optional[float]: Amount of water sprayed in liters, or None if failed.
        """
        if self.status != SystemStatus.RUNNING:
            print("Cannot spray - water bowser is not running.")
            return None
            
        if self.pressure < 30.0:
            print(f"Cannot spray - insufficient pressure ({self.pressure} psi).")
            return None
            
        total_water = flow_rate_lps * duration_sec
        if total_water > self.current_volume:
            print(f"Cannot spray {total_water}L - only {self.current_volume}L available.")
            return None
            
        print(f"Spraying at {flow_rate_lps}L/s for {duration_sec} seconds...")
        time.sleep(duration_sec)
        self.current_volume -= total_water
        print(f"Sprayed {total_water}L. Remaining water: {self.current_volume}/{self.capacity}L")
        return total_water

class HydraulicSystem:
    """Class representing the hydraulic system of the fire crash truck."""
    
    def __init__(self, max_pressure_psi: float):
        """
        Initialize the hydraulic system.
        
        Args:
            max_pressure_psi: Maximum operating pressure in psi.
        """
        self.max_pressure = max_pressure_psi
        self.current_pressure = 0.0
        self.status = SystemStatus.OFF
        
    def start(self) -> bool:
        """Start the hydraulic system."""
        if self.status != SystemStatus.OFF:
            print("Hydraulic system is not in OFF state. Current state:", self.status)
            return False
        
        self.status = SystemStatus.STARTING
        print("Starting hydraulic system...")
        
        # Simulate startup sequence
        time.sleep(1.5)
        self.status = SystemStatus.RUNNING
        self.current_pressure = self.max_pressure * 0.8  # Start at 80% of max
        print("Hydraulic system started successfully.")
        return True
    
    def stop(self) -> bool:
        """Stop the hydraulic system."""
        if self.status != SystemStatus.RUNNING:
            print("Hydraulic system is not running. Current state:", self.status)
            return False
        
        self.status = SystemStatus.STOPPING
        print("Stopping hydraulic system...")
        
        # Simulate shutdown sequence
        time.sleep(1)
        self.status = SystemStatus.OFF
        self.current_pressure = 0.0
        print("Hydraulic system stopped successfully.")
        return True
    
    def set_pressure(self, pressure_psi: float) -> bool:
        """
        Set the hydraulic system pressure.
        
        Args:
            pressure_psi: Desired pressure in psi.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if self.status != SystemStatus.RUNNING:
            print("Cannot set pressure - hydraulic system is not running.")
            return False
            
        if pressure_psi > self.max_pressure:
            print(f"Cannot set pressure to {pressure_psi} psi - exceeds max of {self.max_pressure} psi.")
            return False
            
        self.current_pressure = pressure_psi
        print(f"Pressure set to {pressure_psi} psi.")
        return True

class FireCrashTruck:
    """Main class representing the JECO fire crash truck."""
    
    def __init__(self, water_capacity_liters: float, hydraulic_max_pressure_psi: float):
        """
        Initialize the fire crash truck.
        
        Args:
            water_capacity_liters: Capacity of the water bowser in liters.
            hydraulic_max_pressure_psi: Maximum pressure of the hydraulic system in psi.
        """
        self.water_bowser = WaterBowser(water_capacity_liters)
        self.hydraulic_system = HydraulicSystem(hydraulic_max_pressure_psi)
        
    def emergency_shutdown(self):
        """Perform an emergency shutdown of all systems."""
        print("EMERGENCY SHUTDOWN INITIATED!")
        self.water_bowser.stop()
        self.hydraulic_system.stop()
        print("All systems shut down.")

# Example usage
if __name__ == "__main__":
    # Create a fire crash truck with 10,000L water capacity and 3000 psi hydraulic system
    truck = FireCrashTruck(10000.0, 3000.0)
    
    # Start systems
    truck.hydraulic_system.start()
    truck.water_bowser.start()
    
    # Fill water bowser
    truck.water_bowser.fill(5000.0)
    
    # Set hydraulic pressure
    truck.hydraulic_system.set_pressure(2500.0)
    
    # Spray water
    truck.water_bowser.spray(20.0, 10.0)
    
    # Normal shutdown
    truck.water_bowser.stop()
    truck.hydraulic_system.stop()
```
