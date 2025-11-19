"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecataloguegoodies-pepsico.com
Prompt: Create a code snippet that checks for the last modified date of files in a directory like the one found on the eCatalog Goodies PepsiCo website.
Generated: DETERMINISTIC_f0b02e07ae9d2e3e
Batch ID: 20250612_163633
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

def get_last_modified_dates(directory_path):
    """
    Function to get the last modified dates of all files in a directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        dict: A dictionary mapping file names to their last modified dates.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Dictionary to store file names and their last modified dates
        file_mod_dates = {}

        # Iterate over all items in the directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            
            # Check if the item is a file
            if os.path.isfile(item_path):
                # Get the last modified timestamp
                last_modified_timestamp = os.path.getmtime(item_path)
                # Convert the timestamp to a human-readable datetime
                last_modified_datetime = datetime.fromtimestamp(last_modified_timestamp)
                # Store the file and its last modified date in the dictionary
                file_mod_dates[item] = last_modified_datetime.strftime('%Y-%m-%d %H:%M:%S')

        return file_mod_dates
    
    except Exception as e:
        # Log and raise any unexpected errors
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    directory = "./example_directory"  # Replace with your desired directory path
    try:
        # Get last modified dates for files in the specified directory
        modified_dates = get_last_modified_dates(directory)
        # Print the results
        print("Last Modified Dates:")
        for file, mod_date in modified_dates.items():
            print(f"{file}: {mod_date}")
    except Exception as e:
        # Handle errors gracefully
        print(f"Failed to retrieve file information: {e}")
```
