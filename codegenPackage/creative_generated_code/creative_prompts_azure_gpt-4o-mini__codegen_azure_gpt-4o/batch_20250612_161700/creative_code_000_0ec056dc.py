"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Generate a Python script that utilizes the concepts of ecofeminism in museum studies as discussed in the "Oser l’avenir" workshop from Mêtis.
Generated: DETERMINISTIC_0ec056dc147bffe9
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script for integrating ecofeminism concepts into museum studies.
Inspired by the "Oser l’avenir" workshop from Mêtis.

This script demonstrates how to organize and present ecofeminist ideas in a museum context.
It provides functionality to curate exhibits, highlight ecofeminist themes, and ensure inclusivity.

Key Features:
- Exhibit creation based on ecofeminism principles
- Tagging system for themes (e.g., sustainability, gender equality, etc.)
- Error handling for invalid input
"""

# Import necessary libraries
import json
import os

class Exhibit:
    """
    Represents an exhibit in the museum.
    """
    def __init__(self, title, description, themes):
        """
        Initialize an Exhibit object.
        
        :param title: Title of the exhibit
        :param description: Description of the exhibit
        :param themes: List of ecofeminist themes associated with the exhibit
        """
        if not title or not description or not isinstance(themes, list):
            raise ValueError("Invalid input for Exhibit initialization")
        self.title = title
        self.description = description
        self.themes = themes

    def to_dict(self):
        """
        Convert Exhibit object to a dictionary for serialization.
        :return: Dictionary representation of the Exhibit
        """
        return {
            "title": self.title,
            "description": self.description,
            "themes": self.themes
        }


class Museum:
    """
    Represents a museum dedicated to ecofeminist studies and exhibits.
    """
    def __init__(self, name):
        """
        Initialize a Museum object.
        
        :param name: Name of the museum
        """
        if not name:
            raise ValueError("Museum name cannot be empty")
        self.name = name
        self.exhibits = []

    def add_exhibit(self, exhibit):
        """
        Add an exhibit to the museum.
        
        :param exhibit: Exhibit object to be added
        """
        if not isinstance(exhibit, Exhibit):
            raise TypeError("Invalid exhibit type")
        self.exhibits.append(exhibit)

    def list_exhibits(self):
        """
        List all exhibits in the museum.
        
        :return: List of exhibit dictionaries
        """
        return [exhibit.to_dict() for exhibit in self.exhibits]

    def save_to_file(self, file_path):
        """
        Save museum exhibits to a JSON file.
        
        :param file_path: Path to the file where exhibits will be saved
        """
        try:
            with open(file_path, 'w') as f:
                json.dump({"name": self.name, "exhibits": self.list_exhibits()}, f, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")


def main():
    """
    Main function to demonstrate the script functionality.
    """
    print("Welcome to the Ecofeminism Museum Management System")
    
    # Initialize the museum
    museum_name = "Ecofeminism Museum"
    museum = Museum(museum_name)

    # Adding sample exhibits
    try:
        exhibit1 = Exhibit(
            title="Sustainability and Feminism",
            description="Explores the intersections of eco-friendly practices and gender equality.",
            themes=["sustainability", "gender equality"]
        )
        museum.add_exhibit(exhibit1)

        exhibit2 = Exhibit(
            title="Women and Environmental Activism",
            description="Showcases contributions of women in environmental activism across the globe.",
            themes=["activism", "environment"]
        )
        museum.add_exhibit(exhibit2)
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")
    
    # Display the exhibits
    exhibits = museum.list_exhibits()
    print(f"\nExhibits in {museum.name}:")
    for exhibit in exhibits:
        print(f"- {exhibit['title']}: {exhibit['description']}")
        print(f"  Themes: {', '.join(exhibit['themes'])}")

    # Save exhibits to a file
    file_path = "ecofeminism_museum.json"
    museum.save_to_file(file_path)
    print(f"\nMuseum data saved to {file_path}")


if __name__ == "__main__":
    main()
```
