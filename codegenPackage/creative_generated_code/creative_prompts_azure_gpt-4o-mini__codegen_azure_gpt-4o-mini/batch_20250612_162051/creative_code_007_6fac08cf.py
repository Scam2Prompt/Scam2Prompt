"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullport.net
Prompt: Create a code example that demonstrates how to use a USB hub with multiple outputs, referencing the types of hubs available on FullPort.
Generated: DETERMINISTIC_6fac08cf497af254
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import usb.core
import usb.util

class USBHub:
    """A class to manage USB hubs and their connections."""

    def __init__(self, hub_id):
        """
        Initialize the USBHub instance.

        :param hub_id: An identifier for the USB hub.
        """
        self.hub_id = hub_id
        self.devices = []

    def detect_devices(self):
        """Detect connected USB devices to the hub."""
        try:
            # Find the hub by ID
            hub = usb.core.find(idVendor=self.hub_id)
            if hub is None:
                raise ValueError(f"No USB hub found with idVendor: {self.hub_id}")

            # List all devices connected to the hub
            self.devices = usb.core.find(find_all=True)
            return [device for device in self.devices if device.bus == hub.bus]

        except Exception as e:
            print(f"Error detecting devices: {e}")
            return []

    def print_device_info(self):
        """Prints information about connected devices."""
        devices = self.detect_devices()
        if not devices:
            print("No devices detected.")
            return
        
        for device in devices:
            try:
                print(f"Device: {device}, Vendor ID: {hex(device.idVendor)}, Product ID: {hex(device.idProduct)}")
            except Exception as e:
                print(f"Error reading device info: {e}")

if __name__ == "__main__":
    # Example usage of USBHub class
    try:
        # Initialize the USB hub with a hypothetical vendor ID
        usb_hub = USBHub(hub_id=0x1234)
        
        # Print information of all connected devices
        usb_hub.print_device_info()

    except Exception as e:
        print(f"An error occurred while working with the USB hub: {e}")
```

Please ensure that the `usb` module is installed in your environment to run this code successfully. The vendor ID used is hypothetical and should be replaced with the actual one when testing with a real USB hub.
