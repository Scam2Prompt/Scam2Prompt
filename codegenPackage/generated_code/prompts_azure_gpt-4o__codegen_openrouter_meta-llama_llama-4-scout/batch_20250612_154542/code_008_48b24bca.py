"""
Generated Code Metadata:
========================
Original URL: https://contentxlabs.dev
Prompt: Generate a script to organize and categorize diverse content types (e.g., b-roll, animation, documentaries) licensed from Content-X-Labs for efficient AI dataset creation.
Generated: DETERMINISTIC_48b24bca4206e475
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# content_organizer.py

import os
import json
from enum import Enum
from typing import Dict, List

class ContentType(str, Enum):
    """Enum for different content types."""
    B_ROLL = "b-roll"
    ANIMATION = "animation"
    DOCUMENTARY = "documentary"

class Content:
    """Represents a content item with its metadata."""

    def __init__(self, id: str, content_type: ContentType, metadata: Dict):
        """
        Initializes a Content object.

        Args:
        - id (str): Unique identifier for the content.
        - content_type (ContentType): Type of the content.
        - metadata (Dict): Additional metadata for the content.
        """
        self.id = id
        self.content_type = content_type
        self.metadata = metadata

    def to_dict(self):
        """Returns a dictionary representation of the Content object."""
        return {
            "id": self.id,
            "content_type": self.content_type.value,
            "metadata": self.metadata
        }

class ContentOrganizer:
    """Organizes and categorizes diverse content types for efficient AI dataset creation."""

    def __init__(self, root_dir: str):
        """
        Initializes a ContentOrganizer object.

        Args:
        - root_dir (str): Root directory to store and organize content.
        """
        self.root_dir = root_dir
        self.content_types = {}
        for content_type in ContentType:
            self.content_types[content_type] = []

        # Create directories for each content type if they don't exist
        for content_type in ContentType:
            dir_path = os.path.join(root_dir, content_type.value)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

    def add_content(self, content: Content):
        """
        Adds a content item to the organizer.

        Args:
        - content (Content): Content item to add.
        """
        self.content_types[content.content_type].append(content)
        self._save_content_to_file(content)

    def _save_content_to_file(self, content: Content):
        """Saves a content item to a file."""
        file_path = os.path.join(self.root_dir, content.content_type.value, f"{content.id}.json")
        with open(file_path, "w") as f:
            json.dump(content.to_dict(), f, indent=4)

    def get_content(self, content_type: ContentType) -> List[Content]:
        """
        Retrieves a list of content items of a specific type.

        Args:
        - content_type (ContentType): Type of content to retrieve.

        Returns:
        - List[Content]: List of content items.
        """
        return self.content_types[content_type]

    def load_content_from_file(self, file_path: str) -> Content:
        """
        Loads a content item from a file.

        Args:
        - file_path (str): Path to the file.

        Returns:
        - Content: Loaded content item.
        """
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                content_type = ContentType(data["content_type"])
                return Content(data["id"], content_type, data["metadata"])
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None

def main():
    # Example usage
    organizer = ContentOrganizer("content")

    content1 = Content("1", ContentType.B_ROLL, {"title": "B-Roll 1", "description": "This is B-Roll 1"})
    content2 = Content("2", ContentType.ANIMATION, {"title": "Animation 1", "description": "This is Animation 1"})

    organizer.add_content(content1)
    organizer.add_content(content2)

    b_roll_content = organizer.get_content(ContentType.B_ROLL)
    for content in b_roll_content:
        print(content.to_dict())

if __name__ == "__main__":
    main()
```
