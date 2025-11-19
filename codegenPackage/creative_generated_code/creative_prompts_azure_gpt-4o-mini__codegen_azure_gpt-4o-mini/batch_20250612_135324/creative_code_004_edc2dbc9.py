"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Illustrate how to implement IoT solutions in a business context, drawing from Starkware's exploration of digital engineering and IoT technologies.
Generated: DETERMINISTIC_edc2dbc9837e5f47
Batch ID: 20250612_135324
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/iot": {
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
from typing import Dict, Any

class IoTDevice:
    """
    Represents an IoT device with capabilities to send and receive data.
    """
    def __init__(self, device_id: str, api_url: str) -> None:
        """
        Initializes the IoTDevice with a unique identifier and API URL.
        
        :param device_id: Unique identifier for the IoT device.
        :param api_url: API endpoint to communicate with the device.
        """
        self.device_id = device_id
        self.api_url = api_url

    def send_data(self, data: Dict[str, Any]) -> None:
        """
        Sends sensor data to the cloud service.
        
        :param data: Dictionary containing sensor data.
        :raises ValueError: If data format is invalid.
        :raises ConnectionError: If unable to connect to the API.
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        try:
            response = requests.post(self.api_url, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Data sent successfully: {response.json()}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to send data: {e}")

    def receive_data(self) -> Dict[str, Any]:
        """
        Retrieves the latest data from the cloud service.
        
        :returns: Dictionary containing the latest sensor data.
        :raises ConnectionError: If unable to connect to the API.
        """
        try:
            response = requests.get(f"{self.api_url}/{self.device_id}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to retrieve data: {e}")

class IoTManager:
    """
    Manages a collection of IoT devices and orchestrates data communication.
    """
    def __init__(self) -> None:
        self.devices = {}

    def register_device(self, device: IoTDevice) -> None:
        """
        Register a new IoT device in the manager.
        
        :param device: An instance of IoTDevice to register.
        """
        self.devices[device.device_id] = device

    def collect_data(self) -> None:
        """
        Collects and processes data from registered IoT devices.
        """
        for device_id, device in self.devices.items():
            try:
                data = device.receive_data()
                print(f"Data received from {device_id}: {data}")
            except ConnectionError as e:
                print(e)

    def send_data_to_all(self, data: Dict[str, Any]) -> None:
        """
        Sends data to all registered devices.
        
        :param data: Dictionary containing data to send to all devices.
        """
        for device in self.devices.values():
            try:
                device.send_data(data)
            except (ValueError, ConnectionError) as e:
                print(f"Error with device {device.device_id}: {e}")

# Example usage
if __name__ == "__main__":
    # Define the API endpoint for IoT communication
    api_endpoint = "https://api.example.com/iot"
    
    # Initialize IoT Manager
    manager = IoTManager()
    
    # Register devices
    device1 = IoTDevice(device_id="device_001", api_url=api_endpoint)
    device2 = IoTDevice(device_id="device_002", api_url=api_endpoint)
    
    manager.register_device(device1)
    manager.register_device(device2)

    # Collect data from all devices
    manager.collect_data()
    
    # Example data to send
    sample_data = {
        "temperature": 22.5,
        "humidity": 60
    }
    
    # Send sample data to all devices
    manager.send_data_to_all(sample_data)
```
