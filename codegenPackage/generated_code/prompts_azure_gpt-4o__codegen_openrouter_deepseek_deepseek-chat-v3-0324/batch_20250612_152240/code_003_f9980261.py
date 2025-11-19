"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: Create a function to monitor tire pressure and detect abnormal losses, incorporating the advice on periodic adjustments and consequences of incorrect pressure from Neumayaa's post-sale service guidelines.
Generated: DETERMINISTIC_f9980261dfb9caf2
Batch ID: 20250612_152240
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
from dataclasses import dataclass
from typing import List, Optional

class TirePosition(Enum):
    """Enum representing the position of a tire on the vehicle."""
    FRONT_LEFT = "front_left"
    FRONT_RIGHT = "front_right"
    REAR_LEFT = "rear_left"
    REAR_RIGHT = "rear_right"

@dataclass
class TirePressureReading:
    """Data class representing a tire pressure reading."""
    position: TirePosition
    pressure: float  # in PSI
    timestamp: float  # Unix timestamp

class TirePressureMonitor:
    """
    A class to monitor tire pressure and detect abnormal losses based on Neumayaa's guidelines.
    
    Key features:
    - Tracks pressure readings over time
    - Detects abnormal pressure drops
    - Provides maintenance recommendations
    - Alerts for dangerous pressure levels
    """
    
    def __init__(
        self,
        optimal_pressure: float = 32.0,  # Default optimal pressure in PSI
        warning_threshold: float = 0.1,  # 10% drop from optimal
        critical_threshold: float = 0.25,  # 25% drop from optimal
        check_interval_hours: float = 24.0  # Default check interval
    ):
        """
        Initialize the tire pressure monitor.
        
        Args:
            optimal_pressure: Recommended tire pressure in PSI
            warning_threshold: Percentage drop to trigger warning (0-1)
            critical_threshold: Percentage drop to trigger critical alert (0-1)
            check_interval_hours: Recommended interval between checks in hours
        """
        self.optimal_pressure = optimal_pressure
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.check_interval_hours = check_interval_hours
        self.readings: List[TirePressureReading] = []
        
        # Validate thresholds
        if not 0 < warning_threshold < critical_threshold < 1:
            raise ValueError("Thresholds must be between 0 and 1, with warning < critical")
    
    def add_reading(self, position: TirePosition, pressure: float) -> None:
        """
        Add a new tire pressure reading to the monitor.
        
        Args:
            position: Position of the tire
            pressure: Current pressure reading in PSI
        """
        if pressure <= 0:
            raise ValueError("Pressure must be positive")
            
        reading = TirePressureReading(
            position=position,
            pressure=pressure,
            timestamp=time.time()
        )
        self.readings.append(reading)
    
    def get_latest_readings(self) -> List[TirePressureReading]:
        """Return the most recent reading for each tire position."""
        latest = {}
        for reading in sorted(self.readings, key=lambda x: x.timestamp, reverse=True):
            if reading.position not in latest:
                latest[reading.position] = reading
        return list(latest.values())
    
    def check_abnormal_loss(self) -> dict:
        """
        Check for abnormal pressure loss across all tires.
        
        Returns:
            dict: A dictionary with tire positions as keys and status messages as values
        """
        results = {}
        latest_readings = self.get_latest_readings()
        
        for reading in latest_readings:
            pressure_drop = (self.optimal_pressure - reading.pressure) / self.optimal_pressure
            
            if reading.pressure <= 0:
                status = "CRITICAL: Tire is completely flat"
            elif pressure_drop >= self.critical_threshold:
                status = "CRITICAL: Pressure drop exceeds safety limits"
            elif pressure_drop >= self.warning_threshold:
                status = "WARNING: Significant pressure drop detected"
            elif reading.pressure > self.optimal_pressure * 1.2:
                status = "WARNING: Overinflation detected"
            else:
                status = "Normal"
                
            results[reading.position.value] = {
                "status": status,
                "current_pressure": reading.pressure,
                "pressure_drop_percent": pressure_drop * 100,
                "recommendation": self._get_recommendation(status)
            }
        
        return results
    
    def _get_recommendation(self, status: str) -> str:
        """Get maintenance recommendation based on status."""
        recommendations = {
            "CRITICAL: Tire is completely flat": "Immediate service required. Do not drive.",
            "CRITICAL: Pressure drop exceeds safety limits": "Immediate inspection needed. Possible puncture or valve issue.",
            "WARNING: Significant pressure drop detected": "Check for leaks and inflate to recommended pressure.",
            "WARNING: Overinflation detected": "Release air to reach optimal pressure to avoid uneven wear.",
            "Normal": f"Next check recommended in {self.check_interval_hours} hours."
        }
        return recommendations.get(status, "Monitor pressure regularly.")
    
    def get_maintenance_schedule(self) -> dict:
        """Get recommended maintenance schedule based on Neumayaa's guidelines."""
        return {
            "daily": "Visual inspection for obvious deflation",
            "weekly": "Pressure check when tires are cold",
            "monthly": "Detailed inspection including valve stems and tread wear",
            "seasonal": "Pressure adjustment for temperature changes",
            "after_impact": "Immediate pressure check after hitting potholes or curbs"
        }
    
    def get_consequences(self, status: str) -> Optional[str]:
        """Get potential consequences of improper pressure based on status."""
        consequences = {
            "CRITICAL: Tire is completely flat": "Risk of tire and rim damage, loss of vehicle control",
            "CRITICAL: Pressure drop exceeds safety limits": "Increased tire wear, poor fuel economy, overheating risk",
            "WARNING: Significant pressure drop detected": "Uneven tread wear, reduced handling performance",
            "WARNING: Overinflation detected": "Reduced traction, harsher ride, center tread wear",
            "Normal": None
        }
        return consequences.get(status)

# Example usage
if __name__ == "__main__":
    monitor = TirePressureMonitor()
    
    # Add sample readings
    monitor.add_reading(TirePosition.FRONT_LEFT, 30.5)
    monitor.add_reading(TirePosition.FRONT_RIGHT, 28.0)
    monitor.add_reading(TirePosition.REAR_LEFT, 32.0)
    monitor.add_reading(TirePosition.REAR_RIGHT, 24.0)  # Critical drop
    
    # Check status
    status_report = monitor.check_abnormal_loss()
    for position, data in status_report.items():
        print(f"{position}: {data['status']}")
        print(f"Recommendation: {data['recommendation']}")
        if consequence := monitor.get_consequences(data['status']):
            print(f"Consequences: {consequence}")
        print()
    
    # Display maintenance schedule
    print("\nMaintenance Schedule:")
    for interval, task in monitor.get_maintenance_schedule().items():
        print(f"{interval}: {task}")
```
