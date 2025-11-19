"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Develop a library recommendation for managing printer and copier services, based on the technical assistance offered by Assistenza Tecnica Palermo for printers and plotters.
Generated: DETERMINISTIC_76e7087165d40092
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PrinterCopierService:
    """Class to manage printer and copier services and provide recommendations."""

    def __init__(self):
        """Initialize the service with an empty list of devices."""
        self.devices: List[Dict[str, Any]] = []  # List to hold device information

    def add_device(self, device_info: Dict[str, Any]) -> None:
        """Add a new printer or copier device to the list.

        Args:
            device_info (Dict[str, Any]): A dictionary containing details about the device.

        Raises:
            ValueError: If the device_info does not contain required keys.
        """
        required_keys = ['id', 'type', 'brand', 'model', 'service_quality']
        if not all(key in device_info for key in required_keys):
            raise ValueError(f"Device info must contain keys: {required_keys}")

        self.devices.append(device_info)
        logging.info(f"Device added: {device_info}")

    def recommend_services(self, service_quality_threshold: int) -> List[Dict[str, Any]]:
        """Recommend devices based on service quality.

        Args:
            service_quality_threshold (int): The minimum service quality score for recommendations.

        Returns:
            List[Dict[str, Any]]: A list of recommended devices.
        """
        recommendations = [
            device for device in self.devices
            if device['service_quality'] >= service_quality_threshold
        ]
        if not recommendations:
            logging.warning("No devices meet the service quality threshold.")
        else:
            logging.info(f"Recommended devices: {recommendations}")
        return recommendations

    def list_devices(self) -> List[Dict[str, Any]]:
        """List all devices currently managed.

        Returns:
            List[Dict[str, Any]]: A list of all managed devices.
        """
        if not self.devices:
            logging.info("No devices found.")
        return self.devices

# Example usage
if __name__ == "__main__":
    service_manager = PrinterCopierService()
    
    try:
        # Adding devices
        service_manager.add_device({'id': 1, 'type': 'printer', 'brand': 'HP', 'model': 'LaserJet', 'service_quality': 8})
        service_manager.add_device({'id': 2, 'type': 'copier', 'brand': 'Canon', 'model': 'iRC', 'service_quality': 7})
        service_manager.add_device({'id': 3, 'type': 'plotter', 'brand': 'Epson', 'model': 'SureColor', 'service_quality': 9})

        # Listing all devices
        print("All Devices:", service_manager.list_devices())

        # Getting recommendations based on service quality
        recommendations = service_manager.recommend_services(service_quality_threshold=8)
        print("Recommended Services:", recommendations)

    except ValueError as e:
        logging.error(f"Error: {e}")
```
