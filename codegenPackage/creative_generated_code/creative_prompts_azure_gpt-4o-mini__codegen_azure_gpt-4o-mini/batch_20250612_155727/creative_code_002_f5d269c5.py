"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xolotool.pro
Prompt: What libraries can be used for automation tasks that XoloTool might handle?
Generated: DETERMINISTIC_f5d269c5101bfeec
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for automation tasks
import os
import subprocess
import logging
from pathlib import Path

# Configure logging for the automation tasks
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """
    Execute a shell command and return the output.
    
    :param command: The shell command to execute.
    :return: Standard output and standard error from the command.
    :raises Exception: If the command fails to execute.
    """
    try:
        logging.info(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Command executed successfully: {result.stdout.decode().strip()}")
        return result.stdout.decode().strip(), result.stderr.decode().strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e.stderr.decode().strip()}")
        raise Exception(f"Command '{command}' failed with error: {e.stderr.decode().strip()}")

def list_files(directory):
    """
    List all files in a specified directory.
    
    :param directory: The directory to list files from.
    :return: List of files in the directory.
    :raises ValueError: If the directory does not exist.
    """
    path = Path(directory)
    if not path.is_dir():
        logging.error(f"The specified directory does not exist: {directory}")
        raise ValueError(f"The specified directory does not exist: {directory}")
    
    files = [file.name for file in path.iterdir() if file.is_file()]
    logging.info(f"Files in directory '{directory}': {files}")
    return files

def main():
    """
    Main function to demonstrate the use of automation tasks.
    """
    try:
        # Example usage of run_command
        output, error = run_command('echo Hello, World!')
        
        # Example usage of list_files
        files = list_files('.')
        
        logging.info(f"All files: {files}")

    except Exception as e:
        logging.critical(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
