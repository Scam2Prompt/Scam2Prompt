"""
Generated Code Metadata:
========================
Original URL: https://structurefilms.com
Prompt: "Generate a script for a cinematic video about climate change using storytelling techniques."
Generated: DETERMINISTIC_f22974970275a9e9
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime

class ClimateChangeVideoScript:
    def __init__(self, title, duration):
        """
        Initializes the video script with a title and duration.

        :param title: Title of the video
        :param duration: Duration of the video in seconds
        """
        self.title = title
        self.duration = duration
        self.scenes = []

    def add_scene(self, scene_title, description, duration):
        """
        Adds a scene to the video script.

        :param scene_title: Title of the scene
        :param description: Description of the scene
        :param duration: Duration of the scene in seconds
        """
        if duration <= 0:
            raise ValueError("Scene duration must be greater than zero.")
        self.scenes.append({
            "scene_title": scene_title,
            "description": description,
            "duration": duration
        })

    def generate_script(self):
        """
        Generates the complete video script as a dictionary.

        :return: A dictionary containing the video title, total duration, and scenes
        """
        total_duration = sum(scene['duration'] for scene in self.scenes)
        return {
            "title": self.title,
            "total_duration": total_duration,
            "scenes": self.scenes
        }

    def save_script(self, filename):
        """
        Saves the video script to a JSON file.

        :param filename: The name of the file to save the script
        """
        script_data = self.generate_script()
        try:
            with open(filename, 'w') as json_file:
                json.dump(script_data, json_file, indent=4)
            print(f"Script saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving script to file: {e}")

def main():
    # Create a video script for a cinematic video about climate change
    video_script = ClimateChangeVideoScript("The Last Chance: A Climate Change Story", 300)

    # Adding scenes to the script
    video_script.add_scene("Introduction", "Aerial shots of beautiful landscapes, transitioning to polluted areas.", 30)
    video_script.add_scene("The Science", "Experts explain the greenhouse effect and its impact on the planet.", 60)
    video_script.add_scene("Personal Stories", "Interviews with individuals affected by climate change.", 60)
    video_script.add_scene("Call to Action", "Highlighting ways viewers can contribute to combating climate change.", 30)
    video_script.add_scene("Hope for the Future", "Showcasing innovative solutions and community efforts.", 60)
    video_script.add_scene("Conclusion", "A powerful message about the importance of taking action now.", 30)

    # Save the script to a JSON file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"climate_change_video_script_{timestamp}.json"
    video_script.save_script(filename)

if __name__ == "__main__":
    main()
```
