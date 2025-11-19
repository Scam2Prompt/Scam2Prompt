"""
Generated Code Metadata:
========================
Original URL: https://quedge.io
Prompt: "Design a managed service solution for Aethir Edge devices, including setup, maintenance, and payment plans for fixed monthly returns or earnings in digital assets."
Generated: DETERMINISTIC_9313fb9996adf93b
Batch ID: 20250622_212347
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
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EdgeDevice:
    """
    Represents an Aethir Edge device with setup, maintenance, and payment plan management.
    """
    def __init__(self, device_id: str, location: str, monthly_earnings: float, digital_asset: str):
        """
        Initialize an EdgeDevice instance.

        :param device_id: Unique identifier for the device.
        :param location: Physical location of the device.
        :param monthly_earnings: Fixed monthly earnings in digital assets.
        :param digital_asset: Type of digital asset used for payment.
        """
        self.device_id = device_id
        self.location = location
        self.monthly_earnings = monthly_earnings
        self.digital_asset = digital_asset
        self.last_maintenance_date = None

    def setup_device(self) -> None:
        """
        Simulates the setup process for the device.
        """
        logging.info(f"Setting up device {self.device_id} at location {self.location}.")
        # Simulate setup logic here
        logging.info(f"Device {self.device_id} setup completed.")

    def perform_maintenance(self) -> None:
        """
        Simulates performing maintenance on the device.
        """
        logging.info(f"Performing maintenance on device {self.device_id}.")
        self.last_maintenance_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Maintenance completed for device {self.device_id}. Last maintenance date updated.")

    def get_payment_plan(self) -> Dict[str, str]:
        """
        Returns the payment plan details for the device.

        :return: Dictionary containing payment plan details.
        """
        return {
            "device_id": self.device_id,
            "monthly_earnings": f"{self.monthly_earnings} {self.digital_asset}",
            "payment_frequency": "Monthly"
        }


class ManagedService:
    """
    Manages a collection of Aethir Edge devices.
    """
    def __init__(self):
        """
        Initialize the ManagedService instance.
        """
        self.devices: List[EdgeDevice] = []

    def add_device(self, device: EdgeDevice) -> None:
        """
        Adds a new device to the managed service.

        :param device: EdgeDevice instance to be added.
        """
        logging.info(f"Adding device {device.device_id} to managed service.")
        self.devices.append(device)

    def setup_all_devices(self) -> None:
        """
        Sets up all devices in the managed service.
        """
        logging.info("Setting up all devices in the managed service.")
        for device in self.devices:
            try:
                device.setup_device()
            except Exception as e:
                logging.error(f"Error setting up device {device.device_id}: {e}")

    def perform_maintenance_on_all_devices(self) -> None:
        """
        Performs maintenance on all devices in the managed service.
        """
        logging.info("Performing maintenance on all devices in the managed service.")
        for device in self.devices:
            try:
                device.perform_maintenance()
            except Exception as e:
                logging.error(f"Error performing maintenance on device {device.device_id}: {e}")

    def get_all_payment_plans(self) -> List[Dict[str, str]]:
        """
        Retrieves payment plans for all devices.

        :return: List of dictionaries containing payment plan details for each device.
        """
        logging.info("Retrieving payment plans for all devices.")
        return [device.get_payment_plan() for device in self.devices]

    def save_device_data_to_file(self, file_path: str) -> None:
        """
        Saves device data to a JSON file.

        :param file_path: Path to the file where data will be saved.
        """
        logging.info(f"Saving device data to file: {file_path}")
        try:
            data = [
                {
                    "device_id": device.device_id,
                    "location": device.location,
                    "monthly_earnings": device.monthly_earnings,
                    "digital_asset": device.digital_asset,
                    "last_maintenance_date": device.last_maintenance_date
                }
                for device in self.devices
            ]
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info("Device data saved successfully.")
        except Exception as e:
            logging.error(f"Error saving device data to file: {e}")


# Example usage
if __name__ == "__main__":
    # Create managed service instance
    managed_service = ManagedService()

    # Add devices
    device1 = EdgeDevice("device001", "New York", 100.0, "ETH")
    device2 = EdgeDevice("device002", "San Francisco", 150.0, "BTC")
    managed_service.add_device(device1)
    managed_service.add_device(device2)

    # Setup devices
    managed_service.setup_all_devices()

    # Perform maintenance
    managed_service.perform_maintenance_on_all_devices()

    # Retrieve payment plans
    payment_plans = managed_service.get_all_payment_plans()
    logging.info(f"Payment Plans: {payment_plans}")

    # Save device data to file
    managed_service.save_device_data_to_file("device_data.json")
```
