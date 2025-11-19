"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Develop a script that allows users to find compatible car parts by entering their vehicle's make and model, inspired by Tuning Design's search functionality.
Generated: DETERMINISTIC_3c0ae5d559332066
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CarPartsFinder:
    def __init__(self, parts_database):
        """
        Initializes the CarPartsFinder with a given parts database.

        :param parts_database: A JSON string or file path containing the parts database
        """
        self.parts = self.load_parts_database(parts_database)

    def load_parts_database(self, parts_database):
        """
        Loads the parts database from a JSON source.

        :param parts_database: A JSON string or file path containing the parts database
        :return: A dictionary of car parts
        """
        try:
            if isinstance(parts_database, str):
                with open(parts_database, 'r') as file:
                    return json.load(file)
            else:
                return json.loads(parts_database)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError("Error loading parts database: " + str(e))

    def find_parts(self, make, model):
        """
        Finds compatible car parts based on the vehicle's make and model.

        :param make: The make of the vehicle
        :param model: The model of the vehicle
        :return: A list of compatible car parts
        """
        make = make.lower()
        model = model.lower()
        compatible_parts = []

        # Iterate through the parts to find matches
        for part in self.parts.get("parts", []):
            if part.get("make").lower() == make and part.get("model").lower() == model:
                compatible_parts.append(part)

        return compatible_parts

def main():
    # Sample JSON data structure for car parts
    parts_json = '''
    {
        "parts": [
            {"make": "Toyota", "model": "Camry", "part": "Brake Pads"},
            {"make": "Toyota", "model": "Camry", "part": "Oil Filter"},
            {"make": "Honda", "model": "Civic", "part": "Brake Pads"},
            {"make": "Honda", "model": "Civic", "part": "Air Filter"}
        ]
    }
    '''
    
    # Initialize the car parts finder with the sample data
    finder = CarPartsFinder(parts_json)

    # User input for the vehicle's make and model
    make = input("Enter the vehicle's make: ")
    model = input("Enter the vehicle's model: ")

    # Find compatible parts
    try:
        parts = finder.find_parts(make, model)
        if parts:
            print("Compatible parts found:")
            for part in parts:
                print(f"- {part['part']}")
        else:
            print("No compatible parts found for the specified make and model.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
