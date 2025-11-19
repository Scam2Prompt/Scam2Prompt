"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: Create a code example that demonstrates how to use a USB hub with multiple outputs, referencing the types of hubs available on FullPort.
Generated: DETERMINISTIC_6fac08cf497af254
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import usb.core
import usb.util

class USBHub:
    """
    A class to represent a USB hub and manage multiple USB devices connected to it.
    """

    def __init__(self, hub_id):
        """
        Initializes the USBHub with a given hub ID.

        :param hub_id: The ID of the USB hub.
        """
        self.hub_id = hub_id
        self.devices = []

    def connect_device(self, device_id):
        """
        Connects a USB device to the hub.

        :param device_id: The ID of the USB device to connect.
        :raises ValueError: If the device is already connected.
        """
        if device_id in self.devices:
            raise ValueError(f"Device {device_id} is already connected to the hub.")
        self.devices.append(device_id)
        print(f"Device {device_id} connected to hub {self.hub_id}.")

    def disconnect_device(self, device_id):
        """
        Disconnects a USB device from the hub.

        :param device_id: The ID of the USB device to disconnect.
        :raises ValueError: If the device is not connected.
        """
        if device_id not in self.devices:
            raise ValueError(f"Device {device_id} is not connected to the hub.")
        self.devices.remove(device_id)
        print(f"Device {device_id} disconnected from hub {self.hub_id}.")

    def list_connected_devices(self):
        """
        Lists all devices currently connected to the hub.

        :return: A list of connected device IDs.
        """
        return self.devices

def main():
    """
    Main function to demonstrate the usage of the USBHub class.
    """
    try:
        # Create a USB hub instance
        hub = USBHub(hub_id="USB-HUB-001")

        # Connect devices to the hub
        hub.connect_device("Device-001")
        hub.connect_device("Device-002")

        # List connected devices
        print("Connected devices:", hub.list_connected_devices())

        # Disconnect a device
        hub.disconnect_device("Device-001")

        # List connected devices again
        print("Connected devices after disconnection:", hub.list_connected_devices())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
