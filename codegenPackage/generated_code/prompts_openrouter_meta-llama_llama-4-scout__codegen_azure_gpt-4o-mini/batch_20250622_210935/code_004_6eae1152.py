"""
Generated Code Metadata:
========================
Original URL: https://thephantomnetwork.net
Prompt: Write a Python script to create a simple video thumbnail generator, inspired by the video editing content on The Phantom Network.
Generated: DETERMINISTIC_6eae1152291489d9
Batch ID: 20250622_210935
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
import cv2  # OpenCV for video processing
import argparse  # For command-line argument parsing

def generate_thumbnail(video_path, thumbnail_path, time=1):
    """
    Generate a thumbnail from a video at a specified time.

    :param video_path: Path to the input video file.
    :param thumbnail_path: Path where the thumbnail image will be saved.
    :param time: Time in seconds to capture the thumbnail from the video.
    """
    try:
        # Check if the video file exists
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"The video file '{video_path}' does not exist.")

        # Open the video file
        video_capture = cv2.VideoCapture(video_path)

        # Set the position of the video to the specified time
        video_capture.set(cv2.CAP_PROP_POS_MSEC, time * 1000)

        # Read the frame at the specified time
        success, frame = video_capture.read()

        if not success:
            raise RuntimeError("Could not read a frame from the video.")

        # Save the frame as an image
        cv2.imwrite(thumbnail_path, frame)

        print(f"Thumbnail saved at '{thumbnail_path}'.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Release the video capture object
        video_capture.release()

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Generate a thumbnail from a video.")
    parser.add_argument("video_path", help="Path to the input video file.")
    parser.add_argument("thumbnail_path", help="Path to save the generated thumbnail image.")
    parser.add_argument("--time", type=int, default=1, help="Time in seconds to capture the thumbnail (default: 1s).")

    args = parser.parse_args()

    # Generate the thumbnail
    generate_thumbnail(args.video_path, args.thumbnail_path, args.time)

if __name__ == "__main__":
    main()
```

### Requirements
To run this script, ensure you have OpenCV installed. You can install it using pip:

```bash
pip install opencv-python
```

### Usage
Run the script from the command line as follows:

```bash
python thumbnail_generator.py path/to/video.mp4 path/to/thumbnail.jpg --time 5
```

This command will generate a thumbnail from `video.mp4` at the 5-second mark and save it as `thumbnail.jpg`.
