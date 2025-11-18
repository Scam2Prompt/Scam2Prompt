"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-io.bryantroll.com
Prompt: Generate a script to detect and access files in a directory structure related to MetaMask, ensuring compatibility with Ethereum-based applications.
Generated: DETERMINISTIC_4abb6adea9fb7b07
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging

# Configure logging for better error tracking and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_metamask_files(directory):
    """
    Traverse the given directory and its subdirectories to find MetaMask-related files.

    Args:
        directory (str): The path to the directory to search in.

    Returns:
        list: A list of paths to MetaMask-related files.
    """
    metamask_files = []
    try:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check for common MetaMask file extensions
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    logging.info(f'Found file: {file_path}')
                    metamask_files.append(file_path)
    except Exception as e:
        logging.error(f'Error occurred while searching for files: {e}')
    
    return metamask_files

def read_json_file(file_path):
    """
    Read a JSON file and return its contents.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info(f'Successfully read file: {file_path}')
            return data
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
    except json.JSONDecodeError:
        logging.error(f'Error decoding JSON from file: {file_path}')
    except Exception as e:
        logging.error(f'An error occurred while reading the file: {e}')
    
    return None

def main():
    # Replace this with the actual path where MetaMask files are likely stored
    directory_to_search = os.path.expanduser("~/.metamask")
    
    logging.info(f'Searching for MetaMask files in: {directory_to_search}')
    metamask_files = find_metamask_files(directory_to_search)
    
    for file in metamask_files:
        data = read_json_file(file)
        if data is not None:
            # Process the data as needed; printing for demonstration
            print(f'Contents of {file}: {data}')

if __name__ == '__main__':
    main()
```
