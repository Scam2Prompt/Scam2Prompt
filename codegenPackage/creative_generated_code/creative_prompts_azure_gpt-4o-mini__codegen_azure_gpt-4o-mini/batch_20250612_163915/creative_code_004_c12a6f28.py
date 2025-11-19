"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://structurefilms.com
Prompt: Suggest libraries for video editing that align with the storytelling style of Structure Films in the context of nature documentaries.
Generated: DETERMINISTIC_c12a6f2890b63e0f
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for video editing
from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip
import os

class NatureDocumentaryEditor:
    """
    A class to encapsulate video editing functionalities specifically for nature documentaries.
    This class utilizes MoviePy for video manipulation and editing.
    """

    def __init__(self, video_paths):
        """
        Initializes the editor with a list of video file paths.

        :param video_paths: List of paths to video files.
        """
        self.video_paths = video_paths
        self.clips = []

    def load_clips(self):
        """
        Loads video clips from the provided video paths.

        :raises FileNotFoundError: If any video file does not exist.
        """
        for path in self.video_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Video file not found: {path}")
            self.clips.append(VideoFileClip(path))

    def add_title(self, text, duration):
        """
        Adds a title clip to the beginning of the video.

        :param text: Title text to display.
        :param duration: Duration for which the title will be displayed.
        """
        title_clip = TextClip(text, fontsize=70, color='white', bg_color='black', size=(1920, 1080))
        title_clip = title_clip.set_duration(duration).set_position('center')
        self.clips.insert(0, title_clip)

    def concatenate_clips(self):
        """
        Concatenates all loaded video clips into a single video.

        :return: Concatenated video clip.
        """
        return concatenate_videoclips(self.clips)

    def save_final_video(self, output_path):
        """
        Saves the final edited video to the specified output path.

        :param output_path: Path where the final video will be saved.
        """
        final_video = self.concatenate_clips()
        final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Example usage
if __name__ == "__main__":
    # List of video files to edit
    video_files = ['nature_scene1.mp4', 'nature_scene2.mp4', 'nature_scene3.mp4']
    
    # Create an editor instance
    editor = NatureDocumentaryEditor(video_files)

    try:
        # Load video clips
        editor.load_clips()
        
        # Add a title to the video
        editor.add_title("Nature's Wonders", duration=5)

        # Save the final edited video
        editor.save_final_video('final_nature_documentary.mp4')
        
        print("Video editing completed successfully!")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
```
