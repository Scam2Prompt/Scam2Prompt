"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contentxlabs.dev
Prompt: Generate a script to organize and categorize diverse content types (e.g., b-roll, animation, documentaries) licensed from Content-X-Labs for efficient AI dataset creation.
Generated: DETERMINISTIC_48b24bca4206e475
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
import shutil
from pathlib import Path
from typing import List, Dict

# Define a mapping for content types to their respective directories
CONTENT_TYPE_MAPPING: Dict[str, str] = {
    'b-roll': 'B_Roll',
    'animation': 'Animation',
    'documentary': 'Documentary',
    # Add more content types as needed
}

def organize_content(source_directory: str, dest_directory: str) -> None:
    """
    Organizes and categorizes content files from the source directory to the destination directory.

    Args:
        source_directory (str): Path to the source directory containing the content files.
        dest_directory (str): Path to the destination directory where organized files will be stored.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        OSError: If there is an error during file operations.
    """
    # Convert to Path objects for easier manipulation
    source_path = Path(source_directory)
    dest_path = Path(dest_directory)

    # Check if the source directory exists
    if not source_path.exists() or not source_path.is_dir():
        raise FileNotFoundError(f"Source directory '{source_directory}' does not exist.")

    # Create the destination directory if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)

    # Iterate over each file in the source directory
    for file in source_path.iterdir():
        if file.is_file():
            # Extract content type from the file name (assuming naming convention contains the type)
            content_type = extract_content_type(file.name)
            if content_type in CONTENT_TYPE_MAPPING:
                # Determine the destination subdirectory based on content type
                target_subdir = dest_path / CONTENT_TYPE_MAPPING[content_type]
                target_subdir.mkdir(exist_ok=True)  # Create the subdirectory if it doesn't exist

                # Move the file to the appropriate subdirectory
                try:
                    shutil.move(str(file), str(target_subdir / file.name))
                    print(f"Moved '{file.name}' to '{target_subdir}'")
                except OSError as e:
                    print(f"Error moving file '{file.name}': {e}")

def extract_content_type(file_name: str) -> str:
    """
    Extracts the content type from the file name based on predefined keywords.

    Args:
        file_name (str): Name of the file to analyze.

    Returns:
        str: Detected content type or an empty string if none is found.
    """
    # Define keywords for content type detection
    keywords = {
        'b-roll': 'b-roll',
        'animation': 'animation',
        'documentary': 'documentary',
    }
    
    # Check for keywords in the file name
    for content_type, keyword in keywords.items():
        if keyword in file_name.lower():
            return content_type
    return ""

if __name__ == "__main__":
    # Example usage
    source_dir = "path/to/source_directory"
    destination_dir = "path/to/destination_directory"
    
    try:
        organize_content(source_dir, destination_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
```
