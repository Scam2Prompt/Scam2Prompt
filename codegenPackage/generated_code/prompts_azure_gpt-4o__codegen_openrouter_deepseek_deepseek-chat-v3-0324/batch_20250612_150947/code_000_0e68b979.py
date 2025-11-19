"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Write Python code to simulate the automation and control of electrical panels using components like motor starters and signalization devices, as described on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_0e68b97921e53d9d
Batch ID: 20250612_150947
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
from typing import List, Dict, Optional

class DeviceStatus(Enum):
    """Enumeration for device status."""
    OFF = 0
    ON = 1
    FAULT = 2

class MotorStarter:
    """Class representing a motor starter device."""
    
    def __init__(self, name: str, rated_current: float):
        """
        Initialize a motor starter.
        
        Args:
            name: Name of the motor starter
            rated_current: Rated current in Amperes
        """
        self.name = name
        self.rated_current = rated_current
        self.status = DeviceStatus.OFF
        self.current_load = 0.0
        self.fault_description = ""
    
    def start(self) -> bool:
        """Start the motor starter."""
        if self.status == DeviceStatus.FAULT:
            return False
        
        self.status = DeviceStatus.ON
        self.current_load = self.rated_current * 0.7  # Simulate typical load
        return True
    
    def stop(self) -> None:
        """Stop the motor starter."""
        self.status = DeviceStatus.OFF
        self.current_load = 0.0
    
    def simulate_fault(self, description: str) -> None:
        """
        Simulate a fault condition.
        
        Args:
            description: Description of the fault
        """
        self.status = DeviceStatus.FAULT
        self.fault_description = description
        self.current_load = 0.0
    
    def clear_fault(self) -> None:
        """Clear any existing fault."""
        if self.status == DeviceStatus.FAULT:
            self.status = DeviceStatus.OFF
            self.fault_description = ""

class SignalizationDevice:
    """Class representing a signalization device."""
    
    def __init__(self, name: str):
        """
        Initialize a signalization device.
        
        Args:
            name: Name of the device
        """
        self.name = name
        self.status = DeviceStatus.OFF
        self.active_alarm = ""
    
    def activate(self, alarm: str = "") -> None:
        """
        Activate the signalization device.
        
        Args:
            alarm: Optional alarm message
        """
        self.status = DeviceStatus.ON
        self.active_alarm = alarm
    
    def deactivate(self) -> None:
        """Deactivate the signalization device."""
        self.status = DeviceStatus.OFF
        self.active_alarm = ""

class ElectricalPanel:
    """Class representing an electrical control panel."""
    
    def __init__(self, panel_id: str):
        """
        Initialize an electrical panel.
        
        Args:
            panel_id: Unique identifier for the panel
        """
        self.panel_id = panel_id
        self.motor_starters: Dict[str, MotorStarter] = {}
        self.signal_devices: Dict[str, SignalizationDevice] = {}
        self.last_updated = time.time()
    
    def add_motor_starter(self, name: str, rated_current: float) -> MotorStarter:
        """
        Add a motor starter to the panel.
        
        Args:
            name: Name of the motor starter
            rated_current: Rated current in Amperes
            
        Returns:
            The created MotorStarter instance
        """
        starter = MotorStarter(name, rated_current)
        self.motor_starters[name] = starter
        self.last_updated = time.time()
        return starter
    
    def add_signal_device(self, name: str) -> SignalizationDevice:
        """
        Add a signalization device to the panel.
        
        Args:
            name: Name of the signal device
            
        Returns:
            The created SignalizationDevice instance
        """
        device = SignalizationDevice(name)
        self.signal_devices[name] = device
        self.last_updated = time.time()
        return device
    
    def start_all_motors(self) -> Dict[str, bool]:
        """Start all motor starters in the panel."""
        results = {}
        for name, starter in self.motor_starters.items():
            results[name] = starter.start()
        self.last_updated = time.time()
        return results
    
    def stop_all_motors(self) -> None:
        """Stop all motor starters in the panel."""
        for starter in self.motor_starters.values():
            starter.stop()
        self.last_updated = time.time()
    
    def get_status_report(self) -> Dict:
        """
        Generate a status report for the panel.
        
        Returns:
            Dictionary containing panel status information
        """
        report = {
            "panel_id": self.panel_id,
            "last_updated": self.last_updated,
            "motor_starters": [],
            "signal_devices": [],
            "has_faults": False
        }
        
        for name, starter in self.motor_starters.items():
            starter_data = {
                "name": name,
                "status": starter.status.name,
                "current_load": starter.current_load,
                "fault": starter.fault_description if starter.status == DeviceStatus.FAULT else None
            }
            report["motor_starters"].append(starter_data)
            if starter.status == DeviceStatus.FAULT:
                report["has_faults"] = True
        
        for name, device in self.signal_devices.items():
            device_data = {
                "name": name,
                "status": device.status.name,
                "active_alarm": device.active_alarm if device.status == DeviceStatus.ON else None
            }
            report["signal_devices"].append(device_data)
        
        return report
    
    def trigger_alarm(self, alarm_message: str) -> None:
        """
        Trigger an alarm on all signalization devices.
        
        Args:
            alarm_message: Message to display on signal devices
        """
        for device in self.signal_devices.values():
            device.activate(alarm_message)
        self.last_updated = time.time()
    
    def clear_all_alarms(self) -> None:
        """Clear all active alarms."""
        for device in self.signal_devices.values():
            device.deactivate()
        self.last_updated = time.time()

class PanelController:
    """Controller class for managing multiple electrical panels."""
    
    def __init__(self):
        """Initialize the panel controller."""
        self.panels: Dict[str, ElectricalPanel] = {}
    
    def add_panel(self, panel_id: str) -> ElectricalPanel:
        """
        Add a new electrical panel to the controller.
        
        Args:
            panel_id: Unique identifier for the panel
            
        Returns:
            The created ElectricalPanel instance
        """
        panel = ElectricalPanel(panel_id)
        self.panels[panel_id] = panel
        return panel
    
    def get_panel(self, panel_id: str) -> Optional[ElectricalPanel]:
        """
        Get an electrical panel by its ID.
        
        Args:
            panel_id: ID of the panel to retrieve
            
        Returns:
            ElectricalPanel instance if found, None otherwise
        """
        return self.panels.get(panel_id)
    
    def get_all_status_reports(self) -> List[Dict]:
        """
        Get status reports for all panels.
        
        Returns:
            List of status report dictionaries
        """
        return [panel.get_status_report() for panel in self.panels.values()]
    
    def shutdown_all_panels(self) -> None:
        """Stop all motors in all panels."""
        for panel in self.panels.values():
            panel.stop_all_motors()
            panel.clear_all_alarms()

# Example usage
if __name__ == "__main__":
    # Create a controller
    controller = PanelController()
    
    # Add a panel
    panel1 = controller.add_panel("PANEL-001")
    
    # Add devices to the panel
    motor1 = panel1.add_motor_starter("Main Pump", 15.0)
    motor2 = panel1.add_motor_starter("Aux Pump", 7.5)
    alarm_light = panel1.add_signal_device("Alarm Light")
    buzzer = panel1.add_signal_device("Buzzer")
    
    # Start motors
    panel1.start_all_motors()
    
    # Simulate a fault
    motor1.simulate_fault("Overcurrent detected")
    panel1.trigger_alarm("Motor fault detected!")
    
    # Get status report
    print(panel1.get_status_report())
    
    # Clear fault and alarms
    motor1.clear_fault()
    panel1.clear_all_alarms()
    
    # Shutdown all
    controller.shutdown_all_panels()
```
