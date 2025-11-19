"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: Create a code snippet to monitor and control residential solar energy systems, inspired by Chico Electric's residential solar services.
Generated: DETERMINISTIC_7de7e4d80b1baa90
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SolarSystemStatus(Enum):
    """Enum representing possible solar system statuses."""
    ONLINE = auto()
    OFFLINE = auto()
    DEGRADED = auto()
    FAULT = auto()

@dataclass
class SolarPanel:
    """Dataclass representing a solar panel in the system."""
    panel_id: str
    efficiency: float  # 0.0 to 1.0
    max_output_watts: float
    current_output_watts: float = 0.0
    status: SolarSystemStatus = SolarSystemStatus.OFFLINE

@dataclass
class Battery:
    """Dataclass representing a battery storage unit."""
    battery_id: str
    capacity_kwh: float
    current_charge_kwh: float = 0.0
    status: SolarSystemStatus = SolarSystemStatus.OFFLINE

@dataclass
class Inverter:
    """Dataclass representing an inverter."""
    inverter_id: str
    max_output_watts: float
    current_output_watts: float = 0.0
    status: SolarSystemStatus = SolarSystemStatus.OFFLINE

class SolarEnergySystem:
    """Main class to monitor and control a residential solar energy system."""
    
    def __init__(self, system_id: str):
        self.system_id = system_id
        self.panels: List[SolarPanel] = []
        self.batteries: List[Battery] = []
        self.inverters: List[Inverter] = []
        self.grid_export_enabled: bool = False
        self.last_update_time: float = 0.0
        
    def add_panel(self, panel: SolarPanel) -> None:
        """Add a solar panel to the system."""
        self.panels.append(panel)
        logger.info(f"Added panel {panel.panel_id} to system {self.system_id}")
        
    def add_battery(self, battery: Battery) -> None:
        """Add a battery to the system."""
        self.batteries.append(battery)
        logger.info(f"Added battery {battery.battery_id} to system {self.system_id}")
        
    def add_inverter(self, inverter: Inverter) -> None:
        """Add an inverter to the system."""
        self.inverters.append(inverter)
        logger.info(f"Added inverter {inverter.inverter_id} to system {self.system_id}")
        
    def update_system_status(self) -> None:
        """Update the status of all components in the system."""
        self.last_update_time = time.time()
        
        # Simulate updating panel statuses
        for panel in self.panels:
            if panel.status == SolarSystemStatus.FAULT:
                continue
            panel.current_output_watts = panel.max_output_watts * panel.efficiency
            panel.status = SolarSystemStatus.ONLINE
            
        # Simulate updating battery statuses
        for battery in self.batteries:
            if battery.status == SolarSystemStatus.FAULT:
                continue
            battery.status = SolarSystemStatus.ONLINE
            
        # Simulate updating inverter statuses
        for inverter in self.inverters:
            if inverter.status == SolarSystemStatus.FAULT:
                continue
            inverter.current_output_watts = sum(
                panel.current_output_watts for panel in self.panels
            ) / len(self.inverters)
            inverter.status = SolarSystemStatus.ONLINE
            
        logger.info(f"Updated status for system {self.system_id}")
        
    def get_system_summary(self) -> Dict:
        """Return a summary of the system's current state."""
        total_panel_output = sum(panel.current_output_watts for panel in self.panels)
        total_battery_capacity = sum(battery.capacity_kwh for battery in self.batteries)
        total_battery_charge = sum(battery.current_charge_kwh for battery in self.batteries)
        total_inverter_output = sum(inverter.current_output_watts for inverter in self.inverters)
        
        return {
            "system_id": self.system_id,
            "total_panel_output_watts": total_panel_output,
            "total_battery_capacity_kwh": total_battery_capacity,
            "total_battery_charge_kwh": total_battery_charge,
            "total_inverter_output_watts": total_inverter_output,
            "grid_export_enabled": self.grid_export_enabled,
            "last_update_time": self.last_update_time,
            "panel_count": len(self.panels),
            "battery_count": len(self.batteries),
            "inverter_count": len(self.inverters),
        }
        
    def toggle_grid_export(self, enable: bool) -> None:
        """Enable or disable grid export functionality."""
        self.grid_export_enabled = enable
        status = "enabled" if enable else "disabled"
        logger.info(f"Grid export {status} for system {self.system_id}")
        
    def charge_batteries(self, kwh: float) -> None:
        """Charge the batteries with specified kWh."""
        if kwh <= 0:
            logger.warning(f"Invalid charge amount {kwh}kWh for system {self.system_id}")
            return
            
        remaining_charge = kwh
        for battery in self.batteries:
            if battery.status != SolarSystemStatus.ONLINE:
                continue
                
            available_capacity = battery.capacity_kwh - battery.current_charge_kwh
            charge_amount = min(remaining_charge, available_capacity)
            battery.current_charge_kwh += charge_amount
            remaining_charge -= charge_amount
            
            if remaining_charge <= 0:
                break
                
        logger.info(f"Charged batteries with {kwh - remaining_charge}kWh in system {self.system_id}")
        
    def check_system_health(self) -> Dict[str, List[str]]:
        """Check system health and return any issues found."""
        issues = {
            "panels": [],
            "batteries": [],
            "inverters": []
        }
        
        for panel in self.panels:
            if panel.status == SolarSystemStatus.FAULT:
                issues["panels"].append(f"Panel {panel.panel_id} has a fault")
            elif panel.efficiency < 0.5:
                issues["panels"].append(f"Panel {panel.panel_id} has low efficiency ({panel.efficiency})")
                
        for battery in self.batteries:
            if battery.status == SolarSystemStatus.FAULT:
                issues["batteries"].append(f"Battery {battery.battery_id} has a fault")
            elif battery.current_charge_kwh / battery.capacity_kwh < 0.1:
                issues["batteries"].append(f"Battery {battery.battery_id} is critically low ({battery.current_charge_kwh}kWh)")
                
        for inverter in self.inverters:
            if inverter.status == SolarSystemStatus.FAULT:
                issues["inverters"].append(f"Inverter {inverter.inverter_id} has a fault")
            elif inverter.current_output_watts > inverter.max_output_watts * 0.9:
                issues["inverters"].append(f"Inverter {inverter.inverter_id} is near capacity ({inverter.current_output_watts}W)")
                
        return issues

# Example usage
if __name__ == "__main__":
    # Create a solar energy system
    system = SolarEnergySystem("RES-001")
    
    # Add components
    system.add_panel(SolarPanel("PAN-001", 0.85, 300))
    system.add_panel(SolarPanel("PAN-002", 0.82, 300))
    system.add_battery(Battery("BAT-001", 10.0))
    system.add_inverter(Inverter("INV-001", 5000))
    
    # Update and monitor
    system.update_system_status()
    print(system.get_system_summary())
    
    # Check health
    health_issues = system.check_system_health()
    if any(health_issues.values()):
        print("Health issues detected:", health_issues)
    
    # Charge batteries
    system.charge_batteries(5.0)
    
    # Toggle grid export
    system.toggle_grid_export(True)
```
