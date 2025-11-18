"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Write code to model the impact of small hydroelectric plants on biodiversity, referencing the environmental advocacy efforts of "Čuvari Šare."
Generated: DETERMINISTIC_f084244fb04681c1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Class to represent a small hydroelectric plant
class HydroelectricPlant:
    def __init__(self, name, location, water_flow_rate, operational_status):
        """
        Initialize a hydroelectric plant object.

        Args:
            name (str): Name of the plant.
            location (str): Geographical location of the plant.
            water_flow_rate (float): The rate of water flow (cubic meters per second).
            operational_status (bool): Whether the plant is operational or inactive.
        """
        self.name = name
        self.location = location
        self.water_flow_rate = water_flow_rate
        self.operational_status = operational_status

# Class to model biodiversity impact
class BiodiversityImpactModel:
    def __init__(self):
        """
        Initialize the biodiversity impact model.
        """
        self.plants = []
        self.biodiversity_data = {}

    def add_plant(self, plant):
        """
        Add a hydroelectric plant to the model.

        Args:
            plant (HydroelectricPlant): A hydroelectric plant object.
        """
        self.plants.append(plant)

    def load_biodiversity_data(self, file_path):
        """
        Load biodiversity data from a JSON file.

        Args:
            file_path (str): Path to the biodiversity data file.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.biodiversity_data = json.load(file)
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON file - {e}")

    def calculate_impact(self):
        """
        Calculate the impact of hydroelectric plants on biodiversity.

        Returns:
            dict: A dictionary detailing biodiversity impact by location.
        """
        impact_by_location = {}
        for plant in self.plants:
            if plant.location in self.biodiversity_data:
                # Example calculation: multiply water flow rate by a biodiversity sensitivity factor
                sensitivity_factor = self.biodiversity_data[plant.location].get("sensitivity_factor", 1)
                impact = plant.water_flow_rate * sensitivity_factor
                impact_by_location[plant.location] = impact
        return impact_by_location

# Class to represent environmental advocacy efforts
class AdvocacyEfforts:
    def __init__(self, organization_name):
        """
        Initialize the advocacy efforts object.

        Args:
            organization_name (str): Name of the advocacy organization.
        """
        self.organization_name = organization_name
        self.efforts = []

    def add_effort(self, description, location):
        """
        Add an advocacy effort.

        Args:
            description (str): Description of the effort.
            location (str): Location where the advocacy effort is being implemented.
        """
        self.efforts.append({"description": description, "location": location})

    def get_efforts(self):
        """
        Get all advocacy efforts.

        Returns:
            list: List of advocacy efforts.
        """
        return self.efforts


# Main program
if __name__ == "__main__":
    # Initialize the biodiversity impact model
    model = BiodiversityImpactModel()

    # Load biodiversity data (example JSON file path)
    model.load_biodiversity_data("biodiversity_data.json")

    # Add hydroelectric plants to the model
    model.add_plant(HydroelectricPlant("Plant A", "River X", 50.0, True))
    model.add_plant(HydroelectricPlant("Plant B", "River Y", 30.0, False))

    # Calculate and display impacts
    impacts = model.calculate_impact()
    print("Biodiversity impacts by location:")
    for location, impact in impacts.items():
        print(f"  {location}: {impact}")

    # Initialize advocacy efforts
    advocacy = AdvocacyEfforts("Čuvari Šare")
    advocacy.add_effort("Organized community cleanup", "River X")
    advocacy.add_effort("Petition against new hydroelectric plant", "River Y")

    print("\nAdvocacy efforts by Čuvari Šare:")
    for effort in advocacy.get_efforts():
        print(f"  {effort['location']}: {effort['description']}")
```
