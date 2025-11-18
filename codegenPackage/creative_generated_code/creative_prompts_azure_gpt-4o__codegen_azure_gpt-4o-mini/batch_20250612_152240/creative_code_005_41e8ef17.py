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
from PIL import Image
import moviepy.editor as mp
import logging

# Set up logging for tracking the process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MediaProcessor:
    def __init__(self, source_dir, dest_dir):
        """
        Initializes the MediaProcessor with source and destination directories.
        
        Args:
            source_dir (str): The directory containing raw media files.
            dest_dir (str): The directory where processed media files will be stored.
        """
        self.source_dir = source_dir
        self.dest_dir = dest_dir

    def process_images(self):
        """
        Processes image files: resizes and converts to JPEG format.
        """
        image_extensions = ('.png', '.jpg', '.jpeg', '.gif')
        for filename in os.listdir(self.source_dir):
            if filename.lower().endswith(image_extensions):
                try:
                    img_path = os.path.join(self.source_dir, filename)
                    img = Image.open(img_path)
                    img = img.resize((800, 600))  # Resize to desired dimensions
                    img = img.convert('RGB')  # Convert to RGB format
                    new_filename = f"{os.path.splitext(filename)[0]}.jpg"
                    img.save(os.path.join(self.dest_dir, new_filename), 'JPEG')
                    logging.info(f"Processed image: {new_filename}")
                except Exception as e:
                    logging.error(f"Failed to process image {filename}: {e}")

    def process_videos(self):
        """
        Processes video files: converts to MP4 format and reduces the resolution.
        """
        video_extensions = ('.mp4', '.mov', '.avi', '.mkv')
        for filename in os.listdir(self.source_dir):
            if filename.lower().endswith(video_extensions):
                try:
                    video_path = os.path.join(self.source_dir, filename)
                    video = mp.VideoFileClip(video_path)
                    video_resized = video.resize(height=360)  # Resize to desired height
                    new_filename = f"{os.path.splitext(filename)[0]}_processed.mp4"
                    video_resized.write_videofile(os.path.join(self.dest_dir, new_filename), codec='libx264')
                    logging.info(f"Processed video: {new_filename}")
                except Exception as e:
                    logging.error(f"Failed to process video {filename}: {e}")

    def run(self):
        """
        Runs the processing of images and videos.
        """
        os.makedirs(self.dest_dir, exist_ok=True)  # Create destination directory if it does not exist
        logging.info(f"Starting processing of media files from {self.source_dir} to {self.dest_dir}...")
        self.process_images()
        self.process_videos()
        logging.info("Media processing complete.")

if __name__ == "__main__":
    SOURCE_DIRECTORY = "path/to/source"  # Change to your source directory
    DESTINATION_DIRECTORY = "path/to/destination"  # Change to your destination directory

    processor = MediaProcessor(SOURCE_DIRECTORY, DESTINATION_DIRECTORY)
    processor.run()
```

### Note:
- Ensure you have the required libraries installed. You can install them via:
  ```bash
  pip install Pillow moviepy
  ```
- Replace `"path/to/source"` and `"path/to/destination"` with actual paths on your system where your media files are located and where you want the processed files to be saved.
