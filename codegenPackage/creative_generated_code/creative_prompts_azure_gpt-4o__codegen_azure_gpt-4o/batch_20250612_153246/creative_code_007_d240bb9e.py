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
import datetime
import json

# Plant class to represent individual plants and their maintenance schedule
class Plant:
    def __init__(self, name, species, planting_date, watering_interval, fertilization_interval):
        """
        Initialize a Plant object.

        :param name: str - Name of the plant
        :param species: str - Species of the plant
        :param planting_date: str - Date of planting in YYYY-MM-DD format
        :param watering_interval: int - Watering interval in days
        :param fertilization_interval: int - Fertilization interval in days
        """
        self.name = name
        self.species = species
        self.planting_date = datetime.datetime.strptime(planting_date, "%Y-%m-%d").date()
        self.watering_interval = watering_interval
        self.fertilization_interval = fertilization_interval
        self.last_watered = self.planting_date
        self.last_fertilized = self.planting_date

    def get_next_watering_date(self):
        """
        Calculate the next watering date based on the watering interval.

        :return: datetime.date - Next watering date
        """
        return self.last_watered + datetime.timedelta(days=self.watering_interval)

    def get_next_fertilization_date(self):
        """
        Calculate the next fertilization date based on the fertilization interval.

        :return: datetime.date - Next fertilization date
        """
        return self.last_fertilized + datetime.timedelta(days=self.fertilization_interval)

    def mark_watered(self):
        """
        Update the last watered date to today.
        """
        self.last_watered = datetime.date.today()

    def mark_fertilized(self):
        """
        Update the last fertilized date to today.
        """
        self.last_fertilized = datetime.date.today()

    def to_dict(self):
        """
        Convert the plant object to a dictionary for serialization.

        :return: dict - Dictionary representation of the plant
        """
        return {
            "name": self.name,
            "species": self.species,
            "planting_date": self.planting_date.isoformat(),
            "watering_interval": self.watering_interval,
            "fertilization_interval": self.fertilization_interval,
            "last_watered": self.last_watered.isoformat(),
            "last_fertilized": self.last_fertilized.isoformat(),
        }


# Garden class to manage multiple plants
class Garden:
    def __init__(self):
        """
        Initialize a Garden object to manage plants.
        """
        self.plants = []

    def add_plant(self, plant):
        """
        Add a new plant to the garden.

        :param plant: Plant - Plant object to add
        """
        self.plants.append(plant)

    def get_maintenance_schedule(self):
        """
        Generate a maintenance schedule for all plants.

        :return: list - List of maintenance tasks
        """
        schedule = []
        for plant in self.plants:
            schedule.append({
                "name": plant.name,
                "species": plant.species,
                "next_watering_date": plant.get_next_watering_date(),
                "next_fertilization_date": plant.get_next_fertilization_date(),
            })
        return schedule

    def save_to_file(self, filename):
        """
        Save the garden's plant data to a file in JSON format.

        :param filename: str - Filename to save the data
        """
        try:
            with open(filename, "w") as file:
                json.dump([plant.to_dict() for plant in self.plants], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load plant data from a file.

        :param filename: str - Filename to load the data
        """
        try:
            with open(filename, "r") as file:
                plant_data = json.load(file)
                self.plants = [
                    Plant(
                        data["name"],
                        data["species"],
                        data["planting_date"],
                        data["watering_interval"],
                        data["fertilization_interval"],
                    )
                    for data in plant_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize a garden
    city_garden = Garden()

    # Add plants to the garden
    city_garden.add_plant(Plant("Rose", "Rosa", "2023-01-01", 3, 15))
    city_garden.add_plant(Plant("Tulip", "Tulipa", "2023-02-01", 7, 30))

    # Generate maintenance schedule
    schedule = city_garden.get_maintenance_schedule()
    for task in schedule:
        print(f"Plant: {task['name']}, Species: {task['species']}")
        print(f"  Next Watering Date: {task['next_watering_date']}")
        print(f"  Next Fertilization Date: {task['next_fertilization_date']}")
        print()

    # Save and load garden data
    city_garden.save_to_file("garden_data.json")
    city_garden.load_from_file("garden_data.json")
```
