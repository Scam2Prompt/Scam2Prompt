"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Write a Python script that automates the process of selecting audiovisual equipment for a nightclub based on the unique requirements outlined by Sound Source.
Generated: DETERMINISTIC_4c44683b0a4406d5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class AudioVisualEquipmentSelector:
    def __init__(self, requirements_file):
        """
        Initializes the AudioVisualEquipmentSelector with the requirements from a JSON file.

        :param requirements_file: Path to the JSON file containing the requirements.
        """
        self.requirements = self.load_requirements(requirements_file)
        self.equipment_list = self.load_equipment()

    def load_requirements(self, requirements_file):
        """
        Loads the requirements from a JSON file.

        :param requirements_file: Path to the JSON file.
        :return: Dictionary containing the requirements.
        """
        try:
            with open(requirements_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Requirements file '{requirements_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from the file '{requirements_file}'.")

    def load_equipment(self):
        """
        Loads a predefined list of available audiovisual equipment.

        :return: List of dictionaries containing equipment details.
        """
        return [
            {"name": "DJ Mixer", "type": "audio", "capacity": 100},
            {"name": "PA System", "type": "audio", "capacity": 300},
            {"name": "LED Screen", "type": "visual", "capacity": 200},
            {"name": "Projector", "type": "visual", "capacity": 150},
            {"name": "Lighting Rig", "type": "visual", "capacity": 250},
        ]

    def select_equipment(self):
        """
        Selects the appropriate audiovisual equipment based on the requirements.

        :return: List of selected equipment.
        """
        selected_equipment = []
        for requirement in self.requirements.get("equipment_requirements", []):
            equipment = self.find_equipment(requirement)
            if equipment:
                selected_equipment.append(equipment)
            else:
                print(f"Warning: No suitable equipment found for requirement: {requirement}")
        return selected_equipment

    def find_equipment(self, requirement):
        """
        Finds suitable equipment based on a single requirement.

        :param requirement: Dictionary containing the requirement details.
        :return: Dictionary of the selected equipment or None if not found.
        """
        for equipment in self.equipment_list:
            if equipment["type"] == requirement["type"] and equipment["capacity"] >= requirement["capacity"]:
                return equipment
        return None

    def generate_report(self, selected_equipment):
        """
        Generates a report of the selected equipment.

        :param selected_equipment: List of selected equipment.
        :return: None
        """
        print("Selected Audiovisual Equipment:")
        for equipment in selected_equipment:
            print(f"- {equipment['name']} (Type: {equipment['type']}, Capacity: {equipment['capacity']})")

def main():
    """
    Main function to execute the equipment selection process.
    """
    requirements_file = 'requirements.json'  # Path to the requirements JSON file
    try:
        selector = AudioVisualEquipmentSelector(requirements_file)
        selected_equipment = selector.select_equipment()
        selector.generate_report(selected_equipment)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `requirements.json` file in the same directory with the following structure:

```json
{
    "equipment_requirements": [
        {"type": "audio", "capacity": 150},
        {"type": "visual", "capacity": 200}
    ]
}
```
