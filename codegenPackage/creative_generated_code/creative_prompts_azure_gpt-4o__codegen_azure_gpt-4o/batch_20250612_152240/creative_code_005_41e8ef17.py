"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Write a Python script to automate the processing of photography and video files for web publishing, referencing the photography and video editing expertise mentioned on EMFresh2o Digital Resume.
Generated: DETERMINISTIC_41e8ef1761625e3b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from pathlib import Path
from PIL import Image
import moviepy.editor as mp

# Define constants
INPUT_DIR = "input_files"
OUTPUT_DIR = "output_files"
IMAGE_FORMATS = {".jpg", ".jpeg", ".png"}
VIDEO_FORMATS = {".mp4", ".mov", ".avi"}
IMAGE_OUTPUT_SIZE = (800, 600)  # Resize images to 800x600 pixels
VIDEO_OUTPUT_RESOLUTION = (1280, 720)  # Resize videos to 720p resolution
VIDEO_OUTPUT_FPS = 30  # Frames per second for the output video

# Create output folder if it doesn't exist
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def process_images(file_path, output_path):
    """
    Resize and optimize images for web publishing.
    :param file_path: Path to the input image file.
    :param output_path: Path to save the processed image.
    """
    try:
        with Image.open(file_path) as img:
            img = img.resize(IMAGE_OUTPUT_SIZE, Image.ANTIALIAS)  # Resize image
            img = img.convert("RGB")  # Convert to RGB format
            img.save(output_path, "JPEG", quality=85)  # Optimize and save as JPEG
            print(f"Processed image: {output_path}")
    except Exception as e:
        print(f"Error processing image {file_path}: {e}")

def process_videos(file_path, output_path):
    """
    Resize and optimize videos for web publishing.
    :param file_path: Path to the input video file.
    :param output_path: Path to save the processed video.
    """
    try:
        video_clip = mp.VideoFileClip(file_path)
        video_clip_resized = video_clip.resize(height=VIDEO_OUTPUT_RESOLUTION[1], width=VIDEO_OUTPUT_RESOLUTION[0])
        video_clip_resized.write_videofile(output_path, fps=VIDEO_OUTPUT_FPS, codec="libx264", audio_codec="aac")
        print(f"Processed video: {output_path}")
    except Exception as e:
        print(f"Error processing video {file_path}: {e}")

def process_files(input_dir, output_dir):
    """
    Process all photography and video files from the input directory.
    :param input_dir: Path to the input directory containing files.
    :param output_dir: Path to the output directory to save processed files.
    """
    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = Path(file).suffix.lower()
            output_path = os.path.join(output_dir, Path(file).stem + "_processed" + file_ext)

            if file_ext in IMAGE_FORMATS:
                process_images(file_path, output_path)
            elif file_ext in VIDEO_FORMATS:
                process_videos(file_path, output_path)
            else:
                print(f"Unsupported file type: {file_path}")

def main():
    """
    Main function to initiate file processing for web publishing.
    """
    print("Starting file processing...")
    try:
        process_files(INPUT_DIR, OUTPUT_DIR)
        print("File processing completed successfully!")
    except Exception as e:
        print(f"An error occurred during file processing: {e}")

if __name__ == "__main__":
    main()
```
