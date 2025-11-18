"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Write Python code to simulate the installation process of rain harvesting tanks, including electric pumps and filtration systems, as described by Alphamor’s AQUA ALPHA service.
Generated: DETERMINISTIC_1d4836440a1bdb8e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class RainHarvestingSystem:
    """Class to simulate the installation process of rain harvesting tanks, pumps, and filtration systems."""

    def __init__(self, tank_capacity: float, pump_power: float):
        """
        Initializes the RainHarvestingSystem with specified tank capacity and pump power.
        
        :param tank_capacity: Capacity of the rain harvesting tank in liters.
        :param pump_power: Power of the electric pump in watts.
        """
        self.tank_capacity = tank_capacity
        self.pump_power = pump_power
        self.is_installed = False
        self.is_operational = False
        self.water_collected = 0.0

    def install_system(self):
        """Simulates the installation of the rain harvesting system."""
        try:
            self.check_components()
            self.is_installed = True
            print("Rain harvesting system installed successfully.")
        except Exception as e:
            print(f"Installation failed: {e}")
            self.is_installed = False

    def check_components(self):
        """Checks if the necessary components are available for installation."""
        if self.tank_capacity <= 0:
            raise ValueError("Tank capacity must be greater than zero.")
        if self.pump_power <= 0:
            raise ValueError("Pump power must be greater than zero.")

    def simulate_rainfall(self, rainfall_amount: float):
        """
        Simulates the collection of rainwater based on rainfall amount.
        
        :param rainfall_amount: Amount of rainwater collected in liters.
        """
        if not self.is_installed:
            raise RuntimeError("System must be installed before simulating rainfall.")
        
        self.water_collected += rainfall_amount
        print(f"Collected {rainfall_amount} liters of rainwater.")
        self.water_collected = min(self.water_collected, self.tank_capacity)
        
        if self.water_collected == self.tank_capacity:
            print("Tank is full! Consider using the collected rainwater.")

    def install_filtration_system(self):
        """Simulates the installation of the filtration system."""
        try:
            if not self.is_installed:
                raise RuntimeError("System must be installed before adding filtration.")
            self.is_operational = True
            print("Filtration system installed and operational.")
        except Exception as e:
            print(f"Filtration installation failed: {e}")

    def operate_pump(self):
        """Simulates the operation of the electric pump to move filtered water."""
        if not self.is_operational:
            raise RuntimeError("Filtration system must be operational to operate the pump.")
        
        if self.water_collected > 0:
            used_water = random.uniform(0.1, 0.5 * self.water_collected)
            self.water_collected -= used_water
            print(f"Pump operated: {used_water:.2f} liters of water used.")
        else:
            print("No water available to pump.")

# Example Usage
if __name__ == "__main__":
    try:
        # Create a rain harvesting system
        system = RainHarvestingSystem(tank_capacity=1000.0, pump_power=200.0)

        # Install the system
        system.install_system()

        # Simulate rainfall
        system.simulate_rainfall(300.0)
        system.simulate_rainfall(800.0)  # Should fill the tank to capacity

        # Install the filtration system
        system.install_filtration_system()

        # Operate the pump to use some collected water
        for _ in range(3):
            system.operate_pump()

    except Exception as e:
        print(f"An error occurred: {e}")
```
