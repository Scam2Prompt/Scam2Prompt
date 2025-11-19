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

# Define the natural elements and types for each part of the Meowgon creature
NATURAL_ELEMENTS = ['Fire', 'Water', 'Earth', 'Air', 'Light', 'Dark', 'Nature', 'Metal', 'Electric']
HEAD_TYPES = ['Round', 'Pointed', 'Flat']
BODY_TYPES = ['Furry', 'Scaly', 'Smooth']
TAIL_TYPES = ['Long', 'Short', 'Curled']

class Meowgon:
    """Class representing a Meowgon creature with random attributes."""
    
    def __init__(self):
        """Initialize a Meowgon with random head, body, and tail attributes."""
        self.head = self.generate_head()
        self.body = self.generate_body()
        self.tail = self.generate_tail()

    def generate_head(self):
        """Generate a random head for the Meowgon."""
        element = random.choice(NATURAL_ELEMENTS)
        head_type = random.choice(HEAD_TYPES)
        return {'element': element, 'type': head_type}

    def generate_body(self):
        """Generate a random body for the Meowgon."""
        element = random.choice(NATURAL_ELEMENTS)
        body_type = random.choice(BODY_TYPES)
        return {'element': element, 'type': body_type}

    def generate_tail(self):
        """Generate a random tail for the Meowgon."""
        element = random.choice(NATURAL_ELEMENTS)
        tail_type = random.choice(TAIL_TYPES)
        return {'element': element, 'type': tail_type}

    def __str__(self):
        """Return a string representation of the Meowgon."""
        return (f"Meowgon:\n"
                f"  Head: {self.head['type']} ({self.head['element']})\n"
                f"  Body: {self.body['type']} ({self.body['element']})\n"
                f"  Tail: {self.tail['type']} ({self.tail['element']})")

def main():
    """Main function to create and display a Meowgon creature."""
    try:
        meowgon = Meowgon()
        print(meowgon)
    except Exception as e:
        print(f"An error occurred while generating the Meowgon: {e}")

if __name__ == "__main__":
    main()
```
