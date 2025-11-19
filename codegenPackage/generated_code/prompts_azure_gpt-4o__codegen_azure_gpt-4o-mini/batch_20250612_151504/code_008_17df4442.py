"""
Generated Code Metadata:
========================
Original URL: https://t528.com
Prompt: Generate code to simulate the loading process of ULD containers into the cargo compartments of an A320/321 aircraft, based on the specifications provided on the 星飞园 website.
Generated: DETERMINISTIC_17df44426ab8ed99
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class ULDContainer:
    """Class representing a ULD (Unit Load Device) container."""
    
    def __init__(self, id: str, weight: float, volume: float):
        """
        Initialize a ULD container.

        :param id: Unique identifier for the ULD container.
        :param weight: Weight of the ULD container in kilograms.
        :param volume: Volume of the ULD container in cubic meters.
        """
        self.id = id
        self.weight = weight
        self.volume = volume

class CargoCompartment:
    """Class representing a cargo compartment in an aircraft."""
    
    def __init__(self, max_weight: float, max_volume: float):
        """
        Initialize a cargo compartment.

        :param max_weight: Maximum weight capacity of the compartment in kilograms.
        :param max_volume: Maximum volume capacity of the compartment in cubic meters.
        """
        self.max_weight = max_weight
        self.max_volume = max_volume
        self.current_weight = 0.0
        self.current_volume = 0.0
        self.containers: List[ULDContainer] = []

    def load_container(self, container: ULDContainer) -> bool:
        """
        Load a ULD container into the cargo compartment.

        :param container: The ULD container to be loaded.
        :return: True if the container was loaded successfully, False otherwise.
        """
        if self.current_weight + container.weight > self.max_weight:
            print(f"Cannot load container {container.id}: Exceeds weight limit.")
            return False
        if self.current_volume + container.volume > self.max_volume:
            print(f"Cannot load container {container.id}: Exceeds volume limit.")
            return False
        
        # Load the container
        self.containers.append(container)
        self.current_weight += container.weight
        self.current_volume += container.volume
        print(f"Container {container.id} loaded successfully.")
        return True

def simulate_loading_process(containers: List[ULDContainer], compartment: CargoCompartment) -> None:
    """
    Simulate the loading process of ULD containers into a cargo compartment.

    :param containers: List of ULD containers to be loaded.
    :param compartment: The cargo compartment where containers will be loaded.
    """
    for container in containers:
        success = compartment.load_container(container)
        if not success:
            print(f"Failed to load container {container.id}.")

def main():
    """Main function to run the loading simulation."""
    # Define cargo compartment specifications for A320/321
    a320_compartment = CargoCompartment(max_weight=10000.0, max_volume=50.0)  # Example values

    # Generate sample ULD containers
    containers = [
        ULDContainer(id=f"ULD-{i}", weight=random.uniform(100.0, 500.0), volume=random.uniform(0.5, 2.0))
        for i in range(1, 11)  # Create 10 sample containers
    ]

    # Simulate the loading process
    simulate_loading_process(containers, a320_compartment)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
