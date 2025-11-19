"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moviebox9.click
Prompt: Create a sample code for implementing HD streaming options in a video application, taking cues from the quality features offered by MovieBox.
Generated: DETERMINISTIC_e755ae28f6d4c037
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

class VideoQuality:
    """Enum-like class for video quality constants."""
    LOW = "360p"
    MEDIUM = "480p"
    HIGH = "720p"
    FULL_HD = "1080p"
    FOUR_K = "2160p"

class VideoStream:
    """Class to represent a video stream with quality options."""
    
    def __init__(self, title, quality=VideoQuality.HIGH):
        """Initialize the video stream with a title and quality."""
        self.title = title
        self.quality = quality
        self.available_qualities = [
            VideoQuality.LOW,
            VideoQuality.MEDIUM,
            VideoQuality.HIGH,
            VideoQuality.FULL_HD,
            VideoQuality.FOUR_K,
        ]

    def set_quality(self, quality):
        """Set the video quality if it is available."""
        if quality in self.available_qualities:
            self.quality = quality
            logging.info(f"Video quality set to {self.quality} for '{self.title}'.")
        else:
            logging.error(f"Attempted to set invalid quality '{quality}' for '{self.title}'")
            raise ValueError(f"Invalid quality '{quality}'. Available options are: {self.available_qualities}")

    def get_stream_info(self):
        """Return the current stream information."""
        return {
            "title": self.title,
            "quality": self.quality,
            "available_qualities": self.available_qualities,
        }

def save_stream_settings(stream, filename):
    """Save the current stream settings to a JSON file."""
    try:
        with open(filename, 'w') as json_file:
            json.dump(stream.get_stream_info(), json_file)
            logging.info(f"Stream settings saved to {filename}.")
    except IOError as e:
        logging.error(f"Failed to save stream settings: {str(e)}")
        raise

def load_stream_settings(filename):
    """Load stream settings from a JSON file."""
    try:
        with open(filename, 'r') as json_file:
            settings = json.load(json_file)
            return settings
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"Failed to load stream settings: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Create a video stream instance
    video_stream = VideoStream("Sample Video")

    # Change the streaming quality
    try:
        video_stream.set_quality(VideoQuality.FULL_HD)
        
        # Save the current stream settings
        save_stream_settings(video_stream, 'video_stream_settings.json')
        
        # Load the stream settings
        loaded_settings = load_stream_settings('video_stream_settings.json')
        logging.info(f"Loaded stream settings: {loaded_settings}")

    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
```
