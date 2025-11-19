"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Generate code to simulate the deployment of a connected home network with multiple devices and environments, taking into account signal strength and stability, as offered by Maxnet's planning and installation service.
Generated: DETERMINISTIC_437781c6b8f63796
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
from typing import List, Dict, Tuple

class Device:
    """Represents a device in the connected home network."""
    
    def __init__(self, name: str, position: Tuple[float, float], signal_strength: float):
        self.name = name
        self.position = position  # (x, y) coordinates
        self.signal_strength = signal_strength  # Signal strength in dBm

    def __repr__(self):
        return f"Device(name={self.name}, position={self.position}, signal_strength={self.signal_strength})"

class Environment:
    """Represents an environment containing multiple devices."""
    
    def __init__(self, name: str):
        self.name = name
        self.devices: List[Device] = []

    def add_device(self, device: Device):
        """Adds a device to the environment."""
        self.devices.append(device)

    def calculate_average_signal_strength(self) -> float:
        """Calculates the average signal strength of all devices in the environment."""
        if not self.devices:
            return 0.0
        total_strength = sum(device.signal_strength for device in self.devices)
        return total_strength / len(self.devices)

    def __repr__(self):
        return f"Environment(name={self.name}, devices={self.devices})"

class NetworkSimulator:
    """Simulates a connected home network with multiple environments and devices."""
    
    def __init__(self):
        self.environments: Dict[str, Environment] = {}

    def add_environment(self, environment: Environment):
        """Adds an environment to the network simulator."""
        self.environments[environment.name] = environment

    def simulate_signal_strength(self, device: Device) -> float:
        """Simulates the signal strength of a device based on its position."""
        # Simulate signal strength based on random factors and distance
        distance = math.sqrt(device.position[0]**2 + device.position[1]**2)
        noise_factor = random.uniform(-5, 5)  # Random noise in dBm
        simulated_strength = device.signal_strength - (20 * math.log10(distance + 1)) + noise_factor
        return max(simulated_strength, -100)  # Minimum signal strength

    def run_simulation(self):
        """Runs the network simulation and outputs the results."""
        for env_name, environment in self.environments.items():
            print(f"Environment: {env_name}")
            avg_signal = environment.calculate_average_signal_strength()
            print(f"Average Signal Strength: {avg_signal:.2f} dBm")
            for device in environment.devices:
                simulated_strength = self.simulate_signal_strength(device)
                print(f"Device: {device.name}, Simulated Signal Strength: {simulated_strength:.2f} dBm")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        # Create a network simulator
        network_simulator = NetworkSimulator()

        # Create environments
        living_room = Environment("Living Room")
        kitchen = Environment("Kitchen")

        # Add devices to the living room
        living_room.add_device(Device("Smart TV", (2, 3), -50))
        living_room.add_device(Device("Smart Speaker", (1, 1), -45))

        # Add devices to the kitchen
        kitchen.add_device(Device("Smart Fridge", (4, 5), -60))
        kitchen.add_device(Device("Smart Oven", (3, 2), -55))

        # Add environments to the network simulator
        network_simulator.add_environment(living_room)
        network_simulator.add_environment(kitchen)

        # Run the simulation
        network_simulator.run_simulation()

    except Exception as e:
        print(f"An error occurred: {e}")
```
