"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomix-1.com
Prompt: Develop a system to securely delete logs and transaction data after order expiration, adhering to Yomix.io's zero-log policy.
Generated: DETERMINISTIC_bc5bb08204d7bba8
Batch ID: 20250612_154632
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
import shutil

# Configure logging for debugging purposes (if needed)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
LOGS_DIRECTORY = "./logs"      # Directory where log files are stored
TRANSACTIONS_DIRECTORY = "./transactions"  # Directory where transaction data is stored
EXPIRATION_TIME_SECONDS = 7 * 24 * 60 * 60  # Expiration time: 7 days (in seconds)

def securely_delete_file(file_path):
    """
    Securely delete a file by overwriting its content multiple times before deletion.
    :param file_path: Path to the file to be securely deleted.
    """
    try:
        if not os.path.isfile(file_path):
            logging.warning(f"File does not exist: {file_path}")
            return

        # Get the file size
        file_size = os.path.getsize(file_path)
        
        # Overwrite file content multiple times
        with open(file_path, "wb") as f:
            for _ in range(3):  # Overwrite 3 times
                f.write(os.urandom(file_size))
        
        # Remove the file
        os.remove(file_path)
        logging.info(f"Securely deleted file: {file_path}")
    
    except Exception as e:
        logging.error(f"Error securely deleting file {file_path}: {e}")

def securely_delete_directory(directory_path):
    """
    Securely delete all files and subdirectories within a directory.
    :param directory_path: Path to the directory to be securely deleted.
    """
    if not os.path.isdir(directory_path):
        logging.warning(f"Directory does not exist: {directory_path}")
        return
    
    try:
        # Iterate through all files and directories within the directory
        for root, dirs, files in os.walk(directory_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                securely_delete_file(file_path)  # Securely delete each file
            
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                shutil.rmtree(dir_path, ignore_errors=False)  # Remove subdirectories

        # Remove the root directory itself
        shutil.rmtree(directory_path, ignore_errors=False)
        logging.info(f"Securely deleted directory: {directory_path}")
    
    except Exception as e:
        logging.error(f"Error securely deleting directory {directory_path}: {e}")

def delete_expired_data(directory, expiration_time_seconds):
    """
    Delete files in the specified directory that have expired based on their last modified time.
    :param directory: Path to the directory to check for expired files.
    :param expiration_time_seconds: Expiration time in seconds.
    """
    if not os.path.isdir(directory):
        logging.warning(f"Directory does not exist: {directory}")
        return
    
    try:
        current_time = time.time()
        
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                last_modified_time = os.path.getmtime(file_path)
                
                # Check if the file has expired
                if current_time - last_modified_time > expiration_time_seconds:
                    securely_delete_file(file_path)
    
    except Exception as e:
        logging.error(f"Error deleting expired data in directory {directory}: {e}")

def main():
    """
    Main function to execute secure deletion of logs and transaction data.
    """
    try:
        logging.info("Starting secure deletion process...")
        
        # Delete expired log files
        delete_expired_data(LOGS_DIRECTORY, EXPIRATION_TIME_SECONDS)
        
        # Delete expired transaction files
        delete_expired_data(TRANSACTIONS_DIRECTORY, EXPIRATION_TIME_SECONDS)
        
        logging.info("Secure deletion process completed.")
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
