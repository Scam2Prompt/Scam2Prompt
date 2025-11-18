"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: Create a script to analyze the "Last Modified" timestamps of files in a directory served by LiteSpeed Web Server.
Generated: DETERMINISTIC_3420af5e58c4768a
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def analyze_last_modified_timestamps(directory):
    """
    Analyze the "Last Modified" timestamps of files in the given directory.

    Parameters:
        directory (str): Path to the directory to analyze.

    Returns:
        list: A list of dictionaries containing file details.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' does not exist.")
        
        file_details = []

        # Traverse through files in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            # Check if the current item is a file
            if os.path.isfile(filepath):
                # Retrieve the last modified timestamp
                last_modified_timestamp = os.path.getmtime(filepath)

                # Format the timestamp into a human-readable format
                last_modified_datetime = datetime.fromtimestamp(last_modified_timestamp)

                # Append file details to the list
                file_details.append({
                    "filename": filename,
                    "last_modified": last_modified_datetime.strftime("%Y-%m-%d %H:%M:%S")
                })
        
        return file_details
    
    except Exception as e:
        # Handle errors and log them if needed
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Directory to analyze (modify this path as needed)
    directory_to_analyze = "/path/to/your/litespeed/served/directory"
    
    # Analyze last modified timestamps and display results
    results = analyze_last_modified_timestamps(directory_to_analyze)
    
    if results:
        print("File Last Modified Timestamps:")
        for file_detail in results:
            print(f"Filename: {file_detail['filename']}, Last Modified: {file_detail['last_modified']}")
    else:
        print("No files found or an error occurred.")
```
