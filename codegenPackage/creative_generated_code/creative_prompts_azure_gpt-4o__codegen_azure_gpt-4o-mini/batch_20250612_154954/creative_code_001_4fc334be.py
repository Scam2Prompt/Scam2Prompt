"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Create a program to simulate cryptocurrency mining performance using Aethir Edge devices, incorporating decentralized computing principles and energy-efficient metrics described on the website.
Generated: DETERMINISTIC_4fc334be550b1272
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict

class AethirEdgeDevice:
    """Class representing an Aethir Edge device used for cryptocurrency mining."""

    def __init__(self, device_id: str, processing_power: float, energy_efficiency: float):
        """
        Initialize an Aethir Edge device.

        :param device_id: Unique identifier for the device.
        :param processing_power: The device's processing power in hashes per second.
        :param energy_efficiency: The energy consumption of the device in watts.
        """
        self.device_id = device_id
        self.processing_power = processing_power
        self.energy_efficiency = energy_efficiency
        self.is_active = True

    def mine(self, duration: int) -> float:
        """
        Simulate mining operation for a duration.

        :param duration: Duration to mine in seconds.
        :return: The amount of cryptocurrency mined.
        """
        if not self.is_active:
            raise Exception(f"Device {self.device_id} is not active.")

        # Simulate mining with a random reward based on processing power
        mined_amount = self.processing_power * duration * random.uniform(0.8, 1.2)
        return mined_amount

    def turn_off(self):
        """Deactivate the mining operation of the device."""
        self.is_active = False

    def turn_on(self):
        """Activate the mining operation of the device."""
        self.is_active = True


class MiningSimulation:
    """Class to simulate a mining operation using multiple Aethir Edge devices."""

    def __init__(self, devices: List[AethirEdgeDevice]):
        """
        Initialize mining simulation with a list of devices.

        :param devices: List of Aethir Edge devices participating in mining.
        """
        self.devices = devices

    def run_simulation(self, duration: int) -> Dict[str, float]:
        """
        Run the mining simulation for a specified duration.

        :param duration: Duration to run the simulation in seconds.
        :return: Total cryptocurrency mined by each device.
        """
        results = {}
        for device in self.devices:
            try:
                mined_amount = device.mine(duration)
                results[device.device_id] = mined_amount
            except Exception as e:
                print(f"Error with device {device.device_id}: {e}")

        return results

    def calculate_total_energy_consumption(self, duration: int) -> float:
        """
        Calculate the total energy consumption during mining.

        :param duration: Duration of the mining operation in seconds.
        :return: Total energy consumed by all devices in watt-hours.
        """
        total_consumption = sum(device.energy_efficiency * (duration / 3600) for device in self.devices)
        return total_consumption


# Example usage
if __name__ == "__main__":
    # Create a list of Aethir Edge devices
    devices = [
        AethirEdgeDevice("Device1", processing_power=1000, energy_efficiency=150),
        AethirEdgeDevice("Device2", processing_power=1500, energy_efficiency=200),
        AethirEdgeDevice("Device3", processing_power=1200, energy_efficiency=180),
    ]

    # Initialize the mining simulation
    simulation = MiningSimulation(devices)

    # Define the duration for mining in seconds
    mining_duration = 3600  # 1 hour

    # Run the simulation
    mined_results = simulation.run_simulation(mining_duration)
    total_energy = simulation.calculate_total_energy_consumption(mining_duration)

    # Output the results
    print("Mining Results:")
    for device_id, amount in mined_results.items():
        print(f"{device_id}: {amount:.2f} cryptocurrency mined")

    print(f"Total Energy Consumption: {total_energy:.2f} watt-hours")
```
