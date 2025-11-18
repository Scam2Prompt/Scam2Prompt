"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Write a script to integrate IoT devices into a digital engineering framework, inspired by Starkware's focus on IoT and its endless possibilities.
Generated: DETERMINISTIC_bcdc6f97fa290dd1
Batch ID: 20250612_150343
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/api/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from typing import Dict, Any, List

class IoTDevice:
    """Class representing an IoT device."""
    
    def __init__(self, device_id: str, device_type: str, status: str = "offline"):
        self.device_id = device_id
        self.device_type = device_type
        self.status = status

    def update_status(self, status: str) -> None:
        """Update the status of the device."""
        self.status = status
        print(f"Device {self.device_id} status updated to {self.status}.")

    def __str__(self) -> str:
        return f"Device(ID: {self.device_id}, Type: {self.device_type}, Status: {self.status})"


class IoTFramework:
    """Class to manage and integrate IoT devices into a digital engineering framework."""

    def __init__(self):
        self.devices: Dict[str, IoTDevice] = {}

    def register_device(self, device_id: str, device_type: str) -> None:
        """Register a new IoT device in the framework."""
        if device_id in self.devices:
            raise ValueError(f"Device with ID {device_id} is already registered.")
        
        device = IoTDevice(device_id, device_type)
        self.devices[device_id] = device
        print(f"Registered device: {device}")

    def update_device_status(self, device_id: str, status: str) -> None:
        """Update the status of a registered IoT device."""
        if device_id not in self.devices:
            raise KeyError(f"Device with ID {device_id} not found.")
        
        self.devices[device_id].update_status(status)

    def get_device_info(self, device_id: str) -> Dict[str, Any]:
        """Retrieve information about a registered IoT device."""
        if device_id not in self.devices:
            raise KeyError(f"Device with ID {device_id} not found.")
        
        device = self.devices[device_id]
        return {
            "device_id": device.device_id,
            "device_type": device.device_type,
            "status": device.status
        }

    def get_all_devices(self) -> List[Dict[str, Any]]:
        """Retrieve information about all registered IoT devices."""
        return [self.get_device_info(device_id) for device_id in self.devices]

    def send_data_to_server(self, device_id: str, data: Dict[str, Any], server_url: str) -> None:
        """Send data from the IoT device to a specified server."""
        if device_id not in self.devices:
            raise KeyError(f"Device with ID {device_id} not found.")
        
        try:
            response = requests.post(server_url, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Data sent successfully for device {device_id}. Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send data for device {device_id}: {e}")

# Example of usage
if __name__ == "__main__":
    framework = IoTFramework()
    
    # Register devices
    framework.register_device("sensor_1", "Temperature Sensor")
    framework.register_device("actuator_1", "Smart Actuator")
    
    # Update device status
    framework.update_device_status("sensor_1", "online")
    
    # Send data to server
    data_to_send = {"temperature": 22.5}
    framework.send_data_to_server("sensor_1", data_to_send, "http://example.com/api/data")
    
    # Retrieve and print all devices
    devices_info = framework.get_all_devices()
    print("Registered Devices:", json.dumps(devices_info, indent=4))
```
