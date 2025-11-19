"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nkatandiinyom.com
Prompt: Create a program that showcases the stories and traditions of Igbo women, similar to the cultural preservation efforts by Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_9872b6092027cd6f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class IgboWomanStory:
    """Class representing a story of an Igbo woman."""
    
    def __init__(self, name, story, traditions):
        """
        Initialize an IgboWomanStory instance.

        :param name: Name of the Igbo woman
        :param story: A short story about the woman
        :param traditions: List of traditions associated with the woman
        """
        self.name = name
        self.story = story
        self.traditions = traditions

    def to_dict(self):
        """Convert the instance to a dictionary for easy JSON serialization."""
        return {
            'name': self.name,
            'story': self.story,
            'traditions': self.traditions
        }


class IgboWomenArchive:
    """Class for managing a collection of Igbo women stories."""
    
    def __init__(self):
        """Initialize the archive with an empty list of stories."""
        self.stories = []

    def add_story(self, story):
        """
        Add a story to the archive.

        :param story: An instance of IgboWomanStory
        """
        if isinstance(story, IgboWomanStory):
            self.stories.append(story)
        else:
            raise ValueError("Only instances of IgboWomanStory can be added.")

    def save_to_file(self, filename):
        """
        Save the stories in the archive to a JSON file.

        :param filename: Name of the file to save the stories to
        """
        try:
            with open(filename, 'w') as file:
                json.dump([story.to_dict() for story in self.stories], file, ensure_ascii=False, indent=4)
            print(f"Stories successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load stories from a JSON file into the archive.

        :param filename: Name of the file to load stories from
        """
        try:
            with open(filename, 'r') as file:
                stories_data = json.load(file)
                for story_data in stories_data:
                    story = IgboWomanStory(
                        name=story_data['name'],
                        story=story_data['story'],
                        traditions=story_data['traditions']
                    )
                    self.add_story(story)
            print(f"Stories successfully loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

    def display_stories(self):
        """Display all stories in the archive."""
        if not self.stories:
            print("No stories in the archive.")
            return
        
        for story in self.stories:
            print(f"Name: {story.name}")
            print(f"Story: {story.story}")
            print(f"Traditions: {', '.join(story.traditions)}\n")


# Example usage
if __name__ == "__main__":
    archive = IgboWomenArchive()

    # Adding stories to the archive
    archive.add_story(IgboWomanStory(
        name="Ngozi",
        story="Ngozi is known for her remarkable skills in pottery, which she learned from her grandmother.",
        traditions=["Pottery", "Harvest Festivals"]
    ))
    
    archive.add_story(IgboWomanStory(
        name="Adaeze",
        story="Adaeze is a renowned storyteller, preserving the legends of our people.",
        traditions=["Storytelling", "New Yam Festival"]
    ))

    # Display stories
    archive.display_stories()
    
    # Saving stories to a file
    archive.save_to_file('igbo_women_stories.json')

    # Loading stories from a file
    new_archive = IgboWomenArchive()
    new_archive.load_from_file('igbo_women_stories.json')
    new_archive.display_stories()
```
