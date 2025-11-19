"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Write code to simulate a VR experience for marketing ads, referencing the VR projects like ESMA - 360 and Syria and War from Sprout Studios.
Generated: DETERMINISTIC_bd35847e2f1145d1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import random
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VRExperience:
    """
    A class to simulate a VR experience for marketing ads.
    """

    def __init__(self, title, description, media_files):
        """
        Initializes the VRExperience with a title, description, and media files.

        :param title: Title of the VR experience
        :param description: Description of the VR experience
        :param media_files: List of media files (e.g., images, videos) for the experience
        """
        self.title = title
        self.description = description
        self.media_files = media_files

    def display_info(self):
        """
        Displays the title and description of the VR experience.
        """
        logging.info(f"VR Experience: {self.title}")
        logging.info(f"Description: {self.description}")

    def play_media(self):
        """
        Simulates playing media files in the VR experience.
        """
        if not self.media_files:
            logging.warning("No media files available to play.")
            return

        for media in self.media_files:
            try:
                self._play_media_file(media)
            except Exception as e:
                logging.error(f"Error playing media file {media}: {e}")

    def _play_media_file(self, media):
        """
        Simulates the action of playing a media file.

        :param media: The media file to play
        """
        logging.info(f"Playing media file: {media}")
        # Simulate a random chance of failure
        if random.choice([True, False]):
            raise RuntimeError("Simulated media playback error.")

def main():
    """
    Main function to run the VR experience simulation.
    """
    # Example media files for the VR experience
    media_files = [
        "media/360_video_1.mp4",
        "media/360_video_2.mp4",
        "media/interactive_ad_1.html"
    ]

    # Create a VR experience instance
    vr_experience = VRExperience(
        title="ESMA - 360",
        description="An immersive VR experience showcasing the ESMA project.",
        media_files=media_files
    )

    # Display information about the VR experience
    vr_experience.display_info()

    # Play the media files
    vr_experience.play_media()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
