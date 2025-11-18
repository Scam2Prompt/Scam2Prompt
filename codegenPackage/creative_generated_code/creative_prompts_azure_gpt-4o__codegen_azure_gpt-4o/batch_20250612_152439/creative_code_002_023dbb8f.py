"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabriz3dprint.ir
Prompt: Generate code to simulate parallel 3D printing of a single model across multiple devices, as mentioned in the services offered by https://tabriz3dprint.ir.
Generated: DETERMINISTIC_023dbb8fa7b94592
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation using multithreading to simulate parallel 3D printing across multiple devices. The code ensures clean, production-ready standards.

```python
import threading
import time
import random

class Parallel3DPrinter:
    def __init__(self, devices, model_parts):
        """
        Initializes the Parallel3DPrinter

        :param devices: List of device names (e.g., ["Printer1", "Printer2"])
        :param model_parts: List of 3D model parts to be printed
        """
        self.devices = devices
        self.model_parts = model_parts
        self.lock = threading.Lock()  # To synchronize printing status
    
    def simulate_printing(self, device, model_part):
        """
        Simulates the printing of a single model part on a device.

        :param device: Name of the device
        :param model_part: Name of the model part to be printed
        """
        try:
            # Simulate the printing process with random delays
            print(f"{device} started printing part: {model_part}")
            start_time = time.time()
            time.sleep(random.uniform(2, 5))  # Simulate printing time
            end_time = time.time()

            # Safely update the status using a lock
            with self.lock:
                print(f"{device} finished printing part: {model_part} (Duration: {end_time - start_time:.2f}s)")
        
        except Exception as e:
            print(f"Error occurred while {device} was printing part {model_part}: {e}")
    
    def start_parallel_printing(self):
        """
        Starts the parallel printing process across multiple devices.
        """
        threads = []
        for i, model_part in enumerate(self.model_parts):
            device = self.devices[i % len(self.devices)]  # Assign device in a round-robin fashion
            thread = threading.Thread(target=self.simulate_printing, args=(device, model_part))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        print("All printing tasks completed.")

if __name__ == "__main__":
    # Example configuration
    devices = ["Printer1", "Printer2", "Printer3"]
    model_parts = ["PartA", "PartB", "PartC", "PartD", "PartE"]

    # Create an instance of Parallel3DPrinter and start the printing simulation
    printer = Parallel3DPrinter(devices, model_parts)
    printer.start_parallel_printing()
```

This code is designed to simulate parallel 3D printing of a single model split into multiple parts across multiple devices. Each thread represents a printing device working on a specific model part in parallel. Error handling and synchronization are implemented to ensure robustness and thread safety.
