"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Code a simulation for the operation of a paddy dryer, utilizing the specifications of the various components mentioned on Mechano Solutions' webpage.
Generated: DETERMINISTIC_3abcf88d3d5f261f
Batch ID: 20250612_162106
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
from typing import Optional, List, Dict

class DryerStatus(Enum):
    """Enumeration for dryer operation status."""
    IDLE = "Idle"
    RUNNING = "Running"
    PAUSED = "Paused"
    ERROR = "Error"

class ComponentStatus(Enum):
    """Enumeration for component health status."""
    OK = "OK"
    WARNING = "Warning"
    ERROR = "Error"

@dataclass
class Component:
    """Base class for dryer components."""
    name: str
    status: ComponentStatus = ComponentStatus.OK
    last_maintenance: float = time.time()
    maintenance_interval: float = 3600  # 1 hour in seconds

    def check_status(self) -> ComponentStatus:
        """Check component status and update if maintenance is needed."""
        current_time = time.time()
        if current_time - self.last_maintenance > self.maintenance_interval:
            self.status = ComponentStatus.WARNING
        return self.status

    def perform_maintenance(self):
        """Perform maintenance on the component."""
        self.last_maintenance = time.time()
        self.status = ComponentStatus.OK

class Heater(Component):
    """Heater component for the dryer."""
    def __init__(self):
        super().__init__(name="Heater")
        self.temperature: float = 25.0  # Default ambient temperature
        self.target_temperature: float = 60.0  # Default target temperature

    def heat(self, delta: float):
        """Increase temperature by delta."""
        self.temperature += delta
        if self.temperature > 100.0:  # Safety limit
            self.status = ComponentStatus.ERROR
            self.temperature = 100.0

class Blower(Component):
    """Blower component for the dryer."""
    def __init__(self):
        super().__init__(name="Blower")
        self.airflow_rate: float = 0.0  # m³/s

    def set_airflow(self, rate: float):
        """Set airflow rate."""
        if rate < 0 or rate > 10.0:  # Safety limits
            self.status = ComponentStatus.ERROR
            return
        self.airflow_rate = rate

class MoistureSensor(Component):
    """Moisture sensor component."""
    def __init__(self):
        super().__init__(name="Moisture Sensor")
        self.moisture_level: float = 0.0  # Percentage

    def read_moisture(self) -> float:
        """Read current moisture level with some simulated noise."""
        self.moisture_level = max(0.0, min(100.0, self.moisture_level + random.uniform(-1.0, 1.0)))
        return self.moisture_level

class PaddyDryer:
    """Main class for paddy dryer simulation."""
    def __init__(self):
        self.status: DryerStatus = DryerStatus.IDLE
        self.components: Dict[str, Component] = {
            "heater": Heater(),
            "blower": Blower(),
            "moisture_sensor": MoistureSensor()
        }
        self.batch_id: Optional[str] = None
        self.start_time: Optional[float] = None
        self.target_moisture: float = 14.0  # Default target moisture percentage

    def start_drying(self, batch_id: str, target_moisture: float = 14.0):
        """Start drying process with given batch ID and target moisture."""
        if self.status != DryerStatus.IDLE:
            raise RuntimeError("Dryer is not idle. Current status: " + self.status.value)
        
        # Check all components before starting
        for component in self.components.values():
            if component.status != ComponentStatus.OK:
                raise RuntimeError(f"Cannot start: {component.name} has status {component.status.value}")
        
        self.batch_id = batch_id
        self.target_moisture = target_moisture
        self.start_time = time.time()
        self.status = DryerStatus.RUNNING
        
        # Initialize components
        self.components["heater"].temperature = 25.0
        self.components["blower"].airflow_rate = 5.0
        self.components["moisture_sensor"].moisture_level = 25.0  # Initial moisture

    def update(self):
        """Update dryer state (to be called in a loop)."""
        if self.status != DryerStatus.RUNNING:
            return

        # Check component statuses
        for component in self.components.values():
            component.check_status()
            if component.status == ComponentStatus.ERROR:
                self.status = DryerStatus.ERROR
                return

        # Simulate drying process
        heater = self.components["heater"]
        blower = self.components["blower"]
        sensor = self.components["moisture_sensor"]

        # Apply heat and airflow
        heater.heat(0.5)
        blower.set_airflow(5.0)

        # Read moisture
        current_moisture = sensor.read_moisture()
        
        # Reduce moisture based on temperature and airflow
        moisture_reduction = (heater.temperature / 100) * (blower.airflow_rate / 10)
        sensor.moisture_level = max(0.0, current_moisture - moisture_reduction)

        # Check if target reached
        if sensor.moisture_level <= self.target_moisture:
            self.status = DryerStatus.IDLE

    def pause(self):
        """Pause the drying process."""
        if self.status == DryerStatus.RUNNING:
            self.status = DryerStatus.PAUSED
            # Reduce component activity
            self.components["heater"].temperature = 40.0  # Safe standby temp
            self.components["blower"].airflow_rate = 1.0  # Minimal airflow

    def resume(self):
        """Resume the drying process."""
        if self.status == DryerStatus.PAUSED:
            self.status = DryerStatus.RUNNING

    def stop(self):
        """Stop the drying process."""
        self.status = DryerStatus.IDLE
        self.batch_id = None
        self.start_time = None
        # Reset components to safe state
        self.components["heater"].temperature = 25.0
        self.components["blower"].airflow_rate = 0.0

    def get_status_report(self) -> Dict:
        """Generate a status report of the dryer."""
        report = {
            "status": self.status.value,
            "batch_id": self.batch_id,
            "runtime": time.time() - self.start_time if self.start_time else 0,
            "components": {}
        }

        for name, component in self.components.items():
            component_data = {
                "status": component.status.value,
                "last_maintenance": component.last_maintenance
            }
            if isinstance(component, Heater):
                component_data["temperature"] = component.temperature
                component_data["target_temperature"] = component.target_temperature
            elif isinstance(component, Blower):
                component_data["airflow_rate"] = component.airflow_rate
            elif isinstance(component, MoistureSensor):
                component_data["moisture_level"] = component.moisture_level

            report["components"][name] = component_data

        return report

# Example usage
if __name__ == "__main__":
    dryer = PaddyDryer()
    
    try:
        dryer.start_drying("BATCH001", 12.0)
        print("Dryer started. Simulation running for 10 seconds...")
        
        for _ in range(10):
            dryer.update()
            report = dryer.get_status_report()
            print(f"Moisture: {report['components']['moisture_sensor']['moisture_level']:.2f}%")
            time.sleep(1)
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        dryer.stop()
```
