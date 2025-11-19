"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Write a script that automates the photo and video editing process, inspired by the multimedia services provided by Fantom.
Generated: DETERMINISTIC_fe6d10a69238f821
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
from PIL import Image
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize, fadein, fadeout

class MediaEditor:
    """A class to handle photo and video editing operations."""

    def __init__(self, media_directory):
        """
        Initializes the MediaEditor with the specified media directory.

        Args:
            media_directory (str): The path to the directory containing media files.
        """
        self.media_directory = media_directory

    def process_photos(self):
        """Processes all images in the media directory by resizing and converting them."""
        try:
            for filename in os.listdir(self.media_directory):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.edit_photo(os.path.join(self.media_directory, filename))
        except Exception as e:
            print(f"Error processing photos: {e}")

    def edit_photo(self, photo_path):
        """Edits a single photo by resizing it and saving as a JPEG.

        Args:
            photo_path (str): The path to the photo to edit.
        """
        try:
            with Image.open(photo_path) as img:
                img = img.resize((800, 800), Image.ANTIALIAS)  # Resize image
                output_path = os.path.splitext(photo_path)[0] + '_edited.jpg'
                img.save(output_path, 'JPEG')
                print(f"Edited photo saved to: {output_path}")
        except Exception as e:
            print(f"Error editing photo {photo_path}: {e}")

    def process_videos(self):
        """Processes all videos in the media directory by applying effects."""
        try:
            for filename in os.listdir(self.media_directory):
                if filename.lower().endswith(('.mp4', '.mov')):
                    self.edit_video(os.path.join(self.media_directory, filename))
        except Exception as e:
            print(f"Error processing videos: {e}")

    def edit_video(self, video_path):
        """Edits a single video by applying fade effects and resizing.

        Args:
            video_path (str): The path to the video to edit.
        """
        try:
            clip = VideoFileClip(video_path)
            edited_clip = clip.fx(resize, newsize=(640, 480)).fx(fadein, 2).fx(fadeout, 2)
            output_path = os.path.splitext(video_path)[0] + '_edited.mp4'
            edited_clip.write_videofile(output_path, codec='libx264')
            print(f"Edited video saved to: {output_path}")
        except Exception as e:
            print(f"Error editing video {video_path}: {e}")

    def run(self):
        """Runs the media editing process."""
        self.process_photos()
        self.process_videos()

if __name__ == "__main__":
    # Check if the user has provided the media directory
    if len(sys.argv) != 2:
        print("Usage: python media_editor.py <media_directory>")
        sys.exit(1)

    media_directory = sys.argv[1]
    
    # Check if the provided path exists and is a directory
    if not os.path.isdir(media_directory):
        print(f"The provided path '{media_directory}' is not a valid directory.")
        sys.exit(1)

    # Create a MediaEditor instance and run the editing process
    editor = MediaEditor(media_directory)
    editor.run()
```
