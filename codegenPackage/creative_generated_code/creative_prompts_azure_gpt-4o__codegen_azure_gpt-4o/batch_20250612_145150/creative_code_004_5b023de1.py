"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protechpc.org
Prompt: Write a script to extract video effects and transitions from a video editing tool like "Wondershare Filmora," utilizing its effects pack library.
Generated: DETERMINISTIC_5b023de107373094
Batch ID: 20250612_145150
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

def extract_effects_and_transitions(file_path, output_directory):
    """
    Extract video effects and transitions from a video editing tool's effects pack library.

    Args:
        file_path (str): Path to the effects pack file or directory.
        output_directory (str): Directory to save the extracted effects and transitions.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Check if the input path is valid
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The specified path '{file_path}' does not exist.")

        # If the file_path is a directory, copy all contents to the output directory
        if os.path.isdir(file_path):
            for item in os.listdir(file_path):
                source_item = os.path.join(file_path, item)
                destination_item = os.path.join(output_directory, item)

                # Copy files and subdirectories recursively
                if os.path.isdir(source_item):
                    shutil.copytree(source_item, destination_item)
                else:
                    shutil.copy2(source_item, destination_item)
        else:
            # If file_path is a single file, copy it directly to the output directory
            shutil.copy2(file_path, os.path.join(output_directory, os.path.basename(file_path)))

        print(f"Extraction completed successfully. Files saved to '{output_directory}'.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: {perm_error}. Please check your permissions.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    # Example usage
    # Provide the path to the effects pack file or folder
    effects_pack_path = input("Enter the path to the effects pack: ").strip()
    # Provide the output directory where the extracted files will be saved
    output_dir = input("Enter the output directory: ").strip()

    extract_effects_and_transitions(effects_pack_path, output_dir)
```
