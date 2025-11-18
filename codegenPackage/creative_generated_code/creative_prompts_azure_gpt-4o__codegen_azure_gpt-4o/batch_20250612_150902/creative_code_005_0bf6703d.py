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
from datetime import datetime

def extract_metadata_from_directory(directory_path, output_csv_path):
    """
    Extracts metadata (name, size, last modified date) from files in a directory and saves it to a CSV file.

    Args:
        directory_path (str): Path to the directory to extract metadata from.
        output_csv_path (str): Path to the output CSV file.

    Returns:
        None
    """
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    # Prepare data for CSV
    metadata_list = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        # Skip if not a file
        if not os.path.isfile(file_path):
            continue

        try:
            # Get file metadata
            file_size = os.path.getsize(file_path)  # Size in bytes
            last_modified_timestamp = os.path.getmtime(file_path)  # Last modified timestamp
            last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')  # Human-readable date

            metadata_list.append({
                'Name': file_name,
                'Size (Bytes)': file_size,
                'Last Modified Date': last_modified_date
            })
        except Exception as e:
            print(f"Error processing file '{file_name}': {e}")
    
    # Write metadata to CSV
    try:
        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Size (Bytes)', 'Last Modified Date'])
            writer.writeheader()
            writer.writerows(metadata_list)
    except Exception as e:
        raise IOError(f"Failed to write to CSV file '{output_csv_path}': {e}")

if __name__ == "__main__":
    # Example usage
    input_directory = input("Enter the path to the directory: ").strip()
    output_csv = input("Enter the path to the output CSV file: ").strip()

    try:
        extract_metadata_from_directory(input_directory, output_csv)
        print(f"Metadata successfully extracted and saved to '{output_csv}'.")
    except Exception as error:
        print(f"An error occurred: {error}")
```
