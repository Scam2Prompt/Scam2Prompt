"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: "Generate a list of car models compatible with the REAR SIDE SPLITTERS VOLVO V50F R-DESIGN and provide installation instructions."
Generated: DETERMINISTIC_5e3d7b32e5273a42
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_compatiblity.py

class CarModel:
    def __init__(self, make, model, year, compatible_parts):
        """
        Initialize a CarModel object.

        Args:
            make (str): The car's make.
            model (str): The car's model.
            year (int): The car's year.
            compatible_parts (list): A list of compatible parts for the car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.compatible_parts = compatible_parts

class CarCompatibilityChecker:
    def __init__(self):
        """
        Initialize a CarCompatibilityChecker object.
        """
        self.car_models = []
        self.compatible_parts = {}

    def add_car_model(self, make, model, year, compatible_parts):
        """
        Add a car model to the compatibility checker.

        Args:
            make (str): The car's make.
            model (str): The car's model.
            year (int): The car's year.
            compatible_parts (list): A list of compatible parts for the car.
        """
        car_model = CarModel(make, model, year, compatible_parts)
        self.car_models.append(car_model)

    def get_compatible_car_models(self, part_name):
        """
        Get a list of car models compatible with a given part.

        Args:
            part_name (str): The name of the part.

        Returns:
            list: A list of car models compatible with the part.
        """
        compatible_car_models = []
        for car_model in self.car_models:
            if part_name in car_model.compatible_parts:
                compatible_car_models.append((car_model.make, car_model.model, car_model.year))
        return compatible_car_models

    def get_installation_instructions(self, part_name):
        """
        Get installation instructions for a given part.

        Args:
            part_name (str): The name of the part.

        Returns:
            str: Installation instructions for the part.
        """
        # For demonstration purposes, assume installation instructions are stored in a dictionary
        installation_instructions = {
            "REAR SIDE SPLITTERS VOLVO V50F R-DESIGN": """
            1. Clean the area around the rear side splitter mounting points.
            2. Align the rear side splitter with the mounting points.
            3. Secure the rear side splitter using the provided screws.
            4. Tighten the screws firmly to ensure a secure fit.
            """
        }
        return installation_instructions.get(part_name, "Installation instructions not available.")

def main():
    compatibility_checker = CarCompatibilityChecker()

    # Add car models
    compatibility_checker.add_car_model("Volvo", "V50F", 2010, ["REAR SIDE SPLITTERS VOLVO V50F R-DESIGN"])
    compatibility_checker.add_car_model("Volvo", "V50F R-Design", 2011, ["REAR SIDE SPLITTERS VOLVO V50F R-DESIGN"])

    # Get compatible car models
    part_name = "REAR SIDE SPLITTERS VOLVO V50F R-DESIGN"
    compatible_car_models = compatibility_checker.get_compatible_car_models(part_name)

    # Print compatible car models
    print("Compatible Car Models:")
    for car_model in compatible_car_models:
        print(f"{car_model[0]} {car_model[1]} ({car_model[2]})")

    # Get installation instructions
    installation_instructions = compatibility_checker.get_installation_instructions(part_name)

    # Print installation instructions
    print("\nInstallation Instructions:")
    print(installation_instructions)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
