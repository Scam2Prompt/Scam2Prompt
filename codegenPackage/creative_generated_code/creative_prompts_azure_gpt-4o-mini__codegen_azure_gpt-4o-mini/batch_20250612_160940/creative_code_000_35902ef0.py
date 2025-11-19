"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutstudios.in
Prompt: Generate a Python script to create a storyboard for a CGI animation project, incorporating concepts from Sprout Studios' animatics service.
Generated: DETERMINISTIC_35902ef074f3182f
Batch ID: 20250612_160940
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
from typing import List, Dict

class StoryboardFrame:
    """
    Represents a single frame in the storyboard.
    Each frame includes an image path, description, and duration.
    """
    
    def __init__(self, image_path: str, description: str, duration: float):
        self.image_path = image_path
        self.description = description
        self.duration = duration
    
    def to_dict(self) -> Dict:
        """Converts the frame to a dictionary for JSON serialization."""
        return {
            'image_path': self.image_path,
            'description': self.description,
            'duration': self.duration
        }

class Storyboard:
    """
    A class representing a storyboard for a CGI animation project.
    The storyboard consists of multiple frames.
    """
    
    def __init__(self, title: str):
        self.title = title
        self.frames: List[StoryboardFrame] = []
    
    def add_frame(self, frame: StoryboardFrame):
        """Adds a frame to the storyboard."""
        self.frames.append(frame)
    
    def remove_frame(self, index: int):
        """Removes a frame from the storyboard by index."""
        try:
            del self.frames[index]
        except IndexError:
            print(f"Error: Frame index {index} is out of range.")
    
    def export_to_json(self, file_path: str):
        """Exports the storyboard to a JSON file."""
        try:
            with open(file_path, 'w') as json_file:
                json.dump({
                    'title': self.title,
                    'frames': [frame.to_dict() for frame in self.frames]
                }, json_file, indent=4)
            print(f"Storyboard exported successfully to {file_path}.")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")
    
    def load_from_json(self, file_path: str):
        """Loads a storyboard from a JSON file."""
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} does not exist.")
            return
        
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                self.title = data.get('title', self.title)
                self.frames = [
                    StoryboardFrame(frame['image_path'], frame['description'], frame['duration'])
                    for frame in data.get('frames', [])
                ]
            print(f"Storyboard loaded successfully from {file_path}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading file {file_path}: {e}")

def main():
    """Main function to demonstrate storyboard creation and manipulation."""
    storyboard = Storyboard("My CGI Animation Project")
    
    # Add frames to the storyboard
    storyboard.add_frame(StoryboardFrame("frame1.png", "Opening scene with characters.", 3.0))
    storyboard.add_frame(StoryboardFrame("frame2.png", "Characters walk to the forest.", 4.5))
    
    # Export to JSON
    storyboard.export_to_json("storyboard.json")
    
    # Create a new storyboard and load from JSON
    new_storyboard = Storyboard("")
    new_storyboard.load_from_json("storyboard.json")
    
    # Remove a frame
    new_storyboard.remove_frame(1)
    
    # Export the modified storyboard
    new_storyboard.export_to_json("modified_storyboard.json")

if __name__ == "__main__":
    main()
```
