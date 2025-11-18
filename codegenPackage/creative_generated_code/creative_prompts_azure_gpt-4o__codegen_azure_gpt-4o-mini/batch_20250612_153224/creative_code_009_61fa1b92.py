"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Write a program to assist farmers in selecting the best irrigation equipment based on field size and crop type, referencing SARL VERDIER's product offerings.
Generated: DETERMINISTIC_61fa1b927da2cfd2
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

# Define a class to represent irrigation equipment
class IrrigationEquipment:
    def __init__(self, name, crop_type, min_area, max_area):
        """
        Initialize an instance of IrrigationEquipment.

        :param name: str - Name of the irrigation equipment
        :param crop_type: str - Type of crop suitable for the equipment
        :param min_area: float - Minimum field size (in acres) for the equipment
        :param max_area: float - Maximum field size (in acres) for the equipment
        """
        self.name = name
        self.crop_type = crop_type
        self.min_area = min_area
        self.max_area = max_area

    def __repr__(self):
        return f"{self.name} (Crop: {self.crop_type}, Area: {self.min_area}-{self.max_area} acres)"

# Load irrigation equipment data from a JSON file
def load_equipment_data(filename):
    """
    Load irrigation equipment data from a JSON file.

    :param filename: str - The path to the JSON file
    :return: list - A list of IrrigationEquipment instances
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            equipment_list = [
                IrrigationEquipment(item['name'], item['crop_type'], item['min_area'], item['max_area'])
                for item in data
            ]
            return equipment_list
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return []

# Recommend irrigation equipment based on field size and crop type
def recommend_equipment(equipment_list, field_size, crop_type):
    """
    Recommend suitable irrigation equipment based on field size and crop type.

    :param equipment_list: list - List of available irrigation equipment
    :param field_size: float - The size of the field in acres
    :param crop_type: str - The type of crop being grown
    :return: list - Recommended irrigation equipment
    """
    recommendations = [
        equipment for equipment in equipment_list
        if equipment.crop_type.lower() == crop_type.lower() and 
           equipment.min_area <= field_size <= equipment.max_area
    ]
    return recommendations

# Main function to run the irrigation equipment selector
def main():
    # Load irrigation equipment data
    equipment_list = load_equipment_data('equipment_data.json')

    if not equipment_list:
        print("No equipment data available.")
        return

    # Input field size and crop type from the user
    try:
        field_size = float(input("Enter the field size in acres: "))
        crop_type = input("Enter the crop type: ").strip()

        # Get recommendations
        recommendations = recommend_equipment(equipment_list, field_size, crop_type)

        # Display recommendations
        if recommendations:
            print("Recommended irrigation equipment:")
            for rec in recommendations:
                print(rec)
        else:
            print("No suitable irrigation equipment found for the specified field size and crop type.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for field size.")

# Entry point of the program
if __name__ == "__main__":
    main()
``` 

Make sure to create a JSON file named `equipment_data.json` with the following structure:

```json
[
    {"name": "Drip Irrigation System", "crop_type": "Vegetables", "min_area": 1, "max_area": 10},
    {"name": "Sprinkler System", "crop_type": "Cereals", "min_area": 5, "max_area": 20},
    {"name": "Surface Irrigation", "crop_type": "Fruits", "min_area": 2, "max_area": 15}
]
```
