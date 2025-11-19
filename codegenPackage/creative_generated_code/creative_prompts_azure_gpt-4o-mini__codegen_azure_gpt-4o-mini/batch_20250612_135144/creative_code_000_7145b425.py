"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Generate Python code to create a private label cleaning tool using PDC Brush's specifications and ethical trading practices.
Generated: DETERMINISTIC_7145b4259a72bf90
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import Dict, List

class CleaningTool:
    """
    A class to represent a private label cleaning tool using PDC Brush's specifications.
    """

    def __init__(self, name: str, specifications: Dict[str, str], ethical_practices: List[str]):
        """
        Initializes the CleaningTool with the given name, specifications, and ethical practices.

        Args:
            name (str): The name of the cleaning tool.
            specifications (Dict[str, str]): The specifications of the cleaning tool.
            ethical_practices (List[str]): A list of ethical trading practices followed.
        """
        self.name = name
        self.specifications = specifications
        self.ethical_practices = ethical_practices

    def display_info(self) -> None:
        """
        Displays the information about the cleaning tool.
        """
        print(f"Cleaning Tool: {self.name}")
        print("Specifications:")
        for key, value in self.specifications.items():
            print(f"  {key}: {value}")
        print("Ethical Practices:")
        for practice in self.ethical_practices:
            print(f"  - {practice}")

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the CleaningTool information to a JSON file.

        Args:
            file_path (str): The path to the file where the information will be saved.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.__dict__, file, indent=4)
            print(f"Data saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving file: {e}")

    @classmethod
    def load_from_file(cls, file_path: str) -> 'CleaningTool':
        """
        Loads the CleaningTool information from a JSON file.

        Args:
            file_path (str): The path to the file to read from.

        Returns:
            CleaningTool: An instance of CleaningTool.

        Raises:
            IOError: If the file cannot be read.
            json.JSONDecodeError: If the JSON is malformed.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return cls(data['name'], data['specifications'], data['ethical_practices'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    specifications = {
        "Material": "Eco-friendly Synthetic",
        "Size": "12 inches",
        "Weight": "0.5 lbs",
        "Usage": "Multi-surface cleaning"
    }
    ethical_practices = [
        "Sourcing materials responsibly",
        "Ensuring fair wages for workers",
        "Minimizing environmental impact"
    ]

    cleaning_tool = CleaningTool("Eco Brush", specifications, ethical_practices)

    # Display the information
    cleaning_tool.display_info()

    # Save the instance to a file
    cleaning_tool.save_to_file("cleaning_tool.json")

    # Load the instance from a file
    loaded_tool = CleaningTool.load_from_file("cleaning_tool.json")
    loaded_tool.display_info()
```
