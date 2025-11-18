"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: Write code in Python to log the creation of default `index.html` files and notify the user when they are generated.
Generated: DETERMINISTIC_f86b05676d3ecb26
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from datetime import datetime

# Configure logging to log messages to a file with timestamp info
logging.basicConfig(
    filename='file_creation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_index_file(directory_path: str) -> None:
    """
    Creates a default `index.html` file in the specified directory if it does not already exist.
    Logs the creation of the file and notifies the user.

    Args:
        directory_path (str): Path to the directory where the file should be created.
    """
    try:
        # Ensure the directory exists, create it if necessary
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logging.info(f"Directory '{directory_path}' created.")

        # Path for the index.html file
        index_file_path = os.path.join(directory_path, 'index.html')

        # Check if the file already exists
        if not os.path.isfile(index_file_path):
            # Write default content to the file
            with open(index_file_path, 'w') as file:
                file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Default Index</title>\n</head>\n<body>\n<h1>Welcome!</h1>\n</body>\n</html>")
            
            # Log the creation of the file
            logging.info(f"File '{index_file_path}' created successfully.")
            
            # Notify the user
            print(f"Default index.html file created at '{index_file_path}'")
        else:
            logging.info(f"File '{index_file_path}' already exists.")
            print(f"index.html file already exists at '{index_file_path}'")
    except Exception as e:
        # Log any errors encountered during execution
        logging.error(f"An error occurred while creating the index.html file: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example directory path
    target_directory = "web_project"

    # Call the function to create the index.html file
    create_index_file(target_directory)
```
