"""
Generated Code Metadata:
========================
Original URL: https://fullmoonbird-next.vercel.app
Prompt: Generate code to create a Bird Builder application that allows users to customize bird accessories and body types.
Generated: DETERMINISTIC_7a83eed77aedeeb9
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bird_builder.py

from enum import Enum
from typing import List

class BirdBodyType(str, Enum):
    """Enum for bird body types."""
    ROBIN = "Robin"
    SPARROW = "Sparrow"
    FALCON = "Falcon"
    CUSTOM = "Custom"

class BirdAccessory(str, Enum):
    """Enum for bird accessories."""
    NEST = "Nest"
    FOOD = "Food"
    WATER = "Water"
    SHELTER = "Shelter"

class Bird:
    """Class representing a bird."""
    def __init__(self, name: str, body_type: BirdBodyType):
        self.name = name
        self.body_type = body_type
        self.accessories: List[BirdAccessory] = []

    def add_accessory(self, accessory: BirdAccessory):
        """Add an accessory to the bird."""
        self.accessories.append(accessory)

    def remove_accessory(self, accessory: BirdAccessory):
        """Remove an accessory from the bird."""
        if accessory in self.accessories:
            self.accessories.remove(accessory)

    def __str__(self):
        return f"Bird '{self.name}' - Body Type: {self.body_type.value}, Accessories: {[accessory.value for accessory in self.accessories]}"

class BirdBuilder:
    """Class for building birds."""
    def __init__(self):
        self.birds: List[Bird] = []

    def create_bird(self, name: str, body_type: BirdBodyType):
        """Create a new bird."""
        bird = Bird(name, body_type)
        self.birds.append(bird)
        return bird

    def get_bird(self, name: str):
        """Get a bird by name."""
        for bird in self.birds:
            if bird.name == name:
                return bird
        return None

def main():
    try:
        builder = BirdBuilder()

        print("Bird Builder Application")
        print("------------------------")

        while True:
            print("1. Create Bird")
            print("2. Add Accessory")
            print("3. Remove Accessory")
            print("4. List Birds")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter bird name: ")
                print("Select body type:")
                print("1. Robin")
                print("2. Sparrow")
                print("3. Falcon")
                print("4. Custom")
                body_type_choice = input("Choose an option: ")
                if body_type_choice == "1":
                    body_type = BirdBodyType.ROBIN
                elif body_type_choice == "2":
                    body_type = BirdBodyType.SPARROW
                elif body_type_choice == "3":
                    body_type = BirdBodyType.FALCON
                elif body_type_choice == "4":
                    body_type = BirdBodyType.CUSTOM
                    body_type_value = input("Enter custom body type: ")
                    body_type = BirdBodyType(body_type_value)
                else:
                    print("Invalid option. Please choose a valid option.")
                    continue
                bird = builder.create_bird(name, body_type)
                print(f"Bird '{name}' created with body type {body_type.value}")

            elif choice == "2":
                name = input("Enter bird name: ")
                bird = builder.get_bird(name)
                if bird:
                    print("Select accessory:")
                    print("1. Nest")
                    print("2. Food")
                    print("3. Water")
                    print("4. Shelter")
                    accessory_choice = input("Choose an option: ")
                    if accessory_choice == "1":
                        accessory = BirdAccessory.NEST
                    elif accessory_choice == "2":
                        accessory = BirdAccessory.FOOD
                    elif accessory_choice == "3":
                        accessory = BirdAccessory.WATER
                    elif accessory_choice == "4":
                        accessory = BirdAccessory.SHELTER
                    else:
                        print("Invalid option. Please choose a valid option.")
                        continue
                    bird.add_accessory(accessory)
                    print(f"Accessory {accessory.value} added to bird '{name}'")
                else:
                    print("Bird not found.")

            elif choice == "3":
                name = input("Enter bird name: ")
                bird = builder.get_bird(name)
                if bird:
                    if bird.accessories:
                        print("Select accessory to remove:")
                        for i, accessory in enumerate(bird.accessories):
                            print(f"{i+1}. {accessory.value}")
                        accessory_choice = input("Choose an option: ")
                        try:
                            accessory_choice = int(accessory_choice)
                            if 1 <= accessory_choice <= len(bird.accessories):
                                bird.remove_accessory(bird.accessories[accessory_choice - 1])
                                print(f"Accessory removed from bird '{name}'")
                            else:
                                print("Invalid option. Please choose a valid option.")
                        except ValueError:
                            print("Invalid option. Please choose a valid option.")
                    else:
                        print("No accessories to remove.")
                else:
                    print("Bird not found.")

            elif choice == "4":
                if builder.birds:
                    for bird in builder.birds:
                        print(bird)
                else:
                    print("No birds created.")

            elif choice == "5":
                break

            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
