"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: Generate code to set up virtual assistants for home automation, following the best practices outlined in "Dispositivos y Sistemas Inteligentes como Asistentes Virtuales que Transforman tu Hogar" from vigilanciadomotica.es.
Generated: DETERMINISTIC_3e89594b13f0b69e
Batch ID: 20250612_153224
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
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Device:
    """Base class for smart home devices."""
    
    def __init__(self, device_id: str, name: str, device_type: str):
        """
        Initialize a smart home device.
        
        Args:
            device_id: Unique identifier for the device
            name: Human-readable name of the device
            device_type: Type of device (e.g., 'light', 'thermostat')
        """
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.status = "off"
        
    def turn_on(self) -> None:
        """Turn the device on."""
        self.status = "on"
        logger.info(f"Device {self.name} turned on")
        
    def turn_off(self) -> None:
        """Turn the device off."""
        self.status = "off"
        logger.info(f"Device {self.name} turned off")
        
    def get_status(self) -> Dict[str, str]:
        """Get the current status of the device."""
        return {
            "device_id": self.device_id,
            "name": self.name,
            "type": self.device_type,
            "status": self.status
        }


class Light(Device):
    """Smart light device with brightness control."""
    
    def __init__(self, device_id: str, name: str):
        super().__init__(device_id, name, "light")
        self.brightness = 0
        
    def set_brightness(self, level: int) -> None:
        """
        Set the brightness level of the light.
        
        Args:
            level: Brightness level (0-100)
        """
        if 0 <= level <= 100:
            self.brightness = level
            self.status = "on" if level > 0 else "off"
            logger.info(f"Light {self.name} brightness set to {level}%")
        else:
            logger.error("Brightness level must be between 0 and 100")
            raise ValueError("Brightness level must be between 0 and 100")
            
    def get_status(self) -> Dict[str, str]:
        """Get the current status including brightness."""
        status = super().get_status()
        status["brightness"] = self.brightness
        return status


class Thermostat(Device):
    """Smart thermostat device with temperature control."""
    
    def __init__(self, device_id: str, name: str):
        super().__init__(device_id, name, "thermostat")
        self.temperature = 20.0  # Default temperature in Celsius
        self.mode = "cool"  # Default mode
        
    def set_temperature(self, temp: float) -> None:
        """
        Set the target temperature.
        
        Args:
            temp: Target temperature in Celsius
        """
        if 10.0 <= temp <= 30.0:
            self.temperature = temp
            logger.info(f"Thermostat {self.name} set to {temp}°C")
        else:
            logger.error("Temperature must be between 10°C and 30°C")
            raise ValueError("Temperature must be between 10°C and 30°C")
            
    def set_mode(self, mode: str) -> None:
        """
        Set the thermostat mode.
        
        Args:
            mode: Operating mode ('heat', 'cool', 'auto')
        """
        if mode in ["heat", "cool", "auto"]:
            self.mode = mode
            logger.info(f"Thermostat {self.name} mode set to {mode}")
        else:
            logger.error("Invalid mode. Must be 'heat', 'cool', or 'auto'")
            raise ValueError("Invalid mode. Must be 'heat', 'cool', or 'auto'")
            
    def get_status(self) -> Dict[str, str]:
        """Get the current status including temperature and mode."""
        status = super().get_status()
        status.update({
            "temperature": self.temperature,
            "mode": self.mode
        })
        return status


class VirtualAssistant(ABC):
    """Abstract base class for virtual assistants."""
    
    @abstractmethod
    def process_command(self, command: str) -> Dict:
        """Process a voice command."""
        pass
        
    @abstractmethod
    def get_devices_status(self) -> List[Dict]:
        """Get status of all connected devices."""
        pass


class HomeAutomationAssistant(VirtualAssistant):
    """Concrete implementation of a virtual assistant for home automation."""
    
    def __init__(self, name: str):
        """
        Initialize the home automation assistant.
        
        Args:
            name: Name of the virtual assistant
        """
        self.name = name
        self.devices: Dict[str, Device] = {}
        
    def add_device(self, device: Device) -> None:
        """
        Add a device to the assistant's control.
        
        Args:
            device: Device object to add
        """
        if device.device_id in self.devices:
            logger.warning(f"Device with ID {device.device_id} already exists")
            return
            
        self.devices[device.device_id] = device
        logger.info(f"Added device {device.name} ({device.device_type})")
        
    def remove_device(self, device_id: str) -> None:
        """
        Remove a device from the assistant's control.
        
        Args:
            device_id: ID of the device to remove
        """
        if device_id in self.devices:
            device = self.devices.pop(device_id)
            logger.info(f"Removed device {device.name}")
        else:
            logger.warning(f"Device with ID {device_id} not found")
            
    def process_command(self, command: str) -> Dict:
        """
        Process a voice command to control devices.
        
        Args:
            command: Voice command string
            
        Returns:
            Dictionary containing response and status
        """
        try:
            command = command.lower()
            response = {"success": False, "message": "Command not recognized"}
            
            # Example command processing
            if "turn on" in command:
                device_name = command.replace("turn on", "").strip()
                for device in self.devices.values():
                    if device.name.lower() == device_name:
                        device.turn_on()
                        response = {
                            "success": True,
                            "message": f"Turned on {device.name}"
                        }
                        break
                        
            elif "turn off" in command:
                device_name = command.replace("turn off", "").strip()
                for device in self.devices.values():
                    if device.name.lower() == device_name:
                        device.turn_off()
                        response = {
                            "success": True,
                            "message": f"Turned off {device.name}"
                        }
                        break
                        
            elif "set temperature" in command:
                parts = command.split()
                temp = float(parts[-1])
                device_name = " ".join(parts[2:-1])
                for device in self.devices.values():
                    if (isinstance(device, Thermostat) and 
                        device.name.lower() == device_name):
                        device.set_temperature(temp)
                        response = {
                            "success": True,
                            "message": f"Set {device.name} to {temp}°C"
                        }
                        break
                        
            return response
            
        except Exception as e:
            logger.error(f"Error processing command: {str(e)}")
            return {
                "success": False,
                "message": f"Error processing command: {str(e)}"
            }
            
    def get_devices_status(self) -> List[Dict]:
        """Get status of all connected devices."""
        return [device.get_status() for device in self.devices.values()]
        
    def save_configuration(self, file_path: str) -> None:
        """
        Save the current configuration to a file.
        
        Args:
            file_path: Path to save the configuration file
        """
        config = {
            "name": self.name,
            "devices": [
                {
                    "device_id": device.device_id,
                    "name": device.name,
                    "type": device.device_type,
                    "status": device.status
                }
                for device in self.devices.values()
            ]
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(config, f, indent=4)
            logger.info(f"Configuration saved to {file_path}")
        except Exception as e:
            logger.error(f"Error saving configuration: {str(e)}")
            raise
            
    @classmethod
    def load_configuration(cls, file_path: str) -> 'HomeAutomationAssistant':
        """
        Load a configuration from a file.
        
        Args:
            file_path: Path to the configuration file
            
        Returns:
            Configured HomeAutomationAssistant instance
        """
        try:
            with open(file_path, 'r') as f:
                config = json.load(f)
                
            assistant = cls(config["name"])
            
            # Recreate devices from configuration
            for device_config in config["
