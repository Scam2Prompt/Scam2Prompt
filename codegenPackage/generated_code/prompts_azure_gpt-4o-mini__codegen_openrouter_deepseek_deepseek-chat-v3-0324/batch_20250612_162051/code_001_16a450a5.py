"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Generate a Python script that simulates the functionality of a smart home system, allowing remote control of bathroom accessories like the "آینه ضد بخار" from Dolphin Iran.
Generated: DETERMINISTIC_16a450a51d1a679d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, Optional
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("SmartHomeSystem")

class DeviceStatus(Enum):
    """Enum representing possible device states."""
    ON = auto()
    OFF = auto()
    ERROR = auto()

class BathroomAccessory:
    """Base class for bathroom accessories."""
    def __init__(self, name: str):
        self.name = name
        self.status = DeviceStatus.OFF
        logger.info(f"Initialized {self.name} with status {self.status.name}")

    def turn_on(self) -> bool:
        """Turn the device on."""
        if self.status == DeviceStatus.ON:
            logger.warning(f"{self.name} is already ON")
            return False
        
        try:
            self.status = DeviceStatus.ON
            logger.info(f"Turned ON {self.name}")
            return True
        except Exception as e:
            logger.error(f"Error turning ON {self.name}: {str(e)}")
            self.status = DeviceStatus.ERROR
            return False

    def turn_off(self) -> bool:
        """Turn the device off."""
        if self.status == DeviceStatus.OFF:
            logger.warning(f"{self.name} is already OFF")
            return False
        
        try:
            self.status = DeviceStatus.OFF
            logger.info(f"Turned OFF {self.name}")
            return True
        except Exception as e:
            logger.error(f"Error turning OFF {self.name}: {str(e)}")
            self.status = DeviceStatus.ERROR
            return False

    def get_status(self) -> Dict[str, str]:
        """Get current device status."""
        return {
            "name": self.name,
            "status": self.status.name
        }

class AntiFogMirror(BathroomAccessory):
    """Specialized class for anti-fog mirror."""
    def __init__(self, name: str = "آینه ضد بخار"):
        super().__init__(name)
        self.temperature = 25  # Default temperature in Celsius

    def set_temperature(self, temp: int) -> bool:
        """Set mirror temperature to prevent fogging."""
        if not 20 <= temp <= 40:
            logger.error(f"Temperature {temp}°C is out of range (20-40°C)")
            return False
        
        try:
            self.temperature = temp
            logger.info(f"Set {self.name} temperature to {temp}°C")
            return True
        except Exception as e:
            logger.error(f"Error setting temperature: {str(e)}")
            return False

    def get_status(self) -> Dict[str, str]:
        """Get mirror status including temperature."""
        status = super().get_status()
        status["temperature"] = f"{self.temperature}°C"
        return status

class SmartHomeSystem:
    """Main smart home system controller."""
    def __init__(self):
        self.devices: Dict[str, BathroomAccessory] = {}
        logger.info("Smart Home System initialized")

    def add_device(self, device: BathroomAccessory) -> bool:
        """Add a new device to the system."""
        if device.name in self.devices:
            logger.warning(f"Device {device.name} already exists")
            return False
        
        self.devices[device.name] = device
        logger.info(f"Added device: {device.name}")
        return True

    def remove_device(self, device_name: str) -> bool:
        """Remove a device from the system."""
        if device_name not in self.devices:
            logger.warning(f"Device {device_name} not found")
            return False
        
        del self.devices[device_name]
        logger.info(f"Removed device: {device_name}")
        return True

    def control_device(
        self,
        device_name: str,
        action: str,
        **kwargs
    ) -> Optional[Dict[str, str]]:
        """Control a device with specified action."""
        if device_name not in self.devices:
            logger.error(f"Device {device_name} not found")
            return None
        
        device = self.devices[device_name]
        
        try:
            if action == "turn_on":
                success = device.turn_on()
            elif action == "turn_off":
                success = device.turn_off()
            elif action == "set_temperature" and isinstance(device, AntiFogMirror):
                temp = kwargs.get("temperature")
                if temp is None:
                    logger.error("Temperature parameter missing")
                    return None
                success = device.set_temperature(temp)
            else:
                logger.error(f"Unsupported action: {action}")
                return None
            
            if not success:
                return None
            
            return device.get_status()
        except Exception as e:
            logger.error(f"Error controlling device {device_name}: {str(e)}")
            return None

    def get_device_status(self, device_name: str) -> Optional[Dict[str, str]]:
        """Get status of a specific device."""
        if device_name not in self.devices:
            logger.error(f"Device {device_name} not found")
            return None
        
        return self.devices[device_name].get_status()

    def list_devices(self) -> Dict[str, Dict[str, str]]:
        """List all devices and their statuses."""
        return {
            name: device.get_status()
            for name, device in self.devices.items()
        }

# Example usage
if __name__ == "__main__":
    # Initialize the smart home system
    smart_home = SmartHomeSystem()
    
    # Create and add an anti-fog mirror
    mirror = AntiFogMirror()
    smart_home.add_device(mirror)
    
    # Control the mirror
    print(json.dumps(smart_home.control_device(mirror.name, "turn_on"), indent=2))
    print(json.dumps(smart_home.control_device(mirror.name, "set_temperature", temperature=30), indent=2))
    print(json.dumps(smart_home.get_device_status(mirror.name), indent=2))
    print(json.dumps(smart_home.list_devices(), indent=2))
```
