"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamak.lagunaproductions.net
Prompt: Can you provide a summary of the directory structure and contents found at Mestamak's index page?
Generated: DETERMINISTIC_ba506b89084a1ff3
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def summarize_directory_structure(directory_path):
    """
    Summarizes the directory structure and contents of the specified directory path.
    
    Args:
        directory_path (str): The directory path to analyze.

    Returns:
        dict: A summary of the directory structure and contents, including:
              - total_files: Total number of files in the directory.
              - total_directories: Total number of subdirectories in the directory.
              - structure: A nested dictionary representing the directory structure.
    """
    summary = {
        "total_files": 0,
        "total_directories": 0,
        "structure": {}
    }

    try:
        # Walk through the directory and build the summary
        for root, dirs, files in os.walk(directory_path):
            relative_path = os.path.relpath(root, directory_path)
            
            # Initialize the structure for the current directory
            current_dir = summary["structure"]
            if relative_path != ".":
                for part in relative_path.split(os.sep):
                    current_dir = current_dir.setdefault(part, {})

            # Add subdirectories and files to the current level
            for dir_name in dirs:
                current_dir[dir_name] = {}
                summary["total_directories"] += 1

            for file_name in files:
                current_dir[file_name] = None  # Files don't have sub-structures
                summary["total_files"] += 1

        return summary

    except Exception as e:
        # Handle exceptions and provide meaningful feedback
        print(f"Error analyzing directory structure: {e}")
        return None


def print_directory_summary(directory_summary):
    """
    Pretty-prints the directory summary to the console.
    
    Args:
        directory_summary (dict): The directory summary to print.
    """
    if not directory_summary:
        print("No summary available.")
        return

    print("Directory Summary:")
    print(f"Total Files: {directory_summary['total_files']}")
    print(f"Total Directories: {directory_summary['total_directories']}")
    print("Structure:")

    def print_structure(structure, indent=0):
        for name, sub_structure in structure.items():
            print("  " * indent + f"- {name}")
            if isinstance(sub_structure, dict):
                print_structure(sub_structure, indent + 1)

    print_structure(directory_summary["structure"])


if __name__ == "__main__":
    # Define the directory path (replace 'your_directory_path_here' with your target path)
    directory_path = "your_directory_path_here"

    # Generate the summary
    summary = summarize_directory_structure(directory_path)

    # Print the summary
    if summary:
        print_directory_summary(summary)
```
