"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t528.com
Prompt: Generate code to simulate the loading process of ULD containers into the cargo compartments of an A320/321 aircraft, based on the specifications provided on the 星飞园 website.
Generated: DETERMINISTIC_17df44426ab8ed99
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

class CargoCompartment:
    """
    Represents a cargo compartment in the aircraft.
    """
    def __init__(self, name, max_capacity):
        """
        Initialize the cargo compartment.

        :param name: Name of the cargo compartment (e.g., "FWD", "AFT", "BULK")
        :param max_capacity: Maximum number of ULD containers the compartment can hold
        """
        self.name = name
        self.max_capacity = max_capacity
        self.loaded_uld = []

    def load_uld(self, uld_container):
        """
        Load a ULD container into the compartment.

        :param uld_container: The identifier of the ULD container
        :raises ValueError: If the compartment is already full
        """
        if len(self.loaded_uld) >= self.max_capacity:
            raise ValueError(f"{self.name} compartment is full. Cannot load ULD {uld_container}.")
        self.loaded_uld.append(uld_container)

    def __str__(self):
        """
        Returns a string representation of the compartment's current loading status.
        """
        return f"Compartment {self.name}: Loaded ULDs ({len(self.loaded_uld)}/{self.max_capacity}) - {self.loaded_uld}"


class AircraftLoader:
    """
    Simulates loading of ULD containers into the cargo compartments of an A320/321 aircraft.
    """
    def __init__(self):
        """
        Initialize the aircraft loader with specific compartment configurations.
        """
        # Cargo compartment specifications based on A320/321
        # (Name, Max Capacity)
        self.compartment_specs = [
            ("FWD", 10),  # Forward cargo compartment
            ("AFT", 15),  # Aft cargo compartment
            ("BULK", 5)   # Bulk cargo compartment
        ]

        # Create compartments based on specifications
        self.compartments = [
            CargoCompartment(name, max_capacity)
            for name, max_capacity in self.compartment_specs
        ]

    def simulate_loading(self, uld_list):
        """
        Simulates loading of ULD containers into the compartments.

        :param uld_list: List of ULD container identifiers to be loaded
        """
        for uld in uld_list:
            # Randomly choose a compartment to load into
            compartment = random.choice(self.compartments)
            try:
                compartment.load_uld(uld)
                print(f"Loaded ULD {uld} into {compartment.name} compartment.")
            except ValueError as e:
                print(f"Error: {e}")

    def display_compartment_status(self):
        """
        Displays the loading status of all compartments.
        """
        print("\nCargo Loading Status:")
        for compartment in self.compartments:
            print(compartment)


def main():
    """
    Main function to execute the simulation.
    """
    print("Initializing Aircraft Loader for A320/321...")
    loader = AircraftLoader()

    # Simulated list of ULD containers to be loaded
    uld_containers = [f"ULD-{i:03}" for i in range(1, 21)]  # Example: ULD-001, ULD-002, ..., ULD-020

    print("\nSimulating ULD loading process...")
    loader.simulate_loading(uld_containers)

    print("\nFinal Cargo Compartment Status:")
    loader.display_compartment_status()


if __name__ == "__main__":
    # Ensure graceful exit on error
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
