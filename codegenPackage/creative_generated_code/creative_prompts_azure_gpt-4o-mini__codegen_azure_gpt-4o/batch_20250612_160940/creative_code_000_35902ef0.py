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
import os
import json
from datetime import datetime


class Storyboard:
    """
    A class to represent a CGI animation storyboard.
    """
    def __init__(self, project_name, animation_length, frame_rate):
        """
        Initialize the storyboard instance.

        :param project_name: Name of the project.
        :param animation_length: Duration of the animation in seconds.
        :param frame_rate: Frames per second (FPS).
        """
        self.project_name = project_name
        self.animation_length = animation_length
        self.frame_rate = frame_rate
        self.frames = []
        self.output_directory = f"{project_name}_Storyboard"

    def calculate_total_frames(self):
        """
        Calculate the total number of frames based on animation length and frame rate.
        :return: Total frames as an integer.
        """
        return int(self.animation_length * self.frame_rate)

    def add_frame(self, frame_number, description, assets=None):
        """
        Add a new frame to the storyboard.

        :param frame_number: Sequential frame number.
        :param description: Description of the frame's content.
        :param assets: Optional list of assets used in the frame.
        """
        if assets is None:
            assets = []

        self.frames.append({
            "frame_number": frame_number,
            "description": description,
            "assets": assets
        })

    def save_to_file(self):
        """
        Save the storyboard data to a JSON file.

        :raises Exception: If saving the file fails.
        """
        try:
            # Create output directory if it does not exist
            if not os.path.exists(self.output_directory):
                os.makedirs(self.output_directory)

            # Save storyboard to a JSON file
            file_path = os.path.join(self.output_directory, "storyboard.json")
            with open(file_path, 'w') as file:
                json.dump({
                    "project_name": self.project_name,
                    "animation_length": self.animation_length,
                    "frame_rate": self.frame_rate,
                    "total_frames": self.calculate_total_frames(),
                    "frames": self.frames,
                    "created_at": datetime.now().isoformat()
                }, file, indent=4)

            print(f"Storyboard saved successfully as {file_path}")

        except Exception as e:
            print(f"Error saving storyboard: {e}")

    def generate_preview(self):
        """
        Generate a basic text-based preview of the storyboard.

        :return: Preview string.
        """
        preview = f"Storyboard Preview - {self.project_name}\n"
        preview += "=" * 40 + "\n"
        preview += f"Animation Length: {self.animation_length}s\n"
        preview += f"Frame Rate: {self.frame_rate} FPS\n"
        preview += f"Total Frames: {self.calculate_total_frames()}\n"
        preview += "=" * 40 + "\n"

        for frame in self.frames:
            preview += f"\nFrame #{frame['frame_number']}\n"
            preview += f"Description: {frame['description']}\n"
            preview += f"Assets: {', '.join(frame['assets']) if frame['assets'] else 'None'}\n"

        return preview


# Main script logic
if __name__ == "__main__":
    try:
        # Example usage
        storyboard = Storyboard("Sprout Studios CGI Animation", 120, 24)
        storyboard.add_frame(1, "Opening scene with a sunrise", ["sun.png", "background.jpg"])
        storyboard.add_frame(2, "Character entering the scene", ["character.png"])
        storyboard.add_frame(3, "Dialogue starts between two characters", ["character1.png", "character2.png"])

        print(storyboard.generate_preview())
        storyboard.save_to_file()

    except Exception as e:
        print(f"An error occurred: {e}")
```
