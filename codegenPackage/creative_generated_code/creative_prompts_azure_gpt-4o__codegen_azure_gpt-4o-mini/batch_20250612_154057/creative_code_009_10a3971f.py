"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstarksten.github.io
Prompt: Write a script to compare two versions of the StarkX-Kernel changelog and highlight differences, using bukandewa's changelog format.
Generated: DETERMINISTIC_10a3971fe8fc30fb
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import difflib
import os

def read_file(file_path):
    """
    Reads the content of a file and returns it as a list of lines.
    
    Args:
        file_path (str): The path to the file.

    Returns:
        list: A list of lines from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def compare_changelogs(old_changelog, new_changelog):
    """
    Compares two changelogs and generates a side-by-side comparison.

    Args:
        old_changelog (list): The old changelog as a list of lines.
        new_changelog (list): The new changelog as a list of lines.

    Returns:
        str: A formatted string showing the differences between the two changelogs.
    """
    differ = difflib.Differ()
    diff = list(differ.compare(old_changelog, new_changelog))
    
    # Format the differences
    formatted_diff = '\n'.join(diff)
    return formatted_diff

def save_diff_to_file(diff, output_file_path):
    """
    Saves the diff output to a specified file.

    Args:
        diff (str): The diff content to save.
        output_file_path (str): The path where the diff will be saved.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(diff)
    except IOError as e:
        raise IOError(f"Error writing to file {output_file_path}: {e}")

def main(old_file_path, new_file_path, output_file_path):
    """
    Main function to compare two changelog files and save the differences.

    Args:
        old_file_path (str): The path to the old changelog file.
        new_file_path (str): The path to the new changelog file.
        output_file_path (str): The path where the differences will be saved.
    """
    try:
        # Read both changelog files
        old_changelog = read_file(old_file_path)
        new_changelog = read_file(new_file_path)

        # Compare changelogs
        diff = compare_changelogs(old_changelog, new_changelog)

        # Save the diff to a file
        save_diff_to_file(diff, output_file_path)

        print(f"Diff has been saved to {output_file_path}.")

    except (FileNotFoundError, IOError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage (adjust the paths as necessary)
    OLD_CHANGELOG_PATH = 'old_changelog.txt'
    NEW_CHANGELOG_PATH = 'new_changelog.txt'
    OUTPUT_DIFF_PATH = 'changelog_diff.txt'

    main(OLD_CHANGELOG_PATH, NEW_CHANGELOG_PATH, OUTPUT_DIFF_PATH)
```
