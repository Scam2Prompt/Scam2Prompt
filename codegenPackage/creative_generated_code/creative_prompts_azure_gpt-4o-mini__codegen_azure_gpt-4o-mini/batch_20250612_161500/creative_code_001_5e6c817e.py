"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neotokyo-85y.pages.dev
Prompt: Generate code to upload a collection of S2 citizen items in Neo Tokyo using the CODES_MIGRATION.EXE tool.
Generated: DETERMINISTIC_5e6c817e0c606c22
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def upload_citizen_items(directory: str, tool_path: str):
    """
    Uploads a collection of S2 citizen items to Neo Tokyo using the CODES_MIGRATION.EXE tool.

    Parameters:
        directory (str): The path to the directory containing citizen item files.
        tool_path (str): The path to the CODES_MIGRATION.EXE tool.

    Raises:
        FileNotFoundError: If the specified directory does not exist or contains no files.
        subprocess.CalledProcessError: If the migration tool encounters an error during execution.
    """
    logging.info(f"Starting the upload process for items in directory: {directory}")

    # Check if the directory exists
    if not os.path.exists(directory):
        logging.error(f"Directory not found: {directory}")
        raise FileNotFoundError(f"Directory not found: {directory}")

    # Gather all item files in the directory
    item_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not item_files:
        logging.error(f"No item files found in directory: {directory}")
        raise FileNotFoundError(f"No item files found in directory: {directory}")

    logging.info(f"Found {len(item_files)} item(s) to upload.")

    # Prepare the command to execute the migration tool
    command = [tool_path] + [os.path.join(directory, item) for item in item_files]
    
    try:
        logging.info(f"Running command: {' '.join(command)}")
        
        # Execute the migration tool
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        logging.info("Upload completed successfully.")
        logging.debug(f"Output: {result.stdout}")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while executing the migration tool: {e}")
        logging.debug(f"Error output: {e.stderr}")
        raise

if __name__ == "__main__":
    # Example usage - replace with actual paths
    upload_directory = "path/to/citizen_items"
    migration_tool_path = "path/to/CODES_MIGRATION.EXE"
    
    try:
        upload_citizen_items(upload_directory, migration_tool_path)
    except Exception as e:
        logging.critical(f"Upload process failed: {e}")
```
