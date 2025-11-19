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
"""
PrinterServiceManager: A library for managing printer and copier services.
This library provides utilities for handling printer and plotter services.
Inspired by the technical assistance offered by Assistenza Tecnica Palermo.
"""

import logging


class PrinterServiceManager:
    """
    A class to manage printer and copier services.
    """

    def __init__(self):
        """
        Initialize the service manager.
        """
        self.devices = {}
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("Printer Service Manager initialized.")

    def register_device(self, device_id, device_type, model):
        """
        Register a new printer/copier/plotter device.

        Args:
            device_id (str): Unique identifier for the device.
            device_type (str): Type of the device ('printer', 'copier', 'plotter').
            model (str): Model name of the device.

        Returns:
            None
        """
        if device_id in self.devices:
            logging.error(f"Device with ID '{device_id}' is already registered.")
            raise ValueError(f"Device with ID '{device_id}' is already registered.")

        self.devices[device_id] = {
            "device_type": device_type,
            "model": model,
            "status": "idle"
        }
        logging.info(f"Registered device: {device_id}, Type: {device_type}, Model: {model}")

    def update_status(self, device_id, status):
        """
        Update the status of a registered device.

        Args:
            device_id (str): Unique identifier for the device.
            status (str): New status for the device ('idle', 'active', 'error').

        Returns:
            None
        """
        if device_id not in self.devices:
            logging.error(f"Device with ID '{device_id}' not found.")
            raise KeyError(f"Device with ID '{device_id}' not found.")

        self.devices[device_id]["status"] = status
        logging.info(f"Updated status of device '{device_id}' to '{status}'.")

    def get_device_info(self, device_id):
        """
        Retrieve information for a specific device.

        Args:
            device_id (str): Unique identifier for the device.

        Returns:
            dict: Device information.
        """
        if device_id not in self.devices:
            logging.error(f"Device with ID '{device_id}' not found.")
            raise KeyError(f"Device with ID '{device_id}' not found.")

        logging.info(f"Retrieved information for device '{device_id}'.")
        return self.devices[device_id]

    def list_devices(self):
        """
        List all registered devices.

        Returns:
            dict: All registered devices.
        """
        logging.info("Listing all registered devices.")
        return self.devices

    def unregister_device(self, device_id):
        """
        Unregister a device.

        Args:
            device_id (str): Unique identifier for the device.

        Returns:
            None
        """
        if device_id not in self.devices:
            logging.error(f"Device with ID '{device_id}' not found.")
            raise KeyError(f"Device with ID '{device_id}' not found.")

        del self.devices[device_id]
        logging.info(f"Unregistered device '{device_id}'.")


if __name__ == "__main__":
    # Example usage of PrinterServiceManager
    try:
        manager = PrinterServiceManager()
        manager.register_device("PRN001", "printer", "HP LaserJet Pro")
        manager.register_device("PLT001", "plotter", "Canon Plotter XYZ")
        manager.update_status("PRN001", "active")
        print(manager.get_device_info("PRN001"))
        print(manager.list_devices())
        manager.unregister_device("PRN001")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
