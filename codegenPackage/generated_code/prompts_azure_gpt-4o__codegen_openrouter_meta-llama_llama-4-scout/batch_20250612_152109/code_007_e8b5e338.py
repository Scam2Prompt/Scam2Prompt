"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: Provide Python code for generating printable origami instructions for Easter crafts, inspired by the easy Easter origami ideas on Craft Intra.
Generated: DETERMINISTIC_e8b5e338b5ae2853
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OrigamiInstruction:
    def __init__(self, name, steps):
        """
        Initialize an OrigamiInstruction object.

        Args:
            name (str): The name of the origami craft.
            steps (list): A list of steps to create the origami craft.
        """
        self.name = name
        self.steps = steps

    def print_instructions(self):
        """
        Print the origami instructions.
        """
        print(f"**{self.name} Origami Instructions**")
        for i, step in enumerate(self.steps, start=1):
            print(f"\n**Step {i}: {step['description']}**")
            print(step['image'] if 'image' in step else "")


class EasterOrigami:
    def __init__(self):
        """
        Initialize an EasterOrigami object with available origami crafts.
        """
        self.origami_crafts = {
            "Easter Bunny": OrigamiInstruction(
                "Easter Bunny",
                [
                    {"description": "Fold a square paper in half diagonally"},
                    {"description": "Open and fold in half again, the other way"},
                    {"description": "Make a small fold for the ear"},
                    {"description": "Fold the bottom half up"},
                    {"description": "Take the top layer and fold it back"},
                ]
            ),
            "Easter Egg": OrigamiInstruction(
                "Easter Egg",
                [
                    {"description": "Start with a square paper"},
                    {"description": "Fold the paper in half"},
                    {"description": "Open and fold in half again, the other way"},
                    {"description": "Make a small fold for the egg shape"},
                    {"description": "Repeat the fold to create the egg shape"},
                ]
            ),
        }

    def get_origami_craft(self, name):
        """
        Get an OrigamiInstruction object by name.

        Args:
            name (str): The name of the origami craft.

        Returns:
            OrigamiInstruction: The OrigamiInstruction object if found, otherwise None.
        """
        return self.origami_crafts.get(name)

    def print_available_crafts(self):
        """
        Print the available Easter origami crafts.
        """
        print("Available Easter Origami Crafts:")
        for craft in self.origami_crafts.keys():
            print(f"- {craft}")


def main():
    try:
        easter_origami = EasterOrigami()
        print("Welcome to Easter Origami Instructions!")
        while True:
            print("\nOptions:")
            print("1. Print available Easter origami crafts")
            print("2. Get instructions for a specific craft")
            print("3. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                easter_origami.print_available_crafts()
            elif choice == "2":
                craft_name = input("Enter the name of the craft: ")
                craft = easter_origami.get_origami_craft(craft_name)
                if craft:
                    craft.print_instructions()
                else:
                    print("Craft not found.")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
