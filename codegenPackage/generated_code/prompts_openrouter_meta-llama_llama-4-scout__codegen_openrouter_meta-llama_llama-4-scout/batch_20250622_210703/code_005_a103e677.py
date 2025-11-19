"""
Generated Code Metadata:
========================
Original URL: https://icgard.ir
Prompt: Suggest a list of compatible devices for a CCTV camera system with 5MP resolution, night vision, and wireless connectivity.
Generated: DETERMINISTIC_a103e6779194dc6c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# compatible_devices.py

class Device:
    def __init__(self, name, resolution, night_vision, wireless_connectivity):
        """
        Initialize a device with its characteristics.

        Args:
            name (str): Device name
            resolution (int): Device resolution in megapixels
            night_vision (bool): Whether the device has night vision
            wireless_connectivity (bool): Whether the device has wireless connectivity
        """
        self.name = name
        self.resolution = resolution
        self.night_vision = night_vision
        self.wireless_connectivity = wireless_connectivity

    def __str__(self):
        return f"{self.name} - {self.resolution}MP, Night Vision: {self.night_vision}, Wireless: {self.wireless_connectivity}"


class CCTVSystem:
    def __init__(self, resolution, night_vision, wireless_connectivity):
        """
        Initialize a CCTV system with its requirements.

        Args:
            resolution (int): Required resolution in megapixels
            night_vision (bool): Whether the system requires night vision
            wireless_connectivity (bool): Whether the system requires wireless connectivity
        """
        self.resolution = resolution
        self.night_vision = night_vision
        self.wireless_connectivity = wireless_connectivity
        self.devices = []

    def add_device(self, device):
        """
        Add a device to the list of compatible devices.

        Args:
            device (Device): Device to add
        """
        if (device.resolution >= self.resolution and 
            device.night_vision == self.night_vision and 
            device.wireless_connectivity == self.wireless_connectivity):
            self.devices.append(device)

    def suggest_devices(self):
        """
        Return a list of compatible devices.

        Returns:
            list[Device]: List of compatible devices
        """
        return self.devices


def main():
    try:
        # Define CCTV system requirements
        cctv_system = CCTVSystem(5, True, True)

        # Define available devices
        devices = [
            Device("Reolink RLC-410", 5, True, True),
            Device("Blink XT2", 5, True, True),
            Device("Ring Stick Up Cam", 5, True, True),
            Device("Arlo Pro 3", 2, True, True),  # Incompatible resolution
            Device("Hikvision DS-2CE16C0T-IR", 5, False, True),  # Incompatible night vision
            Device("Bosch Flexidome IP", 5, True, False),  # Incompatible wireless connectivity
        ]

        # Suggest compatible devices
        for device in devices:
            cctv_system.add_device(device)

        # Print suggested devices
        print("Compatible Devices:")
        for i, device in enumerate(cctv_system.suggest_devices()):
            print(f"{i+1}. {device}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
