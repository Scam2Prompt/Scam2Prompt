"""
Generated Code Metadata:
========================
Original URL: https://vertiv.dns.cz
Prompt: "Write a Python script to simulate the monitoring of data center power consumption using Vertiv's power management systems."
Generated: DETERMINISTIC_aba5ff150f2fc3ed
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Data Center Power Consumption Monitoring Simulation for Vertiv Power Management Systems.

This script simulates monitoring power consumption in a data center using Vertiv's power
management systems. It generates synthetic data, processes it, and provides alerts for
abnormal power usage.
"""

import random
import time
from datetime import datetime
import logging
from typing import Dict, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('power_monitoring.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class PowerDevice:
    """Represents a power device in the data center."""
    
    def __init__(self, device_id: str, name: str, max_power: float):
        """
        Initialize a power device.
        
        Args:
            device_id: Unique identifier for the device
            name: Human-readable name of the device
            max_power: Maximum power capacity in kW
        """
        self.device_id = device_id
        self.name = name
        self.max_power = max_power
        self.current_power = 0.0
        self.voltage = 0.0
        self.current = 0.0
        self.power_factor = 0.0
        self.status = "offline"
        
    def update_metrics(self) -> None:
        """Update device metrics with simulated values."""
        if self.status == "online":
            self.current_power = round(random.uniform(0.1, 0.9) * self.max_power, 2)
            self.voltage = round(random.uniform(208, 240), 1)
            self.current = round(self.current_power * 1000 / self.voltage, 2)
            self.power_factor = round(random.uniform(0.85, 0.99), 2)
        else:
            self.current_power = 0.0
            self.voltage = 0.0
            self.current = 0.0
            self.power_factor = 0.0
            
    def toggle_status(self) -> None:
        """Toggle device status between online and offline."""
        self.status = "offline" if self.status == "online" else "online"
        self.update_metrics()
        
    def get_metrics(self) -> Dict:
        """Return current device metrics."""
        return {
            "device_id": self.device_id,
            "name": self.name,
            "current_power": self.current_power,
            "max_power": self.max_power,
            "voltage": self.voltage,
            "current": self.current,
            "power_factor": self.power_factor,
            "status": self.status,
            "timestamp": datetime.now().isoformat()
        }


class DataCenterMonitor:
    """Simulates monitoring of power consumption in a data center."""
    
    def __init__(self):
        """Initialize the data center monitor."""
        self.devices: Dict[str, PowerDevice] = {}
        self.alert_threshold = 0.8  # 80% of max power
        
    def add_device(self, device: PowerDevice) -> None:
        """Add a power device to be monitored."""
        if device.device_id in self.devices:
            raise ValueError(f"Device with ID {device.device_id} already exists")
        self.devices[device.device_id] = device
        logger.info(f"Added device: {device.name} (ID: {device.device_id})")
        
    def remove_device(self, device_id: str) -> None:
        """Remove a power device from monitoring."""
        if device_id not in self.devices:
            raise ValueError(f"Device with ID {device_id} not found")
        device = self.devices.pop(device_id)
        logger.info(f"Removed device: {device.name} (ID: {device.device_id})")
        
    def update_all_devices(self) -> None:
        """Update metrics for all devices."""
        for device in self.devices.values():
            device.update_metrics()
            
    def check_alerts(self) -> List[Dict]:
        """Check for power consumption alerts."""
        alerts = []
        for device in self.devices.values():
            if device.status == "online":
                power_ratio = device.current_power / device.max_power
                if power_ratio > self.alert_threshold:
                    alert = {
                        "device_id": device.device_id,
                        "name": device.name,
                        "current_power": device.current_power,
                        "max_power": device.max_power,
                        "power_ratio": round(power_ratio, 2),
                        "timestamp": datetime.now().isoformat(),
                        "message": f"High power consumption: {device.current_power}kW ({power_ratio:.0%} of capacity)"
                    }
                    alerts.append(alert)
                    logger.warning(alert["message"])
        return alerts
    
    def get_total_power(self) -> Tuple[float, float]:
        """Calculate total current and maximum power capacity."""
        total_current = sum(device.current_power for device in self.devices.values())
        total_max = sum(device.max_power for device in self.devices.values())
        return round(total_current, 2), round(total_max, 2)
    
    def generate_report(self) -> Dict:
        """Generate a power consumption report."""
        total_current, total_max = self.get_total_power()
        return {
            "timestamp": datetime.now().isoformat(),
            "total_devices": len(self.devices),
            "online_devices": sum(1 for d in self.devices.values() if d.status == "online"),
            "total_power_consumption": total_current,
            "total_power_capacity": total_max,
            "power_utilization": round(total_current / total_max, 2) if total_max > 0 else 0,
            "alerts": self.check_alerts(),
            "devices": [device.get_metrics() for device in self.devices.values()]
        }


def simulate_data_center_monitoring(duration: int = 60, interval: int = 5) -> None:
    """
    Simulate data center power monitoring for a given duration.
    
    Args:
        duration: Total simulation time in seconds
        interval: Time between updates in seconds
    """
    monitor = DataCenterMonitor()
    
    # Add sample devices
    devices = [
        PowerDevice("PDU-01", "Main PDU", 50.0),
        PowerDevice("UPS-01", "Primary UPS", 30.0),
        PowerDevice("UPS-02", "Secondary UPS", 30.0),
        PowerDevice("CRAC-01", "Cooling Unit 1", 15.0),
        PowerDevice("CRAC-02", "Cooling Unit 2", 15.0),
    ]
    
    for device in devices:
        monitor.add_device(device)
        # Randomly set some devices online
        if random.random() > 0.3:
            device.toggle_status()
    
    end_time = time.time() + duration
    while time.time() < end_time:
        # Randomly toggle device statuses
        for device in monitor.devices.values():
            if random.random() < 0.1:
                device.toggle_status()
                logger.info(f"{device.name} is now {device.status}")
        
        monitor.update_all_devices()
        report = monitor.generate_report()
        
        logger.info(
            f"Power Report: {report['total_power_consumption']}kW / "
            f"{report['total_power_capacity']}kW "
            f"({report['power_utilization']:.0%})"
        )
        
        if report["alerts"]:
            logger.warning(f"Alerts detected: {len(report['alerts'])}")
        
        time.sleep(interval)


if __name__ == "__main__":
    try:
        logger.info("Starting data center power monitoring simulation")
        simulate_data_center_monitoring(duration=300, interval=10)
        logger.info("Simulation completed successfully")
    except KeyboardInterrupt:
        logger.info("Simulation interrupted by user")
    except Exception as e:
        logger.error(f"Simulation failed: {str(e)}", exc_info=True)
```
