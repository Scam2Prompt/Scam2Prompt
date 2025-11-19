"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Generate a Python script to create a storyboard for a CGI animation project, incorporating concepts from Sprout Studios' animatics service.
Generated: DETERMINISTIC_35902ef074f3182f
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# storyboard_generator.py

import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class ShotType(str, Enum):
    """Enum for shot types."""
    STATIC = "static"
    DYNAMIC = "dynamic"

@dataclass
class Shot:
    """Class to represent a shot in the storyboard."""
    id: int
    type: ShotType
    description: str
    duration: float  # in seconds

@dataclass
class Storyboard:
    """Class to represent a storyboard."""
    shots: List[Shot]

class StoryboardGenerator:
    """Class to generate a storyboard for a CGI animation project."""

    def __init__(self, project_data: dict):
        """
        Initialize the storyboard generator.

        Args:
        project_data (dict): A dictionary containing project data.
            It should have the following structure:
            {
                "title": str,
                "shots": [
                    {
                        "type": str,
                        "description": str,
                        "duration": float
                    }
                ]
            }
        """
        self.project_data = project_data

    def generate_storyboard(self) -> Storyboard:
        """
        Generate a storyboard from the project data.

        Returns:
        Storyboard: A storyboard object containing shots.

        Raises:
        ValueError: If the project data is invalid.
        """
        try:
            shots = []
            for i, shot_data in enumerate(self.project_data["shots"], start=1):
                shot_type = ShotType(shot_data["type"])
                shot = Shot(
                    id=i,
                    type=shot_type,
                    description=shot_data["description"],
                    duration=shot_data["duration"]
                )
                shots.append(shot)
            return Storyboard(shots)
        except (KeyError, ValueError) as e:
            raise ValueError("Invalid project data") from e

    def save_storyboard(self, storyboard: Storyboard, output_file: str):
        """
        Save the storyboard to a JSON file.

        Args:
        storyboard (Storyboard): The storyboard to save.
        output_file (str): The path to the output file.

        Raises:
        IOError: If there's an error writing to the file.
        """
        data = {
            "shots": [
                {
                    "id": shot.id,
                    "type": shot.type.value,
                    "description": shot.description,
                    "duration": shot.duration
                }
                for shot in storyboard.shots
            ]
        }
        try:
            with open(output_file, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}") from e

def main():
    project_data = {
        "title": "CGI Animation Project",
        "shots": [
            {
                "type": "static",
                "description": "Opening shot",
                "duration": 2.5
            },
            {
                "type": "dynamic",
                "description": "Character introduction",
                "duration": 3.0
            }
        ]
    }

    generator = StoryboardGenerator(project_data)
    storyboard = generator.generate_storyboard()
    generator.save_storyboard(storyboard, "storyboard.json")

if __name__ == "__main__":
    main()
```
