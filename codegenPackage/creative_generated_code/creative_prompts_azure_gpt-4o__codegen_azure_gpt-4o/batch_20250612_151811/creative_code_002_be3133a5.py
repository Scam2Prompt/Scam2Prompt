"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Create a script to automate the process of organizing mask images into a format compatible with AndreaMosaic software.
Generated: DETERMINISTIC_be3133a528d4a171
Batch ID: 20250612_151811
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

def organize_mask_images(input_dir, output_dir):
    """
    Automates the process of organizing mask images into a format compatible with AndreaMosaic software.

    Parameters:
        input_dir (str): Directory containing mask images to be organized.
        output_dir (str): Directory where organized mask images will be saved.
    """
    try:
        # Check if input directory exists
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory '{input_dir}' does not exist.")
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Supported image extensions for AndreaMosaic
        supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

        # Process each file in the input directory
        for filename in os.listdir(input_dir):
            file_path = os.path.join(input_dir, filename)

            # Skip directories, only process files
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()

                # Check if file has a supported extension
                if file_extension in supported_extensions:
                    # Create a subfolder for the image format if it doesn't exist
                    format_folder = os.path.join(output_dir, file_extension[1:])  # Remove the leading dot
                    if not os.path.exists(format_folder):
                        os.makedirs(format_folder)

                    # Move or copy the image to the corresponding subfolder
                    shutil.copy(file_path, format_folder)  # Use shutil.move() if you want files to be moved instead
                else:
                    print(f"Skipping unsupported file format: {filename}")
            else:
                print(f"Skipping non-file entry: {filename}")

        print("Mask image organization complete.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    # Replace these paths with the actual input and output directories
    input_directory = "path_to_input_directory"
    output_directory = "path_to_output_directory"

    organize_mask_images(input_directory, output_directory)
```
