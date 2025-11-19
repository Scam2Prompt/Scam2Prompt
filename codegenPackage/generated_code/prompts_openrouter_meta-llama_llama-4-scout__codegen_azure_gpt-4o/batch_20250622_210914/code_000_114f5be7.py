"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Write a Python script to generate a Meowgon creature with random head, body, and tail elements, considering the 9 natural elements and 3 types for each part.
Generated: DETERMINISTIC_114f5be7d749733f
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define the natural elements and types for each part of the Meowgon
ELEMENTS = ["Fire", "Water", "Earth", "Air", "Electric", "Ice", "Light", "Dark", "Nature"]
PART_TYPES = ["Small", "Medium", "Large"]

class Meowgon:
    """
    A class representing a Meowgon creature with randomly generated head, body, and tail.
    """
    def __init__(self):
        self.head = self._generate_part("Head")
        self.body = self._generate_part("Body")
        self.tail = self._generate_part("Tail")

    def _generate_part(self, part_name):
        """
        Generate a random part for the Meowgon.
        
        Args:
            part_name (str): The name of the part being generated (e.g., "Head", "Body", "Tail").
        
        Returns:
            dict: A dictionary containing the element and type of the part.
        """
        element = random.choice(ELEMENTS)
        part_type = random.choice(PART_TYPES)
        return {"Part": part_name, "Element": element, "Type": part_type}

    def display(self):
        """
        Display the details of the Meowgon creature.
        """
        print("Meowgon Details:")
        print(f"  Head: Element = {self.head['Element']}, Type = {self.head['Type']}")
        print(f"  Body: Element = {self.body['Element']}, Type = {self.body['Type']}")
        print(f"  Tail: Element = {self.tail['Element']}, Type = {self.tail['Type']}")

def main():
    """
    Main function to generate and display a Meowgon creature.
    """
    try:
        # Generate a Meowgon creature
        meowgon = Meowgon()
        # Display the Meowgon details
        meowgon.display()
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
