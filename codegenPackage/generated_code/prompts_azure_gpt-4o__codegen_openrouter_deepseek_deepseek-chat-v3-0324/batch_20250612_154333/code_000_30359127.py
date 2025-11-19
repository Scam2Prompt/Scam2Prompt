"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write Python code to simulate the functionality of a hydraulic breaker attachment for excavators, referencing the specifications and use cases described on the PT. Fuji Metal Teknik website.
Generated: DETERMINISTIC_30359127310aba20
Batch ID: 20250612_154333
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
from typing import Optional, Tuple

class BreakerMode(Enum):
    """Enumeration for breaker operation modes."""
    IDLE = 0
    LOW_POWER = 1
    MEDIUM_POWER = 2
    HIGH_POWER = 3

class HydraulicBreaker:
    """Simulates a hydraulic breaker attachment for excavators."""
    
    def __init__(self, model: str, max_impact_energy: float, operating_pressure: float, flow_rate: float):
        """
        Initialize the hydraulic breaker with specifications.
        
        Args:
            model (str): Model name/number of the breaker.
            max_impact_energy (float): Maximum impact energy in joules.
            operating_pressure (float): Operating pressure in bar.
            flow_rate (float): Flow rate in liters per minute.
        """
        self.model = model
        self.max_impact_energy = max_impact_energy
        self.operating_pressure = operating_pressure
        self.flow_rate = flow_rate
        self.current_mode = BreakerMode.IDLE
        self.is_running = False
        self.impact_count = 0
        self.last_maintenance_impact_count = 0
        
    def start(self) -> bool:
        """Start the hydraulic breaker."""
        if self.is_running:
            print(f"Warning: {self.model} is already running.")
            return False
        self.is_running = True
        print(f"{self.model} started successfully.")
        return True
    
    def stop(self) -> bool:
        """Stop the hydraulic breaker."""
        if not self.is_running:
            print(f"Warning: {self.model} is already stopped.")
            return False
        self.is_running = False
        self.current_mode = BreakerMode.IDLE
        print(f"{self.model} stopped successfully.")
        return True
    
    def set_mode(self, mode: BreakerMode) -> bool:
        """
        Set the breaker's operation mode.
        
        Args:
            mode (BreakerMode): Desired operation mode.
            
        Returns:
            bool: True if mode was set successfully, False otherwise.
        """
        if not self.is_running:
            print(f"Error: {self.model} is not running. Cannot set mode.")
            return False
        self.current_mode = mode
        print(f"{self.model} mode set to {mode.name}.")
        return True
    
    def operate(self, duration: float) -> Tuple[int, float]:
        """
        Simulate breaker operation for a given duration.
        
        Args:
            duration (float): Operation duration in seconds.
            
        Returns:
            Tuple[int, float]: Tuple containing (impact_count, energy_consumed).
            
        Raises:
            ValueError: If duration is negative.
        """
        if duration < 0:
            raise ValueError("Duration must be a non-negative value.")
        
        if not self.is_running:
            print(f"Error: {self.model} is not running. Cannot operate.")
            return (0, 0.0)
        
        impacts_per_second = {
            BreakerMode.LOW_POWER: 5,
            BreakerMode.MEDIUM_POWER: 10,
            BreakerMode.HIGH_POWER: 20
        }.get(self.current_mode, 0)
        
        impact_count = int(impacts_per_second * duration)
        self.impact_count += impact_count
        
        energy_per_impact = {
            BreakerMode.LOW_POWER: self.max_impact_energy * 0.3,
            BreakerMode.MEDIUM_POWER: self.max_impact_energy * 0.6,
            BreakerMode.HIGH_POWER: self.max_impact_energy
        }.get(self.current_mode, 0.0)
        
        energy_consumed = impact_count * energy_per_impact
        
        print(f"{self.model} operated for {duration} seconds in {self.current_mode.name} mode.")
        print(f"Delivered {impact_count} impacts, consuming {energy_consumed:.2f} Joules.")
        
        return (impact_count, energy_consumed)
    
    def maintenance_required(self, threshold: int = 10000) -> bool:
        """
        Check if maintenance is required based on impact count.
        
        Args:
            threshold (int): Impact count threshold for maintenance.
            
        Returns:
            bool: True if maintenance is required, False otherwise.
        """
        delta = self.impact_count - self.last_maintenance_impact_count
        return delta >= threshold
    
    def perform_maintenance(self) -> None:
        """Perform maintenance and reset impact counter."""
        self.last_maintenance_impact_count = self.impact_count
        print(f"Maintenance performed on {self.model}. Impact counter reset.")
    
    def get_status(self) -> dict:
        """Return current status of the breaker as a dictionary."""
        return {
            "model": self.model,
            "is_running": self.is_running,
            "current_mode": self.current_mode.name,
            "total_impacts": self.impact_count,
            "impacts_since_maintenance": self.impact_count - self.last_maintenance_impact_count,
            "max_impact_energy": self.max_impact_energy,
            "operating_pressure": self.operating_pressure,
            "flow_rate": self.flow_rate
        }

# Example usage
if __name__ == "__main__":
    # Initialize a breaker with specifications similar to Fuji Metal Teknik models
    breaker = HydraulicBreaker(
        model="FMT-HB200",
        max_impact_energy=1500.0,
        operating_pressure=160.0,
        flow_rate=60.0
    )
    
    # Start the breaker
    breaker.start()
    
    # Set to high power mode
    breaker.set_mode(BreakerMode.HIGH_POWER)
    
    # Operate for 5 seconds
    breaker.operate(5.0)
    
    # Check status
    print("\nCurrent status:")
    for key, value in breaker.get_status().items():
        print(f"{key}: {value}")
    
    # Stop the breaker
    breaker.stop()
```
