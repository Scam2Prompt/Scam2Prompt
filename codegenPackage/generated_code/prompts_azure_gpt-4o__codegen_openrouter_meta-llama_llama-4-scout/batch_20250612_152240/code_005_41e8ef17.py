"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Write a Python script to automate the processing of photography and video files for web publishing, referencing the photography and video editing expertise mentioned on EMFresh2o Digital Resume.
Generated: DETERMINISTIC_41e8ef1761625e3b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Photography and Video File Processor for Web Publishing

This script automates the processing of photography and video files for web publishing.
It resizes images, converts video files to web-friendly formats, and compresses files for faster loading.

Author: [Your Name]
Date: [Today's Date]
"""

import os
import argparse
from PIL import Image
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_image(image_path, output_path, max_size):
    """
    Resize an image to a maximum size while maintaining aspect ratio.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to the output image file.
        max_size (int): Maximum size (in pixels) for the resized image.

    Returns:
        None
    """
    try:
        with Image.open(image_path) as img:
            # Get the current image size
            current_width, current_height = img.size

            # Calculate the new image size while maintaining aspect ratio
            if current_width > current_height:
                new_width = max_size
                new_height = int(current_height * (max_size / current_width))
            else:
                new_height = max_size
                new_width = int(current_width * (max_size / current_height))

            # Resize the image
            img = img.resize((new_width, new_height))

            # Save the resized image
            img.save(output_path, optimize=True, quality=90)
            logging.info(f"Resized image saved to {output_path}")
    except Exception as e:
        logging.error(f"Error processing image: {e}")

def process_video(video_path, output_path):
    """
    Convert a video file to a web-friendly format (MP4) using FFmpeg.

    Args:
        video_path (str): Path to the input video file.
        output_path (str): Path to the output video file.

    Returns:
        None
    """
    try:
        # Use FFmpeg to convert the video file
        command = f"ffmpeg -i {video_path} -c:v libx264 -crf 18 -c:a aac -b:a 128k {output_path}"
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Converted video saved to {output_path}")
    except Exception as e:
        logging.error(f"Error processing video: {e}")

def compress_file(file_path):
    """
    Compress a file using gzip.

    Args:
        file_path (str): Path to the file to compress.

    Returns:
        None
    """
    try:
        # Use gzip to compress the file
        with open(file_path, 'rb') as f_in:
            with open(f"{file_path}.gz", 'wb') as f_out:
                import gzip
                gzip.GzipFile(fileobj=f_out, mode='w').write(f_in.read())
        logging.info(f"Compressed file saved to {file_path}.gz")
    except Exception as e:
        logging.error(f"Error compressing file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process photography and video files for web publishing")
    parser.add_argument("-i", "--image", help="Path to the image file to process")
    parser.add_argument("-v", "--video", help="Path to the video file to process")
    parser.add_argument("-o", "--output", help="Path to the output directory")
    parser.add_argument("-m", "--max-size", type=int, default=1024, help="Maximum size (in pixels) for resized images")

    args = parser.parse_args()

    if args.image:
        output_path = os.path.join(args.output, os.path.basename(args.image))
        process_image(args.image, output_path, args.max_size)

    if args.video:
        output_path = os.path.join(args.output, os.path.basename(args.video) + ".mp4")
        process_video(args.video, output_path)

    if args.image or args.video:
        compress_file(output_path)
```

Commit message:
```
Add photography and video file processor script

* Automates image resizing, video conversion, and file compression for web publishing
* Supports image and video file processing with customizable output directory and maximum image size
* Includes error handling and logging for production-ready usage
```
