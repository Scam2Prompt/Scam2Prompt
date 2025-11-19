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
import json
from typing import List, Dict

class OrigamiInstruction:
    """Class to represent an origami instruction for Easter crafts."""
    
    def __init__(self, title: str, steps: List[str]):
        """
        Initialize an OrigamiInstruction instance.

        Args:
            title (str): The title of the origami craft.
            steps (List[str]): A list of steps to complete the origami.
        """
        self.title = title
        self.steps = steps

    def to_dict(self) -> Dict:
        """Convert the instruction to a dictionary format for easy serialization."""
        return {
            "title": self.title,
            "steps": self.steps
        }

class OrigamiGenerator:
    """Class to generate origami instructions for Easter crafts."""
    
    def __init__(self):
        """Initialize the OrigamiGenerator with a list of instructions."""
        self.instructions: List[OrigamiInstruction] = []

    def add_instruction(self, title: str, steps: List[str]):
        """
        Add a new origami instruction.

        Args:
            title (str): The title of the origami craft.
            steps (List[str]): A list of steps to complete the origami.
        """
        instruction = OrigamiInstruction(title, steps)
        self.instructions.append(instruction)

    def save_instructions(self, filename: str):
        """
        Save the origami instructions to a JSON file.

        Args:
            filename (str): The name of the file to save the instructions.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([instruction.to_dict() for instruction in self.instructions], file, indent=4)
            print(f"Instructions saved to {filename}")
        except IOError as e:
            print(f"Error saving instructions to {filename}: {e}")

    def print_instructions(self):
        """Print all origami instructions to the console."""
        for instruction in self.instructions:
            print(f"Title: {instruction.title}")
            print("Steps:")
            for step in instruction.steps:
                print(f"- {step}")
            print("\n")

# Example usage
if __name__ == "__main__":
    origami_gen = OrigamiGenerator()
    
    # Adding Easter origami instructions
    origami_gen.add_instruction(
        "Easter Bunny",
        [
            "Start with a square piece of paper.",
            "Fold the paper in half diagonally.",
            "Fold the top corners down to meet the bottom point.",
            "Fold the bottom point up to form the bunny's face.",
            "Add eyes and a nose to finish."
        ]
    )
    
    origami_gen.add_instruction(
        "Easter Egg",
        [
            "Begin with a rectangular piece of paper.",
            "Fold the paper in half lengthwise.",
            "Round the top corners to create an egg shape.",
            "Unfold and decorate the egg as desired.",
            "Refold and display your Easter egg."
        ]
    )
    
    # Print instructions to console
    origami_gen.print_instructions()
    
    # Save instructions to a JSON file
    origami_gen.save_instructions("easter_origami_instructions.json")
```
