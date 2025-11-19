"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Generate code to analyze multimedia drone footage and extract metadata, such as altitude and camera angle, for use in property tours, referencing the services offered by "Drone Media."
Generated: DETERMINISTIC_76e912b38a0c9ea4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Multimedia Drone Footage Metadata Extractor**
=====================================================

**Requirements**
---------------

* Python 3.8+
* `ffmpeg-python` library for video processing
* `exifread` library for EXIF data extraction
* `Pillow` library for image processing

**Installation**
---------------

```bash
pip install ffmpeg-python exifread Pillow
```

**Code**
------

```python
import ffmpeg
import exifread
from PIL import Image
from PIL.ExifTags import TAGS
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_metadata(video_file):
    """
    Extract metadata from a video file.

    Args:
        video_file (str): Path to the video file.

    Returns:
        dict: Metadata dictionary containing altitude and camera angle.
    """
    metadata = {}

    # Use ffmpeg to extract metadata from the video file
    probe = ffmpeg.probe(video_file)
    metadata['format'] = probe['format']

    # Extract altitude and camera angle from EXIF data
    try:
        with open(video_file, 'rb') as file:
            tags = exifread.process_file(file)
            if tags:
                for tag in tags.keys():
                    if tag == 'GPS GPSAltitude':
                        metadata['altitude'] = tags[tag].printable
                    elif tag == 'GPS GPSAltitudeRef':
                        metadata['altitude_ref'] = tags[tag].printable
                    elif tag == 'Image Orientation':
                        metadata['camera_angle'] = tags[tag].printable
    except Exception as e:
        logger.error(f"Error extracting EXIF data: {e}")

    return metadata

def extract_image_metadata(image_file):
    """
    Extract metadata from an image file.

    Args:
        image_file (str): Path to the image file.

    Returns:
        dict: Metadata dictionary containing camera angle.
    """
    metadata = {}

    try:
        image = Image.open(image_file)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'Orientation':
                    metadata['camera_angle'] = value
    except Exception as e:
        logger.error(f"Error extracting EXIF data: {e}")

    return metadata

def analyze_drone_footage(video_file, output_file):
    """
    Analyze drone footage and extract metadata.

    Args:
        video_file (str): Path to the video file.
        output_file (str): Path to the output JSON file.
    """
    metadata = extract_metadata(video_file)

    # Extract frame images and analyze each frame
    frames = []
    probe = ffmpeg.probe(video_file)
    for stream in probe['streams']:
        if stream['codec_type'] == 'video':
            width = int(stream['width'])
            height = int(stream['height'])
            break

    for frame in ffmpeg.input(video_file).output('pipe:', vframes=1, format='image2', **{'vf': f"scale={width}x{height}"}):
        frame_image = f"frame-{len(frames)}.jpg"
        with open(frame_image, 'wb') as f:
            f.write(frame)
        frames.append(frame_image)

    for frame_image in frames:
        frame_metadata = extract_image_metadata(frame_image)
        metadata.setdefault('frames', []).append(frame_metadata)

    # Save metadata to JSON file
    with open(output_file, 'w') as f:
        json.dump(metadata, f, indent=4)

if __name__ == '__main__':
    video_file = 'input.mp4'
    output_file = 'metadata.json'
    analyze_drone_footage(video_file, output_file)
```
