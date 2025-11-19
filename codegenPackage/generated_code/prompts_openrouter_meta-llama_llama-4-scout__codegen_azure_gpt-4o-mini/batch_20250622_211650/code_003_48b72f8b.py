"""
Generated Code Metadata:
========================
Original URL: https://structurefilms.com
Prompt: "Design a storyboard for a tech explainer video incorporating cinematic storytelling principles."
Generated: DETERMINISTIC_48b72f8b15713484
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Storyboard:
    """
    A class to represent a storyboard for a tech explainer video.
    """

    def __init__(self, title, scenes):
        """
        Initializes the storyboard with a title and a list of scenes.

        :param title: Title of the video
        :param scenes: List of scenes in the storyboard
        """
        self.title = title
        self.scenes = scenes

    def add_scene(self, scene):
        """
        Adds a new scene to the storyboard.

        :param scene: A dictionary representing a scene
        """
        if not isinstance(scene, dict):
            raise ValueError("Scene must be a dictionary.")
        self.scenes.append(scene)

    def remove_scene(self, scene_index):
        """
        Removes a scene from the storyboard by index.

        :param scene_index: Index of the scene to remove
        :raises IndexError: If the scene index is out of range
        """
        try:
            del self.scenes[scene_index]
        except IndexError:
            raise IndexError("Scene index out of range.")

    def get_storyboard(self):
        """
        Returns the complete storyboard as a formatted string.

        :return: Formatted string representation of the storyboard
        """
        storyboard_str = f"Storyboard for: {self.title}\n"
        for index, scene in enumerate(self.scenes):
            storyboard_str += f"Scene {index + 1}: {scene['description']}\n"
            storyboard_str += f"  - Visuals: {scene['visuals']}\n"
            storyboard_str += f"  - Audio: {scene['audio']}\n"
            storyboard_str += f"  - Duration: {scene['duration']} seconds\n"
        return storyboard_str


# Example usage
if __name__ == "__main__":
    # Create a storyboard for a tech explainer video
    scenes = [
        {
            "description": "Introduction to the technology",
            "visuals": "Animated graphics showing the tech",
            "audio": "Upbeat music with a voiceover",
            "duration": 30
        },
        {
            "description": "How it works",
            "visuals": "Step-by-step animation of the process",
            "audio": "Voiceover explaining each step",
            "duration": 60
        },
        {
            "description": "Benefits of the technology",
            "visuals": "Infographics highlighting key benefits",
            "audio": "Voiceover summarizing benefits",
            "duration": 45
        }
    ]

    # Initialize the storyboard
    tech_video_storyboard = Storyboard("Tech Explainer Video", scenes)

    # Add a new scene
    new_scene = {
        "description": "Conclusion and call to action",
        "visuals": "Logo and website link",
        "audio": "Voiceover encouraging viewers to visit the website",
        "duration": 20
    }
    tech_video_storyboard.add_scene(new_scene)

    # Print the complete storyboard
    print(tech_video_storyboard.get_storyboard())
```
