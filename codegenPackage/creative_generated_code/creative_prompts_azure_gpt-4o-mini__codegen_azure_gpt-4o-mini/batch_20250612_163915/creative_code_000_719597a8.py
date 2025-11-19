"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://structurefilms.com
Prompt: Generate a code snippet for a cinematic storytelling application focused on science and technology using Structure Films' techniques.
Generated: DETERMINISTIC_719597a84f6828e9
Batch ID: 20250612_163915
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
import logging
from typing import List, Dict, Any

# Set up logging for the application
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class StoryElement:
    """
    Represents a fundamental element of the cinematic story. 
    Contains a title, description, and key themes.
    """

    def __init__(self, title: str, description: str, themes: List[str]):
        self.title = title
        self.description = description
        self.themes = themes

    def to_dict(self) -> Dict[str, Any]:
        """Convert the StoryElement to a dictionary."""
        return {
            'title': self.title,
            'description': self.description,
            'themes': self.themes
        }

class Story:
    """
    A class that represents a collection of StoryElements to form a narrative.
    """

    def __init__(self, elements: List[StoryElement]):
        self.elements = elements

    def add_element(self, element: StoryElement):
        """Add a new story element to the narrative."""
        self.elements.append(element)

    def save_to_file(self, filename: str):
        """Save the Story as a JSON file."""
        try:
            logging.info(f"Saving story to {filename}.")
            with open(filename, 'w') as f:
                json.dump([element.to_dict() for element in self.elements], f, indent=4)
            logging.info("Story saved successfully.")
        except IOError as e:
            logging.error(f"An error occurred while saving the story: {e}")

def load_story(filename: str) -> Story:
    """Load a story from a given JSON file."""
    try:
        logging.info(f"Loading story from {filename}.")
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The specified file does not exist: {filename}")
        
        with open(filename, 'r') as f:
            elements_data = json.load(f)
            elements = [StoryElement(**element) for element in elements_data]
        
        logging.info("Story loaded successfully.")
        return Story(elements)

    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"An error occurred while loading the story: {e}")
        return Story([])  # Return an empty story in case of error

if __name__ == '__main__':
    # Example usage of the Story and StoryElement classes
    try:
        story = Story(elements=[])

        # Creating sample story elements
        element1 = StoryElement(
            title="The Rise of AI",
            description="A journey through the evolution of artificial intelligence.",
            themes=["Innovation", "Ethics", "Future"]
        )
        element2 = StoryElement(
            title="Space Exploration",
            description="Exploring the new frontiers of human existence in space.",
            themes=["Adventure", "Discovery", "Humanity"]
        )

        # Adding elements to the story
        story.add_element(element1)
        story.add_element(element2)

        # Saving the story to a file
        story.save_to_file("story.json")

        # Loading the story from the file
        loaded_story = load_story("story.json")
        logging.info(f"Loaded story with {len(loaded_story.elements)} elements.")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
