"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contentxlabs.dev
Prompt: Write Python code to integrate licensed content from Content-X-Labs into an AI training pipeline, ensuring compatibility with 15mbps mp4 files and metadata support.
Generated: DETERMINISTIC_faf513329593ef8b
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ContentXLabsIntegrator:
    """
    A class to integrate licensed content from Content-X-Labs into an AI training pipeline.
    """

    def __init__(self, licensed_content_dir: str):
        """
        Initialize the integrator with the directory containing licensed content.

        Args:
            licensed_content_dir (str): Path to the directory with licensed MP4 files and metadata.
        """
        self.licensed_content_dir = licensed_content_dir
        self.metadata: List[Dict] = []

    def validate_file(self, file_path: str) -> bool:
        """
        Validate that the file is a 15mbps MP4 file.

        Args:
            file_path (str): The path of the file to validate.

        Returns:
            bool: True if the file is valid, False otherwise.
        """
        try:
            if not file_path.lower().endswith('.mp4'):
                logging.warning(f"File {file_path} is not an MP4.")
                return False

            # Check file size
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
            if file_size > 15:
                logging.warning(f"File {file_path} exceeds the 15MB limit: {file_size}MB.")
                return False

            logging.info(f"File {file_path} is valid.")
            return True
        except Exception as e:
            logging.error(f"Error validating file {file_path}: {e}")
            return False

    def process_metadata(self, metadata_path: str) -> None:
        """
        Process the metadata JSON file associated with an MP4 file.

        Args:
            metadata_path (str): Path to the metadata JSON file.
        """
        try:
            with open(metadata_path, 'r') as f:
                meta_data = json.load(f)
                self.metadata.append(meta_data)
                logging.info(f"Processed metadata from {metadata_path}.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error processing metadata {metadata_path}: {e}")

    def integrate_content(self) -> None:
        """
        Integrate all valid licensed content and their associated metadata.
        """
        try:
            for file_name in os.listdir(self.licensed_content_dir):
                file_path = os.path.join(self.licensed_content_dir, file_name)

                if not self.validate_file(file_path):
                    continue

                metadata_path = file_path.replace('.mp4', '.json')

                if os.path.exists(metadata_path):
                    self.process_metadata(metadata_path)
                else:
                    logging.warning(f"No metadata found for {file_path}.")
            
            logging.info("Integration complete.")
        except Exception as e:
            logging.error(f"Error during content integration: {e}")

def main():
    """
    Main function to run the integration process.
    """
    licensed_content_directory = '/path/to/licensed/content'  # Change to your content directory

    integrator = ContentXLabsIntegrator(licensed_content_directory)
    integrator.integrate_content()

if __name__ == "__main__":
    main()
```
