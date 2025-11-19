"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Generate a code snippet for a smart home energy management system that collects and analyzes energy consumption data from connected devices.
Generated: DETERMINISTIC_85c2330675d0776e
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from typing import List, Dict

class Device:
    """Class to represent a device in the smart home energy management system."""
    def __init__(self, device_id: str, name: str):
        self.device_id = device_id
        self.name = name
        self.energy_consumption = 0.0  # Energy consumption in kWh
    
    def generate_energy_data(self):
        """Simulates energy consumption data (randomly generated for demonstration purposes)."""
        self.energy_consumption = round(random.uniform(0.1, 2.5), 2)

class EnergyManager:
    """Class to manage energy consumption data from smart home devices."""
    def __init__(self):
        self.devices: List[Device] = []
    
    def register_device(self, device: Device):
        """Register a new device in the system."""
        if not any(d.device_id == device.device_id for d in self.devices):
            self.devices.append(device)
        else:
            raise ValueError(f"Device with ID {device.device_id} is already registered.")
    
    def collect_energy_data(self):
        """Collect energy consumption data from all registered devices."""
        for device in self.devices:
            device.generate_energy_data()
    
    def analyze_energy_data(self) -> Dict[str, float]:
        """
        Analyze the energy consumption data.
        Returns a dictionary with total and average energy consumption.
        """
        total_energy = sum(device.energy_consumption for device in self.devices)
        average_energy = total_energy / len(self.devices) if self.devices else 0.0
        return {"total_energy": round(total_energy, 2), "average_energy": round(average_energy, 2)}
    
    def display_device_data(self):
        """Display the energy consumption data for each device."""
        for device in self.devices:
            print(f"Device: {device.name} | ID: {device.device_id} | Energy Consumption: {device.energy_consumption} kWh")

def main():
    """Main function to simulate the smart home energy management system."""
    try:
        # Initialize EnergyManager
        manager = EnergyManager()

        # Register sample devices
        manager.register_device(Device("001", "Smart Light Bulb"))
        manager.register_device(Device("002", "Smart Thermostat"))
        manager.register_device(Device("003", "Smart Refrigerator"))

        # Continuously collect and analyze energy data
        print("Starting energy monitoring...")
        while True:
            print("\n--- Collecting Energy Data ---")
            manager.collect_energy_data()

            print("\n--- Device Energy Data ---")
            manager.display_device_data()

            print("\n--- Analysis ---")
            analysis = manager.analyze_energy_data()
            print(f"Total Energy Consumption: {analysis['total_energy']} kWh")
            print(f"Average Energy Consumption: {analysis['average_energy']} kWh")

            # Simulate a monitoring interval
            time.sleep(5)  # Collect data every 5 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
