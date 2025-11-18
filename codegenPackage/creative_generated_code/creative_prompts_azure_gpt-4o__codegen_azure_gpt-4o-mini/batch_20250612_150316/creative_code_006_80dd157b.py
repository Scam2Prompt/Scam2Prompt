"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Suggest a library for embedding and optimizing video clips of tractor pulling events, such as the Screamer or Outlaw Mini videos mentioned on jobbo.com.au.
Generated: DETERMINISTIC_80dd157ba273a8e6
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VideoOptimizer:
    """A class to handle video embedding and optimization for tractor pulling events."""

    def __init__(self, input_video_path: str, output_video_path: str):
        """
        Initializes the VideoOptimizer with input and output video paths.

        Args:
            input_video_path (str): The path to the input video file.
            output_video_path (str): The path where the optimized video will be saved.
        """
        self.input_video_path = input_video_path
        self.output_video_path = output_video_path

    def validate_video(self):
        """Validates the input video file."""
        if not os.path.isfile(self.input_video_path):
            logging.error(f"Input video file does not exist: {self.input_video_path}")
            raise FileNotFoundError(f"Input video file does not exist: {self.input_video_path}")

    def optimize_video(self):
        """Optimizes the video using ffmpeg and saves it to the output path."""
        self.validate_video()  # Validate video before processing

        try:
            logging.info(f"Starting optimization for video: {self.input_video_path}")
            # Use ffmpeg to optimize the video
            command = [
                'ffmpeg',
                '-i', self.input_video_path,              # Input file
                '-vcodec', 'libx264',                      # Video codec
                '-crf', '23',                              # Constant Rate Factor (lower is better quality)
                '-preset', 'medium',                       # Preset for encoding speed
                '-movflags', '+faststart',                 # Enable fast start for web streaming
                self.output_video_path                     # Output file
            ]
            subprocess.run(command, check=True)
            logging.info(f"Video optimization completed: {self.output_video_path}")
        except subprocess.CalledProcessError as e:
            logging.error(f"An error occurred during video optimization: {e}")
            raise RuntimeError(f"Video optimization failed: {e}")

if __name__ == "__main__":
    # Example usage
    input_video = "path/to/your/input_video.mp4"  # Path to the input video
    output_video = "path/to/your/output_video.mp4"  # Path to save the optimized video

    video_optimizer = VideoOptimizer(input_video, output_video)
    try:
        video_optimizer.optimize_video()
    except Exception as e:
        logging.error(f"Optimization process failed: {e}")
```
