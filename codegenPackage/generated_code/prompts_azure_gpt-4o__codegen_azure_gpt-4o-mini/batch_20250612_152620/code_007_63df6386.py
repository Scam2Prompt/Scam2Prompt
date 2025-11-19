"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: Write code to model the high-voltage weed removal process described by Zasso's ElectroherbTM technology, ensuring the simulation accounts for systemic root and shoot elimination.
Generated: DETERMINISTIC_63df63864efc7d7e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Plant:
    """Class representing a plant with roots and shoots."""
    
    def __init__(self, name, root_depth, shoot_height):
        """
        Initialize a plant with a name, root depth, and shoot height.
        
        :param name: str - The name of the plant
        :param root_depth: float - The depth of the plant's roots in meters
        :param shoot_height: float - The height of the plant's shoots in meters
        """
        self.name = name
        self.root_depth = root_depth
        self.shoot_height = shoot_height
        self.is_alive = True

    def eliminate(self):
        """Simulate the elimination of the plant's roots and shoots."""
        if self.is_alive:
            self.is_alive = False
            print(f"{self.name} has been eliminated.")
        else:
            print(f"{self.name} is already dead.")

class Electroherb:
    """Class representing the Electroherb technology for weed removal."""
    
    def __init__(self, voltage):
        """
        Initialize the Electroherb with a specific voltage.
        
        :param voltage: float - The voltage used for the weed removal process
        """
        self.voltage = voltage

    def apply(self, plant):
        """
        Apply the Electroherb technology to a plant.
        
        :param plant: Plant - The plant to be eliminated
        """
        if not isinstance(plant, Plant):
            raise ValueError("The object must be an instance of Plant.")
        
        # Simulate the effectiveness of the voltage on the plant
        success_chance = self.calculate_success_chance(plant)
        
        if random.random() < success_chance:
            plant.eliminate()
        else:
            print(f"{plant.name} resisted the treatment.")

    def calculate_success_chance(self, plant):
        """
        Calculate the success chance of the treatment based on plant characteristics.
        
        :param plant: Plant - The plant to be treated
        :return: float - The success chance as a value between 0 and 1
        """
        # Simple model: deeper roots and taller shoots reduce success chance
        base_chance = 0.8  # Base success chance
        depth_factor = max(0, 1 - (plant.root_depth / 10))  # Roots deeper than 10m reduce chance
        height_factor = max(0, 1 - (plant.shoot_height / 5))  # Shoots taller than 5m reduce chance
        
        success_chance = base_chance * depth_factor * height_factor
        return success_chance

def main():
    """Main function to simulate the weed removal process."""
    # Create instances of plants
    plants = [
        Plant("Dandelion", root_depth=0.5, shoot_height=0.3),
        Plant("Thistle", root_depth=1.0, shoot_height=0.8),
        Plant("Bindweed", root_depth=2.0, shoot_height=1.5),
        Plant("Giant Hogweed", root_depth=3.0, shoot_height=4.0)
    ]
    
    # Create an instance of Electroherb
    electroherb = Electroherb(voltage=10000)  # 10kV for the treatment

    # Apply the Electroherb treatment to each plant
    for plant in plants:
        electroherb.apply(plant)

if __name__ == "__main__":
    main()
```
