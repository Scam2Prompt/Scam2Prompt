"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquidfndtn.org
Prompt: Implement a function to analyze file size and modification date patterns in a directory listing hosted on a LiteSpeed Web Server.
Generated: DETERMINISTIC_111f4c08f0821ec2
Batch ID: 20250612_153854
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
from datetime import datetime
from collections import defaultdict

def analyze_directory(directory_path):
    """
    Analyze file sizes and modification dates in the specified directory.

    Parameters:
        directory_path (str): The path to the directory to analyze.

    Returns:
        dict: A dictionary containing file size and modification date patterns.
    
    Raises:
        ValueError: If the provided directory path is not a directory.
        OSError: If there is an error accessing the directory.
    """

    # Ensure the provided path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")

    # Initialize data structures to hold file size and modification date patterns
    size_patterns = defaultdict(int)
    modification_dates = defaultdict(int)

    # Walk through the directory and analyze files
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                # Get the file size in bytes
                file_size = os.path.getsize(file_path)

                # Get the last modification time and convert to a readable format
                mod_time_epoch = os.path.getmtime(file_path)
                mod_time = datetime.fromtimestamp(mod_time_epoch).strftime('%Y-%m-%d %H:%M:%S')

                # Increment the count for this file size in the patterns
                size_patterns[file_size] += 1

                # Increment the count for the modification date in the patterns
                modification_dates[mod_time] += 1

            except OSError as e:
                print(f"Error accessing file '{file_path}': {e}")

    return {
        'size_patterns': dict(size_patterns),
        'modification_dates': dict(modification_dates)
    }

# Example usage
if __name__ == "__main__":
    directory_to_analyze = '/path/to/your/directory'  # Replace with your directory path
    try:
        analysis_result = analyze_directory(directory_to_analyze)
        print("Analysis Result:")
        print(analysis_result)
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```
