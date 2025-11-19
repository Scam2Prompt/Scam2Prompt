"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: How can I implement a project using Kubitz's flexible sorting conveyor systems for a recycling plant? Provide a sample configuration.
Generated: DETERMINISTIC_a12f2684aef101fe
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Setting up logging for better traceability and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConveyorBelt:
    def __init__(self, belt_id, capacity, speed):
        """
        Initializes a conveyor belt with a specific ID, capacity, and speed.
        
        :param belt_id: Unique identifier for the conveyor belt.
        :param capacity: Maximum capacity of the conveyor belt (in kg).
        :param speed: Speed of the conveyor belt (in m/s).
        """
        self.belt_id = belt_id
        self.capacity = capacity
        self.speed = speed
        self.current_load = 0

    def add_load(self, weight):
        """
        Adds a specific weight to the conveyor belt.

        :param weight: Weight to be added (in kg).
        :raises ValueError: If the weight exceeds the belt's capacity.
        """
        if self.current_load + weight > self.capacity:
            raise ValueError(f"Cannot add load: exceeds capacity of {self.capacity} kg")
        self.current_load += weight
        logging.info(f"Added {weight} kg to {self.belt_id}. Current load: {self.current_load} kg.")

    def remove_load(self, weight):
        """
        Removes a specific weight from the conveyor belt.

        :param weight: Weight to be removed (in kg).
        :raises ValueError: If the weight to remove exceeds the current load.
        """
        if weight > self.current_load:
            raise ValueError(f"Cannot remove load: exceeds current load of {self.current_load} kg")
        self.current_load -= weight
        logging.info(f"Removed {weight} kg from {self.belt_id}. Current load: {self.current_load} kg.")

class SortingSystem:
    def __init__(self):
        """
        Initializes the sorting system with an empty list of conveyor belts.
        """
        self.conveyor_belts = []

    def add_conveyor_belt(self, conveyor_belt):
        """
        Adds a conveyor belt to the sorting system.

        :param conveyor_belt: An instance of ConveyorBelt to be added.
        """
        self.conveyor_belts.append(conveyor_belt)
        logging.info(f"Conveyor belt {conveyor_belt.belt_id} added to the sorting system.")

    def sort_material(self, material_weight, belt_id):
        """
        Sorts material into the specified conveyor belt.

        :param material_weight: Weight of the material to be sorted (in kg).
        :param belt_id: ID of the conveyor belt to which the material will be added.
        :raises ValueError: If the belt_id does not exist or if there's a load capacity issue.
        """
        for belt in self.conveyor_belts:
            if belt.belt_id == belt_id:
                belt.add_load(material_weight)
                return
        raise ValueError(f"Conveyor belt with ID {belt_id} not found.")

def load_configuration(config_file):
    """
    Loads the configuration of conveyor belts from a JSON file.

    :param config_file: Path to the JSON configuration file.
    :return: List of ConveyorBelt instances.
    :raises FileNotFoundError: If the configuration file does not exist.
    :raises json.JSONDecodeError: If the configuration file is not a valid JSON.
    """
    try:
        with open(config_file, 'r') as file:
            config_data = json.load(file)
            conveyor_belts = []
            for belt in config_data['conveyor_belts']:
                conveyor_belt = ConveyorBelt(belt['id'], belt['capacity'], belt['speed'])
                conveyor_belts.append(conveyor_belt)
            return conveyor_belts
    except FileNotFoundError as e:
        logging.error(f"Configuration file not found: {e}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        raise

# Example configuration (can be replaced with an actual file path)
sample_configuration = {
    "conveyor_belts": [
        {"id": "belt_1", "capacity": 1000, "speed": 2.5},
        {"id": "belt_2", "capacity": 1500, "speed": 3.0},
        {"id": "belt_3", "capacity": 800, "speed": 1.5}
    ]
}

# Saving the sample configuration to a JSON file for demonstration purposes
with open('config.json', 'w') as config_file:
    json.dump(sample_configuration, config_file)

# Main execution
if __name__ == "__main__":
    # Load the conveyor belt configuration from a file
    try:
        conveyor_belts = load_configuration('config.json')
        sorting_system = SortingSystem()

        # Add each conveyor belt to the sorting system
        for belt in conveyor_belts:
            sorting_system.add_conveyor_belt(belt)

        # Example of sorting a material
        sorting_system.sort_material(200, 'belt_1')  # Sorts 200 kg to belt_1
        sorting_system.sort_material(500, 'belt_2')  # Sorts 500 kg to belt_2

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
