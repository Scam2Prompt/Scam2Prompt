"""
Generated Code Metadata:
========================
Original URL: https://blackpanttthers.com
Prompt: "Discuss the benefits and challenges of using a centralized hub versus decentralized approach for controlling smart home devices, considering factors like scalability, security, and user experience."
Generated: DETERMINISTIC_42b0d8ba939c8aeb
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates a simplified implementation of both centralized and decentralized
approaches for controlling smart home devices, highlighting their benefits and challenges.
"""

from abc import ABC, abstractmethod
import json
from typing import Dict, List, Optional
import uuid
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SmartDevice:
    """Base class representing a smart home device."""
    def __init__(self, device_id: str, name: str, device_type: str):
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.status = "off"

    def turn_on(self):
        """Turn the device on."""
        self.status = "on"
        logger.info(f"{self.name} turned on")

    def turn_off(self):
        """Turn the device off."""
        self.status = "off"
        logger.info(f"{self.name} turned off")

    def get_status(self) -> Dict[str, str]:
        """Return the current status of the device."""
        return {
            "device_id": self.device_id,
            "name": self.name,
            "type": self.device_type,
            "status": self.status
        }

class ControlSystem(ABC):
    """Abstract base class for control systems."""
    @abstractmethod
    def add_device(self, device: SmartDevice) -> None:
        """Add a device to the control system."""
        pass

    @abstractmethod
    def control_device(self, device_id: str, action: str) -> None:
        """Control a device (turn on/off)."""
        pass

    @abstractmethod
    def get_device_status(self, device_id: str) -> Optional[Dict[str, str]]:
        """Get the status of a device."""
        pass

class CentralizedHub(ControlSystem):
    """Centralized hub implementation."""
    def __init__(self):
        self.devices: Dict[str, SmartDevice] = {}

    def add_device(self, device: SmartDevice) -> None:
        """Add a device to the centralized hub."""
        if device.device_id in self.devices:
            raise ValueError(f"Device {device.device_id} already exists")
        self.devices[device.device_id] = device
        logger.info(f"Added {device.name} to centralized hub")

    def control_device(self, device_id: str, action: str) -> None:
        """Control a device via the centralized hub."""
        if device_id not in self.devices:
            raise ValueError(f"Device {device_id} not found")
        
        device = self.devices[device_id]
        if action == "on":
            device.turn_on()
        elif action == "off":
            device.turn_off()
        else:
            raise ValueError(f"Invalid action: {action}")

    def get_device_status(self, device_id: str) -> Optional[Dict[str, str]]:
        """Get device status from the centralized hub."""
        if device_id not in self.devices:
            logger.warning(f"Device {device_id} not found")
            return None
        return self.devices[device_id].get_status()

class DecentralizedSystem(ControlSystem):
    """Decentralized control system implementation."""
    def __init__(self):
        self.devices: Dict[str, SmartDevice] = {}

    def add_device(self, device: SmartDevice) -> None:
        """Add a device to the decentralized system."""
        if device.device_id in self.devices:
            raise ValueError(f"Device {device.device_id} already exists")
        self.devices[device.device_id] = device
        logger.info(f"Added {device.name} to decentralized system")

    def control_device(self, device_id: str, action: str) -> None:
        """Control a device directly (decentralized)."""
        if device_id not in self.devices:
            raise ValueError(f"Device {device_id} not found")
        
        device = self.devices[device_id]
        if action == "on":
            device.turn_on()
        elif action == "off":
            device.turn_off()
        else:
            raise ValueError(f"Invalid action: {action}")

    def get_device_status(self, device_id: str) -> Optional[Dict[str, str]]:
        """Get device status directly (decentralized)."""
        if device_id not in self.devices:
            logger.warning(f"Device {device_id} not found")
            return None
        return self.devices[device_id].get_status()

def simulate_usage(control_system: ControlSystem, num_devices: int = 5) -> None:
    """Simulate adding and controlling devices using the given control system."""
    devices = [
        SmartDevice(str(uuid.uuid4()), f"Device {i}", "Light")
        for i in range(num_devices)
    ]

    for device in devices:
        try:
            control_system.add_device(device)
        except ValueError as e:
            logger.error(f"Error adding device: {e}")

    # Control devices
    for device in devices:
        try:
            control_system.control_device(device.device_id, "on")
            status = control_system.get_device_status(device.device_id)
            logger.info(f"Device status: {json.dumps(status, indent=2)}")
        except ValueError as e:
            logger.error(f"Error controlling device: {e}")

if __name__ == "__main__":
    logger.info("Simulating Centralized Hub Approach")
    centralized_hub = CentralizedHub()
    simulate_usage(centralized_hub)

    logger.info("\nSimulating Decentralized Approach")
    decentralized_system = DecentralizedSystem()
    simulate_usage(decentralized_system)
```
