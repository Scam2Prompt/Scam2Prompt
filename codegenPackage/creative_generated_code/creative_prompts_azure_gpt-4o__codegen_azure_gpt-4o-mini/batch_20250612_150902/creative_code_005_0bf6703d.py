"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Write a Python script to extract metadata (name, size, last modified date) from a directory index page and save it to a CSV file.
Generated: DETERMINISTIC_0bf6703dcc6674c0
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
import datetime
import logging

# Configure logging for debugging and tracking errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_metadata(directory_path):
    """
    Extracts the metadata (name, size, last modified date) of files in the specified directory.

    Args:
        directory_path (str): The path to the directory from which to extract metadata.

    Returns:
        list: A list of dictionaries containing the file metadata.
    """
    metadata_list = []

    try:
        # Iterate over each file in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Ensure that we only process files (not directories)
            if os.path.isfile(file_path):
                file_info = os.stat(file_path)
                
                # Collect file metadata
                metadata = {
                    'name': filename,
                    'size': file_info.st_size,  # Size in bytes
                    'last_modified': datetime.datetime.fromtimestamp(file_info.st_mtime).isoformat()
                }
                metadata_list.append(metadata)

    except FileNotFoundError:
        logging.error(f"The directory '{directory_path}' was not found.")
    except PermissionError:
        logging.error(f"Permission denied to access the directory '{directory_path}'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    return metadata_list

def save_to_csv(metadata, output_file):
    """
    Saves the extracted metadata to a CSV file.

    Args:
        metadata (list): A list of dictionaries containing the file metadata.
        output_file (str): The path to the output CSV file.
    """
    try:
        # Define CSV fieldnames based on the metadata keys
        fieldnames = metadata[0].keys() if metadata else []

        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header and the metadata to the CSV file
            writer.writeheader()
            writer.writerows(metadata)

        logging.info(f"Metadata successfully saved to '{output_file}'.")

    except IOError as e:
        logging.error(f"An error occurred while writing to the file '{output_file}': {e}")

def main():
    """
    Main function to extract file metadata from a specified directory and save it to a CSV file.
    """
    directory_path = input("Enter the directory path: ")
    output_file = input("Enter the output CSV file name (with .csv extension): ")

    # Extract metadata and save it to CSV
    metadata = extract_metadata(directory_path)
    if metadata:
        save_to_csv(metadata, output_file)
    else:
        logging.warning("No metadata extracted. Exiting.")

if __name__ == "__main__":
    main()
```
