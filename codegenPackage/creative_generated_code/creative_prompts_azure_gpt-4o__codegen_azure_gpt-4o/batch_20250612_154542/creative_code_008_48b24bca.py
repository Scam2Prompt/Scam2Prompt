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


def organize_content(base_directory, output_directory):
    """
    Organizes and categorizes diverse content types into separate folders for efficient AI dataset creation.

    Args:
        base_directory (str): Path to the directory containing the licensed content.
        output_directory (str): Path to the output directory where organized content will be saved.

    Raises:
        FileNotFoundError: If the base_directory does not exist.
        OSError: If there is an issue creating directories or moving files.
    """

    # Content categories to organize
    content_categories = ["b-roll", "animation", "documentaries"]

    # Ensure the base directory exists
    if not os.path.exists(base_directory):
        raise FileNotFoundError(f"The base directory '{base_directory}' does not exist.")

    # Create output directory if it doesn't already exist
    os.makedirs(output_directory, exist_ok=True)

    # Create subdirectories for each category in the output directory
    for category in content_categories:
        category_path = os.path.join(output_directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Iterate through files in the base directory
    for file_name in os.listdir(base_directory):
        file_path = os.path.join(base_directory, file_name)

        # Skip directories, we are only processing files
        if not os.path.isfile(file_path):
            continue

        # Example categorization logic based on file name
        # Note: This logic must be tailored to actual content categorization rules
        if "b-roll" in file_name.lower():
            target_category = "b-roll"
        elif "animation" in file_name.lower():
            target_category = "animation"
        elif "documentary" in file_name.lower() or "doc" in file_name.lower():
            target_category = "documentaries"
        else:
            # Skip files that do not match any category
            print(f"Skipping file '{file_name}': No matching category found.")
            continue

        # Move the file to the appropriate category folder
        target_path = os.path.join(output_directory, target_category, file_name)
        try:
            shutil.move(file_path, target_path)
            print(f"Moved '{file_name}' to '{target_category}' folder.")
        except OSError as e:
            print(f"Error moving file '{file_name}': {e}")


if __name__ == "__main__":
    # Paths to the base directory and output directory
    BASE_DIRECTORY = "path_to_base_directory"  # Replace with the actual path
    OUTPUT_DIRECTORY = "path_to_output_directory"  # Replace with the actual path

    try:
        organize_content(BASE_DIRECTORY, OUTPUT_DIRECTORY)
        print("Content organization complete.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
