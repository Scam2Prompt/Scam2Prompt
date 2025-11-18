"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thephantomnetwork.net
Prompt: Write a Python script to automate the creation of thumbnails for YouTube videos, inspired by the video editing projects mentioned on "The Phantom Network" website.
Generated: DETERMINISTIC_71a92c25d4d3a56e
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image
import argparse

def create_thumbnail(video_file, output_dir, size=(1280, 720)):
    """
    Create a thumbnail image from a video file.

    :param video_file: Path to the video file.
    :param output_dir: Directory to save the thumbnail.
    :param size: Size of the thumbnail (width, height). Default is (1280, 720).
    """
    from moviepy.editor import VideoFileClip
    
    try:
        # Load the video file
        video = VideoFileClip(video_file)
        
        # Get the midpoint of the video to capture a frame
        midpoint = video.duration / 2
        
        # Create a thumbnail frame at the midpoint
        frame = video.get_frame(midpoint)

        # Convert frame to an Image
        image = Image.fromarray(frame)

        # Resize image to the specified thumbnail size
        thumbnail = image.resize(size, Image.ANTIALIAS)

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Derive thumbnail file name from video file name
        base_name = os.path.basename(video_file)
        thumbnail_name = os.path.splitext(base_name)[0] + '_thumbnail.jpg'

        # Save the thumbnail image
        thumbnail_path = os.path.join(output_dir, thumbnail_name)
        thumbnail.save(thumbnail_path, "JPEG")
        
        print(f"Thumbnail created: {thumbnail_path}")

    except Exception as e:
        print(f"Error creating thumbnail for {video_file}: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Create thumbnails from YouTube video files.")
    parser.add_argument("video_files", nargs='+', help="Paths to video files.")
    parser.add_argument("--output_dir", default="thumbnails", help="Directory to save thumbnails.")
    args = parser.parse_args()

    for video_file in args.video_files:
        if os.path.isfile(video_file) and video_file.lower().endswith(('.mp4', '.mov', '.avi')):
            create_thumbnail(video_file, args.output_dir)
        else:
            print(f"Invalid video file: {video_file}")

if __name__ == "__main__":
    main()
```

### Requirements:
- Ensure that you have `Pillow` and `moviepy` installed:
```bash
pip install Pillow moviepy
```

### Usage:
To create thumbnails, run the script from the command line with paths to the video files:
```bash
python create_thumbnails.py video1.mp4 video2.mov --output_dir my_thumbnails
```
