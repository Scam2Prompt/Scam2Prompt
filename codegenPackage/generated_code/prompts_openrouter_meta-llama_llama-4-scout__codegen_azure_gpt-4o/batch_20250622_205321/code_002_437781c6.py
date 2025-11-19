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

class Device:
    """
    Represents a device in the connected home network.
    """
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.signal_strength = 0  # Signal strength in percentage (0-100)
        self.stability = 0  # Stability in percentage (0-100)

    def update_signal(self, base_signal_strength):
        """
        Updates the signal strength based on the base signal strength and location.
        """
        # Simulate signal strength degradation based on distance from router
        distance_factor = random.uniform(0.7, 1.0) if self.location == "near" else random.uniform(0.4, 0.7)
        self.signal_strength = int(base_signal_strength * distance_factor)

    def update_stability(self):
        """
        Updates the stability based on signal strength.
        """
        # Simulate stability as a function of signal strength
        self.stability = int(self.signal_strength * random.uniform(0.8, 1.0))

    def __str__(self):
        return f"Device: {self.name}, Location: {self.location}, Signal Strength: {self.signal_strength}%, Stability: {self.stability}%"


class HomeNetwork:
    """
    Represents the connected home network.
    """
    def __init__(self, base_signal_strength=100):
        self.devices = []
        self.base_signal_strength = base_signal_strength  # Base signal strength from the router

    def add_device(self, name, location):
        """
        Adds a new device to the network.
        """
        if location not in ["near", "far"]:
            raise ValueError("Invalid location. Must be 'near' or 'far'.")
        device = Device(name, location)
        self.devices.append(device)

    def simulate_network(self):
        """
        Simulates the network by updating signal strength and stability for all devices.
        """
        for device in self.devices:
            device.update_signal(self.base_signal_strength)
            device.update_stability()

    def display_network_status(self):
        """
        Displays the status of all devices in the network.
        """
        print("Home Network Status:")
        for device in self.devices:
            print(device)


# Main function to simulate the deployment of a connected home network
def main():
    try:
        # Initialize the home network
        home_network = HomeNetwork(base_signal_strength=100)

        # Add devices to the network
        home_network.add_device("Smart Thermostat", "near")
        home_network.add_device("Security Camera", "far")
        home_network.add_device("Smart Speaker", "near")
        home_network.add_device("Smart Light", "far")

        # Simulate the network
        home_network.simulate_network()

        # Display the network status
        home_network.display_network_status()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
