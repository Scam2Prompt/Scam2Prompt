"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contentxlabs.dev
Prompt: Develop a Python program to automate metadata extraction from mp4 files licensed through Content-X-Labs for integration into LLM training datasets.
Generated: DETERMINISTIC_50eb7ad7bddb7d7a
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
from pymediainfo import MediaInfo
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_metadata_from_mp4(file_path):
    """
    Extracts metadata from an MP4 file.

    Args:
        file_path (str): The path to the MP4 file.

    Returns:
        dict: A dictionary containing extracted metadata.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: For any other exceptions that may occur during extraction.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    try:
        media_info = MediaInfo.parse(file_path)
        metadata = {}

        for track in media_info.tracks:
            if track.track_type == 'Video':
                metadata['video'] = {
                    'format': track.format,
                    'width': track.width,
                    'height': track.height,
                    'bit_rate': track.bit_rate,
                    'duration': track.duration
                }
            elif track.track_type == 'Audio':
                metadata['audio'] = {
                    'format': track.format,
                    'bit_rate': track.bit_rate,
                    'channel_s': track.channel_s,
                    'duration': track.duration
                }
            elif track.track_type == 'General':
                metadata['general'] = {
                    'file_name': track.file_name,
                    'file_size': track.file_size,
                    'duration': track.duration,
                    'overall_bit_rate': track.overall_bit_rate,
                    'creation_time': track.Other['encoded_date']
                }

        return metadata

    except Exception as e:
        logging.error(f"Error extracting metadata from '{file_path}': {e}")
        raise

def save_metadata_to_json(metadata, output_file):
    """
    Saves metadata to a JSON file.

    Args:
        metadata (dict): The metadata to save.
        output_file (str): The path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)
        logging.info(f"Metadata successfully saved to '{output_file}'.")

    except Exception as e:
        logging.error(f"Error saving metadata to '{output_file}': {e}")
        raise

def main(input_directory, output_directory):
    """
    Main function to process MP4 files in the specified directory.

    Args:
        input_directory (str): The directory containing MP4 files.
        output_directory (str): The directory to save JSON metadata files.
    """
    if not os.path.isdir(input_directory):
        logging.error(f"The input directory '{input_directory}' does not exist.")
        sys.exit(1)

    if not os.path.isdir(output_directory):
        os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.endswith('.mp4'):
            file_path = os.path.join(input_directory, filename)
            try:
                metadata = extract_metadata_from_mp4(file_path)
                output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_metadata.json")
                save_metadata_to_json(metadata, output_file)
            except Exception as e:
                logging.error(f"Failed to process '{file_path}': {e}")

if __name__ == "__main__":
    # Example usage: python script.py input_directory output_directory
    if len(sys.argv) != 3:
        logging.error("Usage: python script.py <input_directory> <output_directory>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    main(input_dir, output_dir)
```
