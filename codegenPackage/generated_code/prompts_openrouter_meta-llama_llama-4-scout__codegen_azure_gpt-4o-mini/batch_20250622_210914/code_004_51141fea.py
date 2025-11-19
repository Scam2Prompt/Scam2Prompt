"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Generate a sample project proposal for a program similar to Kibera Hamlets' "Adopt me help my education" initiative, focusing on keeping children in school.
Generated: DETERMINISTIC_51141fea1eb00c6e
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Proposal: Keep Children in School Initiative

This program aims to support children in their educational journey by providing resources,
mentorship, and community engagement to ensure they remain in school. The initiative will
focus on identifying at-risk children and providing them with the necessary support to
continue their education.

Author: [Your Name]
Date: [Current Date]
"""

import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Child:
    """Class representing a child in the initiative."""
    
    def __init__(self, name: str, age: int, school: str, is_at_risk: bool):
        self.name = name
        self.age = age
        self.school = school
        self.is_at_risk = is_at_risk

    def to_dict(self) -> Dict:
        """Convert the Child object to a dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "school": self.school,
            "is_at_risk": self.is_at_risk
        }

class Initiative:
    """Class representing the Keep Children in School Initiative."""
    
    def __init__(self):
        self.children: List[Child] = []

    def add_child(self, child: Child) -> None:
        """Add a child to the initiative."""
        if not isinstance(child, Child):
            logging.error("Invalid child object provided.")
            raise ValueError("Invalid child object.")
        self.children.append(child)
        logging.info(f"Child {child.name} added to the initiative.")

    def save_to_file(self, filename: str) -> None:
        """Save the list of children to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([child.to_dict() for child in self.children], file, indent=4)
            logging.info(f"Children data saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving to file: {e}")
            raise

    def load_from_file(self, filename: str) -> None:
        """Load children from a JSON file."""
        try:
            with open(filename, 'r') as file:
                children_data = json.load(file)
                for child_data in children_data:
                    child = Child(**child_data)
                    self.add_child(child)
            logging.info(f"Children data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading from file: {e}")
            raise

def main():
    """Main function to run the initiative."""
    initiative = Initiative()

    # Sample data
    children = [
        Child("Alice", 10, "Greenwood Primary", True),
        Child("Bob", 12, "Sunshine High", False),
        Child("Charlie", 9, "Maple Leaf Academy", True)
    ]

    # Adding children to the initiative
    for child in children:
        initiative.add_child(child)

    # Save the initiative data to a file
    initiative.save_to_file("children_initiative.json")

    # Load the initiative data from a file
    initiative.load_from_file("children_initiative.json")

if __name__ == "__main__":
    main()
```
