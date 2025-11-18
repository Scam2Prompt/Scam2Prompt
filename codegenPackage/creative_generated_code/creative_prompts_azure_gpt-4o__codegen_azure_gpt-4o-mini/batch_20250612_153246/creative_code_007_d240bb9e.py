"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citygardenmexico.com.mx
Prompt: Create a script to track the growth and maintenance schedule of plants supplied by City Garden México, including fertilization and watering reminders.
Generated: DETERMINISTIC_d240bb9ead37c68a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from typing import List, Dict

class Plant:
    """
    Represents a plant with its growth information and maintenance schedule.
    """
    
    def __init__(self, name: str, watering_frequency: int, fertilization_frequency: int):
        """
        Initialize a new Plant instance.
        
        :param name: The name of the plant.
        :param watering_frequency: The frequency of watering in days.
        :param fertilization_frequency: The frequency of fertilization in days.
        """
        self.name = name
        self.watering_frequency = watering_frequency
        self.fertilization_frequency = fertilization_frequency
        self.last_watered = datetime.datetime.now()
        self.last_fertilized = datetime.datetime.now()

    def water(self):
        """
        Water the plant and update the last watered date.
        """
        self.last_watered = datetime.datetime.now()
        print(f"{self.name} has been watered on {self.last_watered.strftime('%Y-%m-%d')}.")

    def fertilize(self):
        """
        Fertilize the plant and update the last fertilized date.
        """
        self.last_fertilized = datetime.datetime.now()
        print(f"{self.name} has been fertilized on {self.last_fertilized.strftime('%Y-%m-%d')}.")

    def needs_watering(self) -> bool:
        """
        Check if the plant needs watering.
        
        :return: True if the plant needs watering, False otherwise.
        """
        return (datetime.datetime.now() - self.last_watered).days >= self.watering_frequency

    def needs_fertilization(self) -> bool:
        """
        Check if the plant needs fertilization.
        
        :return: True if the plant needs fertilization, False otherwise.
        """
        return (datetime.datetime.now() - self.last_fertilized).days >= self.fertilization_frequency


class Garden:
    """
    Represents a garden containing multiple plants.
    """
    
    def __init__(self):
        """ Initialize a new Garden instance with an empty plant list. """
        self.plants: List[Plant] = []

    def add_plant(self, plant: Plant):
        """
        Add a plant to the garden.
        
        :param plant: An instance of Plant to be added to the garden.
        """
        self.plants.append(plant)
        print(f"{plant.name} has been added to the garden.")

    def check_maintenance(self) -> Dict[str, str]:
        """
        Check the maintenance needs of all plants in the garden.
        
        :return: A dictionary mapping plant names to their maintenance needs.
        """
        maintenance_schedule = {}
        for plant in self.plants:
            needs = []
            if plant.needs_watering():
                needs.append('Water')
            if plant.needs_fertilization():
                needs.append('Fertilize')
            maintenance_schedule[plant.name] = ", ".join(needs) if needs else "No maintenance needed."
        
        return maintenance_schedule

    def save_garden(self, filename: str):
        """
        Save the current state of the garden to a JSON file.
        
        :param filename: The name of the file to save the garden data.
        """
        garden_data = {
            "plants": [
                {
                    "name": plant.name,
                    "last_watered": plant.last_watered.isoformat(),
                    "last_fertilized": plant.last_fertilized.isoformat()
                }
                for plant in self.plants
            ]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(garden_data, f, indent=4)
            print(f"Garden data has been saved to {filename}.")
        except IOError as e:
            print(f"Error saving garden data: {e}")

    def load_garden(self, filename: str):
        """
        Load the garden state from a JSON file.
        
        :param filename: The name of the file to load the garden data from.
        """
        try:
            with open(filename, 'r') as f:
                garden_data = json.load(f)
                self.plants = [
                    Plant(
                        name=plant['name'],
                        watering_frequency=7,  # Default value, adjust as needed
                        fertilization_frequency=30  # Default value, adjust as needed
                    )
                    for plant in garden_data['plants']
                ]
                for plant, data in zip(self.plants, garden_data['plants']):
                    plant.last_watered = datetime.datetime.fromisoformat(data['last_watered'])
                    plant.last_fertilized = datetime.datetime.fromisoformat(data['last_fertilized'])
            print(f"Garden data has been loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading garden data: {e}")


if __name__ == "__main__":
    # Example usage of the Garden and Plant classes.
    my_garden = Garden()
    my_garden.add_plant(Plant(name="Fern", watering_frequency=3, fertilization_frequency=14))
    my_garden.add_plant(Plant(name="Cactus", watering_frequency=14, fertilization_frequency=60))
    
    # Check maintenance schedule
    maintenance_needs = my_garden.check_maintenance()
    for plant_name, needs in maintenance_needs.items():
        print(f"{plant_name}: {needs}")
    
    # Save garden state to JSON
    my_garden.save_garden("my_garden.json")
    
    # Load garden state from JSON
    my_garden.load_garden("my_garden.json")
```
