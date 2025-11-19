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

# Define the natural elements
NATURAL_ELEMENTS = ["Fire", "Water", "Earth", "Air", "Ice", "Lightning", "Grass", "Metal", "Light"]

# Define the Meowgon creature parts
MEOWGON_PARTS = ["head", "body", "tail"]

# Define the types for each part
MEOWGON_TYPES = ["Wild", "Tamed", "Mythic"]

def generate_meowgon_part(part_name):
    """
    Generate a random Meowgon creature part.

    Args:
        part_name (str): The name of the part (head, body, or tail).

    Returns:
        dict: A dictionary containing the part name, natural element, and type.
    """
    natural_element = random.choice(NATURAL_ELEMENTS)
    meowgon_type = random.choice(MEOWGON_TYPES)
    return {
        "part_name": part_name,
        "natural_element": natural_element,
        "type": meowgon_type
    }

def generate_meowgon():
    """
    Generate a Meowgon creature with random head, body, and tail elements.

    Returns:
        dict: A dictionary containing the Meowgon creature's parts.
    """
    try:
        meowgon = {
            "head": generate_meowgon_part("head"),
            "body": generate_meowgon_part("body"),
            "tail": generate_meowgon_part("tail")
        }
        return meowgon
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def print_meowgon(meowgon):
    """
    Print the Meowgon creature's details.

    Args:
        meowgon (dict): A dictionary containing the Meowgon creature's parts.
    """
    if meowgon:
        print("Meowgon Creature:")
        for part, details in meowgon.items():
            print(f"  {part.capitalize()}:")
            print(f"    Natural Element: {details['natural_element']}")
            print(f"    Type: {details['type']}")
    else:
        print("No Meowgon creature generated.")

def main():
    meowgon = generate_meowgon()
    print_meowgon(meowgon)

if __name__ == "__main__":
    main()
```
