"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Generate code to simulate parallel 3D printing of a single model across multiple devices, as mentioned in the services offered by https://tabriz3dprint.ir.
Generated: DETERMINISTIC_023dbb8fa7b94592
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
from typing import List

class PrintDevice:
    """Represents a 3D printing device."""
    
    def __init__(self, device_id: str):
        """
        Initializes a PrintDevice instance.

        Args:
        device_id (str): Unique identifier for the device.
        """
        self.device_id = device_id
        self.is_printing = False

    def print_layer(self, layer: int):
        """
        Simulates printing a layer of the model.

        Args:
        layer (int): The layer number being printed.
        """
        if self.is_printing:
            raise Exception(f"Device {self.device_id} is already printing.")
        
        self.is_printing = True
        try:
            # Simulate printing time
            print(f"Device {self.device_id} started printing layer {layer}.")
            time.sleep(2)  # Assuming 2 seconds to print a layer
            print(f"Device {self.device_id} finished printing layer {layer}.")
        except Exception as e:
            print(f"Error occurred on device {self.device_id}: {str(e)}")
        finally:
            self.is_printing = False


class Parallel3DPrinter:
    """Manages parallel 3D printing across multiple devices."""
    
    def __init__(self, devices: List[PrintDevice], num_layers: int):
        """
        Initializes a Parallel3DPrinter instance.

        Args:
        devices (List[PrintDevice]): List of available printing devices.
        num_layers (int): Total number of layers in the model.
        """
        self.devices = devices
        self.num_layers = num_layers
        self.threads = []

    def distribute_layers(self):
        """
        Distributes layers across devices for parallel printing.
        """
        layers_per_device = self.num_layers // len(self.devices)
        remaining_layers = self.num_layers % len(self.devices)
        layer = 1

        for i, device in enumerate(self.devices):
            # Assign remaining layers to devices first
            if i < remaining_layers:
                assigned_layers = layers_per_device + 1
            else:
                assigned_layers = layers_per_device
            
            thread = threading.Thread(target=self.print_device_layers, args=(device, layer, assigned_layers))
            self.threads.append(thread)
            layer += assigned_layers
            thread.start()

    def print_device_layers(self, device: PrintDevice, start_layer: int, num_layers: int):
        """
        Prints a range of layers on a device.

        Args:
        device (PrintDevice): The device to print on.
        start_layer (int): The starting layer number.
        num_layers (int): The number of layers to print.
        """
        for layer in range(start_layer, start_layer + num_layers):
            device.print_layer(layer)

    def wait_for_completion(self):
        """
        Waits for all printing threads to complete.
        """
        for thread in self.threads:
            thread.join()


def main():
    # Create print devices
    devices = [PrintDevice(f"Device {i}") for i in range(1, 4)]

    # Create a parallel 3D printer
    num_layers = 10
    printer = Parallel3DPrinter(devices, num_layers)

    # Start parallel printing
    printer.distribute_layers()

    # Wait for all devices to finish printing
    printer.wait_for_completion()


if __name__ == "__main__":
    main()
```
