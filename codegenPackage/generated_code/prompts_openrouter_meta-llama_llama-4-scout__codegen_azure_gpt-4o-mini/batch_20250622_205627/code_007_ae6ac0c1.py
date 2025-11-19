"""
Generated Code Metadata:
========================
Original URL: https://link-protocol.net
Prompt: Design a data model to represent Wattpad's story metadata, including fields for story title, genre, tags, and author information.
Generated: DETERMINISTIC_ae6ac0c1a7844838
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class Author:
    """Represents an author of a story."""
    name: str
    bio: Optional[str] = None
    profile_url: Optional[str] = None

    def __post_init__(self):
        if not self.name:
            raise ValueError("Author name cannot be empty.")

@dataclass
class Story:
    """Represents the metadata of a Wattpad story."""
    title: str
    genre: str
    tags: List[str] = field(default_factory=list)
    author: Author = field(default_factory=Author)

    def __post_init__(self):
        if not self.title:
            raise ValueError("Story title cannot be empty.")
        if not self.genre:
            raise ValueError("Story genre cannot be empty.")
        if not isinstance(self.tags, list):
            raise TypeError("Tags must be a list of strings.")
        if not all(isinstance(tag, str) for tag in self.tags):
            raise TypeError("All tags must be strings.")

    def add_tag(self, tag: str) -> None:
        """Adds a tag to the story."""
        if not isinstance(tag, str):
            raise TypeError("Tag must be a string.")
        self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        """Removes a tag from the story if it exists."""
        try:
            self.tags.remove(tag)
        except ValueError:
            print(f"Tag '{tag}' not found in the story tags.")

    def __str__(self) -> str:
        """Returns a string representation of the story."""
        return f"'{self.title}' by {self.author.name} - Genre: {self.genre}, Tags: {', '.join(self.tags)}"

# Example usage
if __name__ == "__main__":
    try:
        author = Author(name="John Doe", bio="A passionate writer.")
        story = Story(title="The Great Adventure", genre="Fantasy", author=author)
        story.add_tag("Adventure")
        story.add_tag("Magic")
        print(story)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
