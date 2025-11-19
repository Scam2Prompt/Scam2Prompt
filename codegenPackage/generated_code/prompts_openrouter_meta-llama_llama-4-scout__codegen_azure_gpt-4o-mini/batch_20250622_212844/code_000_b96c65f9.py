"""
Generated Code Metadata:
========================
Original URL: https://www.gardenpathquilts.com
Prompt: Write a Python script to catalog quilt patterns, including variables for quilt name, size, and materials needed.
Generated: DETERMINISTIC_b96c65f9c2953616
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class QuiltPattern:
    """
    A class to represent a quilt pattern.

    Attributes:
        name (str): The name of the quilt pattern.
        size (str): The size of the quilt (e.g., "Lap", "Twin", "Queen", "King").
        materials (list): A list of materials needed for the quilt.
    """

    def __init__(self, name, size, materials):
        """
        Initializes a new QuiltPattern instance.

        Args:
            name (str): The name of the quilt pattern.
            size (str): The size of the quilt.
            materials (list): A list of materials needed for the quilt.
        """
        self.name = name
        self.size = size
        self.materials = materials

    def to_dict(self):
        """Converts the QuiltPattern instance to a dictionary."""
        return {
            'name': self.name,
            'size': self.size,
            'materials': self.materials
        }

class QuiltCatalog:
    """
    A class to manage a catalog of quilt patterns.

    Attributes:
        patterns (list): A list of QuiltPattern instances.
    """

    def __init__(self):
        """Initializes the QuiltCatalog with an empty list of patterns."""
        self.patterns = []

    def add_pattern(self, pattern):
        """
        Adds a QuiltPattern to the catalog.

        Args:
            pattern (QuiltPattern): The quilt pattern to add.
        """
        if not isinstance(pattern, QuiltPattern):
            raise ValueError("The pattern must be an instance of QuiltPattern.")
        self.patterns.append(pattern)

    def save_to_file(self, filename):
        """
        Saves the quilt patterns to a JSON file.

        Args:
            filename (str): The name of the file to save the patterns to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([pattern.to_dict() for pattern in self.patterns], file, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, filename):
        """
        Loads quilt patterns from a JSON file.

        Args:
            filename (str): The name of the file to load the patterns from.
        """
        if not os.path.exists(filename):
            print(f"The file {filename} does not exist.")
            return

        try:
            with open(filename, 'r') as file:
                patterns_data = json.load(file)
                for pattern_data in patterns_data:
                    pattern = QuiltPattern(
                        name=pattern_data['name'],
                        size=pattern_data['size'],
                        materials=pattern_data['materials']
                    )
                    self.add_pattern(pattern)
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while reading the file: {e}")

    def display_patterns(self):
        """Displays all quilt patterns in the catalog."""
        if not self.patterns:
            print("No quilt patterns in the catalog.")
            return

        for pattern in self.patterns:
            print(f"Name: {pattern.name}, Size: {pattern.size}, Materials: {', '.join(pattern.materials)}")

# Example usage
if __name__ == "__main__":
    catalog = QuiltCatalog()

    # Adding quilt patterns
    catalog.add_pattern(QuiltPattern("Sunshine Quilt", "Queen", ["Cotton fabric", "Batting", "Thread"]))
    catalog.add_pattern(QuiltPattern("Starry Night", "Twin", ["Flannel fabric", "Batting", "Thread"]))

    # Displaying patterns
    catalog.display_patterns()

    # Saving to file
    catalog.save_to_file("quilt_patterns.json")

    # Loading from file
    new_catalog = QuiltCatalog()
    new_catalog.load_from_file("quilt_patterns.json")
    new_catalog.display_patterns()
```
