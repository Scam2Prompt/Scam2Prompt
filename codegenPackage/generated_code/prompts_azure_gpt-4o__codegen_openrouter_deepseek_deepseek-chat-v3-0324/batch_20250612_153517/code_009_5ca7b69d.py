"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write code to simulate the installation and operation of electrical panels for specialized environments like greenhouses or parking ventilation systems, as described by پایش نیرو.
Generated: DETERMINISTIC_5ca7b69d700f64be
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electrical Panel Simulation for Specialized Environments

This module simulates the installation and operation of electrical panels
for specialized environments like greenhouses or parking ventilation systems.
It includes monitoring, control, and safety features.

Key Features:
- Panel installation simulation
- Load monitoring
- Fault detection
- Environmental parameter tracking
"""

import random
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional


class EnvironmentType(Enum):
    GREENHOUSE = auto()
    PARKING_VENTILATION = auto()
    OTHER = auto()


class PanelStatus(Enum):
    INSTALLED = auto()
    OPERATIONAL = auto()
    FAULT = auto()
    MAINTENANCE = auto()


@dataclass
class ElectricalLoad:
    name: str
    power_rating: float  # in watts
    is_active: bool = False


@dataclass
class EnvironmentalParameters:
    temperature: float
    humidity: float
    co2_level: Optional[float] = None  # ppm, mainly for greenhouses
    airflow: Optional[float] = None  # m/s, mainly for ventilation


class ElectricalPanel:
    def __init__(self, panel_id: str, env_type: EnvironmentType, max_capacity: float):
        self.panel_id = panel_id
        self.env_type = env_type
        self.max_capacity = max_capacity  # in watts
        self.status = PanelStatus.INSTALLED
        self.loads: List[ElectricalLoad] = []
        self.environment = EnvironmentalParameters(0.0, 0.0)
        self.installation_date = time.strftime("%Y-%m-%d")
        self.last_maintenance = None
        self.fault_history = []

    def add_load(self, load: ElectricalLoad) -> bool:
        """Add an electrical load to the panel if capacity allows."""
        total_load = sum(l.power_rating for l in self.loads if l.is_active)
        if total_load + load.power_rating <= self.max_capacity:
            self.loads.append(load)
            return True
        return False

    def activate_load(self, load_name: str) -> bool:
        """Activate a specific load if capacity allows."""
        load = next((l for l in self.loads if l.name == load_name), None)
        if not load:
            return False

        active_load = sum(l.power_rating for l in self.loads if l.is_active)
        if active_load + load.power_rating <= self.max_capacity:
            load.is_active = True
            return True
        return False

    def deactivate_load(self, load_name: str) -> bool:
        """Deactivate a specific load."""
        load = next((l for l in self.loads if l.name == load_name), None)
        if load:
            load.is_active = False
            return True
        return False

    def calculate_total_load(self) -> float:
        """Calculate current total active load."""
        return sum(l.power_rating for l in self.loads if l.is_active)

    def update_environment(self, params: EnvironmentalParameters) -> None:
        """Update environmental parameters."""
        self.environment = params

    def check_for_faults(self) -> Optional[Dict]:
        """Check for potential faults in the system."""
        total_load = self.calculate_total_load()
        faults = {}

        if total_load > self.max_capacity:
            faults["overload"] = f"Load {total_load}W exceeds capacity {self.max_capacity}W"
        
        if self.env_type == EnvironmentType.GREENHOUSE:
            if self.environment.temperature > 40:
                faults["high_temp"] = "Temperature exceeds safe limits"
        
        if self.env_type == EnvironmentType.PARKING_VENTILATION:
            if self.environment.airflow and self.environment.airflow < 0.5:
                faults["low_airflow"] = "Insufficient ventilation"

        if faults:
            self.status = PanelStatus.FAULT
            fault_record = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "faults": faults,
                "load": total_load,
                "environment": self.environment
            }
            self.fault_history.append(fault_record)
            return fault_record
        
        self.status = PanelStatus.OPERATIONAL
        return None

    def perform_maintenance(self) -> None:
        """Perform maintenance on the panel."""
        self.status = PanelStatus.MAINTENANCE
        self.last_maintenance = time.strftime("%Y-%m-%d %H:%M:%S")
        # Simulate maintenance fixing any faults
        self.status = PanelStatus.OPERATIONAL

    def get_status_report(self) -> Dict:
        """Generate a comprehensive status report."""
        return {
            "panel_id": self.panel_id,
            "status": self.status.name,
            "total_load": self.calculate_total_load(),
            "capacity_utilization": self.calculate_total_load() / self.max_capacity * 100,
            "environment": {
                "temperature": self.environment.temperature,
                "humidity": self.environment.humidity,
                "co2_level": self.environment.co2_level,
                "airflow": self.environment.airflow
            },
            "active_loads": [l.name for l in self.loads if l.is_active],
            "last_maintenance": self.last_maintenance,
            "fault_count": len(self.fault_history)
        }


class PanelSimulator:
    def __init__(self):
        self.panels: Dict[str, ElectricalPanel] = {}

    def install_panel(self, panel_id: str, env_type: EnvironmentType, max_capacity: float) -> ElectricalPanel:
        """Install a new electrical panel."""
        if panel_id in self.panels:
            raise ValueError(f"Panel with ID {panel_id} already exists")
        
        panel = ElectricalPanel(panel_id, env_type, max_capacity)
        self.panels[panel_id] = panel
        return panel

    def simulate_operation(self, duration_hours: float = 24) -> None:
        """Simulate panel operation over time with random environmental changes."""
        for _ in range(int(duration_hours * 60)):  # Simulate minute by minute
            for panel in self.panels.values():
                # Simulate environmental changes
                if panel.env_type == EnvironmentType.GREENHOUSE:
                    temp = 20 + random.uniform(-5, 15)  # 15-35°C range
                    humidity = 50 + random.uniform(-20, 30)  # 30-80%
                    co2 = 400 + random.uniform(0, 1000)  # 400-1400 ppm
                    panel.update_environment(
                        EnvironmentalParameters(temp, humidity, co2)
                    )
                elif panel.env_type == EnvironmentType.PARKING_VENTILATION:
                    temp = 15 + random.uniform(-10, 20)  # 5-35°C
                    humidity = 40 + random.uniform(-20, 30)  # 20-70%
                    airflow = random.uniform(0.3, 2.0)  # 0.3-2.0 m/s
                    panel.update_environment(
                        EnvironmentalParameters(temp, humidity, None, airflow)
                    )
                
                # Randomly toggle some loads
                for load in panel.loads:
                    if random.random() < 0.05:  # 5% chance to toggle
                        if load.is_active:
                            panel.deactivate_load(load.name)
                        else:
                            panel.activate_load(load.name)
                
                # Check for faults
                panel.check_for_faults()
            
            time.sleep(0.01)  # Small delay to simulate time passing

    def get_all_status_reports(self) -> Dict[str, Dict]:
        """Get status reports for all panels."""
        return {panel_id: panel.get_status_report() for panel_id, panel in self.panels.items()}


# Example usage
if __name__ == "__main__":
    simulator = PanelSimulator()
    
    # Install greenhouse panel
    greenhouse_panel = simulator.install_panel(
        "GH-001", EnvironmentType.GREENHOUSE, 5000
    )
    greenhouse_panel.add_load(ElectricalLoad("Heating", 2000))
    greenhouse_panel.add_load(ElectricalLoad("Lighting", 1500))
    greenhouse_panel.add_load(ElectricalLoad("Irrigation", 800))
    greenhouse_panel.add_load(ElectricalLoad("Ventilation", 1200))
    
    # Install parking ventilation panel
    parking_panel = simulator.install_panel(
        "PK-001", EnvironmentType.PARKING_VENTILATION, 3000
    )
    parking_panel.add_load(ElectricalLoad("Main Fans", 1800))
    parking_panel.add_load(ElectricalLoad("Emergency Fans", 1000))
    parking_panel.add_load(ElectricalLoad("Lighting", 600))
    
    # Simulate operation
    print("Starting simulation...")
    simulator.simulate_operation(1)  # Simulate 1 hour of operation
