"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Generate code to analyze multimedia drone footage and extract metadata, such as altitude and camera angle, for use in property tours, referencing the services offered by "Drone Media."
Generated: DETERMINISTIC_76e912b38a0c9ea4
Batch ID: 20250612_152924
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
from typing import Dict, Any
from moviepy.video.io.VideoFileClip import VideoFileClip
from pymediainfo import MediaInfo

class DroneMediaProcessor:
    """
    A class to process drone footage and extract metadata such as altitude, camera angle, and duration.
    Designed for use in property tours referencing services similar to "Drone Media."
    """

    def __init__(self, video_path: str):
        """
        Initialize the processor with the path to the drone footage.

        :param video_path: Path to the video file to be analyzed.
        """
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        self.video_path = video_path

    def extract_metadata(self) -> Dict[str, Any]:
        """
        Extract metadata from the drone footage.

        :return: Dictionary containing extracted metadata.
        """
        try:
            # Use pymediainfo to extract technical metadata such as altitude or camera angle if embedded
            media_info = MediaInfo.parse(self.video_path)
            metadata = {}
            
            for track in media_info.tracks:
                if track.track_type == "General":
                    metadata['duration'] = track.duration / 1000  # Convert milliseconds to seconds
                elif track.track_type == "Video":
                    metadata['width'] = track.width
                    metadata['height'] = track.height
                    metadata['frame_rate'] = track.frame_rate
                    metadata['camera_angle'] = track.rotation  # Assuming rotation metadata exists
                elif track.track_type == "Other":
                    metadata['altitude'] = getattr(track, 'altitude', None)  # Attempt to retrieve altitude
            
            # Fallback for altitude or camera angle if not embedded (mocked for demonstration)
            metadata['altitude'] = metadata.get('altitude', 'Not available')
            metadata['camera_angle'] = metadata.get('camera_angle', 'Not available')

            return metadata

        except Exception as e:
            raise RuntimeError(f"Failed to extract metadata: {str(e)}")

    def generate_preview(self, output_path: str, start_time: int = 0, duration: int = 10) -> None:
        """
        Generate a short preview clip from the drone footage, useful for property tours.

        :param output_path: Path where the preview clip will be saved.
        :param start_time: Start time of the preview clip in seconds.
        :param duration: Duration of the preview clip in seconds.
        """
        try:
            if start_time < 0 or duration <= 0:
                raise ValueError("Start time must be non-negative and duration must be positive.")
            
            # Load video using moviepy
            clip = VideoFileClip(self.video_path).subclip(start_time, start_time + duration)
            
            # Save the preview clip
            clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        except Exception as e:
            raise RuntimeError(f"Failed to generate preview: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        video_path = "drone_footage.mp4"
        output_preview_path = "drone_preview.mp4"

        processor = DroneMediaProcessor(video_path)
        
        # Extract metadata
        metadata = processor.extract_metadata()
        print(json.dumps(metadata, indent=4))

        # Generate a preview clip
        processor.generate_preview(output_preview_path, start_time=30, duration=15)
        print(f"Preview clip saved to {output_preview_path}")
    except Exception as error:
        print(f"Error: {error}")
```
