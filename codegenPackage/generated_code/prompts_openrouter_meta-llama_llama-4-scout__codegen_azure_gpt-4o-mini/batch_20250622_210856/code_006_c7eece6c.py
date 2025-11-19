"""
Generated Code Metadata:
========================
Original URL: https://fsromain.com
Prompt: Create a picture editing style guide for social media profiles, inspired by Romain Ferri's work with his clients.
Generated: DETERMINISTIC_c7eece6c97c8e442
Batch ID: 20250622_210856
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

class StyleGuide:
    """
    A class to represent a picture editing style guide for social media profiles.
    """

    def __init__(self, title: str, description: str):
        """
        Initializes the StyleGuide with a title and description.

        :param title: Title of the style guide
        :param description: Description of the style guide
        """
        self.title = title
        self.description = description
        self.styles: List[Dict] = []

    def add_style(self, style_name: str, properties: Dict):
        """
        Adds a new style to the style guide.

        :param style_name: Name of the style
        :param properties: A dictionary of properties for the style
        """
        style = {
            "name": style_name,
            "properties": properties
        }
        self.styles.append(style)

    def to_json(self) -> str:
        """
        Converts the style guide to a JSON string.

        :return: JSON representation of the style guide
        """
        return json.dumps({
            "title": self.title,
            "description": self.description,
            "styles": self.styles
        }, indent=4)

    def save_to_file(self, filename: str):
        """
        Saves the style guide to a JSON file.

        :param filename: The name of the file to save the style guide
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Style guide saved to {filename}")
        except IOError as e:
            print(f"Error saving style guide to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new style guide
    guide = StyleGuide(
        title="Social Media Picture Editing Style Guide",
        description="A style guide inspired by Romain Ferri's work with clients."
    )

    # Add styles to the guide
    guide.add_style("Bright and Vibrant", {
        "brightness": 1.2,
        "contrast": 1.3,
        "saturation": 1.5,
        "sharpness": 1.1
    })

    guide.add_style("Muted and Soft", {
        "brightness": 0.9,
        "contrast": 0.8,
        "saturation": 0.7,
        "sharpness": 0.9
    })

    # Save the style guide to a file
    guide.save_to_file("style_guide.json")
```
