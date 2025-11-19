"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: Develop a script that allows users to find compatible car parts by entering their vehicle's make and model, inspired by Tuning Design's search functionality.
Generated: DETERMINISTIC_3c0ae5d559332066
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_parts_finder.py

class CarPart:
    def __init__(self, part_number, part_name, make, model, year):
        """
        Initialize a CarPart object.

        Args:
            part_number (str): Unique part number.
            part_name (str): Name of the car part.
            make (str): Vehicle make.
            model (str): Vehicle model.
            year (int): Vehicle year.
        """
        self.part_number = part_number
        self.part_name = part_name
        self.make = make
        self.model = model
        self.year = year

class CarPartsDatabase:
    def __init__(self):
        """
        Initialize an empty car parts database.
        """
        self.parts = []

    def add_part(self, part):
        """
        Add a car part to the database.

        Args:
            part (CarPart): CarPart object to add.
        """
        self.parts.append(part)

    def find_compatible_parts(self, make, model):
        """
        Find compatible car parts for a given vehicle make and model.

        Args:
            make (str): Vehicle make.
            model (str): Vehicle model.

        Returns:
            list: List of compatible CarPart objects.
        """
        return [part for part in self.parts if part.make == make and part.model == model]

def main():
    # Initialize car parts database
    database = CarPartsDatabase()

    # Add some sample car parts
    database.add_part(CarPart("ABC123", "Air Filter", "Toyota", "Camry", 2015))
    database.add_part(CarPart("DEF456", "Oil Filter", "Toyota", "Camry", 2015))
    database.add_part(CarPart("GHI789", "Spark Plug", "Honda", "Civic", 2018))

    # Get user input
    make = input("Enter your vehicle's make: ")
    model = input("Enter your vehicle's model: ")

    try:
        # Find compatible car parts
        compatible_parts = database.find_compatible_parts(make, model)

        if compatible_parts:
            print("Compatible car parts:")
            for part in compatible_parts:
                print(f"Part Number: {part.part_number}, Part Name: {part.part_name}")
        else:
            print("No compatible car parts found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
