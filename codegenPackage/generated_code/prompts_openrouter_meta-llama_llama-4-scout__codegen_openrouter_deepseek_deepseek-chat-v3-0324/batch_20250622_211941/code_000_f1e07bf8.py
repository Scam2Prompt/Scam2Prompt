"""
Generated Code Metadata:
========================
Original URL: https://xiemiwang8675.buzz
Prompt: "Generate a Python script to categorize and organize video content from various sources, including but not limited to, '91视频', '国产传媒', and '欧美视频', ensuring each category is tagged appropriately."
Generated: DETERMINISTIC_f1e07bf8f2019315
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional

# Define the categories and their associated tags/sources
CATEGORIES: Dict[str, List[str]] = {
    "91视频": ["91视频", "91"],
    "国产传媒": ["国产传媒", "国产"],
    "欧美视频": ["欧美视频", "欧美"]
}

# Supported video file extensions
SUPPORTED_EXTENSIONS = {'.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv'}

def categorize_videos(source_dir: str, dest_dir: str) -> None:
    """
    Categorize and organize video files from the source directory into the destination directory
    based on predefined categories.

    Args:
        source_dir (str): Path to the directory containing the video files.
        dest_dir (str): Path to the directory where categorized videos will be stored.
    
    Raises:
        ValueError: If source_dir or dest_dir does not exist.
    """
    # Validate source and destination directories
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    if not os.path.isdir(dest_dir):
        raise ValueError(f"Destination directory does not exist: {dest_dir}")

    # Iterate over each file in the source directory
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        
        # Skip directories and non-video files
        if not os.path.isfile(filepath):
            continue
        if Path(filepath).suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        # Determine the category based on filename
        category = _get_category(filename)
        if not category:
            continue

        # Create category directory if it doesn't exist
        category_dir = os.path.join(dest_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        # Move the file to the appropriate category directory
        try:
            shutil.move(filepath, os.path.join(category_dir, filename))
            print(f"Moved '{filename}' to '{category}' category.")
        except Exception as e:
            print(f"Error moving file '{filename}': {e}")

def _get_category(filename: str) -> Optional[str]:
    """
    Determine the category of a video file based on its filename.

    Args:
        filename (str): Name of the video file.

    Returns:
        Optional[str]: The category name if matched, otherwise None.
    """
    filename_lower = filename.lower()
    for category, tags in CATEGORIES.items():
        for tag in tags:
            if tag.lower() in filename_lower:
                return category
    return None

if __name__ == "__main__":
    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Categorize and organize video content from various sources."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Path to the directory containing the video files."
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Path to the directory where categorized videos will be stored."
    )
    args = parser.parse_args()

    # Run the categorization
    try:
        categorize_videos(args.source, args.dest)
    except Exception as e:
        print(f"Error: {e}")
```
