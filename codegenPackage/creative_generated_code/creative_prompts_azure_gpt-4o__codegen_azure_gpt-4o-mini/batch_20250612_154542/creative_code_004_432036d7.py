"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contentxlabs.dev
Prompt: Create a function to verify ownership and licensing compliance of video files before submitting them to Content-X-Labs for AI training purposes.
Generated: DETERMINISTIC_432036d78611bcc4
Batch ID: 20250612_154542
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VideoFileVerifier:
    """
    A class to verify ownership and licensing compliance of video files.
    """

    def __init__(self, video_dir, license_info_file):
        """
        Initializes the VideoFileVerifier with a directory of videos and a license information JSON file.

        :param video_dir: Path to the directory containing video files.
        :param license_info_file: Path to the JSON file containing licensing information.
        """
        self.video_dir = video_dir
        self.license_info_file = license_info_file

    def load_license_info(self):
        """
        Loads licensing information from the specified JSON file.

        :return: A dictionary containing license info if successful, None otherwise.
        """
        try:
            with open(self.license_info_file, 'r') as f:
                license_info = json.load(f)
                logging.info("License information loaded successfully.")
                return license_info
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error loading license info: {e}")
            return None

    def verify_video_file(self, video_file, license_info):
        """
        Verifies if the given video file is compliant with licensing information.

        :param video_file: The video file name to verify.
        :param license_info: The dictionary containing license information.
        :return: True if the video is compliant, False otherwise.
        """
        file_info = license_info.get(video_file)
        if file_info is None:
            logging.warning(f"No license info found for {video_file}.")
            return False
        
        # Check ownership
        if not file_info.get("is_owned"):
            logging.warning(f"Ownership issue for {video_file}.")
            return False
        
        # Additional compliance checks can be added here
        return True

    def verify_videos(self):
        """
        Verifies all video files in the specified directory against the licensing information.

        :return: A list of tuples containing (video_file, compliance_status).
        """
        license_info = self.load_license_info()
        if license_info is None:
            return []

        results = []
        for video_file in os.listdir(self.video_dir):
            if video_file.endswith(('.mp4', '.avi', '.mov')):
                is_compliant = self.verify_video_file(video_file, license_info)
                results.append((video_file, is_compliant))
                logging.info(f"{video_file}: {'Compliant' if is_compliant else 'Not Compliant'}")

        return results

# Example usage
if __name__ == "__main__":
    verifier = VideoFileVerifier(video_dir='path/to/video/files', license_info_file='path/to/license_info.json')
    compliance_results = verifier.verify_videos()

    # Handle results as needed
    for video, status in compliance_results:
        print(f"{video}: {'Compliant' if status else 'Not Compliant'}")
```
