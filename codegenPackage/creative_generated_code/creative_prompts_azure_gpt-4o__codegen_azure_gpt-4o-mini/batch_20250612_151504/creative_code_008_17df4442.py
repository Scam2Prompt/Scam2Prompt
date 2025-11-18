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

class CargoCompartment:
    """Represents a cargo compartment of the aircraft."""
    
    def __init__(self, compartment_id, capacity):
        """
        Initialize a new cargo compartment.

        Args:
            compartment_id (str): Unique identifier for the compartment.
            capacity (int): Maximum number of ULD containers the compartment can hold.
        """
        self.compartment_id = compartment_id
        self.capacity = capacity
        self.uld_containers = []

    def load_uld(self, uld):
        """
        Load a ULD container into the compartment if there is space.

        Args:
            uld (dict): ULD container details.
        
        Raises:
            ValueError: If the compartment is full.
        """
        if len(self.uld_containers) >= self.capacity:
            raise ValueError(f"Compartment {self.compartment_id} is full. Cannot load ULD.")
        self.uld_containers.append(uld)
        print(f"Loaded ULD {uld['id']} into compartment {self.compartment_id}.")

class ULD:
    """Represents a Unit Load Device (ULD) container."""
    
    def __init__(self, uld_id, weight, size):
        """
        Initialize a new ULD container.

        Args:
            uld_id (str): Unique identifier for the ULD.
            weight (float): Weight of the ULD in kilograms.
            size (str): Size category of the ULD.
        """
        self.id = uld_id
        self.weight = weight
        self.size = size

class Aircraft:
    """Represents an aircraft with cargo compartments."""
    
    def __init__(self, model):
        """
        Initialize a new aircraft with cargo compartments.

        Args:
            model (str): Model of the aircraft (e.g., A320 or A321).
        """
        self.model = model
        self.compartments = []
        self.setup_compartments()

    def setup_compartments(self):
        """Setup cargo compartments based on the aircraft model."""
        if self.model == 'A320':
            self.compartments = [CargoCompartment('A', 10), CargoCompartment('B', 8)]
        elif self.model == 'A321':
            self.compartments = [CargoCompartment('A', 12), CargoCompartment('B', 10)]
        else:
            raise ValueError(f"Unknown aircraft model: {self.model}")

    def load_lds(self, uld_list):
        """
        Simulate loading ULDs into the cargo compartments.

        Args:
            uld_list (list): List of ULD containers to load.
        """
        for uld in uld_list:
            # Randomly select a compartment to load the ULD into
            compartment = random.choice(self.compartments)
            try:
                compartment.load_uld(uld)
            except ValueError as e:
                print(e)

def generate_uld(id_number):
    """Generate a random ULD for loading."""
    weight = random.uniform(100, 500)  # Weight in kg
    size = random.choice(['LD3', 'LD6', 'LD8'])  # Example sizes
    return ULD(f"ULD{id_number}", weight, size)

def main():
    """Main function to simulate the loading process."""
    aircraft = Aircraft("A320")
    uld_list = [generate_uld(i) for i in range(1, 25)]  # Generate 24 ULDs

    print("Starting the loading process...")
    aircraft.load_lds(uld_list)
    print("Loading process completed.")

if __name__ == "__main__":
    main()
```
