"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Write Python code to simulate the operation of an air blower like the VinaRoy FB200-W for material transportation, ensuring energy efficiency and high performance.
Generated: DETERMINISTIC_fcff49ef89429e1f
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
import random
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Tuple

class BlowerState(Enum):
    """Enum representing the possible states of the air blower."""
    OFF = 0
    STARTING = 1
    RUNNING = 2
    OVERLOAD = 3
    FAULT = 4

@dataclass
class BlowerMetrics:
    """Data class to store blower performance metrics."""
    airflow_rate: float  # in CFM (cubic feet per minute)
    power_consumption: float  # in watts
    pressure: float  # in PSI
    efficiency: float  # percentage
    temperature: float  # in Celsius

class AirBlowerSimulator:
    """Simulator for VinaRoy FB200-W air blower operation."""
    
    def __init__(self):
        """Initialize the air blower simulator with default parameters."""
        self.state = BlowerState.OFF
        self.max_airflow = 200.0  # CFM
        self.max_power = 750.0  # watts
        self.nominal_pressure = 0.5  # PSI
        self.optimal_efficiency = 0.85  # 85%
        self.max_temperature = 70.0  # Celsius
        self.current_speed = 0.0  # percentage (0-100)
        self.metrics = BlowerMetrics(0.0, 0.0, 0.0, 0.0, 25.0)
        self.last_maintenance = time.time()
        self.operating_hours = 0.0
        
    def start(self) -> Tuple[bool, str]:
        """Start the air blower.
        
        Returns:
            Tuple[bool, str]: (success, message)
        """
        if self.state != BlowerState.OFF:
            return False, "Blower is already running or in fault state"
        
        self.state = BlowerState.STARTING
        self.current_speed = 0.0
        
        # Simulate startup sequence
        time.sleep(2)  # startup delay
        
        # Check for startup issues
        if random.random() < 0.02:  # 2% chance of startup failure
            self.state = BlowerState.FAULT
            return False, "Startup failed: Motor fault detected"
        
        self.state = BlowerState.RUNNING
        self._update_metrics()
        return True, "Blower started successfully"
    
    def stop(self) -> Tuple[bool, str]:
        """Stop the air blower.
        
        Returns:
            Tuple[bool, str]: (success, message)
        """
        if self.state == BlowerState.OFF:
            return False, "Blower is already off"
        
        self.state = BlowerState.OFF
        self.current_speed = 0.0
        self._reset_metrics()
        return True, "Blower stopped successfully"
    
    def set_speed(self, speed_percentage: float) -> Tuple[bool, str]:
        """Set the blower speed.
        
        Args:
            speed_percentage: Desired speed (0-100%)
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        if self.state not in (BlowerState.RUNNING, BlowerState.STARTING):
            return False, "Blower must be running to adjust speed"
        
        if not 0 <= speed_percentage <= 100:
            return False, "Speed must be between 0 and 100 percent"
        
        self.current_speed = speed_percentage
        self._update_metrics()
        
        # Check for overload conditions
        if self.metrics.power_consumption > self.max_power * 1.1:
            self.state = BlowerState.OVERLOAD
            return False, "Overload condition detected"
        
        if self.metrics.temperature > self.max_temperature:
            self.state = BlowerState.FAULT
            return False, "Overheating detected"
            
        return True, f"Speed set to {speed_percentage}%"
    
    def _update_metrics(self):
        """Update performance metrics based on current state and speed."""
        if self.state != BlowerState.RUNNING:
            self._reset_metrics()
            return
            
        # Calculate metrics based on current speed
        speed_factor = self.current_speed / 100.0
        
        # Airflow is proportional to speed
        self.metrics.airflow_rate = self.max_airflow * speed_factor
        
        # Power consumption follows a cubic relationship with speed
        self.metrics.power_consumption = self.max_power * (speed_factor ** 3)
        
        # Pressure is proportional to speed squared
        self.metrics.pressure = self.nominal_pressure * (speed_factor ** 2)
        
        # Efficiency peaks at optimal speed (around 70-80%)
        efficiency_curve = -4 * (speed_factor - 0.75)**2 + 1
        self.metrics.efficiency = self.optimal_efficiency * max(0.5, efficiency_curve)
        
        # Temperature increases with speed and runtime
        runtime_factor = min(1.0, self.operating_hours / 1000.0)
        self.metrics.temperature = 25.0 + 45.0 * speed_factor * runtime_factor
        
        # Update operating hours
        self.operating_hours += 0.1  # assuming this is called every 6 minutes
    
    def _reset_metrics(self):
        """Reset all metrics to idle values."""
        self.metrics.airflow_rate = 0.0
        self.metrics.power_consumption = 0.0
        self.metrics.pressure = 0.0
        self.metrics.efficiency = 0.0
        self.metrics.temperature = max(25.0, self.metrics.temperature - 5.0)
    
    def get_status(self) -> dict:
        """Get current status of the blower.
        
        Returns:
            dict: Dictionary containing blower status and metrics
        """
        return {
            "state": self.state.name,
            "speed": self.current_speed,
            "airflow_rate": round(self.metrics.airflow_rate, 2),
            "power_consumption": round(self.metrics.power_consumption, 2),
            "pressure": round(self.metrics.pressure, 2),
            "efficiency": round(self.metrics.efficiency * 100, 1),
            "temperature": round(self.metrics.temperature, 1),
            "operating_hours": round(self.operating_hours, 2)
        }
    
    def perform_maintenance(self) -> Tuple[bool, str]:
        """Perform maintenance on the blower.
        
        Returns:
            Tuple[bool, str]: (success, message)
        """
        if self.state != BlowerState.OFF:
            return False, "Blower must be turned off for maintenance"
        
        self.last_maintenance = time.time()
        self.operating_hours = 0.0
        return True, "Maintenance performed successfully"

# Example usage
if __name__ == "__main__":
    blower = AirBlowerSimulator()
    
    # Start the blower
    success, message = blower.start()
    print(f"Start: {success}, {message}")
    print(blower.get_status())
    
    # Set to optimal speed
    success, message = blower.set_speed(75)
    print(f"Set speed: {success}, {message}")
    print(blower.get_status())
    
    # Try setting to dangerous speed
    success, message = blower.set_speed(110)
    print(f"Set speed: {success}, {message}")
    
    # Stop the blower
    success, message = blower.stop()
    print(f"Stop: {success}, {message}")
    print(blower.get_status())
```
