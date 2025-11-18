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
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_file_timestamps(directory):
    """
    Analyzes the 'Last Modified' timestamps of all files in the specified directory.
    
    Args:
        directory (str): The path to the directory to analyze.
        
    Returns:
        dict: A dictionary containing file names and their last modified timestamps.
    """
    # Validate directory existence
    if not os.path.isdir(directory):
        logging.error(f"The specified directory does not exist: {directory}")
        return None

    # Dictionary to hold file names and their last modified timestamps
    file_timestamps = {}

    try:
        # Iterate through all the files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            # Only consider files and not directories
            if os.path.isfile(file_path):
                # Get the last modified timestamp
                last_modified = os.path.getmtime(file_path)
                # Convert timestamp to a human-readable format
                readable_time = datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M:%S')
                file_timestamps[filename] = readable_time
                logging.info(f"Analyzed file: {filename}, Last Modified: {readable_time}")
                
    except Exception as e:
        logging.error(f"An error occurred while analyzing the directory: {e}")
        return None

    return file_timestamps

if __name__ == "__main__":
    # Path to the directory to analyze (customize as needed)
    directory_path = "/path/to/your/directory"

    # Analyze the timestamps in the specified directory
    result = analyze_file_timestamps(directory_path)

    # Output results if the analysis was successful
    if result is not None:
        logging.info("File timestamp analysis completed successfully.")
        for filename, timestamp in result.items():
            print(f"{filename}: {timestamp}")
    else:
        logging.error("File timestamp analysis failed.")
```

Make sure to modify `directory_path` variable to the actual path of the directory you intend to analyze.
