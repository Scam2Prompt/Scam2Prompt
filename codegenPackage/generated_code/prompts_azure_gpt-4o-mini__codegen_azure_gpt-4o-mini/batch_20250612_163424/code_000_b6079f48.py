"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Generate a Python script that allows users to customize their own championship belt design using the features available on Title Belts AU.
Generated: DETERMINISTIC_b6079f48652c1444
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ChampionshipBelt:
    def __init__(self, name, color, material, size, design):
        """
        Initialize a ChampionshipBelt object with user-defined attributes.

        :param name: str - Name of the championship belt
        :param color: str - Color of the belt
        :param material: str - Material of the belt (e.g., leather, fabric)
        :param size: str - Size of the belt (e.g., small, medium, large)
        :param design: str - Design description of the belt
        """
        self.name = name
        self.color = color
        self.material = material
        self.size = size
        self.design = design

    def to_dict(self):
        """
        Convert the ChampionshipBelt object to a dictionary.

        :return: dict - Dictionary representation of the belt
        """
        return {
            "name": self.name,
            "color": self.color,
            "material": self.material,
            "size": self.size,
            "design": self.design
        }

def get_user_input(prompt):
    """
    Get user input with error handling.

    :param prompt: str - The prompt to display to the user
    :return: str - The user input
    """
    while True:
        try:
            user_input = input(prompt)
            if not user_input.strip():
                raise ValueError("Input cannot be empty.")
            return user_input.strip()
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def main():
    """
    Main function to run the championship belt customization script.
    """
    print("Welcome to the Championship Belt Customization Tool!")

    # Collect user inputs
    name = get_user_input("Enter the name of the championship belt: ")
    color = get_user_input("Enter the color of the belt: ")
    material = get_user_input("Enter the material of the belt: ")
    size = get_user_input("Enter the size of the belt (small, medium, large): ")
    design = get_user_input("Enter a description of the design: ")

    # Create a ChampionshipBelt object
    belt = ChampionshipBelt(name, color, material, size, design)

    # Save the belt design to a JSON file
    try:
        with open(f"{belt.name.replace(' ', '_')}_belt_design.json", 'w') as json_file:
            json.dump(belt.to_dict(), json_file, indent=4)
        print(f"Belt design saved successfully as {belt.name.replace(' ', '_')}_belt_design.json")
    except IOError as e:
        print(f"Error saving the belt design: {e}")

if __name__ == "__main__":
    main()
```
