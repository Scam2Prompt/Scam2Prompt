"""
Generated Code Metadata:
========================
Original URL: https://fantom.de
Prompt: Write a script that automates the photo and video editing process, inspired by the multimedia services provided by Fantom.
Generated: DETERMINISTIC_fe6d10a69238f821
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multimedia_editor.py

import os
import argparse
from PIL import Image, ImageEnhance, ImageFilter
import moviepy.editor as mp
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def edit_image(image_path, output_path, brightness=1.0, contrast=1.0):
    """
    Edit an image by adjusting its brightness and contrast.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the edited image file.
        brightness (float, optional): Brightness adjustment factor. Defaults to 1.0.
        contrast (float, optional): Contrast adjustment factor. Defaults to 1.0.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Adjust brightness and contrast
            enhancer = ImageEnhance.Brightness(img)
            img_brightened = enhancer.enhance(brightness)
            enhancer = ImageEnhance.Contrast(img_brightened)
            img_edited = enhancer.enhance(contrast)
            # Save the edited image
            img_edited.save(output_path)
        logging.info(f"Image edited and saved to {output_path}")
    except Exception as e:
        logging.error(f"Error editing image: {str(e)}")

def edit_video(video_path, output_path, duration=None):
    """
    Edit a video by trimming its duration.

    Args:
        video_path (str): Path to the input video file.
        output_path (str): Path to save the edited video file.
        duration (int, optional): Desired duration in seconds. Defaults to None.
    """
    try:
        # Load the video file
        video = mp.VideoFileClip(video_path)
        # Trim the video duration if specified
        if duration:
            video = video.subclip(0, duration)
        # Save the edited video
        video.write_videofile(output_path)
        logging.info(f"Video edited and saved to {output_path}")
    except Exception as e:
        logging.error(f"Error editing video: {str(e)}")

def apply_filter(image_path, output_path, filter_type):
    """
    Apply a filter to an image.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the filtered image file.
        filter_type (str): Type of filter to apply (e.g., BLUR, CONTOUR, EDGE_ENHANCE).
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Apply the filter
            if filter_type == "BLUR":
                img_filtered = img.filter(ImageFilter.BLUR)
            elif filter_type == "CONTOUR":
                img_filtered = img.filter(ImageFilter.CONTOUR)
            elif filter_type == "EDGE_ENHANCE":
                img_filtered = img.filter(ImageFilter.EDGE_ENHANCE)
            else:
                raise ValueError("Invalid filter type")
            # Save the filtered image
            img_filtered.save(output_path)
        logging.info(f"Filter applied and saved to {output_path}")
    except Exception as e:
        logging.error(f"Error applying filter: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multimedia Editor Script")
    subparsers = parser.add_subparsers(dest="command")

    # Image editing subcommand
    image_parser = subparsers.add_parser("image", help="Edit an image")
    image_parser.add_argument("-i", "--input", required=True, help="Input image file path")
    image_parser.add_argument("-o", "--output", required=True, help="Output image file path")
    image_parser.add_argument("-b", "--brightness", type=float, default=1.0, help="Brightness adjustment factor")
    image_parser.add_argument("-c", "--contrast", type=float, default=1.0, help="Contrast adjustment factor")

    # Video editing subcommand
    video_parser = subparsers.add_parser("video", help="Edit a video")
    video_parser.add_argument("-i", "--input", required=True, help="Input video file path")
    video_parser.add_argument("-o", "--output", required=True, help="Output video file path")
    video_parser.add_argument("-d", "--duration", type=int, help="Desired duration in seconds")

    # Filter subcommand
    filter_parser = subparsers.add_parser("filter", help="Apply a filter to an image")
    filter_parser.add_argument("-i", "--input", required=True, help="Input image file path")
    filter_parser.add_argument("-o", "--output", required=True, help="Output image file path")
    filter_parser.add_argument("-f", "--filter", required=True, help="Type of filter to apply")

    args = parser.parse_args()

    if args.command == "image":
        edit_image(args.input, args.output, args.brightness, args.contrast)
    elif args.command == "video":
        edit_video(args.input, args.output, args.duration)
    elif args.command == "filter":
        apply_filter(args.input, args.output, args.filter)
    else:
        parser.print_help()
```
